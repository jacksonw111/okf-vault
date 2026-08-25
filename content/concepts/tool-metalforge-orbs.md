---
type: Tool
title: "MetalForge（Thinking Orbs）"
description: "跨 SwiftUI / React Native / Web 的「思考中」动效组件库（Thinking Orbs），用 metalforge.xyz 提供统一封装。"
resource: "https://metalforge.xyz"
tags: [ui-component, loading, swiftui, react-native, web, animation]
timestamp: "2026-08-25T19:30:00Z"
---

# MetalForge（Thinking Orbs）

## 它是什么

[MetalForge](https://metalforge.xyz) 提供跨平台统一的 **Thinking Orbs**（思考中球）动效组件：一组表示「AI 正在思考 / 生成中」的视觉指示器，分别发布到：

- **SwiftUI**（Apple 平台）
- **React Native**（跨端移动）
- **Web**（任意前端）

LLM 类应用「流式输出」期间需要给用户「正在处理」的反馈，传统 `Loading…` 文字或旋转图标太枯燥；Thinking Orbs 用视觉上更有质感的小球动画取代它们。

视频：<https://video.twimg.com/amplify_video/2091827088068096000/vid/avc1/1766x1316/-Qx8fT4wF8K1ZjhB.mp4?tag=29>

## 为什么用它 / 适合什么场景

- **AI 聊天 / 生成式 UI 产品**：在「流式响应等待期」展示更有质感的视觉反馈。
- **想避免每个平台各自造轮子**：MetalForge 在三端提供一致 API 与外观。
- **不想写复杂动效**：直接 import 组件即可拿到好看的球动画。
- **跨端一致体验**：iOS / Android / Web 用户看到的「思考中」反馈一致。

## 关键能力

| 能力 | 说明 |
|------|------|
| SwiftUI 组件 | 直接在 SwiftUI 视图里嵌入 |
| React Native 组件 | 跨端移动使用 |
| Web 组件 | 浏览器中使用 |
| 一致外观 | 跨端统一的视觉与动效 |
| 「思考中」反馈 | 替代传统 Loading 文案 / 旋转图标 |

## 相关概念

- [Kinetics](./tool-kinetics.md) — 同样提供动画资源、但面向「运动效果动画」场景
- [beUI Animated Select](./tool-beui-select.md) — 另一种 UI 动效组件

## 参考链接

- 项目链接: <https://metalforge.xyz>
- 原始链接: <https://x.com/Wen_Zw/status/2091998270205935909>