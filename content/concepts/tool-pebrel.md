---
type: "Tool"
title: "Pebrel（前身 Nebula：把 AI 编码 CLI 当一等公民的终端）"
description: "Kuddev 开源：前身为 Nebula（2026 年 8 月改名）；基于 Zed 的 GPUI 框架做界面、Alacritty 做终端核心，跨 Win/macOS/Linux。把 AI 编码 CLI 当一等公民——Claude Code / Codex 各自图标与活动状态，通知标出分屏位置，点击跳回，AI 回答可丢进内置阅读器看 Markdown / 公式。"
resource: "https://github.com/Kuddev/pebrel"
tags: "[pebrel, terminal, ai-coding, gpui, zed, alacritty, claude-code, codex, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# Pebrel（前身 Nebula：把 AI 编码 CLI 当一等公民的终端）

## 它是什么

[Pebrel](https://github.com/Kuddev/pebrel) 是 Kuddev 开源的**跨平台终端**——前身为 Nebula（**2026 年 8 月改名**）。技术栈：

- 界面：**Zed 的 GPUI** 框架
- 终端核心：**Alacritty**
- 平台：**Windows 10/11 / macOS 14+ / Linux**

## 核心设计：AI 编码 CLI 当一等公民

- Claude Code / Codex 有**各自图标**与**活动状态**
- 通知**标出是哪个分屏在跑**
- **点一下直接跳回去**
- AI 的回答**能丢进内置阅读器**看 Markdown / 公式

## 为什么用它 / 适合什么场景

- 同时跑**多个 AI 编码 CLI**（Claude Code + Codex + Hermes），需要在多个分屏里切换但又不想丢上下文。
- 喜欢 **GPUI / Alacritty** 的高性能终端体验。
- 想要一个**专门为「**AI 编码时代**」设计**的终端，而不是通用终端加 AI 插件。
- 经常需要在多个 AI 会话之间**快速跳转 + 复核输出**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 跨平台原生终端 |
| 界面框架 | Zed GPUI |
| 终端核心 | Alacritty |
| 平台 | Win10/11 / macOS 14+ / Linux |
| AI CLI 适配 | Claude Code / Codex（各自图标 + 活动状态） |
| 通知 | 标注分屏位置，点击跳转 |
| 阅读器 | 内置 Markdown / 公式阅读 |

## 媒体

- ![](https://pbs.twimg.com/media/HTJZ45-bMAA7K1-.jpg)

## 相关概念

- [pi-session-hub](./tool-pi-session-hub.md) — 把 6 种 AI 编码工具的会话历史汇总的 Pi 扩展
- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — Pebrel 是 Harness 层在终端 UI 上的具体体现