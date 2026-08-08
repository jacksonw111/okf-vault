---
type: "Tool"
title: "LangGraph"
description: "LangChain 团队推出的 Agent 编排框架：用图结构描述多 Agent / 工具 / 状态之间的流转，支持循环、条件分支、持久化与人工介入。"
resource: "https://langchain-ai.github.io/langgraph/"
tags: [agent-orchestration, langchain, multi-agent, graph, framework]
timestamp: "2026-08-08T20:00:00Z"
---

# LangGraph

## 它是什么

LangGraph 是 LangChain 团队推出的 Agent 编排框架。它把多 Agent 协作、工具调用、状态流转描述成「图」（graph）而非线性链，从而天然支持循环、条件分支、持久化、人在环中等复杂场景。

## 为什么用它 / 适合什么场景

- 想让 Agent 之间有清晰的状态机 / 状态图，而非「单 Agent 多工具」线性流程。
- 需要 Agent 在关键节点停下来等人审批（人在环中）。
- 想用同一套框架支持多 Agent 协作、长期记忆、可视化调试。
- 已用 LangChain / LangSmith 生态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 图结构编排 | 节点 / 边 / 状态定义 Agent 协作 |
| 持久化 | 内置 checkpointer，支持中断 / 恢复 |
| 人在环中 | `interrupt_before` / `interrupt_after` 触发人工介入 |
| Streaming | 节点级 streaming，逐步回传中间状态 |
| 可视化 | LangGraph Studio / LangSmith 调试 |
| LangChain 集成 | 与 LangChain 生态（tool / model / retriever）无缝衔接 |

## 相关概念

- [RepoPilot](./tool-repopilot.md) — 基于 LangGraph 的多角色 Agent 协作软件工程工具
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化原则