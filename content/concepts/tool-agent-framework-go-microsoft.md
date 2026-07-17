---
type: "Tool"
title: "Microsoft Agent Framework (Go 版)"
description: "微软出的 Go 版智能体框架, 用来搭多智能体工作流并往生产环境部署; 支持多家大模型提供方、可插拔中间件, 一张图把工作流串起来——顺序、并发、条件分支、检查点、人工介入都能画。"
resource: "https://github.com/microsoft/agent-framework-go"
tags: "[agent-framework, go, microsoft, multi-agent, production, workflow]"
timestamp: "2026-07-17T09:09:00Z"
---

# Microsoft Agent Framework (Go 版)

[Microsoft Agent Framework Go 版](https://github.com/microsoft/agent-framework-go) 是**微软 Agent Framework 的 Go 语言版本**, 专门面向**生产环境**的多智能体 / 多工作流编排。它把原本 .NET 版的可生产性核心带到了 Go 生态, 主要卖点是:

- **多家大模型提供方** (OpenAI / Azure / Anthropic / 自托管等) 通用
- **可插拔中间件**, 鉴权 / 缓存 / 限流 / 日志都能挂载
- **一张图串工作流**: 顺序、并发、条件分支、**检查点 (checkpoint)**、**人工介入 (human-in-the-loop)** 全部节点化

## 它和 LangGraph / AutoGen 的差别

LangGraph (Python) 偏「先写状态机, 再串节点」; AutoGen 偏「对话角色扮演协作」; **Microsoft Agent Framework Go** 走的是「**一张 DAG 图 + 节点语义化**」的工业编排路线——接近 Temporal / Cadence 的姿势。代价是上手曲线略高, 收益是「检查点、人工介入、可观测性」一类生产需求不需要再外挂。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Provider 抽象 | 换底模不动业务代码 |
| 可插拔中间件 | 鉴权 / 缓存 / 限流 / 观测 各取所需 |
| DAG 工作流 | 顺序 / 并发 / 条件分支一图表达 |
| 检查点 | 工作流可恢复, 不重头算 |
| 人工介入 | 关键节点可暂停等用户回灌 |
| Go 生态 | 单 binary 部署, 资源占用低 |

## 参考链接

- [项目仓库](https://github.com/microsoft/agent-framework-go)
- [Microsoft Agent Framework 主页](https://github.com/microsoft/agent-framework)

## 相关概念

- [dbosify-py](./tool-dbosify-py.md) — Temporal Python 的 Postgres 平替, 都是「为 agent 工作流补持久化」的思路
- [Cotal](./tool-cotal.md) — 多智能体开放协议框架, 拓扑可配; Microsoft Agent Framework Go 是「固定 DAG 图 + 节点」路线
- [MCO](./tool-mco.md) — 中立编排层 (Claude Code / Codex CLI / Gemini CLI), Microsoft Agent Framework Go 是「直接编排内部 agent」的另一种选择
