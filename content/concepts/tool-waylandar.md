---
type: "Tool"
title: "Waylandar（Wayland 桌面上的 Google Calendar 桌面挂件）"
description: "一个给 Wayland 桌面环境用的 Google Calendar 桌面挂件 / 小工具，让你在桌面直接看今日日程和整月日历，不用打开浏览器。"
tags: "[wayland, calendar, google-calendar, desktop, linux, gnome, kde]"
timestamp: "2026-06-22T07:25:00Z"
---

# Waylandar（Wayland 桌面上的 Google Calendar 桌面挂件）

## 它是什么

[samjoshuadud/waylandar](https://github.com/samjoshuadud/waylandar) 是一个 **Wayland 桌面**用的 **Google Calendar 桌面挂件**。把它放到桌面上，你就能直接在桌面上看到今天的日程安排（甚至整月日历视图），而**不必专门打开浏览器**到 Google Calendar 网页。

> 视频演示：<https://video.twimg.com/tweet_video/HLTVVfQasAAtjTZ.mp4>

## 为什么用它 / 适合什么场景

- **Wayland 生态长期缺原生桌面挂件**：X11 时代有 `gcalcli` + conky / i3status 之类组合，但 Wayland 上 X11 协议不再适用，conky 不再能绘桌面，必须用 Wayland 兼容方案（如 `wtype` / `wlr-layer-shell` / GTK4 Wayland）。
- **不想为看一眼日程就开浏览器**：日程这种东西需要"瞥一眼"——浏览器标签页切来切去成本太高。
- **Linux 桌面重度用户**：常驻 Wayland 桌面（GNOME / KDE / Sway / Hyprland 等），希望日历可视化贴近 macOS 的"日历.app"体验。

## 关键能力

| 能力 | 说明 |
|---|---|
| Google Calendar 集成 | 拉取用户的 Calendar 事件 |
| 桌面挂件渲染 | 直接在 Wayland 桌面绘出 UI（推测走 GTK4 / Qt6 / wlroots layer-shell） |
| 日程视图 | 今日日程 + 整月日历 |
| 不开浏览器 | 一站式替代 calendar.google.com |

## Wayland 桌面挂件的实现路径（背景知识）

要在 Wayland 桌面上画"桌面挂件"，常见路径：

| 路径 | 说明 | 代表 |
|---|---|---|
| **wlr-layer-shell** | wlroots 协议（Sway / Hyprland 等）支持图层 shell，能让窗口常驻桌面、桌面之上 / 之下 | waybar、ags |
| **GTK4 + Wayland** | 原生 Wayland 应用，通过 XDG 桌面集成 | GNOME Calendar、Calendar |
| **Qt6 + Wayland** | KDE 风格的桌面挂件 | KDE Plasma widgets |
| **X11 转发（不行）** | XWayland 能跑 X11 应用，但失去原生 Wayland 优势 | — |

waylandar 大概率基于 GTK4 或 wlroots layer-shell。复刻时需要根据目标桌面环境选对应技术栈。

## 适用人群

- Wayland 桌面（GNOME 40+ / KDE Plasma 5.27+ / Sway / Hyprland）用户。
- 重度 Google Calendar 用户（事件多到必须用专门工具管理）。
- 喜欢 macOS "日历.app"风格的视觉密度但用 Linux 的人。

## 参考链接

- [项目链接](https://github.com/samjoshuadud/waylandar)
- [原始链接](https://t.co/vx9GeakNwB)
- [演示视频](https://video.twimg.com/tweet_video/HLTVVfQasAAtjTZ.mp4)

## 相关概念

- [OmniWM（macOS 水平滚动平铺 WM）](tool-omniwm-macos.md) — 桌面环境工具（同属"重塑桌面体验"范畴）
- [Forel（macOS 文件夹自动化）](tool-forel-macos.md) — macOS 文件夹自动化，桌面工具另一面