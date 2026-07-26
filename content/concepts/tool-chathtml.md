---
type: "Tool"
title: "ChatHTML（aietheia/ChatHTML）"
description: "开源聊天界面，能把模型输出的 HTML 内容一边生成一边渲染到沙箱 iframe 里，用户立刻就能看到可操作的结果：支持表单、游戏、图表、画廊、计时器等多种输出类型，并带选择编辑、重新生成、截图修复、导出等迭代功能。"
resource: "https://github.com/aietheia/ChatHTML"
tags: [chat-ui, llm, streaming, html, sandbox, iframe, generative-ui]
timestamp: "2026-07-26T01:21:00Z"
---

# ChatHTML（aietheia/ChatHTML）

## 它是什么

`aietheia/ChatHTML` 是一个**开源聊天界面**：把模型输出的 HTML 内容**一边生成一边渲染**到**沙箱 iframe** 里，用户**立刻就能看到可操作的结果**。支持**表单、游戏、图表、画廊、计时器**等多种输出类型，并带**选择编辑、重新生成、截图修复、导出**等迭代功能。

## 为什么用它 / 适合什么场景

- 想要「**模型一边写 HTML，前端一边渲染**」的实时体验，而不是等全部生成完才显示；
- 想做 Generative UI（让 LLM 直接生成可玩的应用）但又不想自己写沙箱；
- 调试 LLM 输出的 HTML 时，需要**选择编辑 / 重新生成 / 截图修复**这些迭代工具；
- 渲染结果要可导出、可分享（HTML 完整可用）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 流式渲染 | 一边生成 HTML 一边塞进沙箱 iframe |
| 沙箱安全 | iframe 隔离，HTML 不会影响主界面 |
| 多输出类型 | 表单 / 游戏 / 图表 / 画廊 / 计时器 等 |
| 选择编辑 | 直接选中文本编辑 |
| 重新生成 | 局部 / 整体重生成 |
| 截图修复 | 视觉问题可截图标注后让模型修 |
| 导出 | 渲染结果可导出 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOC9JhQaMAAnthP.jpg)
![](https://pbs.twimg.com/media/HOC9KIMa4AAv3mI.jpg)

- 项目链接：<https://github.com/aietheia/ChatHTML>

## 相关概念

- [Conversed](tool-conversed.md) — 同样把 LLM 输出渲染成 UI 组件（Conversed 偏结构化 AST+16 组件，ChatHTML 偏任意 HTML 沙箱）
