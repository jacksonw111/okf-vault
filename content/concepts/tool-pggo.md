---
type: Tool
title: "pgGo（Go 写的极简 Postgres 客户端，专为 coding agent 设计）"
description: "alxshp 出品的 Go 写 Postgres 客户端：~2000 行代码 / ~4 MB 静态二进制 / 直接讲 Postgres wire protocol（无 pgx / 无 libpq），JSON 原生、参数化安全、默认只读、有界输出 + 严格超时 + 可预测错误 + SQLSTATE；端到端一次调用 ~8 ms，专为 coding agent 优化。"
resource: "https://pgGo.dev"
tags: [postgres, golang, coding-agent, cli, database, wire-protocol, agent-tooling]
timestamp: 2026-09-30T23:36:55Z
---

# pgGo

## 它是什么

**pgGo** 是 [alxshp](https://x.com/alxshp) 出品的**轻量、快速、为 coding agent 设计**的 Postgres 客户端——用 **Go** 写的 **~2000 行**，**~4 MB** 静态二进制（**~1.7 MB** 压缩）。

最大特点：**直接讲 Postgres wire protocol**，**不依赖** `pgx`、不依赖 `libpq`、也不做 `psql` 解析。这让 pgGo 做到了：

- **零外部依赖**（single binary）
- **JSON 原生**
- **参数化查询**（安全）
- **默认只读**（防误写）
- **有界输出**（bounded output）
- **严格超时**
- **可预测错误 + SQLSTATE**
- **~8 ms 一次 Postgres 往返**

宣传语：「**Minimal. Fast. Agentic.**」

## 为什么用它 / 适合什么场景

- 让 Claude Code / Codex / 其他编码 agent 在沙箱里**直接连自家 Postgres**，不需要 libpq / pgx 等运行时。
- 想做一个**严格受限**的数据库 CLI：默认只读 + 强制参数化 + 输出有界 + 严格超时。
- 想要**单二进制、零依赖**的小工具塞进 Docker / CI / Edge。
- 对延迟敏感（~8 ms 一次调用），希望不要被 ORM / 解析器拖慢。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实现 | Go（~2000 行） |
| 协议 | 直接讲 Postgres wire protocol |
| 体积 | ~4 MB 静态二进制（~1.7 MB 压缩） |
| 依赖 | 零运行时依赖 |
| 安全 | 参数化查询 + 默认只读 |
| 输出 | JSON 原生 + 有界输出 |
| 错误 | 可预测 + SQLSTATE |
| 超时 | 严格 |
| 延迟 | ~8 ms / 调用 |

## 参考链接

- 官网：<https://pgGo.dev>

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2105338370809528321/vid/avc1/3064x2160/9pFpDND15AN9AEig.mp4?tag=29>

## 相关概念

- [Postgres MCP](./tool-mcp-gsc.md) — 另一种把数据库接入 Agent 的思路（走 MCP 协议）
