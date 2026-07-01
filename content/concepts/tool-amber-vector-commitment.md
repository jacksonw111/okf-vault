---
type: Tool
title: "Amber（offchainthoughts）"
description: "offchainthoughts 开源的「向量嵌入承诺」工具。把一次昂贵的向量嵌入计算冻结为自验证的便携文件，接收方可以脱离模型做完整哈希校验，也可用随机抽样重嵌入概率检测伪造向量。用 int8 量化解决跨硬件浮点不一致问题。"
tags: "[vector-embedding, rag, cryptography, commitment]"
timestamp: "2026-07-01T13:30:00Z"
resource: "https://github.com/offchainthoughts/Amber"
---

# Amber（offchainthoughts）

## 它是什么
offchainthoughts 开源的「向量嵌入承诺」（Vector Embedding Commitment）工具。核心是把一次昂贵的向量嵌入计算冻结为一个**自验证的便携文件**，接收方在不依赖原模型完整重算的前提下，既能做整体哈希校验，也能用随机抽样重嵌入概率检测伪造向量。

## 为什么用它 / 适合什么场景
- 想发布一个嵌入数据集 / 向量索引给用户，但不希望用户完整重算
- 想验证收到的向量确实是「声称的模型 + 声称的输入 + 声称的时间」算出来的
- 想做离线 RAG 而不想信任服务方的算力与诚意

## 关键能力
| 能力 | 说明 |
|------|------|
| 自验证便携文件 | 一次嵌入计算结果可冻结为可分发的文件 |
| 整体哈希校验 | 不依赖模型即可检查文件完整性 |
| 概率抽样审计 | 随机抽几条用同模型重嵌入，比对结果验真伪 |
| int8 量化 | 避免浮点数在不同硬件上的不一致，保证承诺稳定 |
| 离线 RAG 友好 | 接收方在断网 / 低算力环境也能验证 |

## 创新点
作者本人强调：离线 RAG 本身不算创新，**创新主要在这套承诺（commitment）和审计机制上**。它的本质是把「对模型的信任」转成「对承诺的密码学验证」，是对 RAG 数据供应链的一次加固。

## 相关概念
- [cognee](tool-cognee.md) — 自托管的 AI 智能体持久长期记忆（知识图谱 + 向量检索），Amber 可作其向量存储的承诺层
- [codebase-memory-mcp](tool-codebase-memory-mcp.md) — 持久化代码结构索引 MCP，Amber 概念可借鉴到代码向量索引场景
- [RAG 数据完整性校验](tool-cognee.md) — 概念上的同类问题域

## 原始链接
- [项目仓库](https://github.com/offchainthoughts/Amber)