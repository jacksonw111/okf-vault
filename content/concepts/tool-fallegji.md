---
type: Tool
title: "Fallegji"
description: "Rust 写的终端 P2P 群聊应用，完全去中心化、端到端加密（X25519 + ChaCha20-Poly1305）、无服务器无账号无中间人，每个对等体本地 SQLite 自动同步聊天记录。"
resource: "https://github.com/AshLink95/Fallegji"
tags: "[p2p, chat, rust, e2ee, decentralized, terminal]"
timestamp: "2026-07-02T07:00:00Z"
---

# Fallegji

## 它是什么
Rust 写的终端 P2P 群聊应用。完全去中心化、无需服务器、无需账号、无中间人。节点之间直接加密 TCP 通信，消息用 X25519 + ChaCha20-Poly1305 加密，每个对等体本地存一份 SQLite 聊天记录自动同步。

## 为什么用它 / 适合什么场景
- 想在**局域网或 VPN 内**拉一群人聊天，又不想架设服务器 / 注册账号。
- 对隐私要求高、不想任何第三方持有你的消息元数据。
- 喜欢终端 TUI 风格聊天工具（类似 IRC 的现代加密重制版）。
- 离线 / 隔离网络环境：纯本地网络通信，依赖不到公网。

## 关键能力
| 能力 | 说明 |
|------|------|
| 通信模式 | 完全去中心化 P2P，节点直接 TCP 通信 |
| 加密 | 每条消息 X25519 + ChaCha20-Poly1305 |
| 账号体系 | 无账号、无服务器、无中间人 |
| 存储 | 每个对等体本地 SQLite 聊天记录，自动同步 |
| 形态 | 终端应用（TUI） |
| 部署条件 | 局域网 / VPN 内即可使用，无需公网可达 |

## 相关概念
- [SimpleX Chat](tool-simplex-chat.md) — 同为「无用户标识符 + E2EE」消息平台，但是中继服务器架构而非纯 P2P
- [Rust + QUIC 高性能 IM 后端](tool-rust-quic-im.md) — Rust IM 后端参考；Fallegji 是终端 P2P 客户端路线，定位不同
- [Brigade](tool-brigade.md) — 多 AI 代理协作框架；Fallegji 是人去中心化聊天工具

## 项目链接
- 项目主页：<https://github.com/AshLink95/Fallegji>