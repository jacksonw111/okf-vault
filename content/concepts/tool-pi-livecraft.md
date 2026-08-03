---
type: Tool
title: "Pi-Livecraft"
description: "给 Pi 终端 AI 助手套一个随时能被模型改的 React 网页界面，图表、按钮、HTML 这类东西就有了用武之地。"
resource: "https://github.com/sebastienservouze/pi-livecraft"
tags: [pi, react, web-ui, ai-assistant, tool]
timestamp: "2026-08-03T07:19:00Z"
---

# Pi-Livecraft

## 它是什么
Pi-Livecraft（`sebastienservouze/pi-livecraft`）给 Pi 终端 AI 助手**套一个随时能被模型改的 React 网页界面**。Pi 在终端里能干很多事，但空间和交互有限；Livecraft 把 React 组件库暴露出来，让模型可以在执行工具调用时动态生成、带出图表、按钮、HTML 等「终端不太适合」的可视元素。

视频：
- <https://video.twimg.com/tweet_video/HOrq6FGbsAAti1R.mp4>

## 为什么用它 / 适合什么场景
- **突破终端表达瓶颈**：表格、图表、按钮、表单这类交互元素不再受 ASCII 字符限制。
- **模型驱动 UI**：UI 本身就是模型的输出，按需生成、不预定。
- **保留 Pi 终端流**：仅在需要时弹网页 UI，主体流程仍在终端。

## 关键能力

| 能力 | 说明 |
|------|------|
| React 网页界面 | 任何 Pi 调用都能在网页端渲染结果 |
| 动态 UI | 模型可运行时生成 / 调整组件 |
| 终端 + Web 混合 | 主交互仍在终端，可视元素卸载到网页 |
| 协议桥 | Pi ↔ React 通过标准化事件通信 |

## 项目链接
- <https://github.com/sebastienservouze/pi-livecraft>

## 相关概念
- [Chartr](./tool-chartr.md) — Go + Svelte 的 agent 多路复用器，把规划 markdown 渲染成星图
- [OpenBrowser](./tool-openbrowser.md) — 浏览器代理模式（与 React 网页 UI 思路互补）
- [Pi Extensible Workflows](./tool-pi-extensible-workflows.md) — Pi 终端 AI 助手的确定性多代理工作流编排
