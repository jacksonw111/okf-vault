---
type: "Tool"
title: "Pi Durable（Cloudflare Agents SDK 集成的 Pi 持久化层）"
description: "Cloudflare 在 Agents SDK 中集成 Pi Durable 模块（harness/pi/harness.ts），让 Cloudflare Workers 上的 Agent 能复用 Pi 编码 Agent 的持久化能力——badlogicgames（Pi 作者）确认「it just works」，底层直接复用 Pi 的会话 / 状态 / Harness 抽象。"
resource: "https://github.com/cloudflare/agents/blob/df9c0ef6c4541c5552b5ce4d6ba292162dbd0908/packages/agents/src/harness/pi/harness.ts"
tags: "[cloudflare, agents-sdk, pi, persistence, durable, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# Pi Durable

## 它是什么

**Pi Durable** 是 [Cloudflare 在其 Agents SDK 中集成的 Pi 持久化模块](https://github.com/cloudflare/agents/blob/df9c0ef6c4541c5552b5ce4d6ba292162dbd0908/packages/agents/src/harness/pi/harness.ts)——把 Pi 编码 Agent 项目的 **会话持久化 / 状态管理 / Harness 抽象**直接复用到 Cloudflare Agents SDK，让在 Workers 上跑的 Agent 拥有和 Pi 本地一样的「持久会话、跨调用保留上下文」能力。

## 为什么用它 / 适合什么场景

- **Cloudflare Agent 想要持久会话**：传统 Workers 单次请求模型下，Agent 状态难留存；Pi Durable 把 Pi 的状态机搬过来。
- **复用成熟 Harness**：Pi 的 Harness 设计经过作者（badlogicgames）反复打磨，Cloudflare 直接集成省去自研。
- **跨调用上下文**：用户跟 Agent 多轮交互不必每轮重新喂历史。

## 关键能力

| 能力 | 说明 |
|------|------|
| 集成位置 | Cloudflare Agents SDK（`packages/agents/src/harness/pi/harness.ts`） |
| 上游项目 | Pi 编码 Agent（earendil-works/pi） |
| 提供能力 | 会话持久化 + 状态管理 + Harness 抽象 |
| 形态 | TypeScript 模块，可被 Worker 直接 import |
| 状态 | 官方集成，作者确认「it just works」 |

## 参考链接

- 项目链接：<https://github.com/cloudflare/agents/blob/df9c0ef6c4541c5552b5ce4d6ba292162dbd0908/packages/agents/src/harness/pi/harness.ts>

## 相关概念

- [Pi Coding Agent](./tool-pi-coding-agent.md) — Pi Durable 的上游
- [Cloudflare Clef](./tool-cloudflare-clef.md) — 同为 Cloudflare 周边 AI 工具
