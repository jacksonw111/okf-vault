---
type: "Tool"
title: "PageIndex（VectifyAI 树状索引 RAG 框架）"
description: "VectifyAI 开源 PageIndex：彻底抛弃向量检索与切片，改用「树状索引 + LLM 推理」架构解决长文档 RAG 准确率问题。FinanceBench 准确率 98.7%（传统向量 RAG 仅约 50%），千页文档索引成本约 1 美元，420 页查询 token 消耗降低 16.6×。"
resource: "https://github.com/VectifyAI/PageIndex"
tags: "[rag, pageindex, vectifyai, tree-index, long-document, finance-bench, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# PageIndex（VectifyAI 树状索引 RAG 框架）

## 它是什么

[PageIndex](https://github.com/VectifyAI/PageIndex) 是 VectifyAI 开源的 RAG 框架：彻底抛弃向量检索与切片（Chunking），改用「树状层级索引 + LLM 推理」的架构，直接解决长文档检索中最致命的痛点——相似度 ≠ 相关度。

## 它要解决的问题

处理财报 / 法律合同 / 技术手册等长难文档时，传统向量 RAG 经常翻车。核心原因：**相似度（Similarity）不等于相关度（Relevance）**。向量相似度检索本质是「语义氛围匹配」，面对复杂逻辑跳转和上下文依赖，常常找出一堆「看着相似但毫无用处」的内容，反而漏掉真正关键的信息。

## 关键设计

| 设计 | 说明 |
|------|------|
| 树状索引构建 | 从文档版面解析出逻辑树结构，再用轻量模型对节点做总结与提炼，完全不需要分块和向量嵌入 |
| LLM 推理检索 | 面对提问时，Agent 像翻书查阅目录一样，逐层推理并定位目标章节与段落，检索路径全程清晰、可追溯 |

灵感来自 AlphaGo，模拟人类专家的阅读逻辑。

## 实测表现

| 指标 | 数值 | 对比 |
|------|------|------|
| FinanceBench 准确率 | 98.7% | 传统向量 RAG 仅约 50% |
| 千页文档索引成本 | 约 1 美元 / 几分钟 | 极低成本 |
| 420 页文档查询成本 | 降低 16.6× | 相比整篇喂入 LLM |

## 部署形态

- **本地 SDK**：完全私有化运行
- **云端版**：扩展 OCR、多文档 File System、MCP Server 支持

## 媒体预览

视频：<https://video.twimg.com/tweet_video/HTW-xjVW0AA7Vf4.mp4>

## 原始链接

- 项目主页：<https://github.com/VectifyAI/PageIndex>

## 相关概念

- [OpenKB](./tool-openkb.md) — 基于 PageIndex 构建的结构化 Wiki 知识库生成器
- [RAG（检索增强生成）](./term-rag.md) — 通用 RAG 概念背景
- [weknora](./tool-weknora.md) — 腾讯开源的企业级 LLM 知识平台（RAG + ReAct Agent）