---
type: "Note"
title: "Hello-Agents（Datawhale 全覆盖 Agent 教学项目）"
description: "手搓 ReAct 到 RL 训 Agent 的全覆盖 Agent 教学项目，主张穿透框架表象、从核心原理出发亲手构建自己的多智能体应用：基础 / 构建 LLM Agent / 高级扩展 / 案例进阶四部分 15 章。"
resource: "https://github.com/datawhalechina/hello-agents"
tags: "[agent, education, react, rag, mcp, agentic-rl, multi-agent, datawhale]"
timestamp: "2026-09-16T16:18:00Z"
---

# Hello-Agents（Datawhale 全覆盖 Agent 教学项目）

## 它是什么

[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) 是 Datawhale 出品的**全覆盖 Agent 教学项目**，从**手搓 ReAct** 一路讲到 **RL 训 Agent**。项目主张：

> 穿透框架表象，从核心原理出发，亲手构建属于自己的多智能体应用。

可贵之处在于不只是教程——**穿插了大量错误案例与调优经验**（很多教程忽略这一点）。

## 全书结构

| 部分 | 章节 | 主题 |
|------|------|------|
| 第一部分 基础 | 第一章 | 初识智能体：定义 / 类型 / 范式 / 应用 |
| | 第二章 | 智能体发展史：符号主义 → LLM 驱动 |
| | 第三章 | 大语言模型基础：Transformer / 提示 / 主流 LLM / 局限 |
| 第二部分 构建你的 LLM 智能体 | 第四章 | 经典范式构建：手搓 ReAct / Plan-and-Solve / Reflection |
| | 第五章 | 低代码平台：Coze / Dify / n8n（仅做对照） |
| | 第六章 | 框架开发实践：AutoGen / AgentScope / LangGraph |
| | 第七章 | 从 0 构建 Agent 框架 |
| 第三部分 高级扩展 | 第八章 | 记忆与检索：记忆系统 / RAG / 存储 |
| | 第九章 | 上下文工程：持续交互的「情境理解」 |
| | 第十章 | 通信协议：MCP / A2A / ANP 解析 |
| | 第十一章 | Agentic-RL：从 SFT 到 GRPO 实战训练 LLM |
| | 第十二章 | 性能评估：核心指标 / 基准测试 / 评估框架 |
| 第四部分 案例进阶 | 第十三章 | 智能旅行助手：MCP + 多智能体协作 |
| | 第十四章 | 自动化深度研究 Agent：DeepResearch 复现 |
| | 第十五章 | 赛博小镇：Agent 模拟社会动态 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 从原理出发 | 不只教 API 用法，讲透范式由来 |
| 错误案例穿插 | 真实调优经验，对应工程实战痛点 |
| 覆盖 Agentic-RL | SFT 到 GRPO 的 LLM Agent 训练链路 |
| MCP / A2A / ANP | 完整通信协议解析 |
| 上下文工程整章 | 单列一章持续交互的情境理解 |
| 三个完整案例 | 旅行助手 / DeepResearch / 赛博小镇 |

## 相关概念

- [AI Agent Book](./note-ai-agent-book.md) — 同为 Agent 系统性入门资料
- [AgentScope](./tool-agentscope.md) — 第六章框架开发实践提及的框架之一
- [Context Engineering](./term-context-engineering.md) — 第九章专章覆盖
- [MCP](./term-mcp.md) — 第十章专章覆盖