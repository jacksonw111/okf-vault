---
type: Tool
title: "cognee"
description: "为 AI 智能体提供跨会话、可自托管的持久长期记忆，结合知识图谱与向量检索。"
resource: "https://github.com/topoteretes/cognee"
tags: "[ai-agent, memory, knowledge-graph, rag, open-source]"
timestamp: "2026-06-29T16:00:00Z"
---

# cognee

## 它是什么
cognee 是一个开源 AI 记忆平台，专为 AI 智能体设计，提供可自托管的持久长期记忆系统。它通过知识图谱引擎把任意格式的数据（文档 / 对话 / 网页 / 数据库）转化为结构化的智能体记忆，结合向量嵌入与图推理，让代理能记住、关联和检索跨会话的知识。

![](https://pbs.twimg.com/media/HL8WlamawAIxFXj.jpg)

## 为什么用它 / 适合什么场景
- **AI 代理每次新会话都从零开始**：cognee 把每次会话的知识沉淀到图 + 向量库，下次会话代理自动召回。
- **RAG 只做语义相似，缺关系推理**：cognee 的知识图谱能表达实体间的关系，回答「这两个概念怎么关联」类问题。
- **数据要自己掌控**：自托管部署，知识不出本地。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多源数据接入 | 文档 / 对话 / 网页 / DB / API |
| 知识图谱构建 | 自动抽取实体与关系 |
| 向量检索 | 语义相似匹配 |
| 图推理 | 在图上做多跳查询 |
| 自托管 | 数据不出本地 |
| 代理 SDK | Python SDK 直接接入 |

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071534892639539534)
- [项目链接](https://github.com/topoteretes/cognee)

## 相关概念
- [EverOS](./tool-everos.md) — 同样是统一的本地长期记忆层，定位是不同 agent 共享记忆底座
- [Brigade](./tool-brigade.md) — 本地多 AI 代理协作框架，自带 Tideline 共享长期记忆协议
- [second-brain-cloudflare](./tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源共享记忆层，部署门槛更低但强依赖 Cloudflare 生态