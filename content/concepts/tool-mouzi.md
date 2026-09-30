---
type: Tool
title: "Mouzi（下载文件夹自动整理的 Tauri 桌面工具）"
description: "Tauri 2 + React 19 + Rust 写的下载文件夹自动整理工具：常驻系统托盘，按自定义规则把新到的文件移动、重命名、归类到目标文件夹。"
resource: "https://github.com/hsr88/mouzi"
tags: [downloads, file-organization, tauri, rust, react, desktop]
timestamp: 2026-09-30T05:27:00Z
---

# Mouzi

## 它是什么

**Mouzi** 是 [hsr88](https://github.com/hsr88) 维护的桌面应用：常驻系统托盘，**监听下载文件夹**并在新文件到达时按规则**自动移动、重命名、归类**到目标目录。

技术栈：

- **Tauri 2**（系统壳）
- **React 19**（UI）
- **Rust**（后端逻辑）

## 为什么用它 / 适合什么场景

- 下载文件夹常年堆满各种 PDF / 安装包 / 截图，希望按类型自动归档。
- 不喜欢 macOS / Windows 自带下载文件夹的"按时间排序"视图，希望按业务规则重命名 / 归类。
- 想要一款**系统托盘常驻**的小工具，开机即跑、不抢主界面焦点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 系统托盘常驻的桌面应用 |
| 监听目标 | 用户指定文件夹（典型为下载目录） |
| 触发时机 | 新文件到达 |
| 自动动作 | 移动 / 重命名 / 归类 |
| 规则 | 用户可自定义 |
| 技术栈 | Tauri 2 + React 19 + Rust |

## 参考链接

- 仓库：<https://github.com/hsr88/mouzi>

## 媒体

- ![](https://pbs.twimg.com/media/HTXgiYiaUAAjGwm.png)

## 相关概念

- [Tauri 桌面应用](./term-ratatui.md) — Mouzi 用到的 Rust 桌面壳生态