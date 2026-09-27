---
type: "Tool"
title: "WikiCrawl（Wikipedia 链接关系知识图谱）"
description: "Adityavardhanjain 出品的 TypeScript + Next.js 网页应用：从一个 Wikipedia 词条出发，沿出链爬 1–3 跳 50–500 个页面，构造成有向图；Graphology 算社区与指标，SSE 边爬边把节点 / 边 / 进度推到浏览器，Sigma + ForceAtlas2（Worker 里算布局）渲染。"
resource: "https://github.com/Adityavardhanjain/WikiCrawl"
tags: "[wikipedia, knowledge-graph, graphology, sigma, forceatlas2, nextjs, sse]"
timestamp: "2026-09-27T21:55:00Z"
---

# WikiCrawl（Wikipedia 链接关系知识图谱）

## 它是什么

[WikiCrawl](https://github.com/Adityavardhanjain/WikiCrawl) 是 Adityavardhanjain 出品的 **TypeScript + Next.js** 网页应用：把 **Wikipedia 词条之间的链接关系爬成一张可以点击探索的知识图谱**。

工作流程：

1. 用户输入一个 Wikipedia 词条作为起点
2. 沿**出链**爬 **1–3 跳**，共 **50–500 个页面**
3. 把结果**构造成有向图**
4. 用 **Graphology** 算**社区结构与图指标**
5. 通过 **SSE（Server-Sent Events）** 边爬边把节点 / 边 / 进度推到浏览器
6. 浏览器端用 **Sigma** 渲染，**ForceAtlas2 在 Web Worker 里**算布局

爬虫带**明确上限**：上游请求预算 500 次、并发 3、维基链接请求超时 10 秒、搜索接口按客户端 IP 限流（10 分钟 120 次），缓存优先用 **SQLite**。

## 为什么用它 / 适合什么场景

- 想**从单个词条出发探索 Wikipedia 的拓扑结构**（比如从一个科学家爬到他的合作者 / 学生 / 研究领域）。
- 想看**社区结构**：哪些词条在同一个「学术家族 / 时代 / 流派」。
- 想看**实时进度**（不等到全部爬完才显示），SSE 流式更新节点。
- 想**轻量部署**（Next.js 单体），不想自己拼爬虫 + 图数据库 + 前端渲染。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | TypeScript + Next.js 网页应用 |
| 数据源 | Wikipedia |
| 爬取深度 | 1–3 跳，50–500 页 |
| 图结构 | 有向图（出链方向） |
| 图分析 | Graphology（社区 / 指标） |
| 推流 | SSE（边爬边推） |
| 渲染 | Sigma + ForceAtlas2（Worker） |
| 缓存 | SQLite |
| 上限 | 500 次请求 / 并发 3 / 10 秒超时 / 10 分钟 120 次搜索 |

## 媒体

- ![](https://pbs.twimg.com/media/HTLycaPaQAA9nR4.jpg)

## 相关概念

- [Understand-Anything](./tool-understand-anything.md) — 把代码库变成可探索知识图谱（≈8.3 万 ⭐）
- [grove（Entelligentsia）](./tool-grove-tree-sitter.md) — tree-sitter 结构化代码访问工具