---
type: "Tool"
title: "write-notes-like-deepseek（DeepSeek 风格决策笔记 Skill）"
description: "把 DeepSeek Harness 仓库里的「决策笔记」方法做成 Agent Skill：让 AI 写代码前先立规矩、后施工，旧决定可追溯、可校验。"
resource: "https://github.com/czm15053/write-notes-like-deepseek"
tags: "[agent-skill, deepseek, harness, decision-notes, reproducibility]"
timestamp: "2026-09-16T16:10:00Z"
---

# write-notes-like-deepseek（DeepSeek 风格决策笔记 Skill）

## 它是什么

[czm15053/write-notes-like-deepseek](https://github.com/czm15053/write-notes-like-deepseek) 把 **DeepSeek Harness 仓库里的「决策笔记」方法**封装成 **Agent Skill**：让 AI 在动手写代码之前先把决定写下来（为什么这么做 / 选了哪条路 / 拒绝哪些方案），落地后旧决定可追溯、可校验。

## 为什么用它 / 适合什么场景

- 想让 AI 写代码时不再「一次性出活」，而是每一步都有可解释的依据。
- 多人协作时希望 Agent 的选择留下审计痕迹。
- 想把 DeepSeek Harness 的实战经验沉淀为可复用 Skill，挂在自己的 agent 上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 决策前置 | 写代码前先把决策点写下来 |
| 旧决定可追溯 | 历次决策存档，方便回看 |
| 校验机制 | 当前实现与旧决定不一致时给出告警 |
| Skill 形态 | 标准 SKILL.md，可直接接入 agent harness |
| 来源透明 | 把 DeepSeek Harness 的方法论提炼成可复用的步骤 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTrDC6a4AAqpq_.jpg)

## 相关概念

- [Harness Engineering](./term-harness-engineering.md) — write-notes-like-deepseek 是 harness 工程里「决策可追溯」的具体落地
- [DeepSeek Harness Orange Book](./note-deepseek-harness-orange-book.md) — 同源 DeepSeek Harness 实战总结