---
type: Tool
title: "davit"
description: "SwiftUI 写的 macOS 原生界面，用来管理 Apple 官方的 container 容器平台（Apple silicon 上的轻量 Linux 虚拟机容器栈）。"
resource: "https://github.com/wouterdebie/davit"
tags: [tool, macos, swiftui, container, apple-silicon, apple-container]
timestamp: 2026-07-10T07:56:00.000Z
---

# davit

## 它是什么
macOS 原生的 Apple container 管理界面，用 SwiftUI 写成，把 Apple 官方的 container 平台（基于 Apple silicon 上的轻量 Linux VM 容器栈）从命令行提升到 GUI。

## 为什么用它 / 适合什么场景
- 想用 macOS 上的 Apple container（vs Docker Desktop）但不想总敲 `container` CLI。
- 需要 SwiftUI 原生体验与 macOS 系统设置风格的容器管理 UI。
- 想了解 SwiftUI 怎么写"系统级管理工具"的参考实现。

## 关键能力
| 能力 | 说明 |
|------|------|
| SwiftUI 原生 | macOS 原生体验，跟系统设置无缝融合 |
| Apple container 后端 | 适配 Apple silicon 上的官方容器栈 |
| GUI 替代 CLI | 把 `container` 命令的操作搬到可视化界面 |

## 相关概念