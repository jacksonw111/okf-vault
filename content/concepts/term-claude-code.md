---
type: "Term"
title: "Claude Code"
description: "Anthropic 官方出品的命令行编码 Agent——通过终端直接驱动 Claude 模型完成读代码、改代码、跑命令、写 PR 等工作；原生支持 MCP / Agent Skills / Sub-Agent，是当下编码 Agent 生态的事实参考实现之一。"
resource: "https://docs.claude.com/en/docs/claude-code/overview"
tags: "[claude, claude-code, agent, ai-coding-agent, anthropic]"
timestamp: "2026-10-06T22:51:00Z"
---

# Claude Code

## 定义

**Claude Code** 是 Anthropic 官方出品的**终端原生编码 Agent**：以 CLI 形态发布（`npm i -g @anthropic-ai/claude-code`），把 Claude 模型装进本地终端，赋予它读代码 / 改文件 / 跑命令 / 调 MCP / 加载 Skill / 起 Sub-Agent 的能力，让开发者用自然语言驱动复杂工程任务。

## 要点

- **官网 / 文档**：[docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code/overview)
- **形态**：CLI + 本地 daemon；交互以 REPL / slash 命令 / 计划审批为主
- **扩展机制**：
  - **MCP（Model Context Protocol）**：接入任意外部工具 / 数据源
  - **Agent Skills**：把「领域规范 + 工作流」打成 `SKILL.md` 文件让 Agent 按需加载
  - **Sub-Agent**：把任务下放给专用子 Agent（探索 / 评审 / 改代码）
- **典型用法**：读仓库 + 解释代码、跨文件重构、自动化 PR、单元测试生成、CI 修复、Skill / Plugin 编写

## 相关概念

- [AI Coding Agent](./term-ai-coding-agent.md) — Claude Code 是其中代表
- [MCP（Model Context Protocol）](./term-mcp.md) — Claude Code 原生支持
- [Agent Skills 是什么](./term-agent-skills.md) — 扩展机制
- [Codex](./term-codex.md) — 同为 AI 编码 Agent
- [Pi Agent](./term-pi-agent.md) — 同为 AI 编码 Agent
