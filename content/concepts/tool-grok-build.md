---
type: Tool
title: "Grok Build（xAI）"
description: "xAI 官方开源的 Rust 编写的 AI 编码 agent 运行环境，支持全屏 TUI 交互、headless 模式跑 CI / 脚本，以及通过 Agent Client Protocol（ACP）嵌入编辑器。"
resource: "https://github.com/xai-org/grok-build"
tags: "[xai, rust, coding-agent, acp, tui, headless]"
timestamp: "2026-07-19T05:07:00Z"
---

# Grok Build（xAI）

## 它是什么

xai-org/grok-build 是 **xAI 官方**开源的 AI 编码 agent 运行环境，用 Rust 编写。与 Claude Code、Codex CLI 等同类工具相比，它同时支持**三种运行形态**——全屏 TUI 交互、headless 模式嵌入 CI / 脚本，以及通过 **Agent Client Protocol（ACP）** 嵌入编辑器。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全屏 TUI | 类 Codex CLI / Claude Code 的终端交互体验 |
| Headless 模式 | 跑在 CI / 脚本里，非交互完成编码任务 |
| ACP 服务端 | 通过 Agent Client Protocol 协议对接支持 ACP 的编辑器（Zed 等） |
| Rust 实现 | 单二进制、低资源占用、易分发 |

## 三种运行形态

| 形态 | 用途 |
|------|------|
| TUI 交互 | 开发者日常终端编码会话 |
| Headless / CI | 自动化 PR review / 自动修复流水线 |
| ACP 嵌入式 | 在 Zed 等 ACP-native 编辑器里作为编码 agent |

## 与已有 AI 编码 agent 的差别

- [Claude Code](./tool-claude-code.md) — Anthropic 终端 AI 编码 agent
- [Codex CLI](./tool-codex.md) — OpenAI 终端编码 agent
- [Pi](./tool-pi-env.md) — 沙箱化 Pi 编码 agent
- Grok Build 的差异点：**xAI 官方 + Rust 实现 + 协议中立**——同时支持自家 Grok 模型与任意 ACP 客户端

## 媒体预览

![](https://pbs.twimg.com/media/HNaWWEBbYAAtNJp.jpg)

## 相关概念

- [Claude Code](./tool-claude-code.md) — Anthropic 终端 AI 编码 agent
- [Pool](./tool-pool-poolside.md) — Poolside 编码智能体（4 种运行方式）

## 参考链接

- 项目链接: <https://github.com/xai-org/grok-build>