---
type: "Tool"
title: "AgentCrew（多智能体协作聊天应用）"
description: "支持多 AI 模型 + MCP 协议的多智能体聊天应用，可给每个 agent 分配角色（架构师 / 编码员 / 研究员 / 审查员）协作处理任务，提供桌面 GUI / 终端 / 自动化作业 / HTTP API 四种入口。"
resource: "https://github.com/saigontechnology/AgentCrew"
tags: [agent, multi-agent, mcp, chat, orchestration]
timestamp: "2026-06-24T15:30:00Z"
---

# AgentCrew（多智能体协作聊天应用）

## 它是什么

[`saigontechnology/AgentCrew`](https://github.com/saigontechnology/AgentCrew) 是一个**多智能体聊天 / 协作应用**。给每个 agent 分配一个角色（架构师、编码员、研究员、审查员……），让它们在一个工作流里协作完成任务，底层支持多种 AI 模型和 MCP（Model Context Protocol）工具协议。

## 为什么用它 / 适合什么场景

- **想摆脱单一 AI 助手的局限**：与其跟一个万能 agent 聊到底，不如让不同角色的 agent 分工；
- **多入口**：桌面 GUI / 终端 / 自动化作业 / HTTP API 四种用法，分别适合日常协作、远程服务器操作、CI/CD 脚本、多实例部署；
- **MCP 友好**：可以挂各种 MCP 工具，让 agent 真正动手操作。

## 关键能力

| 能力 | 说明 |
|---|---|
| 多模型支持 | Claude / GPT / Gemini 等 |
| MCP 协议 | 接入任意 MCP 工具 |
| 角色编排 | 架构师 / 编码员 / 研究员 / 审查员 等可自定义 |
| 四种入口 | 桌面 GUI / 终端 / 自动化作业 / HTTP API |
| 团队协作 | 多 agent 协同处理同一任务 |

## 媒体 / 参考链接

- [项目链接](https://github.com/saigontechnology/AgentCrew)

## 相关概念

- [Brigade](tool-brigade.md) — 本地多 AI 代理协作框架 + Tideline 共享长期记忆
- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架，把 AI 当同事
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP
