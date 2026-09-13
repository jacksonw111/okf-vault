---
type: "Tool"
title: "Farcaster（多 coding agent 统一桌面工作区）"
description: "把 Codex、Pi、Claude Code 等多个 coding agent 接入同一个原生桌面工作区，用一套键盘操作和内嵌 Neovim 统一调度。"
resource: "https://github.com/behzade/farcaster"
tags: "[agent, ide, coding-agent, neovim, desktop, multi-agent]"
timestamp: "2026-09-13T12:46:00Z"
---

# Farcaster（多 coding agent 统一桌面工作区）

## 它是什么

[behzade/farcaster](https://github.com/behzade/farcaster) 是一个**原生桌面端多 coding agent 协同工作区**：把 Codex、Pi、Claude Code 等多个 coding agent 接入同一个应用，统一键盘操作，并把 Neovim 内嵌为编辑器面板。

## 为什么用它 / 适合什么场景

- 同时维护多个 coding agent 项目，想用一个 IDE 切换。
- 希望把不同 agent 的能力**横向对比**（同一段代码不同 agent 的输出）。
- 不愿意为每个 agent 单独切窗口 / 终端。
- 想把 Neovim 当统一编辑面，但又想用 AI agent 的自动补全 / 重构能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 agent 接入 | Codex / Pi / Claude Code 等统一入口 |
| 统一键位 | 一套键盘操作覆盖所有 agent 上下文 |
| 内嵌 Neovim | 不用切换编辑器 |
| 原生桌面 | 不走网页，走系统级窗口 / 快捷键 |

## 媒体

- ![](https://pbs.twimg.com/media/HR_JHpCboAA6EnI.jpg)

## 项目链接

- 仓库：<https://github.com/behzade/farcaster>

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，是 Farcaster 主要接入对象之一
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 同为 Farcaster 接入对象