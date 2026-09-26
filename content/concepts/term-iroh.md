---
type: "Term"
title: "iroh（Rust 写的 P2P 网络栈：QUIC + NAT 打洞）"
description: "n0-computer 出品的 Rust P2P 网络栈：基于 QUIC 做 NAT 打洞 / 端到端连接，让两个节点无需中心服务器即可直连；常用于去中心化聊天、文件传输、协作等场景（如 tincan-cli 的语音聊天底层）。"
resource: "https://github.com/n0-computer/iroh"
tags: "[iroh, p2p, quic, nat-traversal, rust, no-server, decentralized, open-source]"
timestamp: "2026-09-26T21:50:00Z"
---

# iroh（Rust 写的 P2P 网络栈：QUIC + NAT 打洞）

## 定义

[iroh](https://github.com/n0-computer/iroh) 是 [n0-computer](https://n0.computer/) 开源的 **Rust P2P 网络栈**——基于 **QUIC** 协议做 **NAT 打洞**与端到端连接，让两个节点**无需中心服务器**即可建立直连通道。

## 要点

- **P2P 直连**：两个节点拿到对方的「endpoint id」即可建立连接，无需中转。
- **QUIC 底座**：现代传输协议，内建 TLS 1.3、多路复用、拥塞控制。
- **NAT 打洞**：自动穿透大多数家用 / 移动网络 NAT。
- **无中心**：不依赖任何中心化服务，不持久化元数据。
- **Rust 原生**：性能高、内存安全、易嵌入。

## 典型场景

- **去中心化聊天 / 语音**：如 [tincan-cli](./tool-tincan-cli.md) 的 Opus 音频走 iroh 直连。
- **P2P 文件传输**：无需服务器中转的大文件分发。
- **协作工具**：实时同步无需中心服务的版本。

## 相关概念

- [tincan-cli](./tool-tincan-cli.md) — 用 iroh 做 P2P 语音聊天的终端工具
- [ratatui](./term-ratatui.md) — Rust 终端 UI 库，常与 iroh 搭配做 TUI