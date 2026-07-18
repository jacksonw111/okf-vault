---
type: "Tool"
title: "matterloop（huleidada/matterloop）"
description: "Python 框架，把 AI Agent 从「调一次模型就完事」升级为可验证、可暂停、可恢复的工程闭环：内置人工反馈、多 Agent 编排、预算上限和断点续跑。"
tags: "[python, agent, framework, human-in-loop, multi-agent, orchestration, checkpoint]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/huleidada/matterloop"
---

# matterloop（huleidada/matterloop）

## 它是什么

[`matterloop`](https://github.com/huleidada/matterloop) 是 huleidada 开源的 Python Agent 框架，**核心卖点是把 Agent 从「单次 prompt → 一次推理」推进到「可被工程化托管的闭环」**。

它明确针对当前 agent 开发中最容易踩的几个坑：

- 跑一半崩了 → 怎么从中断点继续；
- 跑飞了 → 怎么在预算 / 步数处自动停下；
- 答得不对 → 怎么把人类反馈接进循环；
- 任务复杂 → 怎么拆给多个 agent 协同。

## 关键能力

| 能力 | 说明 |
|------|------|
| 验证闭环 | 每一步输出可被规则 / 评分函数校验，不通过就重试 |
| 暂停 / 恢复 | 长任务可中断后从 checkpoint 继续 |
| 人工反馈（Human-in-the-loop） | 关键节点可以插入人工审核 / 修订 |
| 多 Agent 编排 | 子任务拆分给不同 agent，并组合结果 |
| 预算上限 | Token / 费用 / 步数都可硬性限制 |
| 断点续跑 | 异常退出后可继续上次未完成的步骤 |

## 与「一次性 prompt」的对比

| 维度 | 一次性 prompt | matterloop |
|------|---------------|------------|
| 失败恢复 | 重头跑 | 从断点继续 |
| 校验 | 全靠 prompt 自洽 | 可在节点上挂规则 |
| 成本控制 | 只能事前估上限 | 运行时硬性 cutoff |
| 多人协作 | 不支持 | 多 agent 编排 |
| 人工介入 | 必须从头复制粘贴 | 在节点处插入反馈 |

## 适合什么场景

- 长任务 / 多步骤的研究、调研、批处理；
- 不允许「跑飞就完蛋」、需要强可靠性的生产 agent；
- 想做「半自动」：大多数步骤交给 agent，关键节点人工把关的工作流。

## 参考链接

- [原始链接](https://github.com/huleidada/matterloop)

## 相关概念

- [forkd](tool-forkd.md) — Agent 安全 / 隔离层的 microVM 方案；matterloop 解决的是「Agent 流程怎么不断不跑飞」，forkd 解决的是「Agent 在哪跑才不污染本机」
- [clawk](tool-clawk.md) — 类似 forkd 的 agent 沙箱思路（一次性 VM）