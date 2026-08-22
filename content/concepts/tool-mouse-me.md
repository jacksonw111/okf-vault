---
type: Tool
title: "mouse-me（Grenish/mouse-me）"
description: "Linux 上统一光标主题：Hyprland / GTK / Qt / X11 一处设置、全部生效"
resource: "https://github.com/Grenish/mouse-me"
tags: "[linux, cursor-theme, hyprland, gtk, qt, x11, ui]"
timestamp: "2026-08-22T05:20:00Z"
---

# mouse-me

## 它是什么
[`Grenish/mouse-me`](https://github.com/Grenish/mouse-me) 解决 Linux 上「换光标主题得分头改四处」的痛点：在 Hyprland / GTK / Qt / X11 这些彼此独立的桌面栈上一次性应用同一份光标配置，**一处设置、全部生效**。

## 为什么用它 / 适合什么场景
- 在 Hyprland（Wayland）+ 部分 Qt 应用 + 偶有 X11 旧软件的环境里被「每个栈光标不统一」困扰的人。
- 主题玩家：经常在 Bibata / Bibata-Modern / Catppuccin / Oxygen 等光标主题之间切换，不想每次都手动改 4 个配置文件。
- 想给同事 / 朋友「一键同步我的光标审美」的小工具。

## 关键能力
| 能力 | 说明 |
|------|------|
| 一次配置 | 一份配置文件覆盖 Hyprland / GTK / Qt / X11 |
| 主题切换 | 改一行即可换整套主题 |
| 跨栈一致 | 不再出现 GTK 应用和 Qt 应用光标样式错位 |
| 轻量 | 单一配置文件 + 命令行工具，无需常驻进程 |

## 媒体
- ![](https://pbs.twimg.com/media/HQPq1LtagAANhPC.jpg)

## 相关概念
- [linux-antiquity](./tool-linux-antiquity.md) — Hyprland 古典艺术风格主题包，思路相近（统一桌面风格）但范围更广
- [TidyFS](./tool-tidyfs.md) — Linux 智能文件整理，按内容与文件名自动归类文档
