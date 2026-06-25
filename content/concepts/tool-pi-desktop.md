---
type: Tool
title: "pi-desktop（Pi Coding Agent 桌面外壳）"
description: "为 Pi Coding Agent 提供的原生桌面外壳，集成真正的 PTY 终端与会话自动化管理。"
resource: "https://github.com/LCorleone/pi-desktop"
tags: [pi, agent, desktop, pty, tauri]
timestamp: "2026-06-25T08:10:00Z"
---

# pi-desktop（Pi Coding Agent 桌面外壳）

## 它是什么

为 Pi Coding Agent（终端里跑的编码 agent）专门做的**原生桌面外壳**。它解决「Pi 本来是 CLI」+「我想要个 GUI」的错位——

- 集成了**真正的 PTY 终端**，不是伪终端模拟（能在 GUI 里跑 TUI 应用、保留 ANSI 颜色）。
- 内置**会话自动化管理**：开 / 停 / 重启 / 调度。

## 为什么用它

- Pi 本身是终端 agent，但要长期挂着跑、跑后台 pipeline、并行多个会话——纯 CLI 不够顺手。
- 原生外壳让 Pi 与 IDE 风格的工作台一样可以「多会话并行」，但底层仍是 PTY，行为不打折。
- 与「Pi 在终端里手敲」相比，**桌面外壳** 提供：会话列表、状态可视化、快捷键启动、跨平台窗口体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生桌面外壳 | 跨平台 GUI（非网页套壳） |
| 真正的 PTY | 不阉割 TUI 行为 |
| 会话管理 | 开 / 停 / 重启 / 调度 |
| 跨平台 | Windows / macOS / Linux |

## 相关概念

- [pi-task](./tool-pi-task-delegation.md) — Pi 的子任务委派扩展；pi-desktop 是「容器」，pi-task 是「容器里的子任务机制」
- [pi-web-agent](./tool-pi-web-agent.md) — Pi 的网页工具包；桌面外壳里同样可以装上
- [pi-fusion](./tool-pi-fusion.md) — Pi 的多模型并行扇出 + 汇总扩展
- [y-times-y / y](./tool-y-times-y.md) — 同为「桌面编码 agent 容器」，但 y 强调自我修改 + 多 agent 并行