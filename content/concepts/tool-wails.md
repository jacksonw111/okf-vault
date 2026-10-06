---
type: "Tool"
title: "Wails"
description: "用 Go 写桌面 GUI 的轻量框架——把 Go 后端 + Web 前端（任意前端框架）打包成原生二进制，无需 Electron 的运行时开销，输出包小、启动快；是 Go 桌面方案的代表之一，与 Tauri 对位。"
resource: "https://wails.io"
tags: "[wails, golang, desktop, gui, framework]"
timestamp: "2026-10-06T22:51:00Z"
---

# Wails

## 定义

**Wails** 是一个让开发者用 **Go + Web 前端**写桌面 GUI 的轻量框架——Go 负责业务逻辑与系统调用，前端用任意框架（Vue / React / Svelte / 纯 HTML），通过 WebView2（Windows）/ WebKit（macOS）/ WebKitGTK（Linux）渲染。相较 Electron，**没有 Node 运行时、没有 Chromium 内嵌**，输出包通常 < 10 MB、启动 < 100 ms。

## 要点

- **官网**：[wails.io](https://wails.io)
- **形态**：Go 后端 + Web 前端 → 单一二进制
- **跨平台**：Windows / macOS / Linux 均原生 WebView 支持
- **典型场景**：内部工具 / 系统托盘常驻 / 跨平台桌面小工具 / CLI 的 GUI 包装
- **对位**：与 Tauri（Rust + Web）形成 Go vs Rust 桌面方案选择

## 相关概念

- [MyGo](./tool-mygo.md) — Go Web 组件库 + libghostty 终端插件
- [Tauri](https://tauri.app) — 同思路的 Rust + Web 框架
