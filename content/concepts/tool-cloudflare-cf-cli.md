---
type: "Tool"
title: "Cloudflare cf CLI（cloudflare/cf：统一 Cloudflare API 的 Agentic CLI）"
description: "Cloudflare 官方出品的统一 CLI：面向公开 Cloudflare API 和 Workers 项目，大部分命令由描述 API 的 OpenAPI schema 自动生成，数量超过 2900 条，按 cf <product> [group] <operation> 组织——专为 coding agent 设计，可直接驱动完整 Cloudflare 平台。"
resource: "https://github.com/cloudflare/cf"
tags: "[cloudflare, cli, openapi, agentic, workers, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# Cloudflare cf CLI

## 它是什么

[Cloudflare cf CLI](https://github.com/cloudflare/cf) 是 **Cloudflare 官方**出品的**统一 CLI**——面向公开 Cloudflare API 和 Workers 项目：

- **大部分命令由 OpenAPI schema 自动生成**
- **2900+ 条命令**，按 `cf <product> [group] <operation>` 组织
- **专为 coding agent 设计**：可直接被 Claude Code / Codex / Cursor 等驱动

## 为什么用它 / 适合什么场景

- **一个 CLI 覆盖整个 Cloudflare 平台**：不必装 wrangler + r2 + d1 + kv … 多个工具。
- **Schema-driven**：Cloudflare 加新 API 时，CLI 自动更新。
- **Agent 友好**：Claude Code 等可以直接 `cf <product> ...` 调所有 Cloudflare 资源。
- **典型场景**：IaC / 自动化 / Agent 编排 / 一次性任务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 命令数 | 2900+ |
| 生成方式 | OpenAPI schema 自动生成 |
| 命名 | `cf <product> [group] <operation>` |
| 范围 | 公开 Cloudflare API + Workers |
| Agent 支持 | 原生设计 |

## 参考链接

- 项目链接：<https://github.com/cloudflare/cf>

## 相关概念

- [Cloudflare Workers](./tool-cloudflare-workers.md) — 部署目标
- [Cloudflare Clef](./tool-cloudflare-clef.md) — 同为 BirthdayWeek 发布
