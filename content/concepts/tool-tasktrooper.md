---
type: "Tool"
title: "TaskTrooper（本机桌面任务看板 + 6 角色 agent）"
description: "Go 后端 + Electron 套壳 + 自带 Postgres 的本机桌面应用；13 列看板开箱即用，卡片带验收条件；6 个角色智能体各管一摊，95 个打底技能。"
resource: "https://github.com/makifbaysal/tasktrooper"
tags: "[kanban, desktop, postgres, electron, go, multi-agent, self-hosted, task-board]"
timestamp: "2026-09-19T16:00:00Z"
---

# TaskTrooper（本机桌面任务看板 + 6 角色 agent）

## 它是什么

[makifbaysal/tasktrooper](https://github.com/makifbaysal/tasktrooper) 是一个**套装在本机的桌面任务管理应用**：

- **后端**：Go
- **前端套壳**：Electron
- **数据**：自带 Postgres

开箱即用：

- **看板 13 列**开箱即用
- 卡片**带验收条件**走流程
- 每个任务**单独开分支 + 提 PR**
- **6 个角色智能体**各管一摊
- 技能库给了 **95 个**打底
- **提示词和工具权限**随便改

## 为什么用它 / 适合什么场景

- 想在**本机**跑一套「任务看板 + 多角色 agent」自托管栈，不依赖云 SaaS。
- 需要把每个任务**结构化带验收条件**，而不是写一段自由描述。
- 喜欢把 agent 角色分工明确化（PM / Dev / Reviewer 等各管各的）。
- 需要每个任务自动开分支 + 提 PR 的开发工作流。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本机一体化 | Go + Electron + Postgres，全跑在本地 |
| 13 列看板 | 比典型 Kanban 更细的列覆盖完整流程 |
| 验收条件卡片 | 每张卡自带通过条件 |
| 分支 + PR 工作流 | 每个任务独立分支并提 PR |
| 6 角色智能体 | 多角色分工协作 |
| 95 个打底技能 | 开箱即用的技能库 |
| 可改提示词 / 工具权限 | 行为不是黑盒 |

## 与相关概念的关系

- [CodexBoard（Codex 任务看板）](./tool-codexboard.md) — 都是「给编码 agent 加任务看板」，但 codexboard 偏 Mac 单机 Codex 中间件，tasktrooper 偏「本机一体化 + 多角色 agent」
- [Agent Launcher](./tool-agent-launcher.md) — 同为多 agent 桌面管理，agent-launcher 是「统一启动 Claude Code / Codex 等多款 CLI」，tasktrooper 是「自带 6 角色 + 看板 + 技能库」

## 参考

- 项目链接：<https://github.com/makifbaysal/tasktrooper>
- 原始推文：<https://x.com/QingQ77/status/2101319651997237608>