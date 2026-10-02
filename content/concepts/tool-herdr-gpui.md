---
type: "Tool"
title: "Herdr GPUI（penso/herdr-gpui：Herdr daemon 的 macOS 原生 GUI 客户端）"
description: "penso 出品的 Herdr 桌面客户端：Rust + GPUI 写的原生窗口，专门接 Herdr daemon，把 daemon 传来的终端画面连同分屏一起画出来——不另外跑终端模拟器。"
resource: "https://github.com/penso/herdr-gpui"
tags: "[herdr, gpui, rust, terminal, tui, macos, native-client, daemon]"
timestamp: "2026-10-02T15:22:00Z"
---

# Herdr GPUI（penso/herdr-gpui：Herdr daemon 的 macOS 原生 GUI 客户端）

## 它是什么

[Herdr GPUI](https://github.com/penso/herdr-gpui) 是 penso 出品的 **Herdr 桌面 GUI 客户端**：

- Herdr daemon 只管终端与会话，没有图形界面
- Herdr GPUI 用 **Rust + GPUI** 写一个原生窗口，专门接 Herdr daemon
- 把 daemon 传来的**终端画面连同分屏一起画出来**，不另外跑终端模拟器

## 为什么用它 / 适合什么场景

| 场景 | 价值 |
|------|------|
| 在 macOS 上用 Herdr daemon | 不必切到独立终端模拟器看画面 |
| 想要原生体验 | Rust + GPUI，启动快、内存低 |
| 想看分屏 / 多 tab | Herdr daemon 传什么，GUI 就画什么 |
| 远程跑 daemon | 本地只是渲染窗口，daemon 在服务器也 OK |

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生窗口 | Rust + GPUI，非 Electron |
| 接 daemon | 直接连 Herdr daemon（TCP / 本地 socket） |
| 渲染分屏 | daemon 多 tab 也能画 |
| 不带终端模拟器 | 仅渲染 daemon 推来的帧，零重复实现 |

## 与同类工具的对比

| 维度 | Herdr GPUI | 普通终端模拟器（iTerm 等） |
|------|-----------|---------------------------|
| 终端模拟 | 不模拟，只渲染 daemon 画面 | 完整 PTY 模拟 |
| 适用 | 配合 Herdr daemon 使用 | 通用 |
| 启动速度 | 快（无 PTY 启动开销） | 取决于 shell |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2106041515835306220>
- 项目链接：<https://github.com/penso/herdr-gpui>

## 相关概念

- [Herdr Browser](./tool-herdr-browser.md) — Herdr 生态里把 Chromium 嵌进 TUI 的工具，与本 GUI 客户端互补
- [Herdr File Annotator](./tool-herdr-file-annotator.md) — Herdr 生态的文件标注工具
- [GPUI 组件](./tool-gpui-component.md) — 用的 UI 框架
