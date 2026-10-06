---
type: "Tool"
title: "Leviathan（Agent 大日志查询引擎）"
description: "elstongun 开源的 Rust 单文件二进制——把 JSONL / JSON / CSV / TSV / SQLite / psql / duckdb 等数据源建一个 FTS5 索引（输出 SQLite 文件），让 Agent 查历史记录时不用把整份数据读进上下文；1M 条 678 MB 数据中位 436 token（grep 是 107122 token），top5 命中率 99.0%。"
resource: "https://github.com/elstongun/leviathan"
tags: "[agent, search, fts5, sqlite, rust, rag]"
timestamp: "2026-10-06T22:51:00Z"
---

# Leviathan（Agent 大日志查询引擎）

## 它是什么

**Leviathan** 是 elstongun 出品的**单文件 Rust 二进制**——针对 Agent 场景设计：当 Agent 要查「几百万条 JSONL / SQLite 记录」中的某条时，**不用把整份历史读进上下文**，而是把数据建一个 FTS5 索引（输出一个 SQLite 文件），按提问返回带引用的卡片。

## 为什么用它 / 适合什么场景

- **Agent 上下文省**：grep 把 1M 条记录的命中行全塞给 LLM（10 万 token），Leviathan 只给几张带引用的卡片（中位 436 token）
- **多源支持**：JSONL / JSON / CSV / TSV / SQLite，还能接 `psql` / `duckdb` 等 CLI 的导出
- **单文件部署**：编译产物 ≈ 几十 MB，丢 PATH 就能跑

## 关键能力

| 能力 | 说明 |
|------|------|
| FTS5 索引 | 输出一个 SQLite 文件，含全文索引 |
| 多数据源 | JSONL / JSON / CSV / TSV / SQLite / CLI 导出 |
| Agent 友好 | 查询返回 3-5 张带引用的卡片 |
| 性能 | 1M 条 678 MB 数据中位 436 token；top5 命中率 99.0%；rank 1 98.5%；中位 33 ms |
| 单二进制 | Rust 编译产物，无运行时依赖 |

## 参考链接

- 项目链接：<https://github.com/elstongun/leviathan>

## 相关概念

- [RAG（检索增强生成）](./term-rag.md) — 同属「检索而非全塞」思路
- [AI Coding Agent](./term-ai-coding-agent.md) — 主要消费方
