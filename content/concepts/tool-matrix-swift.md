---
type: "Tool"
title: "matrix-swift（SwiftUI 点阵库）"
description: "mana-am 移植的 SwiftUI 版本 dot-matrix 库，复刻 LED 点阵屏的字符显示效果，可在 iOS/macOS 应用里渲染动态点阵文字与动画。"
tags: "[swiftui, ios, macos, animation, dot-matrix]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/mana-am/matrix-swift"
---

# matrix-swift（SwiftUI 点阵库）

## 它是什么

[`matrix-swift`](https://github.com/mana-am/matrix-swift) 是把社区里流行的 [dot-matrix](https://github.com/notnotjake/dot-matrix) JavaScript 库移植到 **SwiftUI** 的同名项目。点阵矩阵由若干颗 LED 风格的点组成，可在屏幕上渲染任意字符、表情、动画并保留「老式电子屏」的复古颗粒感。

作者把渲染层改成纯 SwiftUI 视图，原项目以 `View` 方式暴露，开发者一行 import 即可把字符拆成 8×N 点阵并渲染。

## 关键能力

| 能力 | 说明 |
|------|------|
| SwiftUI 原生 | 直接作为 `View` 使用，支持 modifier 与状态绑定 |
| 可定制点阵 | 控制点的尺寸、间距、亮灭色与开关速度 |
| 字符 / 动画 | 渲染单字符、字符串、滚动字幕 / 闪烁效果 |
| 跨 Apple 平台 | iOS / iPadOS / macOS 同一份 API 通用 |
| 复古风格 | 适合做加载动画、空状态文案、签名 footer、品牌 Logo 装饰 |

## 适用场景

- App 启动屏 / 加载动画的复古氛围
- 空状态页或表单错误提示的点阵文案
- 直播 / 游戏 App 的「弹幕」或「跑马灯」效果
- 桌面小组件（Widget / Lock Screen）做像素艺术文字

## 参考链接

- [项目链接](https://github.com/mana-am/matrix-swift)
- [原始链接](https://x.com/zzzzshawn/status/2073364681184649635)
- [原始 dot-matrix 项目](https://github.com/notnotjake/dot-matrix)

## 相关概念

- [gradient-shimmer-swiftui](tool-gradient-shimmer-swiftui.md) — 同类 SwiftUI 视觉装饰库，用渐变闪光替代点阵颗粒
- [Animations.dev / Vocabulary](tool-animations-dev-vocabulary.md) — Emil Kowalski 的动画动作词汇表，可与点阵动画组合做「动画语言」层