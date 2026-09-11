---
type: "Tool"
title: "lantunnel（NAT 穿透型加密私有组网）"
description: "让分散在不同 NAT 后面的自有设备组成加密私有组网，在外直接访问家里的 NAS / GPU 主机等内网服务；QUIC 打洞 + 中继搬密文，免费 5GB/月应急额度。"
resource: "https://github.com/lantunnel/lantunnel"
tags: "[nat-traversal, vpn, quic, p2p, self-host]"
timestamp: "2026-09-11T22:05:00Z"
---

# lantunnel

## 它是什么

[lantunnel/lantunnel](https://github.com/lantunnel/lantunnel) 是把分散在不同 NAT 后面的**自有设备**组成**加密私有组网**的工具：在外直接访问家里的 NAS、GPU 主机等内网服务，**无需端口转发 / 公网 IP / 暴露服务**。

## 工作机制

| 路径 | 用途 |
|------|------|
| **QUIC 打洞** | 设备在同一房间 / 同区域时直连，零中转 |
| **网关中继** | 直连不通时走网关，但网关**只搬密文**，看不到明文 |
| **127.0.0.1:1080** | 装完把应用指到这个本地端口就能访问对端内网 |

## 为什么用它 / 适合什么场景

- 出门想访问家里 NAS / 家用服务器 / 远程 GPU 主机。
- 不想暴露公网端口（安全）。
- 嫌 Tailscale / ZeroTier 还不够轻量，想试一个**直连为主**的方案。

## 关键能力

| 能力 | 说明 |
|------|------|
| NAT 穿透 | QUIC 打洞直连 |
| 加密中继 | 网关不接触明文 |
| 本地端口 | 127.0.0.1:1080 即用 |
| 免费额度 | 中继 5GB/月应急 |
| 自建网关 | 主力通道建议自己搭网关 |
| 跨平台 | 自有设备组网 |

## 参考链接

- 项目仓库：<https://github.com/lantunnel/lantunnel>

## 媒体

- ![](https://pbs.twimg.com/media/HR0e8ReaYAArv3r.png)

## 相关概念

- [Tailtab](./tool-tailtab.md) — 浏览器扩展为每个 profile 配独立 Tailscale 节点
- [swarmllm](./tool-swarmllm.md) — 同样基于 WebRTC / QUIC 的 P2P 思路
- [Pi.Alert](./tool-pi-alert.md) — 同为局域网 / 内网相关工具
</content>
</invoke>