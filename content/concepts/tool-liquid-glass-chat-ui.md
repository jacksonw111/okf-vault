---
type: "Tool"
title: "liquid-glass-chat-ui（Expo iOS 26 液态玻璃聊天界面）"
description: "在 Expo 里复刻 iOS 26 液态玻璃聊天界面的开源仓库，给出两套完整实现：原生材质 + Skia 着色器 + 手势动画整套方案。"
resource: "https://github.com/Appllama/liquid-glass-chat-ui"
tags: "[expo, react-native, ios26, liquid-glass, skia, chat-ui, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# liquid-glass-chat-ui（Expo iOS 26 液态玻璃聊天界面）

## 它是什么

[liquid-glass-chat-ui](https://github.com/Appllama/liquid-glass-chat-ui) 是 Appllama 开源的仓库，在 Expo 框架里复刻 iOS 26 的液态玻璃聊天界面，提供两套完整实现：原生材质方案 + Skia 着色器方案。

## 关键能力

| 能力 | 说明 |
|------|------|
| iOS 26 液态玻璃 | 复刻 iOS 26 新材质的视觉效果 |
| 双方案实现 | 原生材质实现 + Skia 着色器实现，各取所需 |
| 手势动画 | 完整的拖动 / 缩放手势驱动 |
| React Native | 在 Expo 生态里可用，不需切原生开发 |

## 技术要点

要在 Expo 里实现 iOS 26 液态玻璃，需要自己趟：
- 原生材质调用（Liquid Glass material）
- Skia 着色器（自定义渲染）
- 手势动画（react-native-reanimated / gesture-handler）
- 与现有聊天组件的集成

## 媒体预览

![](https://pbs.twimg.com/media/HTWSEF2a8AAA1Rb.jpg)
![](https://pbs.twimg.com/media/HTWSFaVbIAANXE_.jpg)

## 原始链接

- 项目主页：<https://github.com/Appllama/liquid-glass-chat-ui>

## 相关概念

- [Hyalite（液态玻璃）](./tool-hyalite-liquid-glass.md) — 通用液态玻璃 UI 组件方案
- [Plasma UI](./tool-plasma-ui.md) — Web 端液态玻璃面板组件库
- [Liquid Glass](./tool-liquid-glass.md) — 液态玻璃 UI 通用条目