---
type: Tool
title: "语析 Yuxi"
description: "基于大模型的智能知识库与知识图谱智能体开发平台，把 RAG 检索、Milvus 知识图谱与 LangGraph 多智能体编排整合进统一的多租户工作台。"
resource: "https://github.com/zenghui-li/yuxi"
tags: [tool, rag, knowledge-graph, milvus, langgraph, multi-tenant, agent-platform]
timestamp: 2026-07-10T04:48:00.000Z
---

# 语析 Yuxi

## 它是什么
面向企业的智能知识库 + 知识图谱智能体开发平台，把 RAG 检索、Milvus 知识图谱、LangGraph 多智能体编排三件套塞进同一个多租户工作台。

## 为什么用它 / 适合什么场景
- 想搭一个"能跑多业务线"的智能知识库平台，而非单点 demo。
- 业务上既需要语义检索，又需要实体级知识图谱推理。
- 想用 LangGraph 编排多智能体协作（检索 agent + 写作 agent + 校对 agent 等）。

## 关键能力
| 能力 | 说明 |
|------|------|
| RAG 检索 | 大模型 + 向量检索的问答与生成 |
| 知识图谱 | 基于 Milvus 的实体关系存储与推理 |
| 多智能体编排 | LangGraph 驱动的多 agent 协作 |
| 多租户 | 多个业务 / 团队共用一套平台 |

## 媒体
![Yuxi 预览](https://pbs.twimg.com/media/HMwAv26bcAAjkTt.jpg)

## 相关概念
- [cognee](tool-cognee.md) — 同样做"AI 智能体持久长期记忆 + 知识图谱"，cognee 更偏可自托管记忆层，Yuxi 是更完整的应用平台