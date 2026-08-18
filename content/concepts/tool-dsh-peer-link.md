---
type: Tool
title: "dsh-peer-link (czm15053/dsh-peer-link)"
description: "DSH 会话 ↔ 本机其他 agent（如 Claude Code）的 Unix socket 互联插件：用本地 socket 把多个 agent 串成可互相收发消息的协作网络"
resource: "https://github.com/czm15053/dsh-peer-link"
tags: [deepseek, harness, dsh, inter-agent, unix-socket, plugin]
timestamp: "2026-08-18T12:00:00Z"
---

# dsh-peer-link (czm15053/dsh-peer-link)

## 它是什么
`czm15053/dsh-peer-link` 是一个 DSH 插件：当 DSH 会话想和本机其他 agent（如 Claude Code）对话时，它用 **Unix domain socket** 把多个 agent 串起来，让它们可以互相收发消息，形成**本机多 agent 协作网络**。

## 为什么用它 / 适合什么场景
- 同时跑 DSH + Claude Code / Codex 等 agent，想让它们**协同而不是各做各的**。
- 不希望走云端中转：本地 Unix socket 延迟低、流量不出机器。
- 想用 DSH 做「协调者」：派活给其他 agent、收回结果继续推理。

## 关键能力
| 能力 | 说明 |
|------|------|
| Unix socket 互联 | 不依赖网络协议栈，走本地 socket |
| 多 agent 互通 | DSH ↔ Claude Code / Codex 等可互相收发 |
| 本机协作网络 | 形成「同机多 agent」协作拓扑 |
| DSH 插件形态 | 装到 DSH 即可使用 |

## 媒体
- ![](https://pbs.twimg.com/media/HP5FKIUaEAAVOOS.jpg)

## 相关概念
- [项目链接](https://github.com/czm15053/dsh-peer-link) — 仓库地址
