---
type: Tool
title: "Denial（Flutter 桌面图形层的 Wayland 合成器）"
description: "用 Flutter 做桌面图形层的 Wayland 合成器，把 shell、动效和窗口合成统一到 Flutter 场景中。"
resource: "https://github.com/denialwm/denial"
tags: [wayland, flutter, compositor, desktop, shell, ui]
timestamp: "2026-07-28T15:37:00.000Z"
---

# Denial

## 它是什么

一个把 **Flutter** 作为桌面图形层的 **Wayland 合成器**——把 shell、动效、窗口合成统一到 Flutter 场景中。

![截图示例](https://pbs.twimg.com/media/HOSP8ulbMAAf7Yx.jpg)

## 它在做什么

传统 Wayland 合成器（如 sway / Hyprland）：

- 桌面渲染层：各家实现（cairo / OpenGL / Vulkan）
- 动画：自己写或用库
- Shell：单独组件

Denial 用 Flutter 把这三层**统一成一个 Flutter 场景**——你能用 Flutter 的所有能力（Skia、widget 树、动画引擎）做整个桌面。

## 关键能力

| 能力 | 说明 |
|------|------|
| Flutter 桌面层 | widget / Skia / 动效全打通 |
| Wayland 合成器 | 标准协议客户端可用 |
| 统一 shell + 动效 + 窗口合成 | 一个 Flutter 场景 |
| 实验性 / 前沿 | Wayland + Flutter 的少见组合 |

## 适用场景

- 想用 Flutter 写整个桌面的实验者
- 自定义桌面 shell（动效 / 视觉）
- Wayland 生态探索

## 原始链接

- [项目仓库](https://github.com/denialwm/denial)
- [推文剪藏](https://x.com/QingQ77/status/2082128194128478601)

## 相关概念

- [Waylandar](./tool-waylandar.md) — Wayland 桌面上的 Google Calendar 桌面挂件
- [Linux Antiquity（Hyprland 古典艺术风格主题包）](./tool-linux-antiquity.md) — Hyprland 主题 / Quickshell / 终端配色 / 图标
- [DeskBox（WinUI 3 桌面整理工具）](./tool-deskbox.md) — Windows 桌面整理
- [OmniWM（macOS 水平滚动平铺 WM）](./tool-omniwm-macos.md) — macOS 滚动列平铺