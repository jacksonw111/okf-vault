---
type: Tool
title: "Termium（终端里跑真 Chromium 的 TUI 浏览器）"
description: "codr1 出品的 TUI 浏览器：把 Chromium 嵌入终端里跑，用户在纯文本终端里打开真实网页并像浏览器一样操作（点击 / 滚动 / 输入），不需要图形界面 / X Server / 浏览器桌面。"
resource: "https://github.com/codr1/termium"
tags: [tui, browser, chromium, terminal, headless, ssh]
timestamp: 2026-10-01T11:49:00Z
---

# Termium

## 它是什么

**Termium** 是 [codr1](https://github.com/codr1) 开源的**终端内 Chromium 浏览器**——把真 Chromium 装进终端 TUI，让用户在**纯文本终端**里打开真实网页并像浏览器一样操作。

定位：**不需要图形界面**、不需要 X Server / Wayland、不需要装桌面浏览器，直接在 SSH / 服务器 / 容器里就能「打开」网页（点击、滚动、表单填写）。

## 为什么用它 / 适合什么场景

- 远程服务器 / NAS / 容器里只有终端，但仍需要交互式访问网页（例如查看管理面板）。
- 临时调试：不希望给环境装 X Server + 桌面 + 浏览器。
- 在 TUI 工作流里偶尔需要人肉点击网页，而不想跳出终端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 引擎 | 真 Chromium |
| 形态 | TUI（终端 UI） |
| 操作 | 类似浏览器：点击 / 滚动 / 输入 |
| 运行环境 | 纯终端，无需图形栈 |
| 开源 | 是 |

## 参考链接

- 仓库：<https://github.com/codr1/termium>

## 媒体

- ![](https://pbs.twimg.com/media/HThQg2XbAAA4Viv.png)

## 相关概念

- [Browsh](https://www.brow.sh/) — 同样把现代网页渲染成 TUI 文本的同类思路（外部链接）
- [Lynx](https://lynx.invisible-island.net/) — 纯文本网页浏览的老前辈（外部链接）
