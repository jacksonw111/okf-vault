---
type: "Tool"
title: "portlist（AI 工具感知的端口管理 CLI）"
description: "Mr-hunt-007 开源：纯 Python 终端端口管理工具，一次扫描把**监听端口、进程、项目、容器、来源关系**整理成统一视图——还能识别端口是 Claude Code / Codex / Cursor / 终端 / 系统服务起的，并判断服务是否真能从本机之外访问。"
resource: "https://github.com/Mr-hunt-007/portlist"
tags: "[portlist, port-management, cli, python, dev-tools, ai-tool, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# portlist（AI 工具感知的端口管理 CLI）

## 它是什么

[portlist](https://github.com/Mr-hunt-007/portlist) 是 Mr-hunt-007 开源的**纯 Python 终端端口管理工具**——**一次扫描**把以下信息整理成统一视图：

| 信息 | 说明 |
|------|------|
| 监听端口 | 当前所有 LISTEN 状态的端口 |
| 进程 | 每个端口被哪个 PID 占用 |
| 项目 | 进程来自哪个项目目录 |
| 容器 | 是否跑在容器内 |
| **来源** | **服务是 Claude Code / Codex / Cursor / 终端 / 系统服务 哪个起的** |
| **可达性** | 服务是否真能从本机之外访问 |

## 为什么用它 / 适合什么场景

- 跑一堆 **dev server + AI agent** 时，端口经常冲突 / 找不到谁占着。
- 想知道「**这个 3000 端口到底是 Next.js 起的，还是 Codex 自动开的**」。
- 调试 **AI Agent 启动的服务** 是不是真能从同事机器访问（VSCode 端口转发、AI Agent 隧道等坑）。
- 想要**比 `lsof` / `netstat` 更聪明**的端口管理——带上来源识别与可达性判断。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Python CLI |
| 扫描内容 | 端口 / PID / 项目 / 容器 / 来源 / 可达性 |
| AI 工具感知 | 识别 Claude Code / Codex / Cursor / 终端 / 系统 |
| 可达性 | 实际连接测试，不只看 LISTEN 状态 |

## 媒体

- ![](https://pbs.twimg.com/media/HTGXX7ZbkAA3mWE.jpg)

## 相关概念

- [wlctl](./tool-wlctl.md) — Rust 终端网络 TUI（网络层），portlist 在端口层
- [pi-session-hub](./tool-pi-session-hub.md) — 同为「**AI 工具感知的本机效率工具**」的同代产物