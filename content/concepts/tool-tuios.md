---
type: Tool
title: "tuios (Gaurav-Gosain/tuios)"
description: "Go 写的轻量终端复用器：跑在现成终端内部，vim 式模态操作管理多个窗格、9 个工作区、BSP 平铺与命令面板"
resource: "https://github.com/Gaurav-Gosain/tuios"
tags: [terminal, multiplexer, tiling, vim, go, tui]
timestamp: "2026-08-18T12:00:00Z"
---

# tuios (Gaurav-Gosain/tuios)

## 它是什么
`Gaurav-Gosain/tuios` 是一个 Go 写的**轻量终端复用器**：跑在「现成的终端」内部（不需要 tmux / Zellij 那种独立 server），用 **vim 式模态键位** 在一个终端里管理多个窗格、9 个工作区、BSP 平铺布局与命令面板。

## 为什么用它 / 适合什么场景
- 想要 tmux 的多窗格能力，但希望「单进程、随用随关、无 server」。
- 已经习惯 vim 按键，希望复用同一套肌肉记忆到终端布局切换。
- 想在 SSH 进机器后立刻获得 tiling 工作区，不需要额外装 X / Wayland。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端内部运行 | 不开 server、不占额外端口 |
| vim 式模态 | 复用 vim 用户熟悉的按键与模式 |
| 9 个工作区 | 类 vim tab 的多工作区切换 |
| BSP 平铺 | 二叉空间分割自动平铺窗格 |
| 命令面板 | 类 VS Code 命令面板的快速操作入口 |

## 媒体
- 视频：<https://video.twimg.com/amplify_video/2089134810568757248/vid/avc1/1280x720/v__Ftl1Dmk4ws6hh.mp4?tag=29>

## 相关概念
- [项目链接](https://github.com/Gaurav-Gosain/tuios) — 仓库地址
