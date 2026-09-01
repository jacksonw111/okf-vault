---
type: "Tool"
title: "todofy（跨平台桌面待办 / 番茄钟 / 任务循环）"
description: "Tauri + Preact + Rust 写的跨平台桌面待办应用（Linux / macOS / Windows）：智能列表、标签、循环任务、番茄钟、提醒全都有，还能缩到系统托盘里默默干活。"
resource: "https://github.com/salarzeidanlou/todofy"
tags: [todo, desktop, tauri, preact, rust, cross-platform, pomodoro, system-tray]
timestamp: "2026-09-01T10:35:00Z"
---

# todofy

## 它是什么
[todofy](https://github.com/salarzeidanlou/todofy) 是一个**跨平台桌面待办应用**，技术栈是 **Tauri + Preact + Rust**，在 Linux / macOS / Windows 上都能跑。功能覆盖典型桌面 GTD 工具的全套：智能列表、标签、循环任务、番茄钟、提醒，还能在**系统托盘**里常驻做「安静」的后台任务管理。

定位：**轻量、原生、跨平台**——比 Electron 体积小、比 SwiftUI / .NET 跨平台。

## 为什么用它 / 适合什么场景
- 想要**跨平台**桌面 GTD 工具，但**不想用 Electron**（体积、内存都重）；
- 喜欢把待办**缩到系统托盘**里、不抢窗口焦点的工作流；
- 想要「智能列表 + 标签 + 循环任务 + 番茄钟 + 提醒」**一套齐全**而不是各装一个 App；
- 喜欢 Rust + Web 技术栈组合的开发风格，未来想自己改。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | Linux / macOS / Windows 三端都能跑 |
| Tauri 内核 | 比 Electron 更轻，原生窗口体验 |
| Preact 前端 | 类 React 开发体验，体积小 |
| Rust 后端 | 性能与并发安全兼顾 |
| 智能列表 | 按规则自动聚合的列表视图 |
| 标签系统 | 多标签筛选 |
| 循环任务 | 周期重复任务支持 |
| 番茄钟 | 内置番茄工作法定时器 |
| 提醒通知 | 任务到期系统级通知 |
| 系统托盘 | 缩进托盘默默干活 |

## 媒体
![](https://pbs.twimg.com/media/HRBUgwjbwAEL3FF.jpg)

## 相关概念
- [JeffBox](tool-jeffbox.md) — .NET 9 + WPF 单文件 Windows 桌面三件套（含待办）；todofy 跨平台、JeffBox 单文件
- [Beichen Pi / 北辰 Pi](tool-beichen-pi.md) — 同样是 Tauri 路线的桌面应用；面向本地 Agent，todofy 面向待办

## 参考链接
- 项目链接：<https://github.com/salarzeidanlou/todofy>