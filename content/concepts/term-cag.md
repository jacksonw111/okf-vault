---
type: "Term"
title: "CAG（Cache-Augmented Generation，缓存增强生成）"
description: "把相对固定的知识提前放进上下文并缓存 KV Cache，查询时直接用、不再每次走向量检索的 RAG 替代方案；适合中小规模、内容稳定的知识库。"
resource: "https://github.com/hhhuang/CAG"
tags: "[rag, kv-cache, llm, term, ai-knowledge]"
timestamp: "2026-09-11T22:10:00Z"
---

# CAG（Cache-Augmented Generation，缓存增强生成）

## 定义

**CAG**（Cache-Augmented Generation，缓存增强生成）是一种**替代 RAG 的检索范式**：

> 把相对固定的知识**提前放进上下文**并缓存 **KV Cache**，查询时直接用、不再每次走向量检索。

## 与 RAG 的对比

| 维度 | RAG | CAG |
|------|-----|-----|
| 检索 | 每次问都检索向量库 | 不检索，直接用缓存的 KV |
| 知识更新 | 文档变化即重检索 | 知识固定才适合 |
| 延迟 | 受检索 + Embedding 拖累 | 直接 cache hit |
| 维护成本 | 分块 / Embedding / 向量库一条龙 | 一次性预计算 KV |
| 适用规模 | 大 / 频繁更新 | 中小 / 内容稳定 |

## 为什么用它 / 适合什么场景

- FAQ / 产品文档 / 代码说明等**中小规模、内容稳定**的知识库。
- 不想维护向量库的工程团队。
- 想降低 RAG 的延迟与运维成本。

## 不适合场景

- 数据量特别大、更新特别频繁——仍然走 RAG 或 **CAG + RAG 混合**。

## 参考链接

- 项目仓库：<https://github.com/hhhuang/CAG>

## 媒体

- ![](https://pbs.twimg.com/media/HRr-urvacAAvX5a.png)

## 相关概念

- [PixelRAG](./tool-pixelrag.md) — Berkeley 多模态 RAG（视觉版）
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) — OKF 自动补全 agent
</content>
</invoke>