---
type: "Tool"
title: "llmaker（一条命令搭私有 LLM 应用栈）"
description: "Go 写的开源 CLI 工具，用一条命令通过 Docker 编排私有 LLM 应用栈：模型 / Qdrant 向量库 / 嵌入服务 / Redis 缓存 / Langfuse 监控 / LangGraph Agent 全打包，栈定义用声明式 YAML。"
tags: "[ai, llm, rag, docker, self-hosted, agent]"
timestamp: "2026-06-27T13:24:00.000Z"
resource: "https://github.com/raiyanyahya/llmaker"
---

# llmaker（一条命令搭私有 LLM 应用栈）

## 它是什么

[`llmaker`](https://github.com/raiyanyahya/llmaker) 是一个**开源 Go CLI**，通过 Docker 把一整套私有 LLM 应用栈编排起来——一条命令就能跑起 RAG、语音助手、代码助手、FAQ、推荐引擎等完整应用，无需任何第三方 API。栈定义是**声明式 YAML**，`apply --prune` 自动编排与清理。

![私有 LLM 应用栈界面](https://pbs.twimg.com/media/HLz-fO0aAAAeyJ6.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键编排 | 一条命令拉起整条 LLM 应用栈 |
| Docker 化 | 模型 / 向量库 / 嵌入 / 缓存 / 监控 / Agent 全容器化 |
| 声明式 YAML | 栈定义可版本化、可复用 |
| 自动清理 | `apply --prune` 收敛 orphan 资源 |
| 多应用适配 | RAG / 语音助手 / 代码助手 / FAQ / 推荐引擎 |

## 内置组件

| 组件 | 角色 |
|------|------|
| 模型服务 | 本地大模型推理 |
| Qdrant | 向量数据库 |
| Embedding | 嵌入服务 |
| Redis | 缓存层 |
| Langfuse | LLM 调用监控与可观测 |
| LangGraph | Agent 编排 |

## 适用场景

- 想自托管一套 LLM 应用但不想一个个手动部署
- 团队 / 个人需要一个统一可复用的栈模板
- 需要 LLM 可观测性（Langfuse）+ Agent 编排（LangGraph）开箱即用

## 参考链接

- [项目链接](https://github.com/raiyanyahya/llmaker)

## 相关概念

- [12-Factor Agents](tool-12-factor-agents.md) — 把 Agent 当工程系统来设计的原则集合
- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — 桌面侧另一类本地优先 AI 工作台