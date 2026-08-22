---
type: Tool
title: "TrueForge（dorucioclea/trueforge）"
description: "把 LLM 变成能干活 Agent 的运行时层：执行循环 / 工具调用 / 沙箱 / 会话管理打包成一套，开箱即用"
resource: "https://github.com/dorucioclea/trueforge"
tags: "[agent-harness, llm, sandbox, runtime, tools]"
timestamp: "2026-08-22T15:16:00Z"
---

# TrueForge（dorucioclea/trueforge）

## 它是什么
[`dorucioclea/trueforge`](https://github.com/dorucioclea/trueforge) 是一套把 LLM 包装成「能干活的 Agent」的运行时层（harness）——**执行循环、工具调用、沙箱隔离、会话管理**这些通常要自己拼的脏活，被一次性封装好，让开发者只关心「这个 Agent 该干什么」。

## 为什么用它 / 适合什么场景
- 想做 Agent 应用但被 Codex / Claude Code / Hermes / Pi / DSH 这些术语绕晕的人，可以把 TrueForge 当作一个中立、可读的参考实现。
- 想自己拼 harness 但需要先看「别人已经做了哪些层」的工程师。
- 想给同事 / 老板讲「为什么 Agent 项目一定要用 harness 而不是裸 prompt」时的最小可演示样本。

## 关键能力
| 能力 | 说明 |
|------|------|
| 执行循环 | 内置标准 Agent loop：模型推理 → 解析 → 调工具 → 回灌 |
| 工具抽象 | 工具以统一接口注册，Agent 无需感知实现差异 |
| 沙箱隔离 | 工具调用默认跑在受限环境，避免误操作宿主机 |
| 会话管理 | 多轮上下文持久化与恢复，跨重启可继续 |
| 角色拆分 | 与平台具体模型解耦，可换底层 LLM |

## 媒体
- ![](https://pbs.twimg.com/media/HQT_TQYbkAAgc-d.jpg)

## 相关概念
- [dsh-rs](./tool-deepseek-harness-rs.md) — 同类「把 LLM 装进可执行壳」的 Rust CLI 实现
- [Fable Harness](./tool-fable-harness.md) — 把 Claude Code 行为纪律化的 harness
- [Jixu](./tool-jixu.md) — TypeScript 生态下的单 Agent Harness，思路同源但更轻量
