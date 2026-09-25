---
type: "Tool"
title: "tincan-cli（终端 P2P 语音 + 文字聊天室）"
description: "终端里跑的开源不依赖中心服务器的语音 / 文字聊天室，基于 iroh 打洞让同频道的人直接点对点传 Opus 音频；房间元数据走开房者，Opus 流走 P2P。"
resource: "https://github.com/bilalyazicioglu/tincan-cli"
tags: "[p2p, terminal, voice-chat, opus, ratatui, iroh, rust, no-server, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# tincan-cli（终端 P2P 语音 + 文字聊天室）

## 它是什么

[tincan-cli](https://github.com/bilalyazicioglu/tincan-cli) 是一个**终端里的语音 + 文字聊天室**，全程 Rust 写、TUI 用 [ratatui](https://github.com/ratatui/ratatui) 画、底层用 [iroh](https://github.com/n0-computer/iroh) 做 NAT 打洞 —— **不依赖任何中心服务器**。

- 房间的**少量元数据**（名册 / 频道名 / 聊天记录）走开房者那台机器，每秒几百字节
- **音频流**（Opus 编码）走 iroh P2P 通道，同频道成员之间直连
- 想开会就开一个 tincan 房间、复制 invite，朋友们贴进终端就能加进来

## 为什么用它 / 适合什么场景

- 团队 / 社群想有个**零基础设施依赖**的语音 / 文字聊天室——没有服务器、没有账号、没有持久化、没有日志。
- 注重**隐私 / 抗封禁**：不依赖任何中心节点，断网即散。
- 习惯终端工作流、希望所有事都在命令行里完成。
- 已有 [iroh](./term-iroh.md) / 类似 NAT 打洞基建，想快速搭语音聊天。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 终端 TUI（ratatui） |
| 语言 | Rust |
| 网络 | iroh 打洞（P2P，无中心服务器） |
| 音频 | Opus，同频道成员之间直连 |
| 文字 | 走开房者转发（少量元数据） |
| 流量 | 元数据 ≈ 几百字节 / 秒；音频取决于房间人数与编码 |
| 鉴权 | invite 字符串一次性加入 |

## 媒体

![](https://pbs.twimg.com/media/HTBheTibwAABnth.jpg)

## 相关概念

- [iroh](./term-iroh.md) — Rust 写的 P2P 网络栈（NAT 打洞 / QUIC），tincan-cli 的网络底座
- [ratatui](./term-ratatui.md) — Rust 终端 UI 库，本项目 TUI 渲染
