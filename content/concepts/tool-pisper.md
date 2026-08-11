---
type: "Tool"
title: "Pisper（ling-kong-ran/pisper）"
description: "把 Pi Coding Agent 包成桌面端与终端客户端,多个会话并行推进;工具 / 记忆 / MCP / 自动化收进同一个本地应用,适合同时跑多个 Agent 任务、每个还需独立配模型 / 目录 / 权限的场景。"
resource: "https://github.com/ling-kong-ran/pisper"
tags: "[agent, pi, desktop, terminal, parallel, mcp, memory]"
timestamp: "2026-08-11T16:00:00Z"
---

# Pisper

[Pisper](https://github.com/ling-kong-ran/pisper) 把 Pi Coding Agent 包成**桌面端 + 终端客户端**,支持多个会话并行推进,工具 / 记忆 / MCP / 自动化收进一个本地应用。

项目链接：<https://github.com/ling-kong-ran/pisper>

## 它是什么

Pi Coding Agent 的**多会话并行承载层**:Pi 本身是单会话编码代理,Pisper 把多个 Pi 实例的会话、配置、工具链整合到一个客户端里,每个会话可独立配模型 / 目录 / 权限。

## 为什么用它 / 适合什么场景

- **多任务并行**:同时跑多个 agent 任务(不同目录、不同模型、不同权限)而不串行开会话。
- **统一工作台**:工具 / 记忆 / MCP / 自动化集中管,跨任务复用。
- **本地优先**:全部跑在本机,数据不出本地。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多会话并行 | 同时跑多个 agent 任务,互不阻塞 |
| 桌面 + 终端双形态 | 同一份底层,GUI 与 TUI 双前端 |
| 工具统一管理 | 工具注册 / 启用 / 禁用集中处理 |
| 记忆共享 | 跨任务复用记忆(可选范围) |
| MCP 集成 | 支持 Model Context Protocol 工具接入 |
| 自动化 | 任务编排与定时触发 |
| 独立模型配置 | 每个会话可独立选模型 / API Key |
| 独立目录 / 权限 | 每个会话有独立工作目录与权限边界 |

## 媒体

![](https://pbs.twimg.com/media/HPU4GzybMAAiMPd.jpg)

## 参考链接

- [项目仓库](https://github.com/ling-kong-ran/pisper)

## 相关概念

- [Stella Pi Workbench](./tool-stella-pi-workbench.md) — Pi 桌面工作台 + 可审计本地 Agent 团队控制面,本工具是其同生态对照
- [Agent Manager Tmux](./tool-agent-manager-tmux.md) — TUI 架在 tmux 上统一管 Claude Code / Codex / OpenCode 多 agent,本工具是其桌面端对照
- [Codex Bridge](./tool-codex-bridge.md) — Claude Code 插件,跨编码 agent 的另一条整合路线