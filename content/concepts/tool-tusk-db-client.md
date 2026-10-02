---
type: "Tool"
title: "Tusk（alpcanaydin/tusk：Rust 写的原生多数据库客户端）"
description: "alpcanaydin 出品的 Rust + GPUI 原生多数据库客户端，替代 TablePlus 这类 Electron 桌面工具：连 20 种数据库（Postgres/MySQL/SQLite/Snowflake/BigQuery/Redis 等），几百万行表靠虚拟化 + GPU 渲染。"
resource: "https://github.com/alpcanaydin/tusk"
tags: "[database, client, rust, gpui, native, tableplus-alternative, multi-database, gpu-rendering]"
timestamp: "2026-10-02T04:55:00Z"
---

# Tusk（alpcanaydin/tusk：Rust 写的原生多数据库客户端）

## 它是什么

[Tusk](https://github.com/alpcanaydin/tusk) 是 alpcanaydin 出品的**原生多数据库客户端**，用 Rust + GPUI 写，**没有 Electron 也没有 WebView**——几百万行的表靠虚拟化 + GPU 渲染顶住。可连接 **20 种数据库引擎**，定位 TablePlus / DBeaver 的轻量替代。

## 为什么用它 / 适合什么场景

| 场景 | Tusk 的优势 |
|------|-------------|
| 多数据库混合栈 | 一套客户端通吃 Postgres / MySQL / ClickHouse / Snowflake / BigQuery 等 |
| 大表浏览 | 几百万行表不卡（虚拟化 + GPU 渲染） |
| 不想用 Electron 工具 | 原生 Rust，体积小、启动快、内存占用低 |
| 连接管理复杂 | 分组 / 标签 / SSH 隧道 / 从 TablePlus / Docker Compose / URL 导入 |
| 远程 SSH 调试 | 内置 SSH 隧道，连私有网络数据库无需额外工具 |

## 支持的 20 种数据库

| OLTP | OLAP | 缓存 / NoSQL |
|------|------|--------------|
| PostgreSQL、MySQL、SQLite、SQL Server、Oracle、SQL Anywhere | ClickHouse、Snowflake、BigQuery、DuckDB | Redis、MongoDB、Cassandra、DynamoDB、Elasticsearch、InfluxDB |
| 文档 / 图 | 时序 / 其他 |
| Neo4j、ArangoDB、CouchDB | TimescaleDB、Prometheus（HTTP） |

> 不同 build 可能少一两种，以仓库 README 为准。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生 Rust | 启动快、体积小、内存占用低 |
| GPU 渲染 | 大表不卡 |
| 虚拟滚动 | 几百万行只渲染可视区 |
| 连接分组 / 标签 | 多项目管理连接 |
| SSH 隧道 | 内置，连私有 DB |
| 导入 | TablePlus / Docker Compose / URL |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105883222114709876>
- 项目链接：<https://github.com/alpcanaydin/tusk>

## 相关概念

- [GPUI 组件](./tool-gpui-component.md) — Tusk 用的 UI 框架，Zed 编辑器同款
- [Zed](#) — 同为 GPUI 出品的代码编辑器，本仓库目前未收录
- [TablePlus](#) — Tusk 替代对象，本仓库目前未收录
