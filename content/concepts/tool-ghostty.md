---
type: "Tool"
title: "Ghostty"
description: "Mitchell Hashimoto（HashiCorp 联合创始人）主导的高性能终端模拟器：原生 UI + GPU 加速渲染，跨 macOS / Linux，开源免费。"
resource: "https://ghostty.org/"
tags: [terminal, native-ui, gpu-acceleration, open-source, cross-platform]
timestamp: "2026-08-08T20:00:00Z"
---

# Ghostty

## 它是什么

Ghostty 是由 HashiCorp 联合创始人 Mitchell Hashimoto 主导开发的高性能终端模拟器。它坚持「原生 UI + GPU 加速」的路线：在 macOS 用 AppKit + Metal，在 Linux 用 GTK4 + OpenGL，把渲染开销压到 GPU 上，目标是「既快又像系统原生终端」。

## 为什么用它 / 适合什么场景

- 想要一款「能装进生产环境」的开源免费终端。
- 在 macOS / Linux 上跑 AI 编码 agent / TUI 工具，希望渲染流畅。
- 想用 `.config/ghostty/config` 这类纯文本配置集中管理设置。
- 偏好原生体验，不想用 Electron 这类 web 技术栈的终端。

## 关键能力

| 能力 | 说明 |
|------|------|
| GPU 加速渲染 | 走 Metal / OpenGL 把文本 / 图形交给 GPU |
| 原生 UI | 各平台走对应原生框架，不依赖 web |
| 跨平台 | macOS / Linux 都支持 |
| 纯文本配置 | `~/.config/ghostty/config` 集中管理 |
| Shell 集成 | 自动检测 Shell 提示符、跳转点击等 |
| 主题生态 | 兼容主流 Terminal 主题格式 |

## 相关概念

- [Ghostty Studio](./tool-ghostty-studio.md) — macOS 上的 Ghostty 可视化配置工具
- [Lex Ghostty Shaders](./tool-lex-ghostty-shaders.md) — Ghostty 着色器 / 视觉效果配置资源
- [Vesta](./tool-vesta-terminal.md) — 同样基于 GhosttyKit Metal 渲染的 macOS 原生终端