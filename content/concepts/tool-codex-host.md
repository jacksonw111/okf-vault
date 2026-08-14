---
type: "Tool"
title: "codex-host"
description: "BytePioneer-AI 开源的 Codex Desktop 多 Agent 宿主：保留 Codex 原生体验，同时通过 CDP / Electron Inspector 注入 Agent 选择与会话面板，把 Pi、Claude Code 等 Agent 接到 Codex 的 app-server 上。"
resource: "https://github.com/BytePioneer-AI/codex-host"
tags: ["codex", "agent", "multi-agent", "electron", "cdp", "harness", "pi", "claude-code"]
timestamp: "2026-08-14T19:50:00Z"
---

# codex-host

## 它是什么
codex-host 把 Codex Desktop 当宿主界面，通过 CDP / Electron Inspector 注入「Agent 选择器 + 会话面板」UI（不修改安装包），再用 CLI Shim 接 Codex 的 app-server 把请求原样转发；具体执行任务的 Agent（Pi 走 RPC、Claude Code 走 Agent SDK / CLI）通过各家原生 Harness 接口接入。用户在 Codex Desktop 内一键切换 Pi / Claude Code 等后端执行任务，界面体验保持 Codex 原生。

## 为什么用它 / 适合什么场景
- 已经习惯 Codex Desktop 体验，想在不变工作流的前提下自由切换「真正执行任务的 Agent」。
- 不想为不同 Agent 装多套 IDE / 终端界面。
- 适合把 Codex 当作统一入口，Pi / Claude Code / Codex 当多种执行后端来调度的场景。

## 关键能力
| 能力 | 说明 |
|------|------|
| UI 集成 | CDP / Electron Inspector 改官方 Codex Desktop，不改安装包 |
| 协议层 | CLI Shim 接 Codex app-server，请求原样转发 |
| Harness | Pi 走 RPC、Claude Code 走 Agent SDK / CLI |
| 设计目标 | 保留 Codex 原生体验，自由切换执行 Agent |

## 媒体

UI 示例：![UI 示例](https://pbs.twimg.com/media/HPkkEqiaAAAHsXC.jpg)

## 相关概念
- [Vigla](./tool-vigla.md) — 跨 Claude Code / Codex CLI / Antigravity 编程 agent 的统一面板，与 codex-host 都属于「多 Agent 统一入口」思路
- [pi-peer](./tool-pi-peer.md) — 同机多 pi 会话互相发现 + 消息互通，codex-host 集成 Pi 时的同伴能力
- [Claude Code](./tool-claude-code.md) — codex-host 支持的执行后端之一
