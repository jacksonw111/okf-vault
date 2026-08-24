---
type: Tool
title: "vault-graph"
description: "把整个 Obsidian 库画成一张可交互的圆形图谱，可导出离线单文件 HTML。"
resource: "https://github.com/luke321/vault-graph"
tags: [obsidian, graph, visualization, offline, html]
timestamp: "2026-08-24T03:31:00Z"
---

# vault-graph

## 它是什么

[luke321/vault-graph](https://github.com/luke321/vault-graph) 是把整个 Obsidian Vault（Markdown 笔记库）可视化为一张**可交互圆形图谱**的工具，并能导出为离线单文件 HTML——不依赖任何后端服务器，浏览器双击即开。

## 为什么用它 / 适合什么场景

- 想知道笔记库里「节点之间真实的连接结构」（不是 Obsidian 自带 Graph 的近似算法）。
- 想把 Vault 的关系图作为离线备份 / 分享版本（HTML 文件 + 数据内嵌）。
- 想给 OKF 类知识库做一份「可分发的可视化快照」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 圆形图谱布局 | 把 Vault 节点排成环形结构，一眼看出 hub 节点 |
| 可交互 | 鼠标悬停 / 点击展开节点详情 |
| 离线 HTML 导出 | 输出单文件 HTML，可邮件 / U 盘分享 |
| Markdown 解析 | 直接读 `.md` 文件 + wikilink |
| 无后端依赖 | 全部在浏览器内运行 |

## 相关概念

- [Obsidian](./tool-obsidian.md) — vault-graph 的天然编辑器
- [Cabinet](./tool-cabinet.md) — Obsidian + AI 代理的复合方案
- [OKF Static HTML Visualizer](./tool-okf-static-html-visualizer.md) — 同类「OKF bundle → 静态 HTML」思路

## 参考链接

- [项目链接](https://github.com/luke321/vault-graph)
- ![](https://pbs.twimg.com/media/HQc19JQbMAAp35j.jpg)