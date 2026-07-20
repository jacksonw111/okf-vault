---
type: "Tool"
title: "Codex CLI（OpenAI）"
description: "OpenAI 官方开源的终端 AI 编码 agent，与 Claude Code 同类的命令行编码助手；可在本地跑 OpenAI 模型或在 ChatGPT 账号体系下用云端版本。"
resource: "https://github.com/openai/codex"
tags: "[codex, openai, coding-agent, cli, terminal]"
timestamp: "2026-07-20T20:18:00Z"
---

# Codex CLI（OpenAI）

## 它是什么

[Codex CLI](https://github.com/openai/codex) 是 **OpenAI 官方**开源的终端 AI 编码 agent，与 [Claude Code](./tool-claude-code.md) 同类——在命令行里跑编码任务、读改文件、执行命令、上传上下文给云端模型。Codex 还有桌面端（Codex Desktop / ChatGPT 桌面端内嵌）和 Cloud 版本（ChatGPT 账号体系下的浏览器版本），三者共享同一套底层逻辑。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端编码 agent | CLI 形态跑在本机仓库目录下，读改代码 + 跑命令 |
| 多模型支持 | OpenAI 自家 `gpt-5` 系列模型，亦可经 Compatible API 走其它上游 |
| 三种形态 | CLI / 桌面端 / Cloud，覆盖终端 / GUI / Web 三个入口 |
| 安全沙箱 | 默认 sandbox 执行 shell 命令，避免越权 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — Anthropic 终端 AI 编码 agent，与 Codex CLI 同类
- [Codex-X](./tool-codex-x.md) — 基于 Tauri 2 的 Codex 桌面端一站式管理器
- [Codex Control Plane MCP](./tool-codex-control-plane-mcp.md) — 给 Codex Desktop 加持久化任务队列的 MCP
- [Grok Build](./tool-grok-build.md) — xAI 同类工具（Rust，三种运行形态）

## 参考链接

- 项目链接: <https://github.com/openai/codex>
