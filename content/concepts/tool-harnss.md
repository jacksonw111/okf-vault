---
type: "Tool"
title: "Harnss（跨平台多 Agent 整合桌面）"
description: "danielbodnar/harnss，跨平台桌面软件，把 Claude Code / Codex / ACP 兼容的编程代理整合到同一个窗口里跑。"
resource: "https://github.com/danielbodnar/harnss"
tags: "[coding-agent, desktop, multi-agent, claude-code, codex, acp]"
timestamp: "2026-07-23T01:18:00Z"
---

# Harnss（跨平台多 Agent 整合桌面）

## 它是什么

[`danielbodnar/harnss`](https://github.com/danielbodnar/harnss) 是一个**跨平台桌面应用**，把多个**编程代理**（Claude Code、Codex、ACP 兼容的 Agent）整合进**同一个窗口**——一次启动，多个 Agent 同时在跑。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | 支持主流桌面 OS |
| 多 Agent 整合 | Claude Code / Codex / ACP 兼容 Agent |
| 单窗口 | 一个窗口管理多个 Agent 会话 |
| ACP 兼容 | 适配 Agent Client Protocol 标准的 Agent |

## 为什么用它

- **告别多 Tab 切换**：以前开三个 Terminal / IDE Tab 跑三个 Agent，现在一窗搞定
- **跨 Agent 切换**：按任务切不同 Agent（Claude / Codex），不用重启
- **统一上下文**：所有 Agent 输出在同一窗口对比 / 复用

## 适用场景

- 同时跑多个 AI 编程任务的开发者
- 评测 Claude Code vs Codex 的工程师
- Agent Client Protocol（ACP）兼容 Agent 的统一入口

## 媒体

![](https://pbs.twimg.com/media/HNzOFDlbsAAIdDm.jpg)

## 相关概念

- [FreeBuddy](./tool-freebuddy.md) — 同类「GUI 并行承载多编码 Agent」的工具
- [Codex ThreadBeacon](./tool-codex-threadbeacon.md) — Codex 状态原生小窗伴侣
- [Agents Council](./tool-agents-council.md) — Claude Code / Codex CLI 加「召集议会」Skill
- [CAW](./tool-caw-multi-agent-terminal.md) — 浏览器里同时开多个 AI 编程智能体
- [CCMux](./tool-ccmux.md) — tmux 里跟踪多 Agent 会话

## 原始链接

- [项目仓库](https://github.com/danielbodnar/harnss)