---
type: Tool
title: "ZSUI（Rust 轻量原生 UI 框架）"
description: "Rust 写的轻量原生 UI 框架：用组合 + trait 搭界面、用强类型消息管状态，同一份代码能在 Win32、AppKit（macOS）和 Linux 上编译出真正的原生窗口。"
resource: "https://github.com/qiu7824/zsui"
tags: [rust, ui, cross-platform, native, win32, appkit]
timestamp: "2026-07-21T04:39:00Z"
---

# ZSUI（Rust 轻量原生 UI 框架）

## 它是什么
[ZSUI](https://github.com/qiu7824/zsui) 是一款 Rust 写的 **轻量原生 UI 框架**：通过 **组合 + trait** 搭建界面，**用强类型消息**管理状态，让同一份代码能在 Win32（Windows）、AppKit（macOS）和 Linux 上编译出真正的原生窗口——不是 Electron 套壳，也不是自绘 UI。

## 为什么用它 / 适合什么场景
- 想要 **Rust 写原生桌面**，又不想被 Tauri 2 / Electron 的 Web 栈绑住。
- 偏好「强类型消息驱动 UI」（类 Elm / iced）的状态管理模式。
- 写小工具 / 内部工具，目标是「真原生 + 真跨平台 + 真轻量」。

## 关键能力
| 能力 | 说明 |
|------|------|
| Rust 原生 | 性能 / 类型安全 / 内存模型直接套用 |
| 组合 + trait 搭界面 | 不依赖 XML / JSON / DSL，纯代码组合 |
| 强类型消息 | UI 状态通过消息流更新，编译期可校验 |
| 三平台原生 | Win32 / AppKit / Linux 后端各出一份原生窗口 |
| 轻量 | 不依赖浏览器 / WebView |

## 相关概念
- [Claude Code](tool-claude-code.md) — 终端原生 AI 编码 agent（同为原生路线参考）

## 参考链接
- 项目链接: <https://github.com/qiu7824/zsui>
- 预览截图: ![ZSUI 截图](https://pbs.twimg.com/media/HNlMTfObkAA7mCM.jpg)
