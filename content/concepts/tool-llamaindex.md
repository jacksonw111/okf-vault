---
type: "Tool"
title: "LlamaIndex"
description: "面向 LLM 应用的数据框架——提供数据接入（Loader）、索引（Index）、检索（Retriever）、查询引擎（QueryEngine）等抽象，让 RAG / Agent 用统一 API 消费各种异构数据源。"
resource: "https://www.llamaindex.ai"
tags: "[llamaindex, rag, llm, agent, framework]"
timestamp: "2026-10-06T22:51:00Z"
---

# LlamaIndex

## 定义

**LlamaIndex** 是一个面向 LLM 应用的数据框架，把「数据接入 → 分块 → 索引 → 检索 → 拼装到 Prompt」的全链路抽成统一 API（Loader / NodeParser / Index / Retriever / QueryEngine / ResponseSynthesizer），让 RAG 与 Agent 用同一套抽象消费任意异构数据源（PDF、Notion、Slack、数据库、Web 等）。

## 要点

- **官网**：[llamaindex.ai](https://www.llamaindex.ai)
- **核心抽象**：`Document` / `Node` / `Index`（VectorIndex / ListIndex / TreeIndex / KeywordTableIndex 等）/ `Retriever` / `QueryEngine`
- **生态**：与 LangChain 部分重叠但更专注「数据接入与检索」；提供 `LlamaHub` 收纳各类数据 Loader；提供 `create-llama` 一键生成项目
- **典型场景**：企业知识库 RAG、Agent 多步检索、文档问答
- **观点文章**：[LlamaIndex 官方博客](https://www.llamaindex.ai/blog) 是「Agentic OCR」「RAG 反思机制」等观点的主要出处

## 相关概念

- [RAG（检索增强生成）](./term-rag.md) — LlamaIndex 主战场
- [Agentic OCR（LlamaIndex 观点）](./note-llamaindex-agentic-ocr.md) — LlamaIndex 提出的「让 LLM Agent 主动控制截图 / 缩放 / 工具调用」替代传统固定管线 OCR
