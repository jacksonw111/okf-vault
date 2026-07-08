---
type: "Tool"
title: "Picot（Pi 编码 agent 的本地桌面 GUI）"
description: "Picot 是 Pi 编码 agent 的本地桌面 GUI，基于 Tauri 框架开发，作为 deflating/tau 的维护分支。它内置 Pi 运行环境，支持多项目多窗口并行、多会话管理、实时流式聊天，并提供包管理器 UI、费用仪表盘、LAN/移动端访问（QR 码）、语音输入、6 套主题等功能，完全本地运行，无需云端账户。"
resource: "https://github.com/shixin-guo/picot"
tags: "[pi, agent, desktop, tauri, gui, local-first, multi-session]"
timestamp: "2026-07-08T03:15:00Z"
---

# Picot

## 它是什么

[Picot](https://github.com/shixin-guo/picot) 是 **Pi 编码 agent 的本地桌面 GUI**——基于 Tauri 框架，是 [deflating/tau](https://github.com/deflating/tau) 的维护分支。

把 Pi 这个「终端里跑」的命令行 agent 装进一个**真正的桌面窗口**，体验更接近 IDE，同时保留「完全本地运行」的本色。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内置 Pi 运行环境 | 装好 Picot 直接就能跑 Pi，无需单独配置 |
| 多项目多窗口并行 | 同时开多个项目，每个独立窗口 |
| 多会话管理 | 一个项目可开多个 Pi 会话 |
| 实时流式聊天 | LLM 输出实时流式渲染 |
| 包管理器 UI | 装 / 升级 / 切换 Pi 插件的图形界面 |
| 费用仪表盘 | 显示 token 用量与花费 |
| LAN / 移动端访问 | 通过 QR 码扫码在手机 / 平板上继续聊 |
| 语音输入 | 直接语音转 prompt |
| 6 套主题 | 暗色 / 亮色 / 多套配色 |
| 完全本地 | 无云端账户、无网络依赖 |

## 媒体

![Picot 桌面预览](https://pbs.twimg.com/media/HMlyeTEaQAAtN3B.jpg)

## 参考链接

- [项目仓库](https://github.com/shixin-guo/picot)

## 相关概念

- [pi-desktop](./tool-pi-desktop.md) — 同为 Pi 的桌面外壳；pi-desktop 偏原生 PTY 终端，Picot 偏 Tauri 完整桌面 GUI
- [Hermes Desktop](./tool-hermes-desktop.md) — 同为 agent 的桌面外壳