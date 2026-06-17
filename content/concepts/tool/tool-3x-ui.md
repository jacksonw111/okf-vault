---
type: "Tool"
title: "3X-UI"
description: "Xray/V2Ray 的 Web 管理面板，基于 Docker 部署，图形化配置 VLESS / VMess / Trojan 等入站规则，把 Xray 复杂的 JSON 配置变成点鼠标。"
tags: "[network, xray, vless, docker, nas, qos-bypass]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://github.com/mhsanaei/3x-ui"
---

# 3X-UI

## 它是什么

`3X-UI`（也常写作 `3x-ui`）是 [Xray-core](https://github.com/XTLS/Xray-core) 核心的 **Web 图形化管理面板**，用 Go 写成、官方镜像托管在 `ghcr.io/mhsanaei/3x-ui`。它把 Xray 那一坨 `config.json`、路由规则、TLS 证书、inbound/outbound、流控模式都封装成「建一个入站 → 选协议 → 填端口和路径」的表单，等于把核弹级复杂度的 Xray 装进了一个像路由器后台的 UI。

常被用于：自建代理节点、内网穿透、绕过运营商 QoS、家庭服务器暴露（搭配反向代理）。

## 为什么用它

- **零配置文件**：所有 inbound / outbound / routing / 证书都在 Web UI 里改，不用手撸 JSON。
- **协议齐全**：VLESS / VMess / Trojan / Shadowsocks / WireGuard 一应俱全。
- **多用户管理**：内置用户、流量统计、限速、订阅链接，天然适合「节点主」场景。
- **Docker 友好**：单镜像 `network_mode: host` 一行起，配置文件挂卷 `db/` 就能持久化。
- **生态丰富**：开源活跃，中文社区有大量教程；与 [Lucky](tool-lucky.md)、Nginx 反代、各类客户端（Clash / 小火箭）配合顺畅。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多协议入站 | VLESS / VMess / Trojan / SS，单面板同时跑多种 |
| 传输层 | TCP / WebSocket / gRPC / HTTP/2，按场景选 |
| 路由规则 | 域名 / IP / GeoIP 分流，可视化编辑 |
| 流量与限速 | 用户级 / 节点级流量统计、定时重置 |
| 订阅链接 | 一键生成 Clash / Surge / Loon / Shadowrocket 订阅 |
| 证书管理 | 支持 ACME 自动签发 + 上传自有证书 |
| TPROXY / TUN | Linux 下做透明代理，把所有流量都收进 Xray |

## 典型使用模式

3X-UI 本身只负责 Xray 配置和**本机**监听，真正的「公网可达」靠反代 / DDNS / 端口转发——这正是 [VLESS + WebSocket + TLS 绕电信 QoS 方案](../playbook/playbook-vless-bypass-telecom-qos.md) 的核心架构：

```
异地客户端 → 反向代理（Lucky / Nginx，公网 HTTPS） → 3X-UI（仅 127.0.0.1:10080）→ 家里内网服务
```

> ⚠️ **安全要点**：3X-UI 面板不要直接暴露到公网！默认账号 `admin` / `admin` 必须改，面板路径必须改，端口只对内网开放（`127.0.0.1` 监听），TLS / 公网入口交给反代做。

## 部署示例（Docker Compose）

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

启动后访问 `http://NAS-IP:2053`，首次进入立刻改账号密码和面板路径。

## 相关概念

- [VLESS + WebSocket + TLS 绕过电信 QoS 方案（Playbook）](../playbook/playbook-vless-bypass-telecom-qos.md)
- [Lucky（反向代理 / DDNS / ACME）](tool-lucky.md)
- [Xray-core](https://github.com/XTLS/Xray-core) — 3X-UI 管理的核心
