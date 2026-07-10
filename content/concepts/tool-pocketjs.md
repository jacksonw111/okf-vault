---
type: Tool
title: "PocketJS"
description: "在浏览器之外运行 JSX UI 的运行时：Solid / Vue Vapor 组件经 QuickJS 编译执行，布局 / 样式 / 文本 / 动画交给 no_std 的 Rust 核心，8 MB 内存预算下保持 60 FPS。"
resource: "https://github.com/pocket-stack/pocketjs"
tags: [tool, jsx, solid, vue, rust, quickjs, ui-runtime, gaming]
timestamp: 2026-07-10T09:55:00.000Z
---

# PocketJS

## 它是什么
嵌入式 / 跨端的 JSX UI 运行时。把 Solid 或 Vue Vapor 写的 JSX 组件喂给 QuickJS，布局、样式、文本、动画等"重活"交给一个 `no_std` 的 Rust 核心处理，从而能在浏览器之外的轻量环境里跑现代响应式 UI。

## 为什么用它 / 适合什么场景
- 想要在 PSP / PPSSPP / 原生 macOS 窗口 / Bun（无头）等奇怪目标上跑 JSX UI。
- 嵌入式 / 复古硬件 / 低端设备资源预算只有几 MB 内存、但需要 60 FPS 动画。
- 想用熟悉的 Solid / Vue Vapor 组件模型写出跨设备的"游戏机 UI"。

## 关键能力
| 能力 | 说明 |
|------|------|
| 跨目标 | 真实 PSP、PPSSPP 模拟器、浏览器（WASM）、原生 macOS 窗口、无头 Bun |
| JSX 直跑 | Solid / Vue Vapor 组件无需打包即可执行 |
| Rust 核心 | `no_std` 布局 / 样式 / 文本 / 动画引擎 |
| 极小预算 | 8 MB 内存下保持 60 FPS 动画 |

## 媒体
视频（原始剪藏附件）：
- <https://video.twimg.com/amplify_video/2075039773320937472/vid/avc1/1280x684/FMgasEfvf1JMqZ4n.mp4?tag=28>

## 相关概念