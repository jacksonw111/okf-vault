---
type: "Tool"
title: "pi-claude-bridge（Pi 集成 Claude Code 的桥接扩展）"
description: "Pi 编程工具的扩展，通过 Anthropic 官方 Agent SDK 把 Claude Code 接进 Pi：可作为 provider 直接选 Opus / Sonnet / Haiku 模型，也可作为 AskClaude 工具让其他 provider 临时调用 Claude Code。"
tags: "[pi, claude-code, agent, bridge, extension]"
timestamp: "2026-06-27T12:06:00.000Z"
resource: "https://github.com/elidickinson/pi-claude-bridge"
---

# pi-claude-bridge（Pi 集成 Claude Code 的桥接扩展）

## 它是什么

[`pi-claude-bridge`](https://github.com/elidickinson/pi-claude-bridge) 是一个 **Pi 扩展**，通过 Anthropic 官方的 Agent SDK 把 Claude Code 接进 Pi。它有**两种玩法**：

1. **作为 provider**：直接在 Pi 里选 Claude Opus / Sonnet / Haiku 模型，工具调用全部在 Pi 的界面里跑
2. **作为 AskClaude 工具**：用别的 provider 时，可以随时让 Pi 找 Claude Code 帮忙

支持流式输出、MCP 工具、会话恢复、思考链；Pro / Max / Team 订阅都行；默认 200K 上下文，Opus Max 还可开 1M。

![架构示意](https://pbs.twimg.com/media/HLzWdMtaQAASLdi.png) ![配置界面](https://pbs.twimg.com/media/HLzWduAbYAA6uv-.png)

## 关键能力

| 能力 | 说明 |
|------|------|
| 双模式接入 | provider 模式 / AskClaude 工具模式 |
| 多模型选择 | Opus / Sonnet / Haiku 全套可选 |
| 流式输出 | 实时流式显示模型响应 |
| MCP 工具 | 兼容 MCP 协议的工具链 |
| 会话恢复 | 跨会话状态保持 |
| 思考链 | 支持思考过程可视化 |
| 1M 上下文 | Opus Max 可开 1M 上下文窗口 |

## 适用场景

- 主力用 Pi，但某些任务想直接交 Claude Opus 跑
- 用别的 provider，遇到拿不准的子任务想临时让 Claude Code 介入
- 想在 Pi 里统一管理 Claude Code 会话，不用切窗口

## 参考链接

- [项目链接](https://github.com/elidickinson/pi-claude-bridge)

## 相关概念

- [pi-fusion](tool-pi-fusion.md) — Pi 多模型并行扇出 + 汇总扩展
- [pi-web-agent](tool-pi-web-agent.md) — Pi 编码代理的网页工具包
- [Claude Code](tool-claude-code.md) — 被桥接进来的目标 agent