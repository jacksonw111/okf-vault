---
type: "Tool"
title: "Tabminal（leask/tabminal）"
description: "把终端 + 文件编辑 + AI 智能体收进同一网页界面，会话存服务端，手机/平板/电脑换设备无缝接续。"
resource: "https://github.com/leask/tabminal"
tags: [terminal, web-ide, file-editor, ai-agent, koa, node-pty, xterm, monaco, remote]
timestamp: "2026-08-05T06:40:00Z"
---

# Tabminal（leask/tabminal）

## 它是什么

**Tabminal** 是给「同时要用**终端、文件编辑、AI 智能体**」的人准备的网页工作台——把三样收进**同一个网页界面**，终端会话挂在**服务端**，刷新页面、断网重连、换设备都不会丢。

技术栈：

- 后端：**Node.js + Koa + node-pty + WebSocket**
- 前端：**原生 JS + xterm.js + Monaco 编辑器**

## 为什么用它 / 适合什么场景

- **多设备切换**：iPad / 手机 / Mac / Windows 都能开同一会话接着用。
- **不想装桌面客户端**：浏览器就是客户端。
- **会话需要持久**：刷新 / 断网 / 换设备都不丢。
- **统一工作台**：终端、文件、AI agent 三合一，不切窗口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 服务端终端 | node-pty 跑在服务端，会话持久 |
| 断网重连 | WebSocket 断线后状态保留 |
| 换设备接续 | 手机 / 平板 / 电脑无缝接着用 |
| 文件编辑 | Monaco 编辑器（VS Code 同款内核） |
| AI Agent 入口 | 网页界面集成 ACP 智能体调用 |
| 网页交付 | 浏览器即用，无需桌面客户端 |

## 参考链接

- [GitHub 仓库](https://github.com/leask/tabminal)

## 相关概念

- [Pi-Livecraft](./tool-pi-livecraft.md) — 同属「给终端 AI 套网页界面」思路，对照实现
- [Happier](./tool-happier.md) — 端到端加密跨设备 AI 编码客户端，可与本工具对照「安全 vs 便捷」取舍