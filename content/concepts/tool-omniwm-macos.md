---
type: "Tool"
title: "OmniWM（macOS 水平滚动平铺窗口管理器）"
description: "在 macOS 上实现 Niri 风格的水平滚动平铺窗口管理器，基于 OmniWM 改造，仅保留滚动列布局，配置用 TOML 分文件存放，热加载无需重启。"
resource: "https://github.com/macos-in-horiz-scroll/omniwm"
tags: "[macos, tiling, window-manager, niri, toml]"
timestamp: "2026-06-21T00:00:00Z"
---

# OmniWM（macOS 水平滚动平铺窗口管理器）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 macOS 平铺窗口管理器（tiling WM），从 [Niri](https://github.com/YaLTeR/niri) 的思路汲取灵感：把窗口排成一列一列，左右滚动像翻页一样切换。它**只保留 Niri 风格的滚动列布局**，剥离其它花哨功能，做成一个轻量、聚焦的 macOS 工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 布局 | 水平滚动列 —— 窗口列成一行，左右键翻页 |
| 工作区 | 支持多工作区、多显示器 |
| 视觉 | 窗口可加颜色边框、快捷键与命令面板 |
| 配置 | TOML 文件，按模块拆分，改完热加载、无需重启 |
| 底层 | 在 [OmniWM](https://github.com/senekor/omnivium) 基础上改造 |

## 适用场景

- 写代码 / 跑长会话时，希望像 Niri 用户那样用「列」而不是「网格」组织窗口。
- 用腻了 Aerospace、yabai 这类网格平铺 WM，想要更接近 Niri 的滚动体感。
- 喜欢配置即文件、改完即生效的工程文化（TOML > GUI 配置面板）。

## 相关概念

- [Biome](tool-biome.md) — 配置用文件 vs GUI 偏好的同类工程哲学
- [Forel（macOS 文件夹自动化）](tool-forel-macos.md) — 另一个 macOS 本地优先小工具