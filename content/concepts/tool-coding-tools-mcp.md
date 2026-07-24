---
type: Tool
title: "coding-tools-mcp（Rust + Tauri 2 桌面 MCP 编程工作台）"
description: "Rust + Tauri 2 写的桌面端,装好后选个项目目录启动,AI 通过 MCP 就能读文件、改代码、跑命令、git 操作。每轮任务做完可存一个检查点到 docs/history-session/,下个新对话用 history_session_bootstrap 把进度拉回来。"
resource: "https://github.com/mybolide/coding-tools-mcp"
tags: [mcp, coding-agent, tauri, rust, session-history, desktop]
timestamp: "2026-07-24T00:00:00Z"
---

# coding-tools-mcp

[coding-tools-mcp](https://github.com/mybolide/coding-tools-mcp) 是一款 **Rust + Tauri 2** 写的桌面端 MCP（Model Context Protocol）服务器——装好后选个项目目录启动，AI 就能通过 MCP **读文件、改代码、跑命令、做 git 操作**。

## 它解决的问题

把 AI 编程代理真正接到本地项目，常见痛点：

| 痛点 | 本工具的回应 |
|------|------|
| 每次新对话都要重新介绍项目背景 | `history_session_bootstrap` 工具拉回历史会话 |
| 任务中间断了不知道回到哪一步 | 每轮任务做完存检查点到 `docs/history-session/` |
| 文件 / 命令权限没边界 | 启动时选定项目目录，作用域天然受限 |
| 工具散在各处 | 一个桌面端 MCP 服务器全包 |

## 关键能力

| 能力 | 说明 |
|------|------|
| Tauri 2 桌面端 | Rust + Tauri 2 写的原生桌面应用 |
| MCP 服务器 | 标准 MCP 协议，主流 AI 客户端可直接接入 |
| 文件 / 代码 / 命令 / git | 完整的本地开发权限组合 |
| 会话检查点 | 每轮任务做完存 `docs/history-session/` 快照 |
| 自动续接 | 下个新对话调 `history_session_bootstrap` 即可恢复上下文 |
| 项目目录限定 | 启动时选目录，AI 访问被天然圈定 |

## 适用场景

- 想给 Claude Code / Codex / 自研 Agent 一个统一的本地开发入口
- 任务跨多个对话，希望状态可恢复
- 希望 AI 的文件 / 命令权限天然受限（避免误删整盘）

## 参考链接

- 项目仓库: <https://github.com/mybolide/coding-tools-mcp>

## 媒体

![](https://pbs.twimg.com/media/HN9TgOqb0AABf1q.jpg)

## 相关概念

- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP，侧重任务持久化
- [DevSpace](tool-devspace-mcp.md) — 自托管 MCP 编程工作台（ChatGPT 变 Codex CLI），侧重自托管 Web 入口
- [Recall](tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆插件，跨会话上下文注入
- [EchoesVault](tool-echoes-vault-opencode.md) — OpenCode 插件会话结束自动记决策，下次回放