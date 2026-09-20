---
type: "Note"
title: "Agentic Engineering Handbook（系统化 Agent 工程学习路线图）"
description: "keyuchen21/agentic-engineering-handbook：把散落在 OpenAI 博客、Anthropic 工程文、SDK 文档、cookbook、论文里的 179 个精选资源，整成一份从「手写 Agent Loop」到「生产落地/eval/安全」的结构化学习路径，分 Phase 0–6 共 7 个阶段。"
resource: "https://github.com/keyuchen21/agentic-engineering-handbook"
tags: "[agent, learning-path, roadmap, ai-engineering, agentic-engineering, harness]"
timestamp: "2026-09-20T18:00:00Z"
---

# Agentic Engineering Handbook

## 它是什么

[keyuchen21/agentic-engineering-handbook](https://github.com/keyuchen21/agentic-engineering-handbook) 是一份**系统化的 Agent 工程学习路线图手册**——把散落在 OpenAI 博客、Anthropic 工程文、SDK 文档、cookbook、论文里的 **179 个精选资源**，整理成**从「手写 Agent Loop」到「生产落地 / eval / 安全」**的结构化学习路径。

## 7 个阶段学习路径

| 阶段 | 内容 |
|------|------|
| **Phase 0** | 从零手写 Agent Loop（基于 shareAI-lab/mini-claude-code，给了 v0–v4 可跑 Python 代码：bash agent → 模型当 agent → 结构化规划 → 子代理 → skills） |
| **Phase 1** | Agent 基础（该不该建 agent 的 4 问检查表、Building Effective Agents 等） |
| **Phase 2** | MCP & 工具生态 |
| **Phase 3** | Context / Memory / Skills（含 Agent Skills 规范、上下文工程） |
| **Phase 4** | Harness & 长程 Agent（mini coding harness 练习） |
| **Phase 5** | Coding / Workspace Agents（Codex / Claude Code 风格工作流） |
| **Phase 6** | Evals / Safety / Production（smoke / macro eval 套件练习） |

## 为什么用它 / 适合什么场景

- 想学 Agent 工程但**资源太散**——OpenAI / Anthropic / 论文 / cookbook 各说各话，没有一条清晰的爬坡路径。
- 想从**手写 Agent Loop** 起步，逐步走到**生产级 / 安全 / 可评估**的工程化。
- 已经在做 Agent 产品，想**补齐自己知识图谱**——按 Phase 0→6 自检。

## 关键能力

| 能力 | 说明 |
|------|------|
| 资源精选 | 179 个，覆盖官方文档 / 工程文 / cookbook / 论文 |
| 阶段化 | Phase 0–6 共 7 阶段，难度递进 |
| 可跑代码 | Phase 0 提供 v0–v4 Python 可跑示例 |
| 覆盖面 | 从基础概念到 MCP / Memory / Harness / Eval / Safety 全覆盖 |
| 开源 | GitHub 仓库，持续更新 |

## 项目链接

- 仓库：<https://github.com/keyuchen21/agentic-engineering-handbook>

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — Handbook 把「Harness 工程」单列为 Phase 4
- [MCP（Model Context Protocol）](./term-mcp.md) — Phase 2 专章
- [Agent Skills（代理技能包）](./term-agent-skills.md) — Phase 3 专章
- [Context Engineering（上下文工程）](./term-context-engineering.md) — Phase 3 专章
- [Building cloud agent infrastructure（CREAO）](./note-cloud-agent-infrastructure.md) — Handbook 中生产落地阶段的关键参考资料之一
