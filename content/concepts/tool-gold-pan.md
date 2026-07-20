---
type: "Tool"
title: "GoldPan（多模态数据提取 + 本地 RAG 工作台）"
description: "隐私优先的多模态数据提取与本地 RAG 工作台：把 PDF、图片、音频、YouTube 和动态网页转成 AI 能用的 Markdown，并存进 100% 本地的向量库。"
resource: "https://github.com/ptai-eng/GoldPan"
tags: "[rag, local-rag, multimodal, document, privacy, vector-db]"
timestamp: "2026-07-20T20:20:00Z"
---

# GoldPan（多模态数据提取 + 本地 RAG 工作台）

## 它是什么

[ptai-eng/GoldPan](https://github.com/ptai-eng/GoldPan) 是**隐私优先**的本地 RAG 工作台：把 PDF、图片、音频、YouTube、动态网页等异构源一起吃进来，**全部解析为 Markdown**，并落到**100% 本地的向量库**——任何数据不出本机。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模态解析 | PDF / 图片 / 音频 / YouTube / 动态网页都吃 |
| 统一为 Markdown | 异构源全部转 Markdown，便于下游 agent 直接用 |
| 100% 本地向量库 | 数据完全不出本机 |
| 面向 RAG | 输出格式可直接喂给 LLM 做问答 / 检索 |

![GoldPan 截图](https://pbs.twimg.com/media/HNhItRabwAAKKFF.jpg)

## 相关概念

- [Notebrain CLI](./tool-notebrain-cli.md) — 把 Obsidian 笔记库离线索引到本地 ChromaDB，给 agent 语义搜索
- [HermitUI](./tool-hermitui.md) — 本地优先 AI 聊天界面（HTML 单文件）

## 参考链接

- 项目链接: <https://github.com/ptai-eng/GoldPan>
