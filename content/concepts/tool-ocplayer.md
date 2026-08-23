---
type: Tool
title: "OcPlayer · 橘猫播放器（Jellyfin 苹果端原生客户端）"
description: "1824239290/OcPlayer，SwiftUI 界面 + Rust 播放内核的 Jellyfin 苹果端原生客户端，硬解 / 字幕 / 弹幕全支持"
resource: "https://github.com/1824239290/OcPlayer"
tags: [jellyfin, swiftui, rust, media-player, apple]
timestamp: "2026-08-23T08:22:00Z"
---

# OcPlayer · 橘猫播放器（Jellyfin 苹果端原生客户端）

## 它是什么

[1824239290/OcPlayer](https://github.com/1824239290/OcPlayer) 是给 **Jellyfin** 媒体服务器做的**苹果端原生客户端**：

- **SwiftUI** 界面 → 与 macOS / iOS 设计语言一致
- **Rust** 播放内核 → 性能与安全兼顾
- 硬解 / 字幕 / 弹幕全支持

针对的痛点：Jellyfin 在苹果端缺少好用的**原生**客户端。

## 为什么用它 / 适合什么场景

- 自建 Jellyfin 媒体库，日常用 Mac / iPhone / iPad 观看。
- 想要 SwiftUI 原生体验（动画、Haptics、系统集成），而不是 Electron / Web 套壳。
- 看重硬解（4K HDR）与字幕 / 弹幕支持。

## 关键能力

| 能力 | 说明 |
|------|------|
| SwiftUI 界面 | 与苹果生态设计语言一致 |
| Rust 播放内核 | 高性能、低资源占用、内存安全 |
| 硬解支持 | 4K / HDR 等高码率视频本地解码 |
| 字幕 / 弹幕 | 满足二次元 / 海外剧的字幕与互动场景 |
| 与 Jellyfin 协议兼容 | 对接自托管 Jellyfin 服务 |

## 相关概念

- [BiliMusic（B 站音乐播放器）](./tool-bili-music-electron.md) — 同类针对特定媒体服务的桌面客户端
- [LX Music Desktop](./tool-lx-music-electron.md) — 跨平台桌面媒体客户端

## 参考链接

- [项目链接](https://github.com/1824239290/OcPlayer)
