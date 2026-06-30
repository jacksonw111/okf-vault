---
type: Tool
title: "dbosify-py（Temporal Python 的 Postgres 平替）"
description: "用 Postgres 替代 Temporal 服务器的 Python 持久化工作流框架——零额外基础设施，跑持久化工作流、活动、信号、更新、重试和恢复。"
resource: "https://github.com/dbos-inc/dbosify-py"
tags: "[python, postgres, workflow, temporal-alternative, durable-execution]"
timestamp: "2026-06-30T15:30:00Z"
---

# dbosify-py（Temporal Python 的 Postgres 平替）

## 它是什么

dbosify-py 是 Temporal Python SDK 的轻量化平替：用 PostgreSQL 替代 Temporal 的专用服务器，提供持久化工作流、活动、信号、更新、重试和恢复等核心能力，但**零额外基础设施**——只要一个 Postgres 就能跑。

## 关键能力

| 能力 | 说明 |
|------|------|
| 持久化工作流 | 流程状态可跨进程 / 跨重启恢复 |
| 活动（Activity） | 工作流里的可重试 / 可恢复任务单元 |
| 信号（Signal） | 从外部触发工作流内的处理 |
| 更新（Update） | 同步向工作流写入状态 |
| 重试 / 恢复 | 内建重试、错误恢复 |
| 零额外基础设施 | 不需要 Temporal Server，只用 Postgres |
| Python 原生 | Python SDK |

## 与 Temporal 的对比

| 维度 | Temporal | dbosify-py |
|------|----------|-----------|
| 状态存储 | Temporal Server（专用集群） | Postgres（任意现有库） |
| 部署复杂度 | 高（需 Temporal + Cassandra/Postgres + ES 等） | 低（一个 Postgres） |
| 功能完整性 | 完整（Workflow / Activity / Schedule / Nexus） | 核心（Workflow / Activity / Signal / Update） |
| 适用阶段 | 大规模生产 | 中小项目 / 不想运维 Temporal |

## 适用场景

- 需要持久化工作流但不想部署 Temporal 集群的项目。
- 已有 Postgres 实例，想「再叠一层」工作流引擎。
- 中小规模 SaaS / 数据管道的可靠执行。

## 媒体参考

![](https://pbs.twimg.com/media/HL8mxBAacAAPWHd.jpg)

## 相关概念

- [OPG](./tool-opg-backend.md) — 一人公司多 app 后端控制面
- [Rust + QUIC 高性能 IM 后端](./tool-rust-quic-im.md) — Actix-web + QUIC + P2P NAT 打洞

## 参考链接

- 项目链接：<https://github.com/dbos-inc/dbosify-py>