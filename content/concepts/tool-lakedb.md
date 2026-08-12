---
type: "Tool"
title: "LakeDB"
description: "本地优先、覆盖 MySQL/MariaDB/SQLite 的桌面数据库客户端，把可审查的 AI（QuerIA）嵌入普通 SQL 工作流；生成的 SQL 永远可见、执行前必须显式批准，AI 不接触凭据和数据。"
resource: "https://github.com/DavLagoHern/LakeDB"
tags: ["database", "desktop", "local-first", "sql", "ai-assistant", "audit", "mysql", "sqlite"]
timestamp: "2026-08-12T01:26:00Z"
---

# LakeDB

[LakeDB](https://github.com/DavLagoHern/LakeDB) 是一个本地优先的桌面数据库客户端，覆盖 MySQL / MariaDB / SQLite，把可审查的 AI 助手 **QuerIA** 嵌入普通 SQL 工作流。

## 它是什么

桌面端数据库工具，对常见关系型数据库提供统一界面。AI 能力（QuerIA）作为"助手"挂在 SQL 工作流旁，但它只**生成 SQL**，生成的语句全程可见、用户执行前必须显式批准，AI 自身不直接连数据库、不接触凭据和原始数据。

## 为什么用它 / 适合什么场景

- **审计友好**：AI 出的 SQL 永远先让用户看，敏感生产库也能放心让 AI 提议。
- **AI 与数据隔离**：凭据留在本地、查询经用户批准，AI 拿不到执行权。
- **本地优先**：桌面应用、无云依赖、数据不出本机。
- **多数据库一口**：MySQL / MariaDB / SQLite 同界面。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多数据库支持 | MySQL / MariaDB / SQLite |
| AI SQL 生成 | QuerIA 助手把自然语言翻译成 SQL |
| 可审查工作流 | AI 生成的 SQL 在执行前对用户可见、需显式批准 |
| 凭据隔离 | AI 不接触数据库凭据与原始数据 |
| 本地优先 | 桌面应用，数据不外发 |

## 媒体

![](https://pbs.twimg.com/media/HPXtFWjaUAA0b-7.jpg)

## 参考链接

- [项目仓库](https://github.com/DavLagoHern/LakeDB)

## 相关概念

- [Postcat](./tool-postcat.md) — 终端 HTTP 调试 TUI，与 LakeDB 都强调「人先审、工具后做」的审计工作流
- [QuerIA](#) — LakeDB 内置的 AI SQL 助手（无独立资料页）