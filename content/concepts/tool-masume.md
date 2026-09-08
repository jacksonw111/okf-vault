---
type: Tool
title: "masume"
description: "Go 写的终端多引擎数据库客户端：支持 PostgreSQL/MySQL/SQLite/MongoDB 与其上托管服务，左侧对象树 + 完整表/索引/约束/DDL/查询计划/ER 图；并能把连接配置开放给 AI agent 调用。"
resource: "https://github.com/turanmahmudov/masume"
tags: [database, tui, postgresql, mysql, sqlite, mongodb, ai-agent]
timestamp: "2026-09-08T00:00:00Z"
---

# masume

## 它是什么
masume 是 turanmahmudov 用 Go 写的**终端多引擎数据库客户端**：一把梭支持 PostgreSQL、MySQL、SQLite、MongoDB，以及建立在它们之上的托管服务（PaaS / BaaS）。左侧对象树列库对象，表视图里数据、列、索引、约束、DDL、查询计划、ER 图全有；SQL 编辑器自带高亮与目录补全，跑之前先本地校验、服务端能查也查一遍；结果网格能排序过滤、沿外键跳行、冻结列；改行先暂存，复核 SQL 才落库。

## 为什么用它 / 适合什么场景
- 想在一个 TUI 里同时管 Postgres/MySQL/SQLite/Mongo，不想开多个 GUI。
- 想给 AI agent 安全地"开放指定连接配置"——agent 看得到但写仍受规则约束。
- 偏好键盘操作 + 可审 SQL 的工作流。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多引擎 | PG / MySQL / SQLite / Mongo + 其托管服务 |
| 完整对象浏览 | 列 / 索引 / 约束 / DDL / 计划 / ER 图 |
| SQL 编辑 | 高亮 + 目录补全 + 本地/服务端双重校验 |
| 安全写 | 改行先暂存，复核后才落库 |
| Agent 友好 | 可向 agent 开放指定连接配置 |

## 参考
- 原始链接：<https://github.com/turanmahmudov/masume>

## 媒体
- ![](https://pbs.twimg.com/media/HRlWQdRbsAABe8w.jpg)

## 相关概念
- [pgcli](https://www.pgcli.com/) — PG 命令行增强版
- [DBeaver](https://dbeaver.io/) — 跨引擎 GUI 客户端
