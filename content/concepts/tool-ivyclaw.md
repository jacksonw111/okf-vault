---
type: "Tool"
title: "IvyClaw（五 Agent 协作的研发 harness）"
description: "ivyfan-toowell 的 IvyClaw：把单次模型调用解不开的研发任务，拆给五个 Agent（从规划一路干到审查）；三档模型路由 + 最小工具集省 token，沙箱、ARQ 异步、HITL 审批、网关限流审计全塞一个仓库，docker compose 能拉起来就跑。"
resource: "https://github.com/ivyfan-toowell/IvyClaw"
tags: "[multi-agent, harness, dev-orchestration, sandbox, docker-compose, hitl]"
timestamp: "2026-09-14T22:30:00Z"
---

# IvyClaw（五 Agent 协作的研发 harness）

## 它是什么

[ivyfan-toowell/IvyClaw](https://github.com/ivyfan-toowell/IvyClaw) 是一个面向**真实研发**的多 agent harness：单次模型调用做不了研发，所以 IvyClaw 把活拆给**五个 Agent**（从规划一路干到审查），沙箱、异步、审批、网关监控全配齐，**docker compose 能拉起来就跑**。

## 关键设计

| 设计 | 说明 |
|------|------|
| 五个 Agent 分工 | 从规划 → 编码 → 审查，端到端流水线 |
| 三档模型路由 | 简单任务路由到便宜模型，复杂任务路由到强模型 |
| 最小工具集 | 每个 Agent 只暴露必要工具，省 token |
| 沙箱 | Agent 在隔离环境里跑 |
| ARQ 异步任务队列 | 异步执行、长任务可恢复 |
| HITL 审批 | 关键步骤要人工介入 |
| 网关限流 + 审计 | API 网关做限流，所有动作有审计日志 |
| docker compose | 一键拉起整个 harness |

## 与同类对比

| 维度 | IvyClaw | Devin / 类似云端 agent |
|------|---------|------------------------|
| 部署 | docker compose 自托管 | SaaS |
| Agent 数 | 固定 5 个分工 | 单 agent 多角色 |
| 模型路由 | 三档路由 | 单一后端 |
| HITL | 内置审批 | 通常需要外部介入 |

## 项目链接

- 仓库：<https://github.com/ivyfan-toowell/IvyClaw>
