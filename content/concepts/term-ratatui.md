---
type: "Term"
title: "ratatui（Rust 终端 UI / TUI 库）"
description: "Rust 生态主流的终端 UI（TUI）框架：基于 crossterm / termion，提供 widget / layout / 事件循环，让开发者用纯 Rust 在终端里搭出类 GUI 的交互界面；tincan-cli、btop、gitui 等都用它。"
resource: "https://github.com/ratatui/ratatui"
tags: "[ratatui, tui, rust, terminal-ui, crossterm, open-source]"
timestamp: "2026-09-26T21:50:00Z"
---

# ratatui（Rust 终端 UI / TUI 库）

## 定义

[ratatui](https://github.com/ratatui/ratatui)（原 tui-rs）是 **Rust 生态主流的终端 UI 框架**——底层走 [crossterm](https://github.com/crossterm-rs/crossterm) 或 termion 抽象终端能力，上层提供 widget / layout / 事件循环 API，让开发者**用纯 Rust 在终端里搭出类 GUI 的交互界面**。

## 要点

- **跨平台终端抽象**：通过 crossterm / termion 后端支持 Windows / macOS / Linux。
- **组件化 widget**：Block / List / Table / Chart / Gauge 等开箱即用。
- **立即模式 / 重绘循环**：每帧重新绘制整个界面，无 DOM 概念。
- **键盘 / 鼠标事件**：统一事件接口。
- **Rust 原生**：性能好、单二进制发布、无 GC。

## 典型项目

- [tincan-cli](./tool-tincan-cli.md) — 终端 P2P 语音 + 文字聊天室的 TUI
- [btop](https://github.com/aristocratos/btop) — 系统资源监控 TUI
- [gitui](https://github.com/extrawurst/gitui) — Git 终端客户端

## 相关概念

- [iroh](./term-iroh.md) — Rust P2P 网络栈，tincan-cli 用 iroh 做网络 + ratatui 做 UI
- [tincan-cli](./tool-tincan-cli.md) — ratatui + iroh 的典型应用