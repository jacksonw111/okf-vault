---
type: "Tool"
title: "Foundry（开源 AI 数字公司平台）"
description: "开源 AI 数字公司平台：用户创建公司后系统自动生成董事会 → 部门 → 员工的层级化 agent 组织结构，输入目标即可由 AI 自动拆解任务、分配执行、汇总结果；内置实时群聊、三层记忆（公司/部门/agent + RAG）、成本预算、人工审批，CEO Agent 每 30 分钟自动巡查驱动任务流转。"
resource: "https://github.com/axislab-top/Foundry"
tags: "[ai-agents, multi-agent, orchestration, organization-simulation, docker, nestjs, react]"
timestamp: "2026-07-08T00:00:00Z"
---

# Foundry

## 它是什么

[Foundry](https://github.com/axislab-top/Foundry) 是一个**开源 AI 数字公司平台**，把整个公司抽象成**层级化的 agent 组织**：

- **董事会 → 部门 → 员工 agent** 的组织结构自动生成
- 用户给目标，系统自动**拆解任务、分配执行、汇总结果**
- 技术栈：**NestJS + React (TypeScript)**，**Docker Compose** 一键部署

定位与 CrewAI / AutoGen 等「需要用户自己编排协作」框架不同——Foundry 是**开箱即用**的「整家公司」。

## 与传统 agent 框架的区别

| 维度 | CrewAI / AutoGen | Foundry |
|------|-----------------|---------|
| 协作编排 | 用户自己写 | 系统自动按公司层级拆 |
| 组织结构 | 扁平 / 用户定 | 董事会 → 部门 → 员工 三层 |
| 任务流转 | 手动触发 | CEO Agent 自动巡查驱动 |
| 实时群聊 | 通常无 | 内置 |
| 记忆 | 单 agent 记忆 | **三层记忆**（公司 / 部门 / agent + RAG） |
| 成本控制 | 用户自己写 | 内置预算 + 审批 |
| 部署 | Python 库 | Docker Compose 整套服务 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动组织生成 | 一键生成从董事会到员工 agent 的组织结构 |
| 目标 → 任务 | LLM 自动拆解目标为子任务并分配 |
| 三层记忆 | 公司级、部门级、agent 级 + RAG 检索 |
| 实时群聊 | 模拟公司内部的实时沟通 |
| 成本预算 | 内置成本统计与预算管控 |
| 人工审批 | 关键决策点可设人工 review |
| CEO Agent 自动巡查 | 每 30 分钟自动推动任务流转 |

## 媒体

![Foundry 平台预览](https://pbs.twimg.com/media/HMlunJsbkAASYbl.jpg)

## 参考链接

- [项目仓库](https://github.com/axislab-top/Foundry)

## 相关概念

- [Age of Agents](./tool-age-of-agents.md) — 同为 AI agent 生态工具
- [Agent Crew](./tool-agent-crew.md) — 同为多 agent 协作框架