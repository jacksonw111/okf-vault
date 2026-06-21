---
type: "Tool"
title: "桌面 Markdown 浏览 / 编辑器（散落文档聚合工具）"
description: "一个快速、便携的桌面工具，专门用来浏览和编辑散落在电脑各处的 Markdown 文档：分页打开、左侧文件树、右侧渲染预览，按 Ctrl+E 切换到源码编辑；支持 GitHub 风格 Markdown 与 Mermaid 图表；文档之间可用 `文档名` 互链；右侧大纲栏同步高亮当前位置。"
resource: "https://t.co/OKdlc5aIb3"
tags: "[markdown, desktop, viewer, editor, mermaid, file-tree, outline]"
timestamp: "2026-06-21T16:10:00Z"
---

# 桌面 Markdown 浏览 / 编辑器（散落文档聚合工具）

## 它是什么

一个**快速、便携的桌面 Markdown 浏览 / 编辑器**：专门为「Markdown 文档散落在电脑各处」这种现实场景设计 —— 不用先 import 进某个 vault，把所有目录当成浏览根，分页打开多文档，左侧文件树 + 右侧渲染预览，`Ctrl+E` 一键切到源码编辑。

## 为什么用它 / 适合什么场景

- 不想为「看几个散落的 README / 笔记」专门装 Obsidian / Logseq 这种 vault-first 工具。
- 经常要在多个项目的 Markdown 文件之间跳转（代码库的 README、设计稿的 .md、团队的 wiki）。
- 想要 GitHub 风格 Markdown + Mermaid 图表的本地渲染，但又不想拉 VS Code + 插件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 界面布局 | 左侧文件树 + 右侧渲染预览 + 大纲栏 |
| 分页 | 多文档分页打开 |
| 编辑模式 | `Ctrl+E` 在源码编辑 ↔ 渲染预览间切换 |
| Markdown 语法 | GitHub 风格 + Mermaid 图表 |
| 文档互链 | 用 `文档名` 互相链接（解析为相对路径） |
| 大纲 | 右侧大纲栏同步高亮当前章节 |

## 与 Obsidian / VS Code 的差异

- vs Obsidian：不需要建 vault、不需要 .obsidian 配置 —— 直接看任意目录；Obsidian 强在双链图谱，这个工具强在「直接打开」
- vs VS Code：免插件、启动快、专注 Markdown 阅读体验；VS Code 强在 IDE 能力

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLPk5oAbEAAlhfT.jpg)

## 相关概念

- [Obsidian](tool-obsidian.md) — 同样「桌面端 Markdown」，但定位在 vault-first / 双链图谱
- [Cabinet](tool-cabinet.md) — 同样是「Obsidian + AI 代理」的组合，但更深度绑定 Obsidian
- [MD→Slides](tool-markdown-slides.md) — 同样是「Markdown 富内容」的呈现工具，专注演示