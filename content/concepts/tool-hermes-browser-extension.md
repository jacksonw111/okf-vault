---
type: Tool
title: "Hermes Browser Extension（Hermes Agent 浏览器侧边栏）"
description: "给 Hermes Agent 做的浏览器侧边栏扩展，把当前网页的上下文（标题、正文、标签、选区等）接入本地或远程的 Hermes 运行时，做实时对话与分析。"
resource: "https://github.com/abundantbeing/hermes-browser-extension"
tags: "[browser-extension, hermes, agent, sidebar, context, web]"
timestamp: "2026-07-09T20:50:00Z"
---

# Hermes Browser Extension（Hermes Agent 浏览器侧边栏）

## 它是什么
`abundantbeing/hermes-browser-extension` 是一个浏览器扩展，把 **Hermes Agent** 嵌入侧边栏，自动抓取当前网页上下文：
- 页面标题
- 全文 / 摘要
- 标签 / 元信息
- 用户当前选区

把这些上下文**直接送给本地或远端的 Hermes 运行时**，让用户在浏览网页时随时与 Hermes 对话 / 让 Hermes 分析当前页。

## 为什么用它 / 适合什么场景
- 阅读长文章时想让 Hermes Agent **当场解答**而不是把全文复制粘贴。
- 写文档 / 写代码时让 Hermes 帮**解读打开的页面**。
- 想给浏览器装一个**始终在侧的私人助理**。
- 适合：研究员 / 学生 / 写作者 / 写代码看文档的开发。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动抽取上下文 | 标题 / 正文 / 标签 / 选区 |
| Hermes 运行时 | 支持本地 / 远端 |
| 侧边栏常驻 | 不打断浏览节奏 |
| 视频/网页统一 | 浏览器能开的都能喂给它 |

## 媒体参考

演示视频：
- <https://video.twimg.com/tweet_video/HMrPfqxa8AA9gJ5.mp4>

## 相关概念
- [Hermes Desktop](tool-hermes-desktop.md) — Hermes Agent 的原生桌面 GUI 客户端（移动设备 GUI 同样可装 Hermes）
- [Hermex](tool-hermex.md) — SwiftUI 写的 iOS Hermes AI 代理控制端
- [page-agent（阿里浏览器端 GUI Agent）](tool-page-agent.md) — 纯 TS 文本操作 DOM，四种接入（npm / CDN / 扩展 / MCP）

## 参考链接
- 项目链接：<https://github.com/abundantbeing/hermes-browser-extension>
