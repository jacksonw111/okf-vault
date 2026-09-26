---
type: "Tool"
title: "LoopX（长时运行 AI Agent 的状态管理中间件）"
description: "huangruiteng 出品的 AI Agent 状态层：把目标 / 待办 / 进度证据 / 配额统统落盘，重启不丢；不锁死某一家 Agent Harness——Codex / Claude Code / Cursor 都能接进来，换 Agent 上下文照样在；每轮执行自动留痕便于复盘交接。"
resource: "https://github.com/huangruiteng/loopx"
tags: "[agent, state-management, long-running, context-engineering, harness, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# LoopX（长时运行 AI Agent 的状态管理中间件）

## 它是什么

[LoopX](https://github.com/huangruiteng/loopx) 是 huangruiteng 开源的 **AI Agent 状态管理中间件**——给**长时运行**的 Coding Agent 补一层「**目标 / 待办 / 进度证据 / 配额**」的持久化：

- 上下文被压缩了？→ 状态不丢，重启可恢复
- 方向跑偏？→ 目标和待办还在盘上，可随时校准
- 进度说不清？→ 每轮执行干了什么、改了什么都会留痕

## 关键能力

| 能力 | 说明 |
|------|------|
| 持久化 | 目标 / 待办 / 进度证据 / 配额 全部落盘 |
| 跨 Agent | Codex / Claude Code / Cursor 都能接，换 Agent 上下文保留 |
| 留痕 | 每轮干了什么、改了什么自动记录 |
| 重启续 | 跨天任务断了也能接上 |
| 复盘 | 历史动作可追溯，便于交接 |

## 为什么用它 / 适合什么场景

- 跑**跨天 / 长链路** Agent 任务，常被上下文压缩或重启打断。
- 想**切换 Agent Harness**（比如从 Codex 换到 Claude Code）时不丢失上下文。
- 团队协作需要**交接 Agent 进度**——LoopX 让交接像 Git log 一样有迹可循。
- 想给 Agent 加一层**治理层**（配额 / 目标 / 待办 / 证据）而不是只靠 LLM 自己记。

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — 把 LLM 包成稳定可治理产品的工程实践，LoopX 是其一个具体实现
- [HarnessRouter](./tool-harness-router.md) — 把多个 Agent Harness 收进同一 API 网关；LoopX 在更下游做状态持久化
- [Context Engineering（上下文工程）](./term-context-engineering.md) — 围绕上下文窗口的选 / 排 / 省，LoopX 通过落盘绕开窗口限制
- [Orca 工单编排](./playbook-orca-ticket-orchestration.md) — 另一种「长链路 Agent 治理」思路