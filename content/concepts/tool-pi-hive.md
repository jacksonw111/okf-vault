---
type: "Tool"
title: "pi-hive（Pi 的层次化多智能体团队协作工具）"
description: "给 Pi Coding Agent 加一套层次化多智能体团队协作工具，用 YAML 配置定义团队结构，规划与执行分开跑。"
tags: "[pi, agent, multi-agent, yaml, hierarchy, collaboration]"
timestamp: "2026-07-06T08:34:00.000Z"
resource: "https://github.com/demetere/pi-hive"
---

# pi-hive（Pi 的层次化多智能体团队协作工具）

## 它是什么

[`pi-hive`](https://github.com/demetere/pi-hive) 是给 **Pi Coding Agent** 扩展的**层次化多智能体团队协作**工具。它让 Pi 不再是「一个代理单干」，而是按 **YAML 配置**定义出团队结构：一个或多个规划者（planner）拆任务、多个执行者（executor）落地——**规划与执行分离**。

## 核心思路

- **YAML 即配置**：团队拓扑、角色、职责、协作规则都写在 YAML 里
- **规划 / 执行分离**：高层 agent 拆任务派工，底层 agent 干活交付
- **层次化**：支持多层嵌套，复杂任务可逐层下钻

![pi-hive 拓扑示意](https://pbs.twimg.com/media/HMgTBWKaYAADleS.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 团队结构配置 | 一个 YAML 文件描述完整团队拓扑 |
| 多 Agent 协作 | 多个 agent 同时跑，分工明确 |
| 规划执行分离 | Planner 拆解任务 → Executor 落地 |
| Pi 集成 | 作为 Pi 扩展直接挂载 |

## 适用场景

- 复杂任务需要多步拆解、并行执行
- 想用结构化配置管理多 agent 协作而非在 prompt 里硬塞角色
- 给 Pi 增加「团队作战」能力

## 参考链接

- [项目链接](https://github.com/demetere/pi-hive)

## 相关概念

- [pi-claude-bridge](tool-pi-claude-bridge.md) — Pi 接入 Claude Code 的桥接扩展
- [pi-env](tool-pi-env.md) — Pi Coding Agent 的沙箱运行环境
- [Firstmate](tool-firstmate.md) — 终端编码 AI 拆任务派多个 crewmate 并行干活
- [Cotal](tool-cotal.md) — 多智能体开放协议框架，打破固定拓扑