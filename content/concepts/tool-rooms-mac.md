---
type: "Tool"
title: "Rooms（Mac 窗口「房间」一键切换器）"
description: "把 Mac 上散落的项目窗口存成可切换的「房间」——按一次快捷键就能恢复整套窗口并套用布局，省去逐个找窗口 / 切应用 / 重新排版；房间外的窗口会隐藏或推到屏幕外，不会被关闭。"
resource: "https://github.com/saragordic/rooms"
tags: "[macos, window-manager, layout, productivity, rooms, offline, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# Rooms（Mac 窗口「房间」一键切换器）

## 它是什么

[Rooms](https://github.com/saragordic/rooms) 是一个 **Mac 窗口管理工具**，核心概念是「**房间（Room）**」：

- 每个**房间**保存「**一组窗口 + 一份布局**」
- 按 `⌥ Space` 输入房间名 → 一键恢复整套窗口 + 套用布局
- 当前房间**之外**的窗口会**隐藏或推到屏幕外**，**不会被关闭**

布局模板：

| 布局 | 用途 |
|------|------|
| Focus | 单窗口专注 |
| Columns | 左右分栏 |
| Grid | 多格网 |
| My Layout | 自定义 |
| Stack | 堆叠 |

额外能力：

- 按**屏幕**记住布局（外接显示器插拔后能恢复）
- 直接**跳转房间**（不用先关窗口）
- **撤销删除**的房间
- **完全离线**，无账号、无分析、无联网

## 为什么用它 / 适合什么场景

- 经常在「工作 A / 工作 B / 个人项目 / 写代码 / 写文档」之间切——希望一个快捷键切到**完整工作环境**，而不是逐个开窗口、拖位置。
- 不喜欢传统窗口管理工具「**平铺 / 重排**」的强约束——Rooms 把布局做成「**房间**」，切房间就等于切整套工作上下文。
- 担心窗口被关——Rooms 的策略是「**不关、只藏**」，切换无破坏。
- 想完全离线、不上传任何窗口 / 应用信息。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | macOS 原生应用 |
| 快捷键 | `⌥ Space` 唤起房间切换 |
| 房间组成 | 一组窗口 + 一份布局 |
| 房间外窗口 | 隐藏或推到屏幕外（不关闭） |
| 布局模板 | Focus / Columns / Grid / My Layout / Stack |
| 多屏支持 | 按屏幕记住布局 |
| 隐私 | 完全离线、无账号、无分析 |

## 媒体

![](https://pbs.twimg.com/media/HTBqB1IaoAAs6GY.jpg)

## 相关概念

- [Ghostty 主题管理](./tool-sheets-terminal-themes.md) — 同属 macOS 桌面工具，配合 Rooms 使用可一键切到对应主题
- [Tempura](./tool-tempura.md) — Vadim Costin 的桌面专注计时器，可与 Rooms 组合做「专注房间」
