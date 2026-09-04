---
type: Tool
title: "budget-aware-agent（预算感知 Agent：Budget Tracker 与 BATS）"
description: "Google Research 开源的 COLM 2026 论文实现，含 Budget Tracker（每步把剩余搜索 / 浏览次数塞进 ReAct 上下文）与 BATS（在此基础上按剩余额度做规划、自我检查、定时总结，检查不过就换路重来）两套做法。"
resource: "https://github.com/google-research/budget-aware-agent"
tags: [agent, react, budget, planning, self-check, research, python]
timestamp: 2026-09-04T12:00:00Z
---

# budget-aware-agent（预算感知 Agent）

## 它是什么

Google Research 开源的 COLM 2026 论文 Python 实现，主题是**让 Agent 知道自己还剩多少预算，并据此调整行为**。仓库里给了两套做法。

![](https://pbs.twimg.com/media/HRRZIqKbwAAYpY7.jpg)

## 两套做法

| 做法 | 机制 |
|------|------|
| Budget Tracker | 每一步都把**剩余搜索次数与浏览次数**写进 ReAct Agent 的上下文，让模型自己感知余量 |
| BATS | 在 Budget Tracker 基础上再加三件事：按剩余额度**做规划**、**自我检查**、**定时总结**；检查不通过就换一条路重来 |

## 为什么值得看

- 长任务 Agent 最常见的失败模式是「把预算耗在一条走不通的路上」；把余量显式写进上下文，是一种低成本的纠偏手段。
- 「自我检查 + 检查不过就换路」提供了一个可复用的回溯结构，不依赖特定框架。

## 参考链接

- 项目链接：<https://github.com/google-research/budget-aware-agent>
- 原始链接：<https://x.com/QingQ77/status/2095820415813767614>

## 相关概念

- [Semantix](./tool-semantix.md) — 同样以「省下 Agent 运行开销」为目标；Semantix 从缓存命中与上下文复用入手，BATS 从工具调用预算与规划入手
