---
type: "Tool"
title: "Lucky"
description: "NAS / 软路由上的瑞士军刀：DDNS + ACME 自动续签证书 + 反向代理 + 端口转发 + 定时任务，一个 Web 后台全包。"
tags: "[network, ddns, reverse-proxy, acme, nas, qos-bypass]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://github.com/gdy666/lucky"
---

# Lucky

## 它是什么

`Lucky`（`lucky666`）是一个常驻 NAS / 软路由 / 家庭服务器上的「网络管理瑞士军刀」，用 Go 写成，Web UI 集中在单一端口。它把家庭网络里散落的 **DDNS、ACME 证书自动续签、反向代理、端口转发、定时任务、网络唤醒、自定义脚本** 全部塞进一个面板，**省得同时跑 ddns-go + nginx-proxy-manager + acme.sh + 看门狗**。

典型部署平台：群晖、威联通、飞牛 OS、OpenWrt、iKuai、Linux。

## 为什么用它

- **一键 HTTPS**：内置 ACME 客户端（支持 DNS-01 / HTTP-01），证书自动续签，告别 `acme.sh` 黑窗命令行。
- **反代免 Nginx 配置**：填「前端域名 + 后端地址 + 端口」就完事，证书自动绑定。
- **DDNS 全家桶**：阿里云 / 腾讯云 / Cloudflare / 华为云 / Dynadot 等十几家接口可选。
- **轻量**：单二进制 / 单 Docker 镜像，资源占用极低，1C1G 飞牛也能跑。
- **国产工具 / 中文友好**：界面 / 文档 / 社区全是中文，门槛极低。

## 关键能力

| 能力 | 说明 |
|------|------|
| DDNS | 多服务商，IPv4/IPv6 双栈，定时刷新 |
| ACME 自动证书 | DNS-01（CF/阿里/腾讯/DNSPod…）和 HTTP-01，续签自动化 |
| 反向代理 | Web UI 配前端域名 + 后端地址，证书 / 路径 / Header 一应俱全 |
| 端口转发 | 公网 → 内网设备的 TCP/UDP 转发 |
| 定时任务 | crontab 风格，定时跑脚本 / 调用 URL |
| 网络唤醒 | 局域网内远程开机 |
| 存储 / 文件管理 | 小工具集（不是主业） |

## 在「VLESS 绕 QoS 方案」里的角色

[VLESS 绕 QoS 方案](../playbook/playbook-vless-bypass-telecom-qos.md) 的关键设计是 **「Xray 不直接面对公网，反代做 TLS 入口」**。Lucky 就在这一步担任公网入口 + 证书管家：

- **公网入口**：监听 `:22443`（避开运营商封的 443 / 8443），反代到 `127.0.0.1:10080`（3X-UI 的 WebSocket 后端）。
- **证书托管**：用 DNS-01 给 `home.example.com` 签发 + 自动续签，3X-UI 不需要碰证书。
- **DDNS**：在公网 IP 变动时把 `home.example.com` 指向新 IP。

这样的好处：

1. **3X-UI 面板不上公网**，攻击面大幅缩小；
2. **流量指纹 = 普通 HTTPS 站点**，过 QoS 设备不被识别为代理；
3. **证书续签全自动**，三个月一次的手动操作消失了。

## 部署示例（Docker Compose）

```yaml
services:
  lucky:
    image: gdy666/lucky:latest
    container_name: lucky
    restart: unless-stopped
    network_mode: host
    volumes:
      - /volume1/docker/lucky/conf:/goodluck
```

默认后台端口 `16601`，进后台先改密码。

## 相关概念

- [VLESS + WebSocket + TLS 绕过电信 QoS 方案（Playbook）](../playbook/playbook-vless-bypass-telecom-qos.md)
- [3X-UI](tool-3x-ui.md)
- [DDNS](https://github.com/jeessy2/ddns-go) — 替代品参考
- [Nginx Proxy Manager](https://github.com/NginxProxyManager/nginx-proxy-manager) — 替代品参考
