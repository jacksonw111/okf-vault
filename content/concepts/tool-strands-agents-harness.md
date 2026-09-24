---
type: "Tool"
title: "Strands Agents Harness SDK（Amazon 出品）"
description: "Amazon 出品的 AI Agent Harness SDK，Python / TypeScript 双 SDK，内置生命周期控制 / tools + structured output / MCP / 多 agent / 记忆与会话 / 模型可移植 / 流式 / 护栏 / tracing / evals 等可复用能力。"
resource: "https://github.com/strands-agents/harness-sdk"
tags: "[agent, harness, sdk, amazon, python, typescript, mcp, multi-agent, tracing, evals, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Strands Agents Harness SDK（Amazon 出品）

## 它是什么

[Strands Agents Harness SDK](https://github.com/strands-agents/harness-sdk) 是 Amazon 出品的、用 Python / TypeScript 构建和运行 AI Agent 的开源 Harness SDK。在 README 中明确列出一组可复用的 Agent 能力，覆盖「从单步调用到生产级治理」的完整链路。

## 内置 Agent 能力

| 能力 | 说明 |
|------|------|
| 生命周期控制 | turn limits、token budgets、cancellation、stop reasons |
| tools + structured output | 工具注册与结构化输出 |
| MCP | Model Context Protocol 支持 |
| 多 agent 模式 | 子 agent 派发与协调 |
| 记忆与会话 | memory + sessions 持久化 |
| 模型可移植 | model portability，换模型不绑死 |
| 流式 | streaming 输出 |
| 护栏 | guardrails，错误运行前拦截 |
| 追踪 | tracing，默认 trace 每个决策 |
| evals | 评估与回归 |

## 适合谁用

- 想用 Amazon 出品的稳定 SDK 起 agent 项目
- 想一份 SDK 同时覆盖 Python 与 TypeScript（前后端 / 工具链）
- 需要内置「生命周期 / 护栏 / tracing / evals」等生产级特性

## 原始链接
- 项目主页：<https://github.com/strands-agents/harness-sdk>

## 相关概念
- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — Harness 工程的整体方法论
- [What is a Harness（earendil 入门科普）](./note-earendil-agent-harness.md) — Harness 入门科普