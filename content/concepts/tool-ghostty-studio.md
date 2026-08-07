---
type: "Tool"
title: "Ghostty Studio"
description: "macOS 上的 Ghostty 终端可视化配置工具：基于 Tauri + TypeScript，自动定位配置文件（候选多于一个时询问），按本机安装的 Ghostty 版本读取设置目录，支持搜索和编辑设置，视觉类改动带上下文预览。"
resource: "https://github.com/SteinsHead/ghostty-studio"
tags: [ghostty, macos, tauri, terminal-config, gui]
timestamp: "2026-08-07T02:03:00Z"
---

# Ghostty Studio

## 它是什么

Ghostty Studio 是 macOS 上 Ghostty 终端的可视化配置工具，基于 Tauri + TypeScript 构建，目前处于早期预览阶段。它把原本散落在文本配置文件里的 Ghostty 设置搬到图形界面里，并提供搜索、编辑与视觉变更的上下文预览。

## 为什么用它 / 适合什么场景

- 在 macOS 上想用 GUI 而不是手工编辑 `~/.config/ghostty/config`。
- 多版本 Ghostty 共存，需要按本机安装版本加载对应的设置目录。
- 不确定设置项的名字或取值范围，希望边看文档边点选。
- 想在改动配色 / 字体 / 背景等视觉相关项前先看效果。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动定位配置文件 | 扫描常见配置位置，候选多于一个时弹询问，让用户挑一份 |
| 版本感知 | 读取本机安装的 Ghostty 版本，按版本对应加载设置目录 |
| 设置搜索 | 提供全文搜索，快速跳到目标设置项 |
| 可视化编辑 | 表单 / 单选 / 颜色拾取等控件代替手写文本 |
| 视觉项上下文预览 | 配色、字体、背景类改动提供即时预览窗口 |
| 原生 macOS 体验 | Tauri 打包，应用体积小、启动快、跟系统观感一致 |

## 相关概念

- [Ghostty](./tool-ghostty.md) — 由 Mitchell Hashimoto 等人主导的高性能终端模拟器（本工具的配置对象）
- [Lex Ghostty Shaders](./tool-lex-ghostty-shaders.md) — Ghostty 的着色器 / 视觉效果配置资源（可与本工具配合）