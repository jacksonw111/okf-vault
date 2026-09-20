---
type: "Tool"
title: "Jev Browser（headless 浏览器自动化：按任务逐步执行）"
description: "jkudish/jev-browser：让 Agent 自己上网点页面又不按分钟烧钱或硬写选择器；给定一个任务 + 起始 URL，指挥真实 headless 浏览器一步步点下去，跑完把页面正文 / 截图 / 每一步判定记录一起交回来。"
resource: "https://github.com/jkudish/jev-browser"
tags: "[browser-automation, headless, jev, agent, web]"
timestamp: "2026-09-20T18:00:00Z"
---

# Jev Browser

## 它是什么

[jkudish/jev-browser](https://github.com/jkudish/jev-browser) 想解决「**让 agent 自己上网点页面，又不想按分钟烧钱或者硬写选择器**」。

## 工作方式

1. 接收**一个任务 + 一个起始 URL**。
2. 指挥**真实 headless 浏览器**一步步点下去。
3. 跑完把以下一起交回来：
   - 页面正文
   - 截图
   - **每一步的判定记录**

## 为什么用它 / 适合什么场景

- 不想按分钟 / 按调用烧 LLM token——Jev 类决策层做机械判断，主模型只在该出手时出手。
- 不想**硬写选择器**——Agent 自己理解页面 + 决定点哪。
- 需要**事后审计**：每一步判定记录都留下来。

## 关键能力

| 能力 | 说明 |
|------|------|
| Headless 真实浏览器 | 不是 HTML 解析模拟，是真浏览器渲染 |
| 按任务驱动 | 一次执行一个任务，目标导向 |
| 全量产物 | 页面正文 + 截图 + 判定记录一并交付 |
| 成本控制 | 用 Jev 类决策层降低每步成本 |

## 项目链接

- 仓库：<https://github.com/jkudish/jev-browser>

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HSnzQxIaYAA0Vf9.mp4>

## 相关概念

- [Obscura（Rust 无头浏览器）](./tool-obscura-headless-browser.md) — 同类反检测 / CDP 浏览器思路
- [JEV Ultrafast](./tool-jev-ultrafast.md) — 同基于 Jev 模型的浏览器自动化打分思路
- [Proxide](./tool-proxide.md) — 让 Agent 走浏览器桥接强模型的另一思路
