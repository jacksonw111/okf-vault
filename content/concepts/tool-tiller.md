---
type: Tool
title: "Tiller（基于 Chromium 的 macOS 浏览器 + 内置 Agent 面板）"
description: "基于 Chromium 的 macOS 浏览器，UI 用原生 Swift / AppKit 编写，内置一个「能驱动浏览器」的 Agent 面板，把浏览与代理操作合并到同一界面。"
resource: "https://github.com/sorrycc/tiller"
tags: [browser, chromium, macos, agent, swift, appkit]
timestamp: 2026-09-30T15:49:00Z
---

# Tiller

## 它是什么

**Tiller** 是 [sorrycc](https://github.com/sorrycc) 维护的一款 **macOS 浏览器**——核心引擎走 Chromium，UI 层用**原生 Swift / AppKit** 自己写，而不是套一个 Electron 壳。它的差异化在于内置一个**能驱动浏览器的 Agent 面板**，让"打开网页"和"让 Agent 操作网页"在同一个窗口里。

## 为什么用它 / 适合什么场景

- 想要一个轻量、原生体验的 Chromium 浏览器，不想用 Electron 套壳产品。
- 在用 Browser Use / Computer Use 这类 Agent，希望它**直接住在浏览器里**而不是另一个窗口。
- macOS 重度用户，希望 UI 是 Swift 原生而不是 webview 假装。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内核 | Chromium |
| UI 层 | Swift / AppKit 原生 |
| 平台 | macOS |
| 特色 | 内置 Agent 面板（能驱动浏览器） |
| 形态 | 一款独立浏览器 |

## 参考链接

- 仓库：<https://github.com/sorrycc/tiller>

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2105158102777733120/vid/avc1/1920x1080/6U6u03NdBTQatUQA.mp4?tag=29>

## 相关概念

- [Computer Use](./term-computer-use.md) — 让 Agent 操作桌面 / 浏览器的通用思路；Tiller 把这条路做到浏览器里内置面板
- [Browser Use Agent](./tool-jev-browser-use.md) — 同类"让 Agent 驱动浏览器"的方向