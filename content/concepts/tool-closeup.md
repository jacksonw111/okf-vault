---
type: Tool
title: "CloseUp"
description: "开源 macOS 原生小工具，在 macOS Mission Control（调度中心）界面直接为每个窗口添加关闭 / 最小化 / 最大化 / 隐藏 / 退出按钮，支持完整键盘操作（⌘W / ⌘M / ⌘F / ⌘H / ⌘Q），并可一键批量关 / 最小化 / 隐藏其他窗口。"
resource: "https://github.com/oomol-lab/CloseUp"
tags: "[macos, mission-control, window-management, swift, native, keyboard-shortcuts]"
timestamp: "2026-07-03T10:27:00Z"
---

# CloseUp

## 它是什么
**开源的 macOS 原生小工具**，在 macOS **Mission Control（调度中心）**界面里，直接给每个缩略图窗口加上「关闭 / 最小化 / 最大化 / 隐藏 / 退出」五个按钮——鼠标移过去就浮现，不用先点窗口再去找按钮。

支持完整键盘操作（`⌘W` / `⌘M` / `⌘F` / `⌘H` / `⌘Q` 等），全部能自定义改键。还能一键批量关掉所有窗口、最小化全部、或只保留当前窗口隐藏其他。

由 oomol-lab 出品。

## 为什么用它 / 适合什么场景
- 经常开几十个窗口，用 Mission Control 找目标，但每次都得点中窗口再操作——CloseUp 让 Mission Control 本身就能直接关。
- 喜欢键盘流（`⌘W` 关 / `⌘M` 最小化等），希望在 Mission Control 缩略图里也能用。
- 一键「关掉所有窗口」或「只留当前」——演示前快速清场。
- 不喜欢装 Bartender / Magnet 等大型窗口管理 App，只想要 Mission Control 增强。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | macOS（原生） |
| 集成界面 | Mission Control（调度中心） |
| 注入按钮 | 关闭 / 最小化 / 最大化 / 隐藏 / 退出 |
| 默认快捷键 | `⌘W` / `⌘M` / `⌘F` / `⌘H` / `⌘Q` |
| 快捷键自定义 | 全部可改键 |
| 批量操作 | 关掉所有 / 最小化所有 / 只保留当前 |
| 形态 | 开源 macOS 原生小工具 |

## 相关概念
- [MacTools](tool-mac-tools.md) — 综合 macOS 菜单栏工具集（含深色模式 / 防休眠等）；CloseUp 专攻 Mission Control 窗口操作
- [OmniWM](tool-omniwm-macos.md) — macOS 水平滚动平铺 WM；CloseUp 不改窗口管理范式，只是给 Mission Control 加按钮

## 项目链接
- 项目主页：<https://github.com/oomol-lab/CloseUp>

## 媒体
![](https://pbs.twimg.com/media/HMRPxH-bAAAQ01y.png)