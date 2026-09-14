---
type: "Term"
title: "RAG（Retrieval-Augmented Generation，检索增强生成）"
description: "让 LLM 在回答前先从外部知识库检索相关片段，再把片段 + 问题一起喂给模型。解决模型「不知道最新 / 私有 / 专域知识」的核心范式。"
tags: "[rag, retrieval, llm, embeddings, vector-db, knowledge-base]"
timestamp: "2026-09-14T22:30:00Z"
---

# RAG（Retrieval-Augmented Generation，检索增强生成）

## 它是什么

**RAG（检索增强生成）** 是当前让 LLM 接入私有 / 最新 / 专域知识的**主流范式**：

1. **检索（Retrieval）** —— 把用户问题变成 query，从知识库（向量库 / 全文索引 / 混合检索）找出最相关的若干片段
2. **增强（Augmented）** —— 把检索到的片段作为上下文拼到 prompt 里
3. **生成（Generation）** —— LLM 基于「问题 + 检索片段」生成最终回答

## 为什么需要 RAG

- **知识时效**：模型训练有截止日期，RAG 能接实时 / 增量更新的知识
- **私有知识**：企业内部文档、产品手册、代码库不进训练集
- **可追溯**：回答里能附上引用来源
- **成本**：相比 fine-tuning，RAG 不改模型权重、迭代快
- **可控**：能拒绝答 / 加权限过滤

## 核心组件

| 组件 | 作用 | 常见选型 |
|------|------|----------|
| Embedding 模型 | 把文本 / 代码 / 表格变成向量 | OpenAI text-embedding-3 / bge-m3 |
| 向量数据库 | 高效存 / 查向量 | pgvector / Milvus / Qdrant / Weaviate |
| 重排序（Rerank） | 检索后再精排 | bge-reranker / Cohere Rerank |
| 文档加载 / 切片 | 把源文档切成可索引的小块 | LangChain / LlamaIndex |
| 生成模型 | 最终回答 | GPT-4 / Claude / Qwen |

## 演进方向

- **GraphRAG** —— 用知识图谱替代纯向量检索
- **Agentic RAG** —— agent 决定检索时机 / 多步检索
- **Hybrid Retrieval** —— 向量 + 全文 + 关键词混合
- **Multimodal RAG** —— 检索图片 / 表格 / 视频

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Agent 经常用 RAG 取领域知识
- [LLM Wiki 模式](./term-llm-wiki.md) — 一种面向 agent 消费的轻量知识库形态，可与 RAG 结合
- [awesome-llm-apps](./tool-awesome-llm-apps.md) — 大量可直接跑的 RAG 应用样例

## 参考链接

- 原始论文：<https://arxiv.org/abs/2005.11401>
