---
type: Tool
title: "asciicut（Entelligentsia/asciicut）"
description: "面向 asciinema .cast 终端录屏的可视化剪辑工具，Rust 引擎 + Tauri 桌面壳 + SolidJS 界面，时间线波形一眼看出死区"
resource: "https://github.com/Entelligentsia/asciicut"
tags: "[terminal-recording, asciinema, video-editing, tauri]"
timestamp: "2026-08-19T16:00:00Z"
---

# asciicut（Entelligentsia/asciicut）

## 它是什么
[`Entelligentsia/asciicut`](https://github.com/Entelligentsia/asciicut) 是一个专门给 **asciinema `.cast` 终端录屏**用的可视化剪辑工具：Rust 引擎做核心、Tauri 桌面壳承载 UI、SolidJS 负责交互。它把录屏画成「活动时间线波形」——终端在安静等待的段落是平的谷，能一眼看出哪些位置是「卡住等输出 / 没动作的死区」，便于直接拖拽裁剪。

## 为什么用它 / 适合什么场景
- 录了很长的终端演示视频，需要去掉中间发呆 / 编译等待 / 翻文档的空段。
- 想用 GUI 而不是 ffmpeg 一行一行试参数来 cut。
- 维护终端教程 / agent 工作流演示视频。

## 关键能力
| 能力 | 说明 |
|------|------|
| 波形时间线 | 把录屏画成波形，谷底即死区，剪哪里一目了然 |
| Tauri 桌面壳 | 跨平台原生窗口，体积小、启动快 |
| SolidJS 界面 | 响应式 UI，拖拽时间轴流畅 |
| 专注 .cast | 不抢通用视频剪辑的活，只解决「终端录屏」一类问题 |

## 媒体
- ![asciicut 时间线截图](https://pbs.twimg.com/media/HP-qZLqb0AAGjug.jpg)

## 相关概念
- [项目仓库](https://github.com/Entelligentsia/asciicut) — 仓库主页