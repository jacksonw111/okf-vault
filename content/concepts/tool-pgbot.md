---
type: Tool
title: "pgbot (pgrundev/pgbot)"
description: "PostgreSQL 只读健康诊断 CLI：读 Postgres 自带统计视图，生成带健康评分 + 历次变化对比的诊断报告，DBA 与 AI 代理可直接消费"
resource: "https://github.com/pgrundev/pgbot"
tags: [postgresql, database, diagnostics, dba, cli, go]
timestamp: "2026-08-18T12:00:00Z"
---

# pgbot (pgrundev/pgbot)

## 它是什么
`pgrundev/pgbot` 是一个 Go 写的 **PostgreSQL 只读健康诊断** 静态二进制：以只读连接连上数据库，读 Postgres 自带的统计视图（pg_stat_* 等），输出按**问题严重度排序**的健康报告，并与上次运行结果对比变化，**DBA 与 AI 代理都可直接消费**。

## 为什么用它 / 适合什么场景
- DBA 想快速给一个 Postgres 实例做体检，又不想写一堆 ad-hoc SQL。
- 让 AI 编码 agent / 运维 agent 拥有一个「结构化、可机读」的 Postgres 健康诊断信号源。
- 想做定期巡检：pgbot 跑完存报告，下次跑还能对比上次，定位退化项。

## 关键能力
| 能力 | 说明 |
|------|------|
| 只读连接 | 不写库、不动 schema，零风险接入生产 |
| 统计视图直读 | 直接消费 Postgres 自带的 `pg_stat_*` 等视图 |
| 健康评分 | 输出总体评分 + 严重度排序的诊断项 |
| 历次对比 | 与上一次结果对比，定位恶化项 |
| 静态二进制 | Go 编译产物，单文件、无运行时依赖 |
| AI 友好 | 输出结构化，可被 agent 直接消费 |

## 媒体
- ![](https://pbs.twimg.com/media/HP0SYhQbIAAmezL.jpg)

## 相关概念
- [项目链接](https://github.com/pgrundev/pgbot) — 仓库地址
