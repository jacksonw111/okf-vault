---
type: "Tool"
title: "OpenKB（VectifyAI 出品的结构化 Wiki 知识库生成器）"
description: "VectifyAI 开源工具，把 PDF / 论文 / 文档直接整理成结构化 Wiki 知识库：超长文档 + 多模态 + 不依赖向量数据库，基于 PageIndex 构建树状索引让 AI 按文档结构推理检索。"
resource: "https://github.com/VectifyAI/OpenKB"
tags: "[rag, knowledge-base, wiki, pageindex, vectifyai, document, tree-index, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# OpenKB（VectifyAI 出品的结构化 Wiki 知识库生成器）

## 它是什么

[OpenKB](https://github.com/VectifyAI/OpenKB) 是 [VectifyAI](https://github.com/VectifyAI) 开源的结构化 Wiki 知识库生成工具，针对传统 RAG「查一次、检索一次、知识无法沉淀」的痛点，把 PDF / 论文 / 文档一次性整理成可持续更新的结构化 Wiki 知识库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 超长文档 | 支持超长文档与多模态内容（不依赖向量数据库） |
| 树状索引 | 基于 PageIndex 构建树状索引，让 AI 按文档结构进行推理检索 |
| 自动交叉引用 | 自动生成交叉引用、概念页与实体页 |
| 持续更新 | 知识可持续更新，无需每次从零检索 |
| 多产物 | 一键生成 Agent Skill、幻灯片、知识图谱 |

## 与传统 RAG 的差异

| 维度 | 传统 RAG | OpenKB |
|------|----------|--------|
| 检索方式 | 向量相似度 / 切片 | 树状索引 + LLM 推理 |
| 知识沉淀 | 每次查都要重新检索 | 一次整理持续复用 |
| 输出形态 | 临时回答 | Wiki 概念页 + 实体页 + 交叉引用 |
| 文档能力 | 受限于切片长度 | 完整支持超长 + 多模态 |

## 媒体预览

![](https://pbs.twimg.com/media/HTTRAx6aYAEurUu.png)

## 原始链接

- 项目主页：<https://github.com/VectifyAI/OpenKB>

## 相关概念

- [PageIndex（VectifyAI 树状索引 RAG）](./tool-pageindex.md) — OpenKB 底层的树状索引 + LLM 推理检索核心
- [RAG（检索增强生成）](./term-rag.md) — 通用 RAG 概念背景