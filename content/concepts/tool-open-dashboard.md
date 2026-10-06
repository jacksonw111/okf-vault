---
type: "Tool"
title: "Open Dashboard（自然语言 → SQL/TSX 数据看板）"
description: "simonliu-ai-product 开源——你给 Claude Code 一句「按月看营收、TOP 10 商品、按地区筛」，Agent 写出 `queries.sql` 与 `index.tsx`，框架负责渲染、**只读执行**与热更新；面向 LLM Agent 时代的轻量 BI。"
resource: "https://github.com/simonliu-ai-product/open-dashboard"
tags: "[dashboard, bi, llm, sql, claude-code, ai-coding-agent]"
timestamp: "2026-10-06T22:51:00Z"
---

# Open Dashboard（自然语言 → SQL/TSX 数据看板）

## 它是什么

**Open Dashboard** 是 simonliu-ai-product 开源的项目——你给 Claude Code 一句「按月看营收、TOP 10 商品、按地区筛」，Agent 自动写出 `queries.sql` 与 `index.tsx`，框架负责渲染、**只读执行**和热更新；面向 LLM Agent 时代的轻量 BI。

## 为什么用它 / 适合什么场景

- **自然语言生成看板**：业务人员用自然语言描述需求 → Agent 出 SQL + 渲染代码
- **只读执行**：框架强制只读 SQL，agent 写不出 `DROP` / `UPDATE`
- **热更新**：改完 SQL 立即重新出图，无需重新部署
- **LLM 友好**：与 Claude Code 原生协作

## 关键能力

| 能力 | 说明 |
|------|------|
| 自然语言 → SQL | Agent 写 `queries.sql` |
| 自动渲染 | 框架生成 `index.tsx` 渲染层 |
| 只读执行 | 强制 SELECT-only SQL，规避数据破坏 |
| 热更新 | 改 SQL 后立即重渲染 |
| Claude Code 集成 | 直接给 Agent 喂数据库连接 |

## 参考链接

- 项目链接：<https://github.com/simonliu-ai-product/open-dashboard>

## 相关概念

- [Claude Code](./term-claude-code.md) — 主要驱动力
- [RAG（检索增强生成）](./term-rag.md) — 思路接近「让模型查询而非写」
