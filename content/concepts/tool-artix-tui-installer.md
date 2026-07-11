---
type: Tool
title: "Artix TUI Installer"
description: "YellowHearth1 用 Rust + ratatui 写的 Artix Linux 终端安装器，带乌克兰语 / 英语双语界面，专门给用 dinit 的 Artix 做系统安装，也能进系统恢复模式。"
resource: "https://github.com/YellowHearth1/artix-tui-installer"
tags: "[linux, artix, installer, rust, tui, ratatui]"
timestamp: "2026-07-11T20:00:00Z"
---

# Artix TUI Installer

## 它是什么

`YellowHearth1/artix-tui-installer` 是一个**Artix Linux 的 TUI 终端安装器**：

- 用 **Rust + ratatui** 写的 TUI（终端 UI），不依赖桌面环境。
- **乌克兰语 / 英语双语**界面。
- 专门适配 Artix Linux（用 **dinit** 做 init，不用 systemd）。
- 除了正常安装，也能进**系统恢复模式**。

## 为什么用它 / 适合什么场景

- 想装 Artix Linux，但不想用 Calamares 这种 GTK 桌面安装器。
- 偏好「纯终端」装机体验，对 TUI 比对 GUI 更熟。
- dinit 用户——主流发行版工具多假设 systemd，Artix 用户需要专属工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| TUI | Rust + ratatui，终端里操作 |
| 双语 | 乌克兰语 / 英语切换 |
| Artix 专用 | 针对 dinit init 系统适配 |
| 恢复模式 | 除正常安装外支持进救援模式 |

## 媒体参考

- 项目截图：

![Artix TUI Installer](https://pbs.twimg.com/media/HM6yyknaIAAu5k0.jpg)

## 相关概念

- [Tork](tool-tork.md) — 终端 BT 客户端 + 一键拉 Linux ISO
- [Linux Antiquity](tool-linux-antiquity.md) — Hyprland 主题包

## 项目链接

- 项目仓库：<https://github.com/YellowHearth1/artix-tui-installer>