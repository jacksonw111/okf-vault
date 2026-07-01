---
type: Tool
title: "gradient-shimmer-swiftui"
description: "zanweiguo 写的 SwiftUI 渐变闪光（shimmer）效果库，封装好可直接用在任何 SwiftUI 视图上，给加载状态 / 骨架屏 / 卡片增加高级感。"
tags: "[swiftui, ios, macos, ui-effect]"
timestamp: "2026-07-01T15:15:00Z"
resource: "https://github.com/zanwei/gradient-shimmer-swiftui"
---

# gradient-shimmer-swiftui

## 它是什么
SwiftUI 版本的渐变闪光（shimmer / skeleton loader）效果库。在 iOS / macOS / iPadOS 上，把任何视图（按钮 / 卡片 / 列表行）包一层就能获得一条斜向滑过的高光动画，常用于内容加载占位与按钮点击反馈。

## 为什么用它 / 适合什么场景
- SwiftUI 原生，没有 UIKit 依赖
- 几行代码接入，类型安全
- 想给 Apple 平台应用加上 shadcn / Linear / Vercel 风格的「高级感」动效
- 想给系统级 App 加统一骨架屏体验

## 关键能力
| 能力 | 说明 |
|------|------|
| SwiftUI 原生 | `.shimmer()` modifier 形式一行接入 |
| 自定义渐变方向 | 角度 / 颜色 / 速度可调 |
| 跨 Apple 平台 | iOS / macOS / iPadOS / visionOS 通吃 |
| 静态 / 动画切换 | 加载中用动画，结束自动停 |

## 接入示例
```swift
Text("Loading...")
    .redacted(reason: .placeholder)
    .shimmering()
```

## 相关概念
- [Liquid Glass（液态玻璃组件）](tool-liquid-glass.md) — 另一种 Apple 平台流行的视觉特效
- [ShipSwift](tool-shipswift.md) — AI 原生 SwiftUI 组件库，可搭配 gradient-shimmer
- [Number Stepper UX](note-number-stepper-ux.md) — 数字步进器动效原则，另一种 SwiftUI 动效细节

## 原始链接
- [项目仓库](https://github.com/zanwei/gradient-shimmer-swiftui)
- [演示视频](https://video.twimg.com/amplify_video/2072168447199567872/vid/avc1/3840x2160/gpJQBjruU8oROc-P.mp4?tag=28)