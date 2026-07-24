---
type: Tool
title: "guidebridge（Python AI 代理操控 React 页面的桥）"
description: "让 Python AI 代理实时看到 React 页面内容,并用光标指、点、拖、打字、高亮——全在用户自己的浏览器标签页里,无需截图也不依赖视觉模型。"
resource: "https://github.com/pramodthe/guidebridge"
tags: [ai-agent, browser-automation, react, accessibility, python]
timestamp: "2026-07-24T00:00:00Z"
---

# guidebridge

[guidebridge](https://github.com/pramodthe/guidebridge) 是给 **Python AI 代理**搭的一座桥，让它能在用户的 React 页面里**实时看到 DOM**、**用光标指**、**点击**、**拖动**、**输入**、**高亮**——这一切都在用户自己的浏览器标签页里完成，**不依赖截图也不依赖视觉模型**。

## 它解决的问题

让 AI 代理操作 Web 页面，传统路径有几条：

| 路径 | 痛点 |
|------|------|
| Playwright + 截图 + VLM | 慢、贵、对 React 高频更新不友好 |
| 直接读 DOM JSON | 没法"操作"，只能"观察" |
| 浏览器扩展 | 通常给 JS/TS 用，Python 代理接不进来 |

guidebridge 的关键差异：
- **不走视觉模型**——直接走 React 组件树与 DOM，省 token、快、稳。
- **不离开用户自己的浏览器**——在用户的真实标签页里操作，反作弊 / 真实登录态 / 真实前端行为都保留。
- **Python 原生**——给 Python AI 代理（Hugging Face / LangGraph / 自研 agent）直连。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时 DOM 读取 | 看到 React 当前组件树与渲染结果 |
| 光标动作 | 指 / 点 / 拖 / 输入 / 高亮 |
| 真实标签页 | 操作发生在用户自己的浏览器，不开无头环境 |
| 无截图 | 走 DOM 与组件树，省 token |
| 无视觉模型 | 不依赖 VLM |
| Python 友好 | 给 Python AI 代理直接接入 |

## 适用场景

- 自研 Python AI 代理需要"动手"操作 Web 应用
- 想避免 Playwright + VLM 的高 token / 高延迟
- 已有真实登录态 / 真实前端的复杂 Web 流程需要 AI 介入

## 参考链接

- 项目仓库: <https://github.com/pramodthe/guidebridge>

## 媒体

视频演示：<https://video.twimg.com/tweet_video/HN9SV-abYAA_hds.mp4>

## 相关概念

- [page-agent](tool-page-agent.md) — 阿里浏览器端 GUI Agent，纯 TS 文本操作 DOM，提供 npm / CDN / 扩展 / MCP 四种接入
- [sim-use](tool-sim-use.md) — CLI 让 AI Agent 观察与操作 iOS 模拟器与 Android 设备屏幕（移动端侧）