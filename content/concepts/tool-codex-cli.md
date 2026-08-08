---
type: "Tool"
title: "Codex CLI"
description: "OpenAI 推出的终端原生 AI 编码 Agent：自然语言驱动代码读写、命令执行、PR 提交，与 Claude Code / Gemini CLI 对位。"
resource: "https://github.com/openai/codex"
tags: [coding-agent, cli, openai, terminal, agent]
timestamp: "2026-08-08T20:00:00Z"
---

# Codex CLI

## 它是什么

Codex CLI 是 OpenAI 推出的终端原生 AI 编码 Agent，直接对位 Anthropic 的 Claude Code。它在终端里接受自然语言指令，执行代码读写、命令运行、PR 提交等动作，并把工具调用结果回显给用户。

## 为什么用它 / 适合什么场景

- 习惯在终端里干活，希望 AI 编码 agent 无缝接入。
- 已有 OpenAI API key，想直接用官方工具。
- 想跟 Claude Code 做对比评测。
- 需要在 CI / 远程服务器上跑编码 agent。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自然语言驱动 | 直接用自然语言提需求 |
| 终端原生 | 与 shell / git / 包管理器无缝结合 |
| 文件读写 | 自动读写项目内文件 |
| 命令执行 | 可跑 shell 命令并解析输出 |
| PR 工作流 | 自动创建分支 / 提交 / 推送 |
| 多模型 | 支持 GPT 系列不同模型 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 Agent 的标杆
- [oh-my-cli](./tool-oh-my-cli.md) — 用 Node.js 写的小型编码 Agent 替代品
- [Agent Skills](./term-agent-skills.md) — 给 Agent 加装能力的标准形式