---
type: Tool
title: "md2hd"
description: "把 Markdown 笔记文件夹在浏览器里渲染成交互式超图（hypergraph）：frontmatter 变成节点、wikilink 变成连线，让脑子里的笔记结构变成能直接看的图"
resource: "https://github.com/evan-steinhilb/md2hd"
tags: [markdown, hypergraph, visualization, obsidian, notes, knowledge-graph]
timestamp: 2026-08-17T16:00:00Z
---

# md2hd

## 它是什么

`evan-steinhilb/md2hd` 是一个**纯浏览器**的 Markdown 超图可视化工具：把任意一个 Markdown 笔记文件夹（包含 frontmatter 和 `[[wikilink]]` / 标准链接）解析成**节点 + 连线**的交互式图谱，**frontmatter 字段作为节点属性，wikilink / 链接作为边**。

用户只要指向一个目录，就能在网页里看到「笔记之间的关系」长什么样——尤其是 Obsidian vault / Hugo / 任意 OKF bundle 风格的 Markdown 仓库。

## 为什么用它 / 适合什么场景

- 想在浏览器里**直接看到**笔记的关联结构，而不是凭记忆。
- Obsidian 已有 Graph View 但想换一种更轻量、可托管在静态站的视图。
- 想给 OKF / 个人 wiki 做一张可嵌入的「知识地图」。
- 想要纯客户端方案——数据不外发。

## 关键能力

| 能力 | 说明 |
|------|------|
| Markdown → 超图 | frontmatter → 节点、wikilink → 连线 |
| 纯浏览器渲染 | 无需后端、可静态托管 |
| 交互式 | 缩放 / 拖拽 / 点击节点查看 frontmatter |
| 适用任意 .md 文件夹 | Obsidian / Hugo / OKF bundle / 普通 wiki 都可 |
| 节点属性来自 frontmatter | 标签 / 类型 / 描述直接显示 |

## 媒体

- ![](https://pbs.twimg.com/media/HPvUVOlbsAAKcf2.jpg)

## 原始链接

- [项目仓库](https://github.com/evan-steinhilb/md2hd)

## 相关概念

- [Obsidian](./tool-obsidian.md) — Obsidian 自带 Graph View 是桌面端方案；md2hd 是浏览器端、可托管的轻量替代
- [OKF 是什么](./term-okf.md) — md2hd 的输入模型直接对应 OKF 的 frontmatter + 链接规范，能可视化整个 OKF bundle