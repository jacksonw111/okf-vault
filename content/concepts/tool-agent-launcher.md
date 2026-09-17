---
type: "Tool"
title: "Agent Launcher（多 Agent CLI 桌面工作台）"
description: "agent-launch 组织开源的 Electron + TypeScript 桌面工作台，统一管理 6 款 Agent CLI：Claude Code / Codex CLI / OpenCode / Pi / Gemini CLI / Hermes Agent。"
resource: "https://github.com/agent-launch/agent-launcher"
tags: "[electron, typescript, agent-cli, claude-code, codex-cli, opencode, pi, gemini-cli, hermes, desktop-workbench]"
timestamp: "2026-09-17T00:31:00Z"
---

# Agent Launcher（多 Agent CLI 桌面工作台）

## 它是什么

[agent-launch/agent-launcher](https://github.com/agent-launch/agent-launcher) 是 **agent-launch** 组织开源的本地桌面工作台，基于 **Electron + TypeScript**。它把已装好的编程 Agent CLI **统一装进一个桌面应用里**——配账号、切模型、开会话，不必再为每个 Agent 单独开一个终端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一处管理 6 款 CLI | Claude Code / Codex CLI / OpenCode / Pi / Gemini CLI / Hermes Agent |
| 链接而非重装 | 只链接系统里现有的 CLI，不重新安装 |
| 首启向导 | 环境检测 + 一键补装缺失 CLI + 账号 / API Profile 配置 |
| 多账号切换 | 各 CLI 的多账号配置在同一界面集中管理 |
| 模型切换 | 同一应用内对不同 CLI 的可用模型做切换 |

## 适合什么场景

- 同时使用 2 款以上 Agent CLI（Claude Code + Codex / Pi + Gemini 等）需要统一工作台的 AI 重度用户。
- 想把「每个 Agent 一个终端标签页」收纳成单一桌面应用的开发者。
- 想研究 Electron 应用如何包装多个外部 CLI 子进程的工程实现者。

## 与相关概念的关系

- [Claude Code](./tool-claude-code.md) — Agent Launcher 内置管理的 6 款 CLI 之一。
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 同样在 6 款 CLI 之列。

## 参考

- 项目链接：<https://github.com/agent-launch/agent-launcher>

![preview](https://pbs.twimg.com/media/HSTt9wxaMAA3Ci5.jpg)
