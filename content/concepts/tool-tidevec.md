---
type: "Tool"
title: "TideVec（ashishodu2023/TideVec）"
description: "带时间衰减的向量数据库：把时间衰减直接算进 HNSW 检索打分，旧文档自动降权，不用重新嵌入、不用手动设 TTL。"
resource: "https://github.com/ashishodu2023/TideVec"
tags: [vector-db, hnsw, time-decay, rag, embeddings, retrieval]
timestamp: "2026-08-05T00:45:00Z"
---

# TideVec（ashishodu2023/TideVec）

## 它是什么

**TideVec** 是一款**带时间衰减的向量数据库**，专为解决「**RAG 检索质量随嵌入老化逐年下滑**」的问题。

大多数向量数据库（Chroma / Milvus / Weaviate / pgvector 等）在检索时**不分数据新旧**——18 个月前插入的文档和昨天的排同一位。TideVec 把**时间衰减**直接算进 **HNSW 检索打分**：

- 旧文档自动降权。
- **不用重新嵌入**（昂贵的 batch 任务）。
- **不用手动设 TTL**（容易误杀重要长尾文档）。

## 为什么用它 / 适合什么场景

- 长期运行的 RAG 系统（知识库 / 客服 / 企业内部搜索）。
- 文档半衰期差异大（如新闻、财报、技术博客）。
- 想用「新鲜度」作为隐式排序信号，而非硬切。

## 关键能力

| 能力 | 说明 |
|------|------|
| 时间衰减打分 | 把 freshness 直接融入 HNSW 距离打分 |
| 不重新嵌入 | 不需要昂贵的再嵌入批任务 |
| 不需手动 TTL | 旧文档自然降权，无需人工过期 |
| HNSW 兼容 | 基于主流近似最近邻索引结构 |

## 参考链接

- [GitHub 仓库](https://github.com/ashishodu2023/TideVec)

## 相关概念

- [Amber（向量嵌入自验证便携文件）](./tool-amber-vector-commitment.md) — 同属「向量数据库 / 嵌入管理」领域，可对照完整性校验
- [NeoSearch](./tool-neosearch.md) — 另一款去重去追踪的 AI 搜索引擎，对照实现思路