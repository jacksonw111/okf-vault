---
type: "Tool"
title: "macOS Web"
description: "用一个不带构建步骤、不依赖框架的 HTML 文件，在浏览器里复刻一个能用的 macOS 桌面环境：包含窗口管理、Dock、菜单栏和三十个应用。"
resource: "https://github.com/StarKnightt/macos-web"
tags: [macos, html, web-os, single-file, demo, no-framework]
timestamp: "2026-08-07T12:44:00Z"
---

# macOS Web

## 它是什么

macOS Web 是一个单一 HTML 文件，不带构建步骤、不依赖任何前端框架，在浏览器里复刻出一个可用的 macOS 桌面环境——包含窗口管理、Dock、菜单栏和三十个应用，整套体验塞进一个文件就能跑。

## 为什么用它 / 适合什么场景

- 想做 macOS 桌面交互的演示 / 教学 / 录屏，无需安装模拟器或虚拟机。
- 想研究「如何在一个 HTML 文件里把窗口系统 / Dock / 菜单栏 / 应用全装下」的设计参考。
- 想做产品截图型 hero image / 落地页里的交互演示。
- 想给非 macOS 用户展示 macOS 桌面长什么样、用起来是什么感觉。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单文件 HTML | 整站塞进一个 `.html`，下载即可双击运行 |
| 无构建步骤 | 不需要 webpack / vite / npm install |
| 无前端框架 | 不依赖 React / Vue / Svelte，纯粹 vanilla |
| 窗口管理 | 拖动、最小化、最大化、聚焦、层级切换 |
| Dock | 仿 macOS 底部 Dock，含启动 / 切换效果 |
| 菜单栏 | 顶部菜单栏，含系统图标与下拉菜单 |
| 三十个应用 | 内置约 30 个可点击的「应用」（计算器、文本编辑、Terminal 之类） |

## 媒体

- ![macOS Web 界面截图](https://pbs.twimg.com/media/HPAcgMubsAAx0Jq.jpg)

## 相关概念

- [Win11 Web](./tool-win11-web.md) — 同类项目，定位 Windows 11 的浏览器复刻
- [Single File Web Apps](./note-single-file-web.md) — 「无构建 / 无框架 / 单文件」风格的代表性项目集
- [Windows 98 in Browser](./tool-win98-browser.md) — 更早期的同类怀旧项目