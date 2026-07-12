---
type: Tool
title: "annotai（Phoenix / LiveView 元素级 AI 编码注释工具）"
description: "只在开发环境用的 Phoenix / LiveView 小挂件：在跑着的页面上点元素写备注，把 CSS 选择器、phx-* 属性和渲染它的 HEEx 文件位置一并打包，直接甩给你的 AI 编码智能体去改。"
resource: "https://github.com/andrielfn/annotai"
tags: [tool, phoenix, liveview, heex, dev-tools, ai-coding]
timestamp: 2026-07-12T16:30:00Z
---

# annotai（Phoenix / LiveView 元素级 AI 编码注释工具）

## 它是什么
仅在开发环境加载的 Phoenix / LiveView 挂件：开发者在浏览器里看到的页面上点任意元素即可写注释，annotai 自动把该元素的 CSS 选择器、phx-* 属性以及渲染它的 HEEx 模板文件位置打包成结构化上下文，喂给 AI 编码智能体（如 Claude Code / Codex）去做修改。

## 为什么用它 / 适合什么场景
- 用 Phoenix + LiveView + HEEx 开发 Web 应用，调试 UI 时希望"点哪个 → 注释哪个 → 改哪个"一气呵成。
- 给 AI 编码 agent 提供精准的「元素 → 源文件」映射，避免它猜错目标 HEEx 文件。
- 仅在 dev 环境加载，不影响 prod 性能。

## 关键能力
| 能力 | 说明 |
|------|------|
| 元素点选 | 在浏览器页面上点击任意元素添加注释 |
| 自动上下文 | 自动捕获 CSS 选择器、phx-* 属性、HEEx 文件位置 |
| AI 上下文打包 | 把所有上下文打包成可粘贴给 AI 编码 agent 的格式 |
| 仅 dev 环境 | 不影响生产性能 |

## 参考链接
- [项目链接](https://github.com/andrielfn/annotai)
- [原始链接](https://x.com/QingQ77/status/2076220013648695781)

视频：<https://video.twimg.com/tweet_video/HM7SE0abAAANt22.mp4>

## 相关概念
- [Browser Search Agent（浏览器侧搜索 agent）](tool-browser-search-agent.md) — 同类"浏览器上下文 → AI agent"思路
- [Hermes Browser Extension（给 Hermes Agent 用的浏览器侧边栏）](tool-hermes-browser-extension.md) — 同类浏览器扩展 → agent 上下文注入工具