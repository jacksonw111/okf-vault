---
type: Tool
title: "LilBot Agent（Python 本地编码 Agent 框架）"
description: "基于 Python 的本地编码代理框架，采用 prompt_toolkit 全屏 TUI 界面，优先支持 Windows 终端和 DeepSeek 等 OpenAI 兼容提供商。"
resource: "https://github.com/terrense/LilBot-agent"
tags: [python, agent, coding-agent, tui, prompt-toolkit, windows, deepseek]
timestamp: 2026-06-26T16:50:00Z
---

# LilBot Agent

## 它是什么

LilBot Agent 是一个**用 Python 写的本地编码 Agent 框架**，定位是"在终端里直接用的轻量编码搭档"。

形态特征：

- **全屏 TUI**：基于 [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) 的全屏交互界面
- **平台偏好**：Windows 终端优先适配
- **模型偏好**：DeepSeek 等 **OpenAI 兼容 API** 提供商（不绑定 OpenAI 官方）
- **本地**：跑在用户自己机器上，不走云

## 它与现有方案的差异

| 维度 | Claude Code | LilBot |
|------|-------------|--------|
| 实现语言 | TypeScript | Python |
| 终端 | TUI 命令 | prompt_toolkit 全屏 |
| 模型绑定 | Anthropic | OpenAI 兼容 API（DeepSeek 等）|
| 平台 | 跨平台 | Windows 优先 |

## 关键能力

| 能力 | 说明 |
|------|------|
| prompt_toolkit TUI | 全屏交互，类 vim 操作 |
| Windows 适配 | 优先保证 Windows 终端体验 |
| OpenAI 兼容 | 支持 DeepSeek / 任何兼容端点 |
| Python 实现 | 适合 Python 生态用户二开 |
| 本地优先 | 跑在用户机器，代码不上云 |

## 原始链接

- [项目仓库](https://github.com/terrense/LilBot-agent)
- [原始推文剪藏](https://x.com/QingQ77/status/2070451755213603279)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 同为"终端 AI 编码 Agent"，但实现和生态都不同
- [Lumina（端侧 AI Agent 运行时）](./tool-lumina-agent-runtime.md) — 同样强调"端侧 / 本地"，但 Lumina 是"运行时"而非"完整 Agent"
- [DeepSeek MCP WebSearch](./tool-deepseek-mcp-websearch.md) — DeepSeek 在 MCP 搜索场景的封装
