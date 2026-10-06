---
type: "Tool"
title: "SpiceDB"
description: "AuthZed 出品的开源**权限数据库**——把 Google Zanzibar（Google Docs / Drive / YouTube 用的权限模型）以关系数据库形态开放出来，支持关系型权限检查（has / can / expand / lookup），是现代 SaaS / 文档协作场景的事实权限底座之一。"
resource: "https://github.com/authzed/spicedb"
tags: "[spicedb, zanzibar, authz, permissions, authzed]"
timestamp: "2026-10-06T22:51:00Z"
---

# SpiceDB

## 定义

**SpiceDB** 是 AuthZed 公司出品的开源**权限数据库（Permission Database）**——把 Google 内部用于 Docs / Drive / YouTube 的 **Zanzibar** 一致性全局权限模型以数据库形态开放出来。它提供 `has` / `can` / `expand` / `lookup` 等关系型权限 API，让 SaaS / 文档协作 / 多租户应用以「关系图 + 共享视图 + ACL」方式建模和检查权限。

## 要点

- **官网 / 仓库**：`https://github.com/authzed/spicedb`
- **底层模型**：Zanzibar 关系元组（subject × relation × object）+ 一致性全局视图
- **API 形态**：`CheckPermission` / `ExpandPermissionTree` / `LookupSubjects` / `WriteRelationships`
- **存储后端**：MySQL / PostgreSQL / CockroachDB / Spanner
- **典型场景**：SaaS 多租户权限、文档协作文档权限、文档库（Wiki / Notion-like）的可见性

## 相关概念

- [JevBox（文档库）](./tool-jevbox.md) — 使用 SpiceDB 做权限引擎的文档库
- [RAG](./term-rag.md) — 文档问答场景下 SpiceDB 也能做「按权限过滤可检索集合」
