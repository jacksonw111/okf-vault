---
type: "Tool"
title: "Hindsight（vectorize-io：Agent 仿生记忆网络）"
description: "vectorize-io 开源（≈40k Star）的 Agent 记忆底座：用「世界事实 / 经历 / 观察 / 心智模型」四层仿生架构替代「向量检索即记忆」，原生集成 Claude Code / Cursor / LangGraph / CrewAI 等 60+ 框架，每个 Bank 自带 MCP 端点。"
resource: "https://github.com/vectorize-io/hindsight"
tags: "[agent-memory, bionic, vector-rag, bm25, knowledge-graph, mcp, claude-code, cursor]"
timestamp: "2026-09-28T23:45:00Z"
---

# Hindsight（vectorize-io：Agent 仿生记忆网络）

## 它是什么

[Hindsight](https://github.com/vectorize-io/hindsight) 是 **vectorize-io** 开源的 **Agent 记忆底座**（GitHub 接近 40k Star）。它打破「向量检索即记忆」的局限，用**仿生认知体系**重新组织 Agent 的记忆网络。

设计哲学：现有 Agent 「长记忆」本质上是「聊天记录拼进 Prompt」或「粗糙的向量 RAG 检索」——会话一多就混乱、毫无认知沉淀。Hindsight 让 Agent **学会学习**，而不只是死记硬背。

## 四层仿生记忆架构

| 层 | 作用 |
|----|------|
| **World Facts（世界事实）** | 客观规律与外部常识 |
| **Experiences（经历记录）** | Agent 自身的行动与交互历史 |
| **Observations（信念观察）** | 后台自动去重、归纳事实形成的认知，自带引用证据链与置信度更新 |
| **Mental Models / Knowledge Pages（心智模型）** | 高频问题（如「用户偏好」「项目规范」）在后台预先提炼为常驻活文档，Agent 启动时仅需普通数据库读取，零额外 LLM 检索开销 |

## 三个极简交互原语

- **Retain**：输入新信息，LLM 后台自动抽取实体、因果关系与时间轴，结构化入库
- **Recall**：4 路混合检索（语义向量 + BM25 关键词 + 实体/因果图谱 + 时间范围过滤），经交叉编码重排输出最准上下文
- **Reflect**：记忆反思与推演，专为复杂任务规划、长效决策与归因分析设计

## 为什么用它 / 适合什么场景

- 想给 Agent 做**真正长期可用的记忆**，而非「对话记录 → Prompt」。
- 想用**仿生分层**而非纯向量召回（语义 + BM25 + 实体/因果图谱 + 时间）。
- 项目已用 **Claude Code / Cursor / LangGraph / CrewAI** 之一——Hindsight 提供 60+ 框架的原生集成，每个 Bank 都自带 MCP 端点。
- 需要**多租户隔离**、针对 45 种敏感数据的内置隐私过滤（Memory Defense）、原生多语言保留。
- 在 LongMemEval 基准上拿到 SOTA。

## 关键能力

| 能力 | 说明 |
|------|------|
| 出品 | vectorize-io |
| 集成方式 | `wrap_openai` / `wrap_anthropic` 两行代码 |
| 检索 | 4 路混合（语义 + BM25 + 实体/因果图谱 + 时间） |
| 框架 | 60+（Claude Code / Cursor / LangGraph / CrewAI / LlamaIndex 等） |
| 协议 | 每个 Bank 自带 MCP 端点 |
| 多租户 | 原生支持 |
| 隐私 | Memory Defense（45 种敏感数据内置过滤） |
| 基准 | LongMemEval SOTA |

## 相关概念

- [RAG（检索增强生成）](./term-rag.md) — Hindsight 替代 / 升级了「朴素向量 RAG」的记忆模式
- [Recall（Claude Code 离线持久化项目记忆）](./tool-recall-claude-code.md) — Claude Code 的轻量记忆插件（与 Hindsight 的全功能记忆底座互补）