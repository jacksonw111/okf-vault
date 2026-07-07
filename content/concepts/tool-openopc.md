---
type: Tool
title: "OpenOPC"
description: "香港大学数据科学团队（HKUDS）开源框架：用 AI 角色组成虚拟公司执行复杂任务，自建团队、自主运行、自我成长。"
resource: "https://github.com/HKUDS/OpenOPC"
tags: [agent, multi-agent, simulation, org]
timestamp: "2026-07-07T12:00:00Z"
---

# OpenOPC

## 它是什么
香港大学数据科学团队（HKUDS）开源的多智能体框架 `OpenOPC`，核心理念是把 AI 角色 **组成虚拟公司** 来执行复杂任务。项目提供 **CLI 与 Office UI（React + Phaser）** 两种交互界面，按"自建团队、自主运行、自我成长"三个机制运作。

## 为什么用它 / 适合什么场景
- 想看到 AI 角色真的作为一个"虚拟组织"在协作，而不是简单的「两个 agent 对话」。
- 需要 Kanban / 角色 / 协作流程这类"组织级"可视化与控制。
- 适合研究多智能体组织动态、自动化办公流水线、以及 AI 团队拓扑实验。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自建团队 | 根据任务目标自动创建组织架构、招募 AI 员工 |
| 自主运行 | 看板管理 + 角色间协作推进执行 |
| 自我成长 | 执行结果沉淀为员工经验和共享手册 |
| CLI / Office UI 双形态 | 终端自动化与可视化协作两种入口 |
| HKUDS 出品 | 港大数据科学团队长期在多智能体组织方向有积累 |

## 相关概念
- [Fundamental-Ava](tool-fundamental-ava.md) — Python 大规模多智能体模拟框架，能跑上千智能体观察涌现
- [AgentCrew](tool-agent-crew.md) — 多智能体协作聊天应用，4 种入口（GUI / 终端 / 自动化作业 / HTTP API）
- [Cotal](tool-cotal.md) — 多智能体开放协议框架，拓扑可配（对等 / 经理制 / 指挥链 / 混搭）
- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架
- [Brigade](tool-brigade.md) — 本地 AI 代理团队 + Tideline 共享长期记忆，多模型可切换
