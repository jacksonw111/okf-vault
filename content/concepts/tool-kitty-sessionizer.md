---
type: Tool
title: "kitty-sessionizer（kitty 终端的项目会话管理器）"
description: "给 kitty 终端补上 tmux-sessionizer 式的项目会话管理，让多项目切换不用手动开窗口、恢复布局"
resource: "https://github.com/BearDad/kitty-sessionizer"
tags: [kitty, terminal, session-manager, tmux-sessionizer, rust]
timestamp: "2026-08-23T02:47:00Z"
---

# kitty-sessionizer（kitty 终端的项目会话管理器）

## 它是什么

[BearDad/kitty-sessionizer](https://github.com/BearDad/kitty-sessionizer) 给 **kitty 终端**补上一套 `tmux-sessionizer` 风格的项目会话管理：选个项目 → 自动开 / 切到该项目的 kitty 窗口 → 恢复布局，**多项目切换不用手动开窗口**。

## 为什么用它 / 适合什么场景

- 经常在多个项目之间来回切换，每个项目又有自己的目录结构、命令、虚拟环境。
- 已经用 kitty 终端，但嫌原生命令 / session manager 不够「按项目」。
- 喜欢 tmux-sessionizer 的工作流，但希望直接基于 kitty（而不是在 kitty 里再嵌 tmux）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 项目级切换 | 选项目 → 一键进入对应 kitty 窗口 |
| 布局恢复 | 不只是开窗口，连同布局、cwd 一起恢复 |
| kitty 原生 | 不绕道 tmux，直接复用 kitty 的窗口 / 标签能力 |
| 轻量 | sessionizer 类工具的经典套路 |

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HQUGkLIasAA6G6v.mp4>

## 相关概念

- [tmux-workbench](./tool-tmux-workbench.md) — 另一种 tmux / kitty 多项目会话管理思路

## 参考链接

- [项目链接](https://github.com/BearDad/kitty-sessionizer)
