---
type: Tool
title: "tailcat（Tailscale 推出的 netcat 风格数据传输工具）"
description: "Tailscale 开源的 netcat 替代：跑在 Tailscale 数据平面上，无需 control plane、不需要账号；WireGuard + DERP 协调、gVisor netstack、userspace 模式无需 root；可管道 stdin、转发端口、跑免认证的 SSH 服务器。"
resource: "https://github.com/tailscale/tailcat"
tags: [tailscale, netcat, ssh, port-forwarding, derp, wireguard, userspace]
timestamp: "2026-08-29T21:30:00Z"
---

# tailcat（Tailscale 推出的 netcat 风格数据传输工具）

## 它是什么

[tailscale/tailcat](https://github.com/tailscale/tailcat) 是 Tailscale 官方开源的 **netcat 替代**：把 `nc` 风格的数据流搬上 **Tailscale 数据平面**——无需 control plane、不需要 Tailscale 账号，纯靠 **WireGuard + DERP** 做 NAT 穿透与对端发现。

设计要点：

- **gVisor netstack** 用户态 TCP/IP 栈——**不需要 root**；
- **DERP 中继**做 NAT 穿透——两端任一在 NAT 后也能直连；
- 一行命令跑出**免认证 SSH 服务器**（临时场景）；
- 可管道 stdin / stdout、转发端口、做 netcat 的全部事。

README 几乎是「一连串命令行示例」——直接抄就能用。

## 为什么用它 / 适合什么场景

- 想跨 NAT / 跨网络**点对点**传文件 / 跑命令，又不想装 Tailscale 客户端、配账号；
- 临时给同事一台机器的 shell 访问（**慎用**：免认证 SSH 是把双刃剑）；
- 给容器 / CI / serverless 跑个用户态 netcat（无 root 权限）；
- 端口转发 / 反向 shell / 内网穿透的轻量替代；
- 在企业防火墙 / NAT 后端做应急通道。

## 关键能力

| 能力 | 说明 |
|------|------|
| Tailscale 数据平面 | 走 WireGuard + DERP，绕开 NAT |
| 无 control plane | 不必装控制服务器、不必注册账号 |
| 无 root | gVisor netstack userspace |
| netcat 全兼容 | 管道 stdin、转发端口、做隧道 |
| 免认证 SSH | 一行启动免密 SSH server（仅限可信网络） |
| 跨平台 | Tailscale 覆盖的 OS 都能跑 |

## 相关概念

- [Lucky](./tool-lucky.md) — DDNS + ACME + 反代瑞士军刀，tailcat 是 Tailscale 体系内的端到端小工具
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板，tailcat 是更轻量的 NAT 穿透替代

## 参考链接

- 项目链接：<https://github.com/tailscale/tailcat>
- 原始推文：<https://x.com/Wen_Zw/status/2093561750532874663>