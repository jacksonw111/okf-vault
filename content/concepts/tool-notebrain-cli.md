---
type: Tool
title: "NoteBrain CLI"
description: "把 Obsidian 笔记库离线索引到本地 ChromaDB 向量库，给 AI 编码智能体与命令行脚本提供语义搜索、wikilink 图遍历与隐藏关联发现的 JSON 接口。"
resource: "https://github.com/nmdra/notebrain-cli"
tags: [tool, obsidian, vector-db, chromadb, semantic-search, rag, agent]
timestamp: 2026-07-10T01:20:00.000Z
---

# NoteBrain CLI

## 它是什么
命令行工具，把 Obsidian 笔记库离线索引进本地 ChromaDB 向量库，并对外暴露 JSON 接口，让 AI 编码 agent 或 shell 脚本能直接做语义搜索、wikilink 图遍历与"你不知道但相关"的隐藏关联发现。

## 为什么用它 / 适合什么场景
- 想让 Claude Code / Cursor / Codex 在写代码时参考自己的 Obsidian 笔记语义搜索。
- 想给本地知识库加 RAG 检索但不想自建 Embedding / 向量库管线。
- 想用脚本批量发现笔记之间"未链接但语义相关"的潜在关联。

## 关键能力
| 能力 | 说明 |
|------|------|
| 离线索引 | 一次性把 Obsidian vault 索引进本地 ChromaDB |
| 语义搜索 | 基于 Embedding 的相似度检索，远超关键词搜索 |
| wikilink 遍历 | 沿 `[[...]]` 链接做图遍历 |
| 隐藏关联 | 发现"未显式链接但语义相关"的笔记对 |
| JSON 接口 | CLI 输出 JSON，agent 与脚本都能消费 |

## 媒体
![NoteBrain CLI 预览](https://pbs.twimg.com/media/HMsC8AHbEAAwxqw.jpg)

## 相关概念
- [Obsidian](tool-obsidian.md) — NoteBrain 的数据源就是 Obsidian vault
- [LLM Wiki 模式](term-llm-wiki.md) — NoteBrain 是 LLM Wiki 的"语义检索引擎"实现层