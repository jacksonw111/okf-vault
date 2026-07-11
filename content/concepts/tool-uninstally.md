---
type: Tool
title: "Uninstally（macOS 卸载工具）"
description: "gostonx 用 SwiftUI 写的原生 macOS 卸载工具，删除 App 同时清理残留文件，并支持从 Finder 右键直接卸载、管理 Homebrew 包。"
resource: "https://github.com/gostonx/uninstally"
tags: "[macos, uninstaller, swiftui, homebrew, finder]"
timestamp: "2026-07-11T20:00:00Z"
---

# Uninstally（macOS 卸载工具）

## 它是什么

`gostonx/uninstally` 是一个**原生 macOS 卸载工具**，用 SwiftUI 写。三件事：

1. **卸载 App + 清理残留文件**——不只是把 `.app` 拖进废纸篓，还会扫 `~/Library/Application Support`、`~/Library/Caches`、`~/Library/Preferences` 等位置的关联残留。
2. **Finder 右键直接卸载**——选中 `.app` 右键就能调用本工具。
3. **管理 Homebrew 包**——不只能卸 App，也能管 Homebrew Cask / Formula。

## 为什么用它 / 适合什么场景

- macOS 自带卸载经常留一堆 `~/Library` 垃圾。
- 想从 Finder 直接右键卸，不用打开专用 App。
- 同时用 Homebrew + 图形 App，想一个工具统一管。

## 关键能力

| 能力 | 说明 |
|------|------|
| 残留清理 | 扫 `~/Library` 多目录 |
| Finder 集成 | 右键直接卸载 |
| Homebrew 管理 | 也能管 brew install 的包 |
| SwiftUI | 原生 macOS 体验 |

## 媒体参考

- 演示视频：<https://video.twimg.com/amplify_video/2075803286243057664/vid/avc1/960x540/RmQ4tP4e-59VQ646.mp4?tag=28>

## 相关概念

- [MacTools](tool-mac-tools.md) — 另一款 macOS 菜单栏工具集
- [Davit](tool-davit.md) — SwiftUI 写的 macOS Apple container 管理界面

## 项目链接

- 项目仓库：<https://github.com/gostonx/uninstally>