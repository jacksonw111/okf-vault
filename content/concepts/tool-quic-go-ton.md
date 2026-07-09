---
type: Tool
title: "quic-go-ton（带 Ed25519 身份与 RFC 7250 的 TON 网络 QUIC）"
description: "quic-go 的 TON 网络分支：用纯 Go 实现与 TON 参考节点线兼容的 QUIC 传输，并用 RFC 7250 原始公钥（Ed25519 ADNL 身份）替代 X.509 证书。"
resource: "https://github.com/xssnick/quic-go-ton"
tags: "[quic, go, ton, blockchain, ed25519, rfc7250, adnl]"
timestamp: "2026-07-09T20:50:00Z"
---

# quic-go-ton（带 Ed25519 身份与 RFC 7250 的 TON 网络 QUIC）

## 它是什么
`xssnick/quic-go-ton` 是知名 Go 语言 QUIC 库 **`quic-go`** 的一个 **TON 网络分支**：

- **纯 Go**实现
- 与 **TON 参考节点线兼容**的 QUIC 传输
- 用 **RFC 7250 原始公钥（Ed25519 ADNL 身份）** 替代传统 X.509 证书
- 这是 TON 网络协议栈实践的参考实现

## 为什么用它 / 适合什么场景
- 想**在 Go 中实现 TON 节点 / 客户端**。
- 想了解 **QUIC 协议 + 非 PKI 身份**的真实例子（RFC 7250 用原始公钥替代证书）。
- 想做区块链 / Web3 项目的**自定义传输层**研究。
- 对比传统 HTTPS+TLS：本项目用 Ed25519 ADNL 身份直接做认证，省掉 CA 与 X.509 体系。

## 关键能力
| 能力 | 说明 |
|------|------|
| 纯 Go 实现 | 与上游 `quic-go` 同生态 |
| TON 协议兼容 | 参考节点线的 QUIC 传输 |
| RFC 7250 | 原始公钥模式（带 Ed25519） |
| 去除 X.509 | 不再依赖传统 CA 证书体系 |
| 可作 TON Node / 客户端起点 | 协议栈完整 |

## 媒体参考

架构图：
- ![](https://pbs.twimg.com/media/HMq5w6QbEAA_SUf.jpg)

## 相关概念
- [Rust + QUIC 高性能 IM 后端](tool-rust-quic-im.md) — Rust Actix-web QUIC + P2P NAT 打洞的 IM 后端（同样 QUIC 主题）
- [Rust + QUIC 高性能 IM 后端（不复述）](tool-rust-quic-im.md) — 另一个 QUIC 实现，做 P2P + 协议不同

## 参考链接
- 项目链接：<https://github.com/xssnick/quic-go-ton>
