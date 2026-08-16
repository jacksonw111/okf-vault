---
type: Tool
title: "DeepSeek-Harness-Desktop (sleep2agi)"
description: "给 DeepSeek 官方命令行 agent 运行时（dsh）套一个 macOS / Windows 桌面外壳，双击启动内核并在内置受控窗口内使用 Web UI"
resource: "https://github.com/sleep2agi/DeepSeek-Harness-Desktop"
tags: [deepseek, harness, dsh, desktop-shell, cross-platform]
timestamp: 2026-08-16T16:00:00Z
---

# DeepSeek-Harness-Desktop (sleep2agi)

## 它是什么
`sleep2agi/DeepSeek-Harness-Desktop` 是另一个 **DeepSeek Harness (DSH)** 桌面壳项目，给 DeepSeek 官方的命令行 agent 运行时 `dsh` **套一层跨平台桌面外壳**（macOS / Windows），**双击图标** 即可在受控窗口里启动 DSH 内核并打开 Web UI。

## 为什么用它 / 适合什么场景
- 把 DSH 当成「普通应用」分发给非技术用户。
- 桌面图标常驻 + 自动后台拉起内核，体验类似 Electron 应用。
- 想用 DSH 但不想手动起 CLI、记端口号。
- 同一桌面壳可以挂主题（鲸鱼娘 / 暗色 / 自定义品牌）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 双击启动 | 不需要命令行知识，普通用户也能跑 DSH |
| 内核托管 | 桌面壳负责拉起、监控、关闭 DSH 进程 |
| 受控窗口 | Web UI 在桌面壳提供的窗口里渲染，与浏览器隔离 |
| 跨平台 | macOS + Windows 双端一份体验 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvKgOJaMAA8QGl.jpg)

## 相关概念
- [项目链接](https://github.com/sleep2agi/DeepSeek-Harness-Desktop)