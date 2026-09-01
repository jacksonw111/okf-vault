---
type: "Tool"
title: "JeffBox（.NET 9 + WPF 单文件 Windows 桌面工具箱）"
description: ".NET 9 + WPF 构建的 Windows 桌面工具箱，发布为约 450KB 的单文件程序，零外部依赖；包含待办清单（无限层级子任务 + 优先级 + 提醒）、Markdown 笔记模块（编辑 / 预览同屏切换、3.5MB+ 文档秒开）、快速启动器（分类标签 + 拖拽排序 + 启动频率统计）三件套。"
resource: "https://github.com/Jeffrey56400/JeffBox"
tags: [windows, desktop, dotnet, wpf, todo, markdown-editor, launcher, single-file]
timestamp: "2026-09-01T06:30:00Z"
---

# JeffBox

## 它是什么
[JeffBox](https://github.com/Jeffrey56400/JeffBox) 是一个**基于 .NET 9 + WPF 构建的 Windows 桌面工具箱**，定位是「**一个 .exe 干三件事**」：发布后是约 **450KB** 的**单文件程序**，**零外部依赖**（不依赖 .NET 运行时预装、不依赖第三方 dll）。

打包了三个常用模块：

| 模块 | 能力 |
|------|------|
| 待办清单 | 无限层级子任务、优先级、提醒 |
| 笔记模块 | 编辑 / 预览同屏切换、完整 Markdown + 流式渲染（3.5MB+ 文档秒开） |
| 快速启动器 | 分类标签、拖拽排序、启动频率统计 |

## 为什么用它 / 适合什么场景
- 想要**单文件 .exe** 的 Windows 桌面工具箱——双击即用，不用安装、零依赖；
- 想把「待办 + Markdown 笔记 + 应用启动」**塞进同一个原生 Windows 应用**；
- 公司 / 学校**机器锁权限**（不让装、不让运行时不联网）也能用——一个文件传过去就能跑；
- 喜欢**WPF 原生体验**（不像 Electron 那么重），又不想自己撸一套窗口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单文件发布 | 约 450KB，一个 .exe 顶全套 |
| 零外部依赖 | .NET 9 + WPF 自包含 |
| 待办清单 | 无限层级子任务 + 优先级 + 提醒 |
| 笔记模块 | 编辑 / 预览同屏切换 |
| 流式渲染 | 3.5MB+ Markdown 文档秒开 |
| 启动器 | 分类标签 + 拖拽排序 + 启动频率统计 |
| 原生 WPF | 不用 Electron，性能更好 |
| Windows 原生体验 | 与系统外观 / 通知深度集成 |

## 媒体
![](https://pbs.twimg.com/media/HRBPVzGboAASTsy.png)

## 相关概念
- [Kenote](tool-kenote.md) — 同样基于 Tauri + React 的跨平台 Markdown 笔记；JeffBox 是 Windows 原生 + 单文件路线
- [Todofy](tool-todofy.md) — Tauri + Preact + Rust 的跨平台桌面待办；JeffBox 多了笔记 + 启动器两件

## 参考链接
- 项目链接：<https://github.com/Jeffrey56400/JeffBox>