---
type: Tool
title: "what-cant-i-press"
description: "ericwbailey/what-cant-i-press，跑在 macOS 菜单栏 / Windows 系统托盘里的无障碍快捷键探查工具：扫描当前聚焦应用或全部已打开应用，从 JAWS / Narrator / NVDA / Orca / VoiceOver 文档取快捷键列表，告诉你「这里按啥」。"
resource: "https://github.com/ericwbailey/what-cant-i-press"
tags: "[accessibility, a11y, keyboard, screen-reader, menu-bar, tray]"
timestamp: "2026-08-01T20:30:00Z"
---

# what-cant-i-press

## 它是什么

[`ericwbailey/what-cant-i-press`](https://github.com/ericwbailey/what-cant-i-press) 是一个**跑在 macOS 菜单栏 / Windows 系统托盘**的无障碍快捷键探查工具。打开后能扫「当前聚焦的应用」或「全部已打开的应用」，告诉你「这个按钮 / 菜单项 / 控件**可以按哪个键**触发」。

快捷键列表的来源很扎实——从 **JAWS / Narrator / NVDA / Orca / VoiceOver** 等屏幕阅读器的官方文档里抽取，再合并操作系统级和各应用的菜单快捷键。

## 关键能力

| 能力 | 说明 |
|------|------|
| 菜单栏 / 系统托盘常驻 | 点一下就能呼出，不抢主屏幕 |
| 单应用扫描 | 扫当前聚焦的应用，给出当前界面所有可触发的快捷键 |
| 全应用扫描 | 一次性扫所有已打开的应用，做「全局快捷键地图」 |
| 多源数据 | 屏幕阅读器文档 + 系统级 + 应用级快捷键聚合 |
| 无障碍导向 | 本身就是一个无障碍工具（点出哪些键可以替代鼠标） |

## 解决什么痛点

- 「这个按钮有快捷键吗？」——鼠标右键看菜单只能看到菜单项，看不到隐藏快捷键
- 「我想只用键盘操作这个应用」——但不知道有哪些可用快捷键
- 视障 / 运动障碍用户依赖快捷键，但发现成本极高

## 适合什么场景

- 想提升键盘效率的开发者 / 写作者
- 无障碍用户（screen reader 用户 + 残障用户）需要了解所有可触发快捷键
- 给一个新应用做 onboarding，想快速上手所有快捷键

## 与同类工具的差异

| 工具 | 范围 | 差异 |
|------|------|------|
| CheatSheet（macOS） | 单应用 | 长按 ⌘ 弹窗，只显示当前应用菜单快捷键 |
| 通用按键查看工具 | 单应用 | 不聚合屏幕阅读器文档 |
| what-cant-i-press | 全局 + 多源 | 全应用扫描 + 屏幕阅读器文档来源 |

## 媒体

视频：

- <https://video.twimg.com/amplify_video/2083013361860853760/vid/avc1/2276x1496/cSpsdPOAEKg9vs8F.mp4?tag=29>

## 原始链接

- [项目仓库](https://github.com/ericwbailey/what-cant-i-press)
- [原始推文](https://x.com/QingQ77/status/2083466260923486648)