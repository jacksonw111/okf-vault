---
type: "Note"
title: "earendil.com/posts 文章集（Agent 设计原理）"
description: "earendil.com/posts 上 7 篇被社区点名的 Agent 设计原理文章合集：Measuring the Sloppiness of Code / Harness 解析 / Compaction / Prompt Caching / Minimal Pi / Session 限制等。"
resource: "https://earendil.com/posts/"
tags: "[agent, harness, pi, compaction, prompt-cache, article, learning-path]"
timestamp: "2026-09-24T21:55:00Z"
---

# earendil.com/posts 文章集（Agent 设计原理）

## 它是什么

[earendil.com/posts/](https://earendil.com/posts/) 上 pidotdev 写的 7 篇被社区反复点名的 Agent 设计原理文章合集——读完一遍「对整个 Agent 的设计和原理都有一个很深的理解」。

## 文章清单

| # | 标题 | 主题 |
|---|------|------|
| 1 | Measuring the Sloppiness of Code | 量化代码的「脏」程度 |
| 2 | There are many agent harnesses, but this one is mine. | 作者视角的 harness 选型 |
| 3 | What is a Harness? | Harness 入门科普 |
| 4 | How Compaction Works in Pi | Pi 中的上下文压缩原理 |
| 5 | Pi, Minimal and Performant | Pi 极简且高性能的设计 |
| 6 | The Session You Cannot Take With You | 长会话的会话持久化边界 |
| 7 | Prompt Caching In Agents | Agent 中的 prompt 缓存 |

## 适合谁读

- 想系统理解 Agent 的内部设计（不只看 API 调用）
- 在做 harness / coding agent 项目，想参考别人的取舍
- 想补齐「为什么这么设计」的体系化知识

## 阅读顺序建议

1. 先读 **What is a Harness?**（已有概念 [note-earendil-agent-harness](./note-earendil-agent-harness.md)）建立概念
2. 再读 **Measuring the Sloppiness of Code** 看作者怎么量化设计取舍
3. 然后按顺序读 **Compaction / Prompt Caching / Session** 三篇，理解 Agent 性能与持久化的核心机制
4. 最后读 **Pi, Minimal and Performant** 与 **There are many agent harnesses** 看综合视角

## 原始链接
- 文章列表：<https://earendil.com/posts/>

## 相关概念
- [What is a Harness（earendil 入门科普长文）](./note-earendil-agent-harness.md) — 同作者的另一篇 Harness 入门长文
- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — Harness 工程的整体方法论