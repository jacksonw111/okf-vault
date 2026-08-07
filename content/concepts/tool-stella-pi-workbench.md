---
type: Tool
title: "Stella Pi Workbench"
description: "Pi 用户的桌面工作台 + 本地 Agent 团队控制面：单机内完成多 Agent 委派、任务看板、人工验收与本地自动化，无需引入远程后端。"
resource: "https://github.com/ZY-LI-F/pi-workbench"
tags: [pi, workbench, agent-control-plane, multi-agent, task-board, local-first]
timestamp: 2026-08-06T09:30:00Z
---

# Stella Pi Workbench

## 它是什么

ZY-LI-F 开发的桌面工作台，专为 Pi（pi-mono / pi-coding-agent）用户设计，把 Pi 实例升级为可审计、可协作、可验收的多 Agent 控制面。

## 为什么用它 / 适合什么场景

- 想在 Pi 之外给本地 agent 团队装一个原生桌面 UI，又不想引入远程后端 / 云服务。
- 想让 agent 任务从「对话框里聊天」升级为「带看板、有验收、有审计日志」的工作流。
- 需要 Pi 多 Agent 委派时给人类保留验收闸门，避免 agent 静默改关键文件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生桌面工作台 | 给 Pi 用户提供 macOS / Linux 桌面 UI |
| 多 Agent 委派 | 在单机范围内管理多 Agent 协作 |
| 任务看板 | 每条任务可视化跟踪与人工验收 |
| 可审计 | 操作日志留痕，便于回溯与责任归属 |

## 相关概念
- [Mypaios](./tool-mypaios.md) — Python/FastAPI 自托管本地优先 AI 工作台
- [Tabminal](./tool-tabminal.md) — 把终端 + 文件编辑 + AI 智能体收进同一网页界面
- [Pi Workbench (tool-pi-tbox)](./tool-pi-tbox.md) — Pi 扩展工具开关面板