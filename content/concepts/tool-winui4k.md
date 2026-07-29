---
type: Tool
title: "WinUI4K（Kotlin / Java 直接调 WinUI 的桥）"
description: "在 Windows 上做 Java / Kotlin 桌面应用，UI 只能用 Swing 或 JavaFX；想用微软官方的 WinUI 就得把整个项目改成 C#。WinUI4K 让 Kotlin / Java 直接调 WinUI，不用碰 C#，也不用装 Visual Studio。"
resource: "https://github.com/nttr-tech/winui4k"
tags: [kotlin, java, winui, windows, desktop, jni]
timestamp: "2026-07-29T06:41:00.000Z"
---

# WinUI4K

## 它是什么

**Kotlin / Java 直接调 WinUI 的桥**——微软的现代 Windows UI 框架（WinUI）原是 C# / XAML 领域，Java / Kotlin 桌面开发者的 UI 选型被锁在 Swing / JavaFX。

WinUI4K 让 Kotlin / Java 项目**直接调用 WinUI**，无需改语言、无需装 Visual Studio。

![截图示例](https://pbs.twimg.com/media/HOSQ2bybgAAf9Fk.jpg)

## 解决的痛点

| 痛点 | WinUI4K 解法 |
|------|-------------|
| Java / Kotlin 只能 Swing / JavaFX | 直接调 WinUI |
| 想用现代 UI 必须改 C# | 保持 Kotlin / Java 栈 |
| 必须装 Visual Studio | 无需 VS |
| UI 跨平台缺失 | Windows 原生现代 UI |

## 关键能力

| 能力 | 说明 |
|------|------|
| Kotlin / Java 直调 WinUI | 语言不换 |
| 无需 C# | 工程不重写 |
| 无需 Visual Studio | 工具链轻 |
| Windows 原生 UI | 现代外观 + 性能 |
| 适合 Kotlin / Java 桌面开发者 | 拓展 UI 选型 |

## 原始链接

- [项目仓库](https://github.com/nttr-tech/winui4k)
- [推文剪藏](https://x.com/QingQ77/status/2082355693181370466)

## 相关概念

- [DeskBox（WinUI 3 桌面整理工具）](./tool-deskbox.md) — WinUI 3 桌面整理，托盘 / 全局快捷键
- [ZSUi（Rust 轻量原生 UI 框架）](./tool-zsui.md) — Rust 的原生 UI 框架，类似思路
- [OpenNook](./tool-opennook.md) — Swift 框架在 macOS 刘海区域跑自定义 SwiftUI 应用
- [WSL / VS Code 桌面 UI 思路（vscode）](./tool-vscode-fork.md) — 跨语言的桌面 UI 桥