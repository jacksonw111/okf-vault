---
type: "Tool"
title: "Seeder（小团队自托管项目管理 + MCP）"
description: "danielsyauqi/Seeder —— 面向小团队的轻量级自托管项目管理工具，看板任务 + 客户请求队列 + 内置 MCP 服务器，可部署在 Cloudflare Workers（D1 + R2）或单台 Node VM。"
tags: "[project-management, kanban, mcp, self-hosted, cloudflare-workers, small-team]"
timestamp: "2026-06-22T16:01:00Z"
---

# Seeder（小团队自托管项目管理 + MCP）

## 它是什么

[`danielsyauqi/Seeder`](https://github.com/danielsyauqi/Seeder) 是一套**面向小团队的轻量级自托管项目管理工具**。可部署在 Cloudflare Workers（D1 + R2）或者单台 Node VM 上，自带 MCP 服务器让 AI 代理可编程接入。

核心功能：

- **看板任务管理**：阶段、标签、优先级、指派、截止日期
- **客户请求队列**：新建 → 审核 → 转化 → 关闭（独立于内部任务流）
- **公开客户看板**：把工单状态透明化给客户
- **日常计划表**：团队每日 stand-up 辅助
- **活动日志**：操作审计 + 时间线回顾

> 截图：![](https://pbs.twimg.com/media/HLThWgGasAAbBiX.jpg)
> 截图：![](https://pbs.twimg.com/media/HLThY5jbcAAZOlv.jpg)

## 为什么用它 / 适合什么场景

- **自托管 + Cloudflare Workers 部署**：无需运维服务器，用免费额度就能跑小团队；不依赖 SaaS 订阅。
- **看板 + 客户请求双队列**：内部任务与客户工单天然分离，又能在同一 UI 看。
- **内置 MCP**：Claude Code / Codex / Cursor 等 agent 可直接通过 MCP 接口查询 / 修改任务。
- **公开客户看板**：客户自助查进度，减少「这个事儿进展如何」的问询。

适合：

- 3 ~ 20 人小团队，**不想用 Jira / Linear / Trello SaaS**的工程团队。
- 需要 **AI 代理协作**（agent 自动从工单拉任务 / 推进状态）的场景。
- 客户对接型工作室 / 自由职业团队。

## 关键能力

| 能力 | 说明 |
|---|---|
| 部署目标 | Cloudflare Workers（D1 + R2）或 Node VM 单机 |
| 任务模型 | 阶段 / 标签 / 优先级 / 指派 / 截止日期 |
| 客户请求 | 独立队列 + 审核流程 + 公开看板 |
| MCP 服务器 | 内置，让 AI agent 可读写任务 |
| 日常计划表 | 团队 stand-up 辅助视图 |
| 活动日志 | 完整操作审计 |

## 部署选项

| 部署目标 | 数据 | 适用 |
|---|---|---|
| Cloudflare Workers | D1（SQLite）+ R2（对象存储） | 免费 / 低成本、抗运维 |
| Node VM | Postgres / SQLite + 本地盘 | 完全控制权、内网部署 |

## 参考链接

- [项目链接](https://github.com/danielsyauqi/Seeder)

## 相关概念

- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面（账号 / AI 网关 / 视频 / 支付）
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Kamal 一键部署
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP