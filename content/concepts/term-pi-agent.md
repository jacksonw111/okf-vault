---
type: "Term"
title: "Pi Agent"
description: "由 Mario Zechner 出品的本地 AI 编码 Agent——Rust 写的小型 daemon，用最小依赖提供「终端 + Agent + 可挂工具」的轻量可嵌入形态；强调可被宿主应用（CLI / GUI / 桌面 / iOS）调用，而非只做一个独立 App。"
resource: "https://github.com/badlogic/pi-mono"
tags: "[pi-agent, ai-coding-agent, agent, rust, local]"
timestamp: "2026-10-06T22:51:00Z"
---

# Pi Agent

## 定义

**Pi Agent** 是 Mario Zechner (`badlogic`) 出品的**本地优先** AI 编码 Agent，原生以 Rust 写成，仓库 [`badlogic/pi-mono`](https://github.com/badlogic/pi-mono) 公开。Pi 的核心定位是「**可被宿主应用调用的 Agent 引擎**」——终端版 / GUI 版 / 桌面 widget / iOS 客户端都只是宿主，Pi 本身是一个工具可挂、记忆可持久、协议可替换的运行时。

## 要点

- **核心仓库**：`https://github.com/badlogic/pi-mono`
- **形态**：Rust 写的本地 daemon + 多宿主（CLI / GUI / 桌面 / iOS）
- **特性**：可挂工具、可热插拔模型、可持久化（[`tool-pi-durable-cloudflare`](tool-pi-durable-cloudflare.md) / `tool-pi-pocket` 等衍生项目都基于 Pi 的可持久化运行时）
- **典型宿主**：Pi 终端版 / Pi-TUI / Pi iOS / Pi Pocket

## 相关概念

- [AI Coding Agent](./term-ai-coding-agent.md) — Pi Agent 是其中代表
- [Claude Code](./term-claude-code.md) — 同类但商业闭源
- [Codex](./term-codex.md) — 同类
- [Computer Use（计算机使用）](./term-computer-use.md) — Pi Agent 也能驱动 Computer Use（如 `tool-lcu`）
