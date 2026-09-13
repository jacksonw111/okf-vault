---
type: "Tool"
title: "ThinkingBox（微软智能体评测与训练框架）"
description: "ThinkingBox 是微软开源的智能体评测与训练框架，通过 MCP Session Proxy 调度多个隔离的工具服务进程，驱动 Agent LLM、模拟用户 LLM 和裁判 LLM 完成多轮工具调用与断言评测。"
resource: "https://github.com/microsoft/thinkingbox"
tags: "[agent, eval, mcp, microsoft, training, benchmark]"
timestamp: "2026-09-13T13:45:00Z"
---

# ThinkingBox（微软智能体评测与训练框架）

## 它是什么

[microsoft/thinkingbox](https://github.com/microsoft/thinkingbox) 是微软开源的**智能体评测与训练框架**。它的核心组件是 **MCP Session Proxy**：调度多个隔离的工具服务进程，并行驱动三类 LLM：

- **Agent LLM** —— 被测的智能体
- **模拟用户 LLM** —— 扮演用户角色发起多轮对话
- **裁判 LLM** —— 对工具调用 / 任务完成度做断言评测

## 为什么用它 / 适合什么场景

- 想系统评估 coding agent / browser agent 的真实多轮工具调用能力。
- 需要**沙箱化工具**（让 agent 调用 MySQL / HTTP / shell 但又不让它越权）。
- 想用 LLM-as-judge 做端到端断言，而不是手工打分。
- 在做 RL 训练 / agent 后训练，需要可重放的多轮工具轨迹。

## 关键能力

| 能力 | 说明 |
|------|------|
| MCP Session Proxy | 调度隔离工具服务 |
| 三角色 LLM | Agent / User / Judge 协作跑评测 |
| 多轮工具调用 | 模拟真实任务链路 |
| 断言评测 | LLM-as-judge 写断言 |
| 沙箱工具 | 每个工具进程独立隔离 |

## 项目链接

- 仓库：<https://github.com/microsoft/thinkingbox>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — ThinkingBox 适合给装好 Skills 的 Agent 跑评测
- [MCP（Model Context Protocol）](./term-mcp.md) — ThinkingBox 的工具隔离机制基于 MCP