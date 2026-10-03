---
type: "Tool"
title: "dbx（t8y2/dbx：25 MB 的开源数据库客户端）"
description: "t8y2 出品的轻量开源数据库 GUI 客户端：仅 25 MB，支持 MySQL / PostgreSQL / Redis / MongoDB / 达梦等 100+ 数据库，免装 Java、无内嵌浏览器、内置 AI 助手自动写 SQL + 安全检查；Claude Code / Cursor 等编码 Agent 可直接通过其连接查询数据。"
resource: "https://github.com/t8y2/dbx"
tags: "[database-client, gui, ai-sql, open-source, lightweight]"
timestamp: "2026-10-03T00:00:00Z"
---

# dbx

## 它是什么

[dbx](https://github.com/t8y2/dbx) 是 **t8y2** 出品的轻量开源数据库客户端——**仅 25 MB** 安装包，覆盖 **100+ 种数据库**（MySQL / PostgreSQL / Redis / MongoDB / 达梦等），免 Java、免浏览器内核，开箱即用。

## 为什么用它 / 适合什么场景

- **告别 DBeaver 启动慢、Navicat 收费**：25 MB 安装包、几秒启动。
- **国产数据库支持**：达梦等国产库直接连，不必切客户端。
- **AI 写 SQL**：选中表 → 用大白话说要查什么 → AI 自动写 SQL + 执行前安全检查。
- **给编码 Agent 用**：Claude Code / Cursor 等可通过 dbx 配好的连接查数据，权限分「只读 / 可改 / 高风险」三档。
- **统一多类型数据源**：Kafka、RabbitMQ 这类消息队列也有控制台。

## 关键能力

| 能力 | 说明 |
|------|------|
| 安装包大小 | 25 MB |
| 数据库支持 | 100+ 种（MySQL / PG / Redis / Mongo / 达梦…） |
| 启动 | 无需 Java / 无内嵌浏览器 |
| AI SQL 助手 | 自然语言 → SQL + 执行前安全检查 |
| 编码 Agent 接入 | 复用 dbx 连接，权限分三档 |
| 平台 | macOS / Windows / Linux + Docker |
| 导入 | 兼容 DBeaver / Navicat 连接配置 |

## 参考链接

- 项目链接：<https://github.com/t8y2/dbx>

## 相关概念

- [SiphonDB](./tool-siphondb.md) — 同类跨平台桌面数据库 GUI
- [Tusk DB Client](./tool-tusk-db-client.md) — 同类多数据库 GUI（Rust + GPUI 原生）
