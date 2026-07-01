---
type: Tool
title: "MacOS-DPIManager"
description: "HasBrain 用 SwiftUI + IOKit 写的 macOS 工具，给外接显示器启用 HiDPI 模式，按显示器 VendorID + ProductID 识别设备，支持预设与自定义分辨率 + 字体平滑调整。"
tags: "[macos, hidpi, display, swiftui, iokit]"
timestamp: "2026-07-01T00:15:00Z"
resource: "https://github.com/HasBrain/MacOS-DPIManager"
---

# MacOS-DPIManager

## 它是什么
HasBrain 写的 macOS 工具，用 SwiftUI 做界面 + IOKit 直接读显示器硬件 ID。给外接显示器启用 HiDPI（Retina）模式，按显示器的 VendorID + ProductID 识别具体设备，让每一台外接屏都能像内置屏一样清晰。

## 为什么用它 / 适合什么场景
- 外接 4K 显示器但 macOS 没自动开 HiDPI
- 用 SwitchResX 等付费工具觉得贵
- 想给特定型号的外接屏自定义分辨率 / 缩放比例
- 想在字体渲染上做精细调节（字体平滑开关）

## 关键能力
| 能力 | 说明 |
|------|------|
| SwiftUI 界面 | 原生 macOS 体验 |
| IOKit 硬件读取 | 直接读显示器的 VendorID / ProductID 精准识别 |
| HiDPI 一键开 | 不需要手动写 RDM 配置文件 |
| 预设分辨率 | 常见外接屏型号的预设（如 LG 4K / Dell U 系列） |
| 自定义分辨率 | 任意输入分辨率创建自定义模式 |
| 字体平滑 | 调整字体渲染设置（关掉 macOS 的字体灰度） |
| 设备库管理 | 已识别设备列表，按需启用 / 禁用 |

## 已知同类工具
- **SwitchResX**：付费老牌，功能最全
- **BetterDummy**：开源，免费方案但只能通过虚拟显示器开 HiDPI
- **MacOS-DPIManager**：本项目，免费 + 直接读 IOKit，介于二者之间

## 相关概念
- [OpenMac](tool-openmac.md) — Swift 写的 macOS 本地 HTTP 服务，把 Vision / Translation 等系统能力暴露成 JSON API
- [gradient-shimmer-swiftui](tool-gradient-shimmer-swiftui.md) — SwiftUI 视觉库，与 MacOS-DPIManager 同为 SwiftUI macOS 工具

## 原始链接
- [项目仓库](https://github.com/HasBrain/MacOS-DPIManager)
- [截图](https://pbs.twimg.com/media/HMCZWLDXoAAKGvR.jpg)