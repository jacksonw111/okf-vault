---
type: "Note"
title: "Pi 三篇经典长文（Session Portability / Prompt Caching / Compaction）"
description: "Pi agent 的三篇深度长文：The Session You Cannot Take With You（会话不可移植）、Prompt Caching In Agents（Agent 里的 prompt 缓存）、How Compaction Works in Pi（Pi 的压缩机制），合在一起解释 Pi 为何这么设计。"
resource: "https://pi.xiaomovps.com/translations/session-portability"
tags: "[pi, agent, prompt-caching, compaction, session]"
timestamp: "2026-09-14T22:45:00Z"
---

# Pi 三篇经典长文（Session Portability / Prompt Caching / Compaction）

## 三篇是什么

| 标题 | 主题 | 链接 |
|------|------|------|
| The Session You Cannot Take With You | 会话不可移植性：换台机器/换个会话，状态为何带不走 | <https://pi.xiaomovps.com/translations/session-portability> |
| Prompt Caching In Agents | Agent 内部 prompt 缓存的设计取舍 | <https://pi.xiaomovps.com/translations/prompt-caching> |
| How Compaction Works in Pi | Pi 的压缩机制：长上下文如何折叠 | <https://pi.xiaomovps.com/translations/compaction-in-pi> |

## 为什么合在一起读

这三篇是理解 **Pi agent** 设计哲学的关键入口：

- **Session Portability**：揭示会话状态在不同载体间迁移的代价——为什么「换个机器继续干」不是默认就能做到的事。
- **Prompt Caching**：讨论 Agent 在多轮 / 多任务下缓存 prompt 的策略——比传统 LLM 缓存更复杂，因为 Agent 自身行为会污染 prompt。
- **Compaction in Pi**：Pi 是怎么把长上下文**压扁**的——这关系到长会话会不会越来越慢。

## 适合谁

- 在选 / 自建 Agent 的工程团队
- 想搞清楚「**Pi 这么设计**」背后原因的读者
- 想了解 prompt caching、context compaction 这两块基础设施在 Agent 场景里如何工作

## 媒体

![](https://pbs.twimg.com/media/HSKmXM7boAAWqfd.jpg)

## 相关概念

- [Context Engineering（上下文工程）](term-context-engineering.md) — 三篇文章都围绕上下文的设计取舍
- [Pi Coding Agent](tool-pi-coding-agent.md) — 三篇文章的对象