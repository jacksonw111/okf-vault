---
type: "Tool"
title: "Repo→Agent（把任意 GitHub 仓库生成为专属 AI Agent）"
description: "通过浏览器或命令行，把任意 GitHub 仓库打包成一个完整的 npm 包：专属 npx CLI + MCP Server + 项目记忆 + 权限策略 + Ed25519 签名认证，兼容 Claude Code / Codex / pi / Hermes 等 8 个 Agent 平台，预置 19 个垂直场景模板。"
resource: "https://github.com/qingq77/repo-agent"
tags: "[agent, mcp, npm, scaffold, ed25519]"
timestamp: "2026-06-21T00:00:00Z"
---

# Repo→Agent（把任意 GitHub 仓库生成为专属 AI Agent）

## 它是什么

Agent 生成框架：把「一个 GitHub 仓库 → 一个独立的 AI Agent」做成模板化的 npm 包生成器。生成的产物不仅是个 CLI，而是 **完整的 Agent 基础设施**：

- **专属 npx 命令**：每个 Agent 都有自己独立的入口。
- **MCP Server**：让其它 Agent 也能调用它。
- **项目记忆**：Agent 自带可持久化的项目上下文。
- **权限策略**：明确 Agent 能 / 不能做什么。
- **Ed25519 签名认证**：保证产物的可信来源。

## 兼容性

支持 8 个 Agent 平台：Claude Code、Codex、pi、Hermes 等。

预置 **19 种垂直场景模板**（开发、研究、交易、法律……），开箱即用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 入口 | 浏览器 UI 或命令行 |
| 产物 | 完整 npm 包（含 CLI / MCP / 记忆 / 权限 / 签名） |
| 平台兼容 | Claude Code / Codex / pi / Hermes 等 8 个 |
| 场景模板 | 19 个垂直领域（开发 / 研究 / 交易 / 法律……） |
| 安全 | Ed25519 签名认证每个 Agent 产物 |

## 媒体

![Repo Agent 截图](https://pbs.twimg.com/media/HLD7RTgaMAA_9vY.jpg)

## 相关概念

- [MCP（Model Context Protocol）](term-agent-skills.md) — 这是该工具的核心协议支撑
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — 同为 filesystem-convention Agent 框架
- [Agent Skills（代理技能包）](term-agent-skills.md) — 「Agent 即包」的生态化产物