---
type: "Tool"
title: "AgentScope 2.0（多租户多会话的 Agent 运行环境）"
description: "agentscope-ai 的 Agent 运行环境：事件总线 + 实时追踪 + 人工介入 + 细粒度权限 + 多租户多会话隔离 + 多种执行后端（本地 / Docker / E2B / Daytona）+ 多 Agent / MCP / Skill Hub / 中间件。模型负责想，它负责让 Agent 安全稳定地干活。"
resource: "https://github.com/agentscope-ai/agentscope"
tags: "[agent-runtime, multi-tenant, sandbox, mcp, skill-hub, multi-agent]"
timestamp: "2026-09-14T22:30:00Z"
---

# AgentScope 2.0（多租户多会话的 Agent 运行环境）

## 它是什么

[agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) 是 **AgentScope 2.0** —— 一个**多租户多会话的 Agent 运行环境**。

> 很多 Agent 不是模型不行，而是一上线就扛不住。多用户、多会话、权限隔离、代码沙箱——这些生产环境的基本功没做好，模型再强也白搭。
>
> AgentScope 2.0 走的就是另一条路：**不负责教模型思考，专门把 Agent 运行环境搭扎实**。
>
> 一句话：模型负责想，它负责让 Agent 安全、稳定地干活。

## 关键能力

| 能力 | 说明 |
|------|------|
| 事件总线 | 支持实时追踪 |
| 人工介入 | HITL 干预 |
| 细粒度权限 | 工具 / 资源 / 操作权限控制 |
| 多租户 | 用户隔离 |
| 多会话 | 会话间互不影响 |
| 多执行后端 | 本地 / Docker / E2B / Daytona |
| 沙箱 | 代码丢进沙箱跑 |
| 多 Agent | 多 agent 协作 |
| MCP | 原生 MCP 集成 |
| Skill Hub | 技能管理 |
| 中间件 | 拦截 / 监控 / 重试 |

## 与同类对比

| 维度 | AgentScope 2.0 | Pi Coding Agent | Claude Code |
|------|----------------|------------------|-------------|
| 定位 | Agent 运行时 | 终端 CLI + 库 | 终端 CLI |
| 多租户 | ✅ | ❌ | ❌ |
| 多会话隔离 | ✅ | ❌ | ❌ |
| 多执行后端 | ✅ | 部分 | 部分 |
| MCP | ✅ | ✅ | ✅ |
| Skill Hub | ✅ | ✅（git 安装） | ✅ |

## 项目链接

- 仓库：<https://github.com/agentscope-ai/agentscope>

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — AgentScope 2.0 是 harness 的典型实现
- [Sandbox（沙箱）](./term-sandbox.md) — 它的核心安全机制
- [Multi-Agent（多智能体协作）](./term-multi-agent.md) — 它内置多 agent 协作
