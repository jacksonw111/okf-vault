---
type: "Tool"
title: "orbien"
description: "orbien-org 开源的 Rust + Tokio 内网穿透工具：单个二进制约 5MB，支持 TCP / QUIC / KCP / WebSocket，把本地 TCP/UDP/HTTP/HTTPS 服务映射到公网。"
resource: "https://github.com/orbien-org/orbien"
tags: ["nat-traversal", "rust", "tokio", "tcp", "quic", "kcp", "websocket", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# orbien

## 它是什么
orbien 是一个 Rust + Tokio 写的轻量、高性能内网穿透工具。单二进制 ~5MB，支持 TCP / QUIC / KCP / WebSocket 等多种传输层协议，把本地 TCP/UDP/HTTP/HTTPS 服务映射到公网。适合没有公网 IP 的家用网络 / 小型办公室暴露本地 Web 服务。

## 为什么用它 / 适合什么场景
- 家里 NAS / 树莓派 / 软路由上有 Web 服务想临时暴露给外部。
- 在公司内部跑开发服务器，需要从公网访问。
- 比 frp / nps 更现代的 Rust 实现，体积小、协议覆盖全。

## 关键能力
| 能力 | 说明 |
|------|------|
| 实现语言 | Rust + Tokio |
| 二进制大小 | 约 5MB |
| 传输协议 | TCP / QUIC / KCP / WebSocket |
| 协议层 | TCP / UDP / HTTP / HTTPS |
| 定位 | 内网穿透 |

## 媒体

架构示例：![架构示例](https://pbs.twimg.com/media/HPkYBmnagAAxqEo.jpg)

## 相关概念
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板，与 orbien 互补（3X-UI 偏代理协议，orbien 偏内网穿透）
- [WARP-Manager](./tool-warp-manager.md) — VPS WARP 路由工具，与 orbien 共同解决「网络可达性」问题
- [Rathole Engine](./tool-rathole-engine.md) — 另一类轻量 NAT 穿透引擎，可与 orbien 对比使用
