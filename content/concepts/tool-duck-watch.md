---
type: Tool
title: "duck-watch（MotherDuck 极简可观测性工具）"
description: "MotherDuck 账户的极简可观测性工具，展示账户正在执行什么查询、花费多少成本。"
resource: "https://github.com/CogitatorTech/duck-watch"
tags: [motherduck, observability, duckdb, cost, monitoring]
timestamp: "2026-09-03T00:00:00Z"
---

# duck-watch（MotherDuck 极简可观测性工具）

## 它是什么

[duck-watch](https://github.com/CogitatorTech/duck-watch) 是给 **MotherDuck** 账户准备的**极简可观测性工具**——实时展示账户正在执行什么查询、花了多少钱。

MotherDuck 是云端 DuckDB 服务，按查询计算量计费；duck-watch 让你一眼看清当前哪些 query 在跑、累计 cost，避免账单爆炸。

## 为什么用它 / 适合什么场景

- 用 MotherDuck 但没有一个简单面板看「现在在跑什么、花了多少」；
- 想给团队 / 客户展示 MotherDuck 跑查询的可观测性数据；
- 偏好极简、独立可部署的小工具，而不是接入完整 APM 平台。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时查询列表 | 当前正在执行的查询 |
| 成本展示 | 累计 / 单次 cost |
| MotherDuck 集成 | 专为 MotherDuck 设计 |
| 极简 | 单一可观测性面板，不堆功能 |

## 参考链接

- 项目链接：<https://github.com/CogitatorTech/duck-watch>
- 原始推文：<https://x.com/QingQ77/status/2095528995467215019>
- 媒体：<https://pbs.twimg.com/media/HRN5N3Ha4AAZz_8.jpg>

## 相关概念

- [Microduck](./tool-microduck.md) — Pollen Robotics 开源机器鸭
- [Microduck Replica](./tool-microduck-replica.md) — Microduck 第三方复刻研究
