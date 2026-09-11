---
type: "Tool"
title: "PixelRAG（Berkeley 多模态 RAG）"
description: "Berkeley 团队的多模态 RAG：不急着把页面变成纯文本，而是先把网页 / PDF 渲染成视觉页面，再基于截图做检索；保留表格、图表、排版的上下文。"
resource: "https://github.com/StarTrail-org/PixelRAG"
tags: "[rag, multimodal, vision, retrieval, ai-research]"
timestamp: "2026-09-11T22:15:00Z"
---

# PixelRAG

## 它是什么

[StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG) 是 **Berkeley 团队**的多模态 RAG 项目：

> 不急着把页面变成纯文本，而是先把网页 / PDF 等内容**渲染成视觉页面**，再基于这些页面截图进行检索。

## 它解决的问题

传统 RAG 的尴尬：

> 网页明明有信息，解析完却只剩文字。
> 表格、图表、排版和信息图一旦被传统解析器拆散，原本的上下文关系也很容易跟着丢掉。

PixelRAG 的做法：

> 这样一来，AI 检索到的不只是"文字内容"，连表格长什么样、图表怎么组织、信息在哪里都能保留下来。

## 配套能力

| 能力 | 说明 |
|------|------|
| 大规模 Wikipedia 索引 | 现成可用 |
| 文字 + 图片查询 | 多模态检索 |
| Claude Code 插件 | 让 Agent 直接利用页面视觉信息 |

## 为什么用它 / 适合什么场景

- 做**多模态 RAG**、文档问答、网页理解方向研究。
- 传统文本 RAG 丢失图表 / 排版信息的场景。
- 想让 Agent 在 PDF / 网页上做\"看到形状\"的检索。

## 关键能力

| 能力 | 说明 |
|------|------|
| 视觉渲染 | 把页面渲染成视觉 |
| 截图检索 | 基于截图做检索 |
| 多模态 | 文字 + 图片查询 |
| Wikipedia 索引 | 大规模现成 |
| Claude Code 插件 | Agent 可直接用 |

## 参考链接

- 项目仓库：<https://github.com/StarTrail-org/PixelRAG>

## 媒体

- ![](https://pbs.twimg.com/media/HRsFLWqbEAEJdSa.png)

## 相关概念

- [term-cag](./term-cag.md) — Cache-Augmented Generation 另一种 RAG 替代
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) — OKF bundle 自动补全
</content>
</invoke>