---
type: "Tool"
title: "Cloudflare Forge（schema 优先 OpenAPI 代码生成框架）"
description: "Cloudflare 开源的 schema 优先 OpenAPI 代码生成与表面工具框架：把 OpenAPI 3.x 规范解析 + JSONPath 覆盖 + 生成带类型的 SDK / CLI / 运行时辅助 / 文档，用插件式架构统一 API 表面实现。"
resource: "https://github.com/cloudflare/forge"
tags: "[cloudflare, openapi, codegen, sdk, schema, plugin, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# Cloudflare Forge（schema 优先 OpenAPI 代码生成框架）

## 它是什么

[Forge](https://github.com/cloudflare/forge) 是 Cloudflare 开源的 schema 优先 OpenAPI 代码生成与表面工具框架：把 OpenAPI 3.x 规范解析、叠加 JSONPath 覆盖并生成带类型的 SDK、CLI、运行时辅助和文档，用插件式架构统一 API 的「表面实现」。

## 关键能力

| 能力 | 说明 |
|------|------|
| OpenAPI 3.x 解析 | 解析 OpenAPI 3.x 规范作为单一事实源 |
| JSONPath 覆盖 | 用 JSONPath 表达式在规范上叠加覆盖配置 |
| 多产物生成 | 带类型的 SDK、CLI、运行时辅助、文档 |
| 插件式架构 | 统一 API 表面实现，扩展能力强 |

## 它解决的问题

API 项目里同时维护 SDK、CLI、文档、运行时辅助很容易各自漂移：
- 字段定义不一致
- 文档和实际 SDK 不匹配
- 不同产物的类型定义不互通

Forge 让 OpenAPI 规范成为唯一事实源，所有产物从这里派生。

## 适合谁

- Cloudflare 生态项目需要统一 API 表面
- 给 OpenAPI 规范做类型安全的 SDK / CLI 生成
- 想要插件式扩展的 codegen 框架

## 原始链接

- 项目主页：<https://github.com/cloudflare/forge>

## 相关概念

- [Cloudflare Nimbus](./tool-cloudflare-nimbus.md) — Cloudflare 官方文档站生成框架，与 Forge 同属 Cloudflare 生态
- [Cloudflare Security Audit Skill](./tool-cloudflare-security-audit-skill.md) — Cloudflare 多阶段安全审计 Skill