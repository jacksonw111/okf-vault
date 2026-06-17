---
type: "Playbook"
title: "VLESS + WebSocket + TLS 绕过电信 QoS，把家里内网伪装成 HTTPS 访问"
description: "当 Tailscale / 自建 DERP 被运营商 UDP/TCP 限速时，把「异地访问家庭内网」伪装成一个普通 HTTPS 网站；用 3X-UI + Lucky + 反代 + 端口转发，端到端复原上行带宽。"
tags: "[network, qos-bypass, vless, websocket, tls, nas, playbook]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://x.com/xiaojingshe/status/2064554366783381583"
---

# VLESS + WebSocket + TLS 绕过电信 QoS

## 适用场景

- 异地要访问家庭内网（NAS 后台、路由器、智能家居、远程桌面、SSH）。
- 原本用 Tailscale / ZeroTier / 自建 DERP，但被运营商**对 UDP 或特征明显的 TCP 流量做 QoS 限速**（典型表现：刚连上能跑 30Mbps，几秒后掉回 2-5Mbps）。
- 普通 HTTPS 业务（DDNS + 端口转发、上传视频到 B 站）**不被限速**——这是本方案的成立前提。
- 具备一定网络经验：会配 Docker / 反向代理 / DNS 证书 / Clash 或小火箭。

> **核心思路**：运营商认不出「代理」就限不了速。所以把代理流量**伪装成一次普通的 HTTPS 网站访问**，公网上看到的只是一个挂着合法证书的 Web 站点。

## 前置条件

| 条件 | 说明 |
|------|------|
| 家庭动态公网 IP | 拨号获得；联系运营商要或路由器开桥接 |
| 一个域名 | 便宜的几块钱一年，托管在支持 API 的 DNS 服务（CF / 阿里 / 腾讯） |
| 24h 在线设备 | 群晖 / 飞牛 / 软路由 / 迷你主机 |
| 域名能解析回家里 IP | 由 Lucky / ddns-go 做 DDNS 兜底 |
| 路由器可做端口转发 | 外部 TCP 高位端口 → 内网设备 |
| 客户端支持 VLESS+WS+TLS | Clash / 小火箭 / Shadowrocket / NekoBox 均可 |

## 最终拓扑

```
异地设备
  ↓
Clash / 小火箭 客户端分流（只把"家网段"打到下面节点）
  ↓
路由器端口转发：公网 :22443 → Lucky 设备 :22443
  ↓
Lucky：HTTPS 反向代理 + ACME 证书（前端 home.example.com:22443）
  ↓
3X-UI / Xray：VLESS + WebSocket（仅 127.0.0.1:10080，TLS 交给 Lucky）
  ↓
家里内网服务（192.168.31.0/24）
```

**每个组件只做一件事**：Xray 只提供 WebSocket 后端；Lucky 只做 TLS 入口 + 证书；路由器只做端口转发。组合起来流量指纹 = 一次正常 HTTPS GET。

## 步骤

### 1. Docker 部署 3X-UI

群晖 Container Manager / Portainer / 命令行都行，Compose 示例：

```yaml
services:
  3x-ui:
    image: ghcr.io/mhsanaei/3x-ui:latest
    container_name: 3x-ui
    restart: unless-stopped
    network_mode: host
    volumes:
      - /volume1/docker/3xui/db:/etc/x-ui
```

启动后访问 `http://NAS-IP:2053` 进入面板，**立刻**：

- 改默认账号 `admin` / `admin`
- 改面板访问路径（不要用 `/`）
- 确认面板**只监听内网或 127.0.0.1**，**绝不放公网**

### 2. 在 3X-UI 新建入站

| 字段 | 值 |
|------|----|
| 协议 | VLESS |
| 监听 | `127.0.0.1` |
| 端口 | `10080`（不冲突随意） |
| 传输 | WebSocket |
| Path | `/home`（任意名称，前后对应） |
| 安全 | **无**（TLS 交给 Lucky） |

> **踩坑提醒**：进 Xray 设置删掉「`geoip:private` → direct」这条路由规则。客户端发起的内网 IP 目标如果被服务端强制 direct，会被自家路由器拦截导致看似"通了"但拿不到响应。

### 3. Lucky 配 DDNS + ACME 证书

Lucky 后台：

1. **DDNS**：选 DNS 服务商、填 API Token，绑定 `home.example.com` 到家庭公网 IP，定时刷新。
2. **ACME 证书**：用 DNS-01 方式给 `home.example.com` 签证书，开自动续签。

### 4. Lucky 新增 Web 服务规则（反向代理）

| 字段 | 值 |
|------|----|
| 服务类型 | 反向代理 |
| 前端地址 | `home.example.com:22443` |
| 后端地址 | `http://127.0.0.1:10080` |
| 证书 | 选刚才签的 ACME 证书 |
| 端口 | `22443`（避开运营商常封的 443 / 8443） |

> 3X-UI 和 Lucky 不在同一台设备时，后端填 `http://群晖IP:10080` 即可。

### 5. 路由器做端口转发

主路由器（拨号拿公网 IP 的那台）：

```
外部 TCP 22443 → 192.168.31.X（群晖/Lucky）:22443
```

端口用大一点的数字，运营商一般只盯 80 / 443 / 8443 / 8080。

### 6. 客户端节点配置（小火箭示例）

自建节点导入，**关键 4 个字段**：

| 字段 | 值 |
|------|----|
| 地址 | `home.example.com` |
| 端口 | `22443` |
| UUID | （3X-UI 入站里的） |
| 传输方式 | WebSocket，**路径 = `/home`** |
| TLS | 默认开启，SNI 同 `home.example.com` |

### 7. 设置分流规则

家里网段是 `192.168.31.0/24`，分流规则放**最前**：

```text
- IP-CIDR,192.168.31.0/24,🏠 回家,no-resolve
```

> **避坑**：很多客户端默认带 `192.168.0.0/16 不走代理` 这种"局域网绕过"规则，**必须删掉**，否则访问家里内网 IP 时流量根本不进节点。
>
> **SSH 走代理**：SSH 默认不被系统代理接管，客户端开 **TUN 模式** 强制接管全部流量，才能从外面 SSH 回家里设备。

## 验证 / 自检

- [ ] 客户端能看到节点延时（没有就是配置错）
- [ ] 访问 `192.168.31.1`（路由器后台）能打开，且 Lucky / 3X-UI 后台能看到对应流量
- [ ] SSH 回家里设备可连（TUN 模式开）
- [ ] 实测上行带宽恢复到运营商承诺（电信 40Mbps 上行）
- [ ] 持续 10 分钟不掉速（QoS 设备对"特征明显"的流量是「先放后杀」）

**没流量时排查顺序**：

1. 节点信息是否正确（地址 / 端口 / UUID / 路径 / SNI）
2. 客户端分流规则是否命中
3. 局域网绕过是否删干净
4. 策略组是否选中了"回家"节点
5. 路由器端口转发是否生效（外网 `telnet home.example.com 22443` 测试）

## 配套工具

| 工具 | 角色 | 文档 |
|------|------|------|
| [3X-UI](./tool-3x-ui.md) | Xray 图形面板、VLESS+WS 入站 | [./tool-3x-ui.md](./tool-3x-ui.md) |
| [Lucky](./tool-lucky.md) | DDNS + ACME + 反向代理三合一 | [./tool-lucky.md](./tool-lucky.md) |
| Clash / 小火箭 / Shadowrocket | 客户端 | 各客户端官网 |

## 复用价值

这套架构不只是「回家」——**把 NAS 换成 VPS，这就是一份完整的「自建 VPS 节点绕过 QoS」教程**。所有依赖（3X-UI、Lucky、域名、证书）原样可用，唯一变的是把 `127.0.0.1:10080` 换到 VPS 上。

## 相关概念

- [3X-UI](./tool-3x-ui.md)
- [Lucky](./tool-lucky.md)
- [Tailscale](https://tailscale.com/) — 之所以要绕开它的原因（UDP QoS）
- [Xray-core](https://github.com/XTLS/Xray-core)
- [OKF 是什么](./term-okf.md)
