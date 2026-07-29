---
type: Tool
title: "Zestmem（多智能体协作的分布式持久化记忆服务）"
description: "Go 写的分布式记忆服务，让 Codex、Claude Code 这类 AI Agent 之间能跨会话存取知识。核心就两个 MCP 工具：remember 存、recall 搜，后端用 PostgreSQL 17 + pgvector 做存储和向量检索。"
resource: "https://github.com/jahwag/zestmem"
tags: [memory, multi-agent, mcp, postgresql, pgvector, persistence]
timestamp: "2026-07-28T05:09:00.000Z"
---

# Zestmem

## 它是什么

多 Agent 协作团队的**持久化记忆服务**——核心特点：

- **跨 Agent 共享**：Codex、Claude Code 等共用一份
- **跨会话持久**：会话断了知识还在
- **可搜索**：基于 PostgreSQL 17 + pgvector
- **极简接口**：就两个 MCP 工具

![示意图](https://pbs.twimg.com/media/HONo_JyagAA6Dq5.jpg)

## 核心 API（只有两个）

| MCP 工具 | 用途 |
|----------|------|
| `remember` | 存知识 |
| `recall` | 搜知识 |

## 与「每个 Agent 自带记忆」的差异

| 自带记忆 | Zestmem |
|----------|---------|
| 知识孤岛 | 跨 Agent 共享 |
| 各自一套存储 | 集中服务 |
| 难搜索 | 向量 + 全文 |
| 跨 Agent 重复劳动 | 知识复用 |

## 关键能力

| 能力 | 说明 |
|------|------|
| MCP 协议 | 任何支持 MCP 的 Agent 都能接 |
| PostgreSQL 17 | 现代 PG + pgvector |
| 向量检索 | 语义级 recall |
| 跨 Agent | 知识团队共享 |
| 持久 | 会话结束不丢 |

## 原始链接

- [项目仓库](https://github.com/jahwag/zestmem)
- [推文剪藏](https://x.com/QingQ77/status/2081970152728363258)

## 相关概念

- [OptMem（426 token 极简记忆）](./tool-optmem.md) — 单 Agent 极简记忆思路
- [EverOS](./tool-everos.md) — 统一本地长期记忆层，让不同 agent 共享并进化记忆
- [second-brain-cloudflare](./tool-second-brain-cloudflare.md) — Cloudflare Workers 上的共享记忆层
- [EchoesVault（OpenCode 持久记忆）](./tool-echoes-vault-opencode.md) — OpenCode 插件，会话结束自动记决策