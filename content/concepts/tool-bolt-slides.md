---
type: Tool
title: "bolt-slides（stackblitz）"
description: "让 Claude Code、Codex、Cursor、Bolt 这类 AI 编程智能体，用一句话提示就能生成以 Web 应用为底座、可交互的动态幻灯片。"
resource: "https://github.com/stackblitz/bolt-slides"
tags: "[slides, web-app, ai-agent, presentation, interactive]"
timestamp: "2026-07-19T15:08:00Z"
---

# bolt-slides（stackblitz）

## 它是什么

stackblitz/bolt-slides 是 StackBlitz 出的工具，让 AI 编程智能体（Claude Code / Codex / Cursor / Bolt）**用一句话提示生成可交互的动态幻灯片**。和传统「幻灯片生成器」不同，它产出的不是 PDF / PPTX 文件，而是一个**真正的 Web 应用**——每一页都是可点击 / 可动画 / 可交互的 React 组件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一句话生成 | 提示词到可运行幻灯片 Web App |
| 多 Agent 兼容 | Claude Code / Codex / Cursor / Bolt 都可作为生成入口 |
| Web 应用底座 | 交互 / 动画 / 数据可视化都不受限 |
| 实时可改 | 幻灯片就是 React 组件，随时调整行为 |

## 与已有幻灯片工具的差别

- [MD→Slides](./tool-markdown-slides.md) — Markdown 转静态幻灯片
- [presenter-mode](./tool-presenter-mode.md) — 给静态幻灯片加演示者视图
- [Space Multi-Design PPT](./tool-multi-design-ppt.md) — 按 62 种品牌设计语言出 HTML/PPTX/PDF
- bolt-slides 的差异点：**强调「Web App 即幻灯片」**——交互 / 动画 / 状态管理原生支持，不只是排版

## 适合谁

- 内部技术分享需要带可交互 demo 的幻灯片
- 产品演示需要「点哪儿响哪儿」的引导式介绍
- 把「用 AI 生成幻灯片」做成一条工作流，而不是手工排版

## 媒体预览

![](https://pbs.twimg.com/media/HNepYsvaEAAKb-j.jpg)

## 相关概念

- [MD→Slides](./tool-markdown-slides.md) — Markdown 转静态幻灯片
- [presenter-mode](./tool-presenter-mode.md) — 演示者视图

## 参考链接

- 项目链接: <https://github.com/stackblitz/bolt-slides>