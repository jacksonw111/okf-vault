---
type: "Tool"
title: "pi-fabric（Pi 多工具合成 TypeScript 执行器）"
description: "Pi 编码助手扩展：把多个工具调用合成一段 TypeScript 程序，由 fabric_exec 执行，运行前过类型检查，模型无需反复拼接零散步骤。"
tags: "[pi, agent, typescript, code-execution, tool-chaining]"
timestamp: "2026-08-15T07:18:00Z"
resource: "https://github.com/monotykamary/pi-fabric"
---

# pi-fabric（Pi 多工具合成 TypeScript 执行器）

## 它是什么

`monotykamary/pi-fabric` 是 Pi Coding Agent 的扩展，提出一种「**把多次工具调用合成一段 TypeScript 程序**」的范式：

- 多个工具被封装成可被 `fabric_exec` 调用的 TypeScript 函数。
- 模型不必一次发一条工具调用，而是直接写一段调用这些函数的 TypeScript 代码。
- `fabric_exec` 在执行前先过一遍 TypeScript 类型检查，保证参数合法。

> ![](https://pbs.twimg.com/media/HPpgudga0AA-BFh.jpg)

## 为什么用它 / 适合什么场景

- **避免反复拼接零散步骤**：传统 agent 框架里，模型要分多次工具调用完成「读 A → 解析 → 调 B → 写 C」这类组合任务，每步都可能因上下文丢失而出错。
- **类型检查兜底**：TS 在运行前先校验参数类型，发现问题直接报错，不必等到运行失败。
- **可调试**：每段 fabric_exec 的输入输出都是一段 JS，便于事后审计。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工具 → TS 函数映射 | 把 agent 工具暴露成可直接 import 的 TS 函数 |
| `fabric_exec` | 执行合成 TS 代码的统一入口 |
| 运行前类型检查 | tsc 先校验参数，再调用实际工具 |
| 组合任务原子性 | 多工具 / 多数据源的组合任务写在同一段代码里 |
| 错误前置 | 类型不匹配 / 缺失字段，运行前就失败 |
| 可观测 | 每次执行的输入 / 输出 / 中间值都可记录 |

## 与相关范式的差异

| 范式 | 工具调用方式 | 适合 |
|------|-------------|------|
| 传统 ReAct | 多次独立工具调用 | 简单、每步需独立决策的任务 |
| [CodeAct](tool-12-factor-agents.md) | 让 LLM 生成 Python 代码调工具 | 偏 Python 生态 |
| **pi-fabric** | 生成 TS 代码 + 运行前类型检查 | **TypeScript 生态 + 强类型校验** |

## 适用人群

- Pi Coding Agent 用户，工具调用量大、且任务经常组合。
- 想给 agent 加一层「类型安全」的人。
- TypeScript 重度用户，希望 agent 输出的代码可被自己的工程直接复用。

## 参考链接

- [项目链接](https://github.com/monotykamary/pi-fabric)

## 相关概念

- [pi-claude-bridge](tool-pi-claude-bridge.md) — Pi 接入 Claude Code 的桥接扩展
- [12-Factor Agents](tool-12-factor-agents.md) — 12 条让 Agent 从 demo 到实盘的工程原则
- [pi-task](tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展