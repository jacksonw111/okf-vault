---
type: "Tool"
title: "Windshift（单二进制自托管项目管理工具）"
description: "团队想自托管项目管理工具又不想在功能上做减法——Windshift 用 Go 写后端 + Svelte 写前端，编译完只剩一个可执行文件，默认落 SQLite，要换 PostgreSQL 也行。"
resource: "https://github.com/Windshiftapp/core"
tags: "[project-management, self-hosted, single-binary, golang, svelte, sqlite, postgresql, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# Windshift（单二进制自托管项目管理工具）

## 它是什么

[Windshift](https://github.com/Windshiftapp/core) 是一个**自托管的项目管理工具**——目标是把「功能完整」和「部署极简」同时做到位：

- **后端**：Go 单二进制
- **前端**：Svelte，编译进同一份二进制
- **数据库**：默认 SQLite（开箱即用），要换 PostgreSQL 也支持
- **部署**：下载 → 运行 → 完事，不需要 Docker / nginx / 反代配置

## 为什么用它 / 适合什么场景

- 团队 5–50 人，希望**自己掌控**任务 / 迭代 / 文档数据，不想继续给 Jira / Linear / Asana 按席位付费。
- 不想养一套 Docker Compose / 反代 / 备份 / 升级脚本——单二进制 + SQLite 一次启动就是终态。
- 既要传统 PM 工具的「完整功能」（任务 / 看板 / 迭代 / 角色 / 权限），又不希望工具商 SaaS 化后悄悄改条款。
- 之后业务长大、想迁到 PostgreSQL，可以**原地升级**而不必换工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 后端 | Go（编译为单二进制） |
| 前端 | Svelte（同样打进二进制） |
| 默认数据库 | SQLite（零依赖） |
| 可切换数据库 | PostgreSQL（业务增长后可平滑迁移） |
| 部署形态 | 单文件 + 单命令启动 |
| 私有 | 完全自托管，数据不出本机 |

## 媒体

![](https://pbs.twimg.com/media/HTBhsIRaMAAD_IM.jpg)

## 相关概念

- [self-hosted（自托管）](./term-self-hosted.md) — 数据可控 / 长期低成本 / 可深度定制的部署形态，Windshift 是典型代表
- [OpenMuse](./tool-openmuse.md) — 同类「自托管 + 单二进制 / 单容器」的轻量任务执行台
