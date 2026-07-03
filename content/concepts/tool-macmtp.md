---
type: Tool
title: "MacMTP"
description: "macOS 上通过 USB MTP 协议原生传输文件到 Android 设备；SwiftUI 前端 + Go MTP 引擎（基于 OpenMTP / Kalam）通过 C 桥接层集成；双面板文件浏览器、批量传输带进度、冲突处理（覆盖 / 跳过 / 按大小比对）、拖拽、快捷键、暗色模式；Apple Silicon + Intel，macOS 14+。"
resource: "https://github.com/kalabhaftu/MacMTP"
tags: "[macos, android, mtp, file-transfer, swift, swiftui, go, open-source, usb]"
timestamp: "2026-07-03T15:39:00Z"
---

# MacMTP

## 它是什么
**macOS 上通过 USB MTP 协议原生传输文件到 Android 设备**——无需 Android File Transfer（已被 Google 弃用）、OpenMTP、MacDroid 等第三方付费工具。

技术架构：
- **前端**：Swift / SwiftUI
- **MTP 引擎**：Go 实现（基于 OpenMTP / Kalam）
- **桥接层**：C 接口把 Go 引擎集成进 Swift 应用

双面板文件浏览器（左边本地、右边 Android 设备），支持**批量传输带进度**、**冲突处理**（覆盖 / 跳过 / 按大小比对）、**拖拽**、**快捷键**、**暗色模式**。同时支持 **Apple Silicon 和 Intel**，需要 **macOS 14.0+**。

由 kalabhaftu 开发。

## 为什么用它 / 适合什么场景
- Android File Transfer 被 Google 弃用后，macOS 用户传文件到 Android 一直不方便——MacMTP 是原生 MTP 协议替代。
- 已有 OpenMTP 但觉得它 UI 旧 / 不原生——MacMTP 用 SwiftUI 重写，UI 更现代、macOS 原生。
- 经常批量传输照片 / 视频到 Android，需要进度显示与冲突处理。
- 想在 macOS 上像访达一样用双面板浏览 Android 文件系统。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | macOS 14.0+ |
| 架构支持 | Apple Silicon + Intel |
| 协议 | USB MTP（Android 原生文件传输协议） |
| 前端 | Swift / SwiftUI（原生 UI） |
| MTP 引擎 | Go（基于 OpenMTP / Kalam） |
| 桥接 | C 接口集成 Go 引擎 |
| 文件浏览器 | 双面板（左本地 / 右 Android） |
| 批量传输 | 支持，带进度条 |
| 冲突处理 | 覆盖 / 跳过 / 按大小比对 |
| 交互 | 拖拽 / 快捷键 |
| 主题 | 暗色模式 |

## 相关概念
- [Targie](tool-targie-similar-finder.md) — macOS 重复 / 相似视频与图片扫描；MacMTP 是传输，Targie 是整理去重

## 项目链接
- 项目主页：<https://github.com/kalabhaftu/MacMTP>

## 媒体
![](https://pbs.twimg.com/media/HMRS34YbkAAWVUH.jpg)