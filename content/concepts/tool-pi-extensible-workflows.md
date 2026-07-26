---
type: "Tool"
title: "pi-extensible-workflows（vekexasia/pi-extensible-workflows）"
description: "为 Pi 终端 AI 助手提供确定性多代理工作流编排：支持并行派发、审批暂停和断点恢复。"
resource: "https://github.com/vekexasia/pi-extensible-workflows"
tags: [pi, workflow, multi-agent, orchestration, durable, approval]
timestamp: "2026-07-26T07:40:00Z"
---

# pi-extensible-workflows（vekexasia/pi-extensible-workflows）

## 它是什么

`vekexasia/pi-extensible-workflows` 是给 [Pi](./tool-pi-desktop.md) 终端 AI 助手加的**确定性多代理工作流编排扩展**。相比 LLM「自己决定下一步」的非确定性，多代理工作流要做到**可预期**：并行派发子任务、关键节点人工审批暂停、出错可断点恢复。

## 为什么用它 / 适合什么场景

- 跑涉及多个子代理的复杂任务时，需要**可预期**的编排，而不是让 LLM 即兴发挥；
- 关键节点（合并、生产动作）需要**人工审批暂停**，不能全自动；
- 任务可能跑很久 / 中途崩溃，需要**断点恢复**而不是从头再来。

## 关键能力

| 能力 | 说明 |
|------|------|
| 确定性编排 | 工作流定义明确，行为可复现 |
| 并行派发 | 多个子代理可同时跑 |
| 审批暂停 | 关键节点等人工确认 |
| 断点恢复 | 中断后可从断点继续 |
| Pi 生态 | 为 Pi 终端 AI 助手量身定做 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOEvNY2bwAAh0hI.jpg)

- 项目链接：<https://github.com/vekexasia/pi-extensible-workflows>

## 相关概念

- [pi-fusion](tool-pi-fusion.md) — 同样为 Pi 扩展（多模型并行扇出而非确定性多代理）
- [pi-hive](tool-pi-hive.md) — 同样为 Pi 加多智能体（YAML 配置团队，规划/执行分离）
- [pi-task](tool-pi-task-delegation.md) — 同样为 Pi 派生子任务（轻量子代理，本工具偏确定性工作流）
