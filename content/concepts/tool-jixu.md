---
type: Tool
title: "Jixu（joe960913/Jixu）"
description: "TypeScript 单 Agent Harness：把恢复 / 重放 / 上下文延续等脏活封装成一个 API，TypeScript Agent 应用直接调"
resource: "https://github.com/joe960913/Jixu"
tags: "[typescript, agent-harness, replay, resume, context]"
timestamp: "2026-08-22T12:12:00Z"
---

# Jixu

## 它是什么
[`joe960913/Jixu`](https://github.com/joe960913/Jixu) 是面向 **TypeScript 生态**的单 Agent Harness——把 Agent 应用里通常要自己搭的「会话恢复、轨迹重放、上下文延续」等脏活打包成**一个简洁的 API**，让 TypeScript 项目用几行代码就能拥有工业级 Agent 能力，不必重复造轮子。

## 为什么用它 / 适合什么场景
- 正在用 TypeScript 写 Agent 应用，但被状态管理 / 上下文截断 / 失败重试这些基础设施活拖慢。
- 想要一个**轻量**的 harness，而不是 Hermes / Claude Code / Pi 这种完整的 CLI 工具。
- 想给现有 TypeScript 项目加一层「Agent 行为基础设施」而不是换语言。

## 关键能力
| 能力 | 说明 |
|------|------|
| 单 API 接入 | 一组函数覆盖恢复 / 重放 / 上下文延续 |
| 会话恢复 | Agent 中途崩溃后可从断点继续 |
| 轨迹重放 | 任意历史步骤可重新跑一遍，便于调试与评测 |
| 上下文延续 | 跨会话保留关键事实，不被窗口截断吃掉 |
| TypeScript 优先 | 类型友好，能直接被 Next.js / Node 服务消费 |

## 媒体
- ![](https://pbs.twimg.com/media/HQT-pR7asAASkzS.jpg)

## 相关概念
- [TrueForge](./tool-trueforge.md) — 同为「把 LLM 装进可执行壳」的运行时层，更偏中立 / 可读参考
- [Fable Harness](./tool-fable-harness.md) — 把 Claude Code 行为纪律化的 harness，方向是「纪律」而非「基础设施」
- [LongHorizon-Harness](./tool-longhorizon-harness.md) — 高德 AMAP-ML 给「几十几百步长程任务」做的 harness
