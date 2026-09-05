---
type: Tool
title: "LedgeIndex"
description: "开发者文档抓取 / 分块 / 嵌入 / 索引工具，提供带引用出处的可信问答与检索，把文档变成可信赖的答案源"
resource: "https://github.com/ledgeindex/ledgeindex"
tags: [rag, embedding, documentation, search, qa]
timestamp: 2026-09-05T15:00:00Z
---

# LedgeIndex

## 它是什么
`ledgeindex/ledgeindex` 是一款**文档转可信问答索引的工具**：把开发者文档抓取、分块、嵌入并建立索引，提供**带引用出处的问答与检索**，让模型基于文档回答时能挂上原文位置，回答可追溯、可验证。

## 为什么用它 / 适合什么场景
- 想给内部 SDK / API 文档搭一个带引用出处的智能问答，而不是单纯聊天。
- 不希望模型「编」答案——每条结论都要可回溯到原始文档某段。
- 研发支持 / 客服 / 新人 onboarding 场景：让 AI 帮新人查文档，但保留审计证据。

## 关键能力
| 能力 | 说明 |
|------|------|
| 文档抓取 | 自动从文档源（站点 / 仓库 / 文件）抓取内容 |
| 分块 | 切分为适合嵌入的小段 |
| 嵌入与索引 | 构建可检索的向量 / 关键词索引 |
| 带引用问答 | 回答时附带原文出处，可点击跳转验证 |
| 检索 API | 供前端 / agent 调用的搜索接口 |

## 媒体
- ![](https://pbs.twimg.com/media/HRYS5DGbYAE7i-T.jpg)

## 相关概念
- [原始链接](https://github.com/ledgeindex/ledgeindex)