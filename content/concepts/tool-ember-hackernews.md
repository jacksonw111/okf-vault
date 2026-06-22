---
type: "Tool"
title: "Ember（原生 SwiftUI Hacker News 阅读器）"
description: "DatanoiseTV/ember-hackernews —— 原生、无障碍友好的 Hacker News iOS / iPad / Mac 客户端，零第三方依赖，纯 SwiftUI 构建，原生评论展开 + 离线缓存 + 自动匹配无障碍设置。"
tags: "[hacker-news, ios, mac, swiftui, reader, accessibility, zero-dependency]"
timestamp: "2026-06-22T16:10:00Z"
---

# Ember（原生 SwiftUI Hacker News 阅读器）

## 它是什么

[`DatanoiseTV/ember-hackernews`](https://github.com/DatanoiseTV/ember-hackernews) 是一个**原生的、无障碍友好的 Hacker News iOS / iPad / Mac 客户端**。

特性：

- **零第三方依赖** —— 不引入任何外部库
- **纯 SwiftUI** 构建
- **一套代码跑通 iPhone / iPad / Mac**
- **评论原生展开** —— 不依赖 WebView 加载
- **无障碍友好** —— 首次启动读取设备无障碍设置，自动匹配偏好
- **离线缓存** —— 看过的内容离线可读

> 截图：![](https://pbs.twimg.com/media/HLY33eLa0AAPIm5.jpg)

## 为什么用它 / 适合什么场景

- **macOS / iOS 重度用户**：不想开 Safari 看 HN。
- **无障碍依赖**：VoiceOver / 增大字体 / 减少动效偏好被原生尊重。
- **零依赖审美**：纯 SwiftUI 一个仓库搞定，没有 React Native / Flutter 这种跨平台抽象。
- **离线通勤**：缓存过的故事地铁上也能读。

适合：

- HN 资深读者（每天刷几十条）
- 重视 Apple 平台原生体验的开发者
- 无障碍用户 / 测试员

## 关键能力

| 能力 | 说明 |
|---|---|
| 纯 SwiftUI | 无 UIKit 兜底 |
| 零第三方依赖 | 单仓单 target |
| iOS / iPadOS / macOS | 一套代码多端 |
| 原生评论展开 | 不走 WebView |
| 无障碍自动匹配 | 读取设备偏好 |
| 离线缓存 | 本地存储历史 |

## 与同类工具对比

| 维度 | 第三方 HN App | Ember |
|---|---|---|
| 形态 | 通常 WebView 包装 | **纯 SwiftUI 原生** |
| 第三方依赖 | 多个包 | **零** |
| 评论展开 | WebView 加载 | **原生展开** |
| 无障碍 | 通常手动配置 | **自动匹配设备偏好** |
| 离线 | 视应用而定 | 内置缓存 |

## 参考链接

- [项目链接](https://github.com/DatanoiseTV/ember-hackernews)

## 相关概念

- [ShipSwift](tool-shipswift.md) — AI 原生 SwiftUI 组件库 + MCP skills（同属「SwiftUI 生态」方向）
- [Obsidian](tool-obsidian.md) — 知识管理（HN 资深读者通常与 Obsidian 共用做技术笔记）