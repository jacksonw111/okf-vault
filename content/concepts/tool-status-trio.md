---
type: "Tool"
title: "Status Trio"
description: "原生 macOS 菜单栏应用，把 Wi-Fi / 电量 / 音量三项系统状态合并成一个可配置的组合图标，灵感来自 iPhone Duo 的合并状态栏（Mac 上用音量代替蜂窝数据）。"
resource: "https://github.com/lingyired/status-trio"
tags: "[macos, menubar, system-status, swiftui, native, minimalist]"
timestamp: "2026-09-16T16:12:00Z"
---

# Status Trio

## 它是什么

[lingyired/status-trio](https://github.com/lingyired/status-trio) 是一款**原生 macOS 菜单栏应用**，把 **Wi-Fi、电量、音量** 三项系统状态合并成**一个可配置的组合图标**。灵感来自 iPhone Duo 的合并状态栏——Mac 上没有蜂窝数据，所以改用音量作为第三个状态。

## 为什么用它 / 适合什么场景

- 觉得 macOS 菜单栏默认图标太占空间。
- 想要一个「看一眼就知道三项关键状态」的状态聚合器。
- 偏好原生 SwiftUI 小工具、不想装 Electron 类重客户端。
- 想要在 iPhone Duo 与 MacBook 之间保持一致的状态栏观感。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三合一图标 | Wi-Fi / 电量 / 音量合并到单一菜单栏位 |
| 可配置 | 各状态的呈现顺序 / 阈值可调 |
| 原生 SwiftUI | 占用低、跟随系统主题 |
| Duo 灵感 | 与 iPhone Duo 合并状态栏观感一致 |
| 状态聚合 | 减少视觉噪音，节省菜单栏位 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTtRNDb0AALi15.png)

## 相关概念

- [Sheets (终端主题管理器)](./tool-sheets-terminal-themes.md) — 同为「macOS 原生小工具」谱系，把多余菜单栏位让出来
- [NetFluss](./tool-netfluss.md) — 另一款 macOS 菜单栏聚合工具