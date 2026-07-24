---
type: Tool
title: "libredb-studio（开源 AI 驱动 Web SQL IDE）"
description: "一个开源、AI 驱动的 Web SQL IDE,支持 PostgreSQL / MySQL / SQLite / MongoDB 等多种数据库,无需安装,浏览器打开即用。"
resource: "https://github.com/libredb/libredb-studio"
tags: [sql, database, ide, ai, web, postgresql, mysql, sqlite, mongodb]
timestamp: "2026-07-24T00:00:00Z"
---

# libredb-studio

[libredb-studio](https://github.com/libredb/libredb-studio) 是一款**开源、AI 驱动的 Web SQL IDE**——浏览器打开即用，**无需安装**，支持 PostgreSQL、MySQL、SQLite、MongoDB 等多种数据库。

## 它解决的问题

传统 SQL IDE 的两条路线：
- **桌面 IDE**（DataGrip、DBeaver）→ 要装、要授权、绑定单机。
- **Web IDE**（云厂商托管）→ 数据出境风险 + 强制账号。

libredb-studio 把「Web + AI + 多数据库 + 开源」四件事打包到一起：
- 浏览器打开就写
- AI 辅助写 SQL
- 数据源由用户自管，不必上云

## 关键能力

| 能力 | 说明 |
|------|------|
| 零安装 | 浏览器打开即用 |
| 多数据库 | PostgreSQL / MySQL / SQLite / MongoDB |
| AI 辅助 | 内置 LLM 协助写 SQL / 解释执行计划 |
| 完全开源 | 数据不强制出境，可自托管 |

## 适用场景

- 临时需要查一下线上数据，又不想装桌面客户端
- 团队里非技术同学需要写 SQL，让 AI 来帮写
- 出于合规考虑，不想用云厂商托管 SQL IDE

## 参考链接

- 项目仓库: <https://github.com/libredb/libredb-studio>

## 媒体

![](https://pbs.twimg.com/media/HN8wCXZaMAAalZq.jpg)

## 相关概念

- [SiphonDB](tool-siphondb.md) — Tauri v2 跨平台桌面数据库 GUI（PostgreSQL / MySQL / SQLite），本工具是 Web 端版本
- [TradingView MCP](tool-tradingview-mcp.md) — 把 TradingView / 回测 / 扫描器通过 MCP 暴露给 AI，是 AI ↔ 数据源的另一类集成