---
type: Tool
title: "OpenNook"
description: "OpenNook 是 Swift 写的开源 macOS 框架,在刘海(Notch)区域里跑自定义 SwiftUI 应用:展开 / 收起、磨砂背景、快捷键、设置面板、文件拖放架、扩展组件全套内置。"
resource: "https://github.com/athledev-labs/opennook"
tags: [opennook, macos, swift, swiftui, notch, menubar, framework]
timestamp: "2026-07-04T15:00:00Z"
---

# OpenNook

## 它是什么

`athledev-labs/opennook` 是一个开源的 Swift 框架,目的是给 macOS 顶部「刘海(Notch / Dynamic Island)」区域写自己的轻量应用。它分三层:

| 层 | 职责 |
|------|------|
| `NookSurface` | 管 notch 窗口的形状与展开/收起动画 |
| `NookKit` | 管顶栏、设置面板、应用生命周期 |
| `NookComponents` | 可选扩展组件包 — 文件拖放架、活动队列、音量图标等 |

<https://video.twimg.com/amplify_video/2073051214137401344/vid/avc1/530x360/OxF8iZEMnDucrfCa.mp4?tag=28>

项目链接：<https://github.com/athledev-labs/opennook>

## 为什么用它 / 适合什么场景

- **macOS 14+ MacBook 用户的特殊硬件资产**:刘海外观是 Apple 花了硬件成本做出来的,目前主流 macOS 应用基本不利用。OpenNook 直接面向这块区域做应用。
- **比菜单栏更显眼**:菜单栏图标小且挤,notch 区域可滑动展开,可承载更复杂的小工具(剪贴板历史 / 翻译 / 系统监控 / 会议中控)。
- **免去自己写窗口管理**:notch 的形状、动画、与系统顶栏的协调都帮你处理好了。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自定义 SwiftUI 视图 | 在刘海区域渲染任意 SwiftUI 内容 |
| 展开 / 收起动画 | 内置手势 / 点击展开动画(磨砂背景) |
| 快捷键 | 自定义全局快捷键呼出 / 隐藏 |
| 设置面板 | 自带设置面板模板 |
| 文件拖放架 | 拖文件到 notch 区域触发接收 |
| 活动队列 | 通知中心式排队展示异步任务 |
| 音量 / 状态图标 | 扩展组件 |

## 相关概念

- [MacTools](tool-mac-tools.md) — 同是 macOS 菜单栏工具集,与 OpenNook 都关注 macOS 系统表面区域
- [Vesta](tool-vesta-terminal.md) — macOS 原生终端,同样基于 SwiftUI + 原生 GUI
- [gradient-shimmer-swiftui](tool-gradient-shimmer-swiftui.md) — Apple 平台 SwiftUI 动效库
- [OpenNook 仓库](https://github.com/athledev-labs/opennook) — 项目链接
