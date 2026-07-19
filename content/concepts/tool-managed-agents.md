---
type: Tool
title: "managed-agents（sandbaseai）"
description: "与 Claude Managed Agents API 兼容的开源 Agent 运行时，让团队在本地运行多 Agent 系统，支持任意模型和可视化 Dashboard。"
resource: "https://github.com/sandbaseai/managed-agents"
tags: "[agent, runtime, multi-agent, claude-api, open-source]"
timestamp: "2026-07-19T15:43:00Z"
---

# managed-agents（sandbaseai）

## 它是什么

sandbaseai/managed-agents 是一个**与 Anthropic Claude Managed Agents API 兼容**的开源 Agent 运行时，让团队可以在自己的基础设施上跑多 Agent 系统，**不再被 Claude 托管代理服务的封闭环境绑定**，同时保持 API 兼容层以便现有调用方零修改切换。

## 核心定位

| 维度 | 说明 |
|------|------|
| API 兼容 | 完整实现 Claude Managed Agents API 协议，对调用方透明 |
| 模型无关 | 支持任意模型（Anthropic / OpenAI / 开源 / 本地 GGUF），不锁单一供应商 |
| 部署形态 | 本地或私有云运行，数据与执行都在用户边界内 |
| 可观测性 | 内置可视化 Dashboard，实时查看 Agent 状态 / 工具调用 / 任务进度 |

## 适合谁

- 已经接入 Claude Managed Agents，但希望摆脱托管服务定价 / 配额 / 数据出境限制的团队
- 需要在**多模型之间混跑**（用 Claude 做规划、本地模型做执行）的多 Agent 系统搭建者
- 企业内需要把 Agent 执行**留在自有 VPC** 满足合规要求的项目

## 与类似工具的差别

- [firstmate](./tool-firstmate.md) 是「目录约定 + 派 worker」的轻量多 Agent 模式
- [Comando](./tool-comando.md) 是桌面 GUI 多 Agent 协作编辑器
- [Cotal](./tool-cotal.md) 是多智能体开放协议框架（拓扑可配）
- managed-agents 的差异点：**唯一明确「100% 兼容 Claude Managed Agents API」**——其他工具大多自创协议层

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Agent 能力的封装单位
- [Claude Code](./tool-claude-code.md) — Anthropic 的终端 AI 编码 agent
- [12-Factor Agents](./tool-12-factor-agents.md) — 23.5k 星 Agent 工程原则

## 参考链接

- 项目链接: <https://github.com/sandbaseai/managed-agents>