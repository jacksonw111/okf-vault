---
type: Note
title: "What is an Agent Harness（earendil 入门科普长文）"
description: "earendil.com 上 pidotdev 写的科普长文，把「agent harness」拆给想了解但不知道从哪里开始的读者：定义、组成、能力边界与生态现状。"
resource: "https://earendil.com/posts/what-is-a-harness/"
tags: [agent, harness, llm, ai, note, reading, primer]
timestamp: 2026-08-21T00:50:15Z
---

# What is an Agent Harness（earendil 入门科普长文）

## 它是什么
一篇面向「听过 agent harness 这个词但没完整用过 / 不知道从哪里开始」的读者的科普长文，把抽象概念拆成可消化的章节：什么是 harness、为什么需要它、它由哪些组件构成、与裸模型 / 工具调用框架的边界在哪里，以及生态里目前能见到的几种主流实现。

## 适合谁读
- 想给现有 LLM 加「能跑多步、能用工具、能记忆」的最小骨架，但被 Codex / Claude Code / Hermes / Pi / DSH 等一堆新词绕晕的工程师；
- 想要从零拼一个自己的 harness、但需要先了解「别人已经做了哪些层」的人；
- 给同事 / 产品 / 老板解释「为什么我们这个 agent 项目一定要用 harness 而不是裸 prompt」的人。

## 这篇能告诉你什么
- **定义**：harness = 「把一次模型推理、一次工具调用、一次会话状态串成一步可执行闭环」的运行时壳，模型本身只负责推理。
- **组成**：循环（loop）/ 工具注册 / 上下文管理 / 子代理派发 / 权限与审计 / 长会话持久化 等基本件各自承担什么角色。
- **边界**：harness 不是模型，也不是 IDE；它跟「单纯写 prompt 调函数」的关键差异在「多步 + 状态」。
- **生态**：Codex / Claude Code / Hermes / Pi / DeepSeek Harness / LongHorizon-Harness 等开源 / 闭源实现的取舍与共性。

## 一句话总结
把「harness 到底是什么、为什么需要、需要什么、不需要什么」一次性讲明白的入门级长文，比官方 README 友好，比 talk-of-the-town 严肃。

## 原始链接
- [earendil.com/posts/what-is-a-harness/](https://earendil.com/posts/what-is-a-harness/) — 原始长文

## 相关概念
- [DeepSeek Harness 生态（dsh-*）](./concepts/tool-deepseek-harness-rs.md) — 当前最被开源社区拆解 / 改造的 harness 之一
- [LongHorizon-Harness](./concepts/tool-longhorizon-harness.md) — AMAP-ML 给「几十几百步的长程任务」做的 harness
- [Fable Harness](./concepts/tool-fable-harness.md) — 把 Claude Code 行为纪律化的 harness