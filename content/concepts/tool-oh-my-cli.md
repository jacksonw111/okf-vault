---
type: "Tool"
title: "oh-my-cli"
description: "用 Node.js 22 + TypeScript + ESM 写的小型代码智能体：自托管、任意 OpenAI 兼容端点即可接入，终端内提供 read / write / edit / shell 等工具，工作区外与符号链接逃逸会被拦截。"
resource: "https://github.com/qwen-code-dev-bot/oh-my-cli"
tags: [coding-agent, cli, nodejs, typescript, openai-compatible, self-hosted]
timestamp: "2026-08-07T11:46:00Z"
---

# oh-my-cli

## 它是什么

oh-my-cli 是一款用 Node.js 22 + TypeScript + ESM 编写的小型代码智能体 CLI，可自托管、任意 OpenAI 兼容端点都能接入。它在终端内提供 read / write / edit / shell 等工具，并对工作区外的访问与符号链接逃逸做硬性拦截，避免 Agent 越界改动文件。

## 为什么用它 / 适合什么场景

- 想用 Node.js 生态工具自建一套小型 Coding Agent，不想被 Python 生态绑定。
- 已有 OpenAI 兼容端点（自托管模型 / 第三方代理 / Anthropic 兼容层），希望即插即用。
- 关心 Agent 的工作区隔离，希望对越权访问有明确边界。
- 想用一份极简代码库来理解 Coding Agent 的最小可工作单元。

## 关键能力

| 能力 | 说明 |
|------|------|
| Node.js 22 + TS + ESM | 现代栈，启动快，类型安全 |
| 自托管 | 代码开源，部署到自己的环境 |
| OpenAI 兼容端点 | 任意兼容 OpenAI Chat Completions 的服务都能驱动 |
| 工具集（read / write / edit / shell） | 覆盖读写编辑、命令执行的最小闭环 |
| 工作区隔离 | 工作区外的文件路径被硬性拒绝 |
| 符号链接逃逸拦截 | 防止通过 symlink 跳出工作区 |
| 小型代码库 | 代码体量小，便于审阅、二次开发、改造为内部分支 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 Agent 的标杆，本工具与其设计哲学相近
- [Codex CLI](./tool-codex-cli.md) — 另一款终端 Coding Agent，定位与本工具对位
- [Agent Skills](./term-agent-skills.md) — 给 Agent 加装能力的标准形式，本工具可作为 skill 的执行宿主