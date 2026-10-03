---
type: "Tool"
title: "QuietGlass（macOS 屏幕隐私保护：转头 / 第二张脸 / 快捷键自动打码）"
description: "clintonimaroo 出品的开源原生 macOS 菜单栏应用：用 Swift + SwiftUI/AppKit 写成（要求 macOS 14+），提供三种触发源——兼容款 AirPods 的头部动作、摄像头的头部朝向估计、纯手动的快捷键打码；触发时自动给屏幕打码或弹警告，全程本地运行。"
resource: "https://github.com/clintonimaroo/quietglass"
tags: "[macos, privacy, screen-privacy, swift, native, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# QuietGlass

## 它是什么

[QuietGlass](https://github.com/clintonimaroo/quietglass) 是 **clintonimaroo** 出品的**开源原生 macOS 菜单栏应用**——**Swift + SwiftUI/AppKit** 写成（要求 macOS 14+），提供**三种触发源**自动保护屏幕隐私：

| 触发源 | 技术 | 场景 |
|--------|------|------|
| 兼容款 AirPods 头部动作 | Core Motion | 转头离开屏幕自动打码 |
| 摄像头头部朝向估计 | Vision | 有人凑到背后就盖屏 / 弹警告 |
| 手动快捷键 | 系统快捷键 | 任意时刻主动打码 |

## 为什么用它 / 适合什么场景

- **星巴克 / 咖啡馆写代码**：转头拿咖啡那一下屏幕自己糊掉；有人凑到背后摄像头认出第二张脸就弹警告或直接盖屏。
- **全部本地**：面部识别 / 头部朝向估算不联网。
- **MIT 协议**：可二次开发、可商业使用。
- **多触发冗余**：AirPods / 摄像头 / 快捷键可叠加，避免单点失效。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | macOS 14+（Apple Silicon + Intel） |
| 触发 1 | AirPods 头部动作（Core Motion） |
| 触发 2 | 摄像头头部朝向（Vision） |
| 触发 3 | 手动快捷键 |
| 行为 | 屏幕打码 / 弹警告 / 盖屏 |
| 网络 | 全本地，零上传 |
| 协议 | MIT |
| 形态 | 菜单栏应用 |

## 参考链接

- 项目链接：<https://github.com/clintonimaroo/quietglass>

## 相关概念

- [Abide](./tool-abide-rubric.md) — 同一仓库内的 Agent 软规则检查模块
