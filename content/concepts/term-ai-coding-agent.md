---
type: "Term"
title: "AI Coding Agent（AI 编码代理）"
description: "由 LLM 驱动、能自主完成真实软件工程任务的 Agent——以 Claude Code / Codex / Pi Agent / Cursor / Devin 等为代表；核心能力是读代码 / 改代码 / 跑命令 / 调工具 / 长跑多步任务 / 与开发者协作完成 PR；与早期「代码补全 Copilot」有质的区别。"
resource: "https://en.wikipedia.org/wiki/Software_agent"
tags: "[ai-coding-agent, agent, llm, claude-code, codex, devin]"
timestamp: "2026-10-06T22:51:00Z"
---

# AI Coding Agent（AI 编码代理）

## 定义

**AI Coding Agent** 是由 LLM 驱动、能在真实软件工程环境中**自主完成多步任务**的智能体——区别于早期 Copilot 式「下一行补全」，它具备读仓库、改文件、跑命令、调用工具、规划任务、长跑数小时、与开发者协作完成 PR 的能力。代表产品：**Claude Code**、**Codex**、**Pi Agent**、**Cursor Agent**、**Devin**、**Windsurf**、**GitHub Copilot Workspace**、**Aider** 等。

## 要点

- **核心能力**：仓库级理解 / 多文件重构 / 命令执行 / 工具调用 / 子 Agent / 长跑任务
- **扩展机制**：
  - **MCP（Model Context Protocol）**：挂外部工具 / 数据源
  - **Agent Skills / Plugins**：注入领域规范与工作流
  - **Sub-Agent**：把任务下放给专用子 Agent
- **任务谱**：bug fix / 重构 / 写测试 / PR Review / 文档 / 长跑迁移 / 端到端功能开发
- **评估基准**：SWE-Bench、HumanEval、RepoBench、LiveCodeBench 等

## 相关概念

- [Claude Code](./term-claude-code.md) — Anthropic 出品
- [Codex](./term-codex.md) — OpenAI 出品
- [Pi Agent](./term-pi-agent.md) — 本地优先轻量代表
- [EmDash](./tool-emdash.md) — AI Coding 后台任务运行器
