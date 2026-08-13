---
type: Tool
title: "repowise"
description: "为 AI 编码代理预先建立一次代码库持久索引——代理无需每次从零 grep / 重读 / 再忘掉代码库，可直接查询该索引，节省上下文与时间。"
resource: "https://github.com/repowise-dev/repowise"
tags: "[ai-agent, codebase-index, retrieval, rag, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# repowise

## 它是什么
一个**代码库持久索引工具**，专为 AI 编码代理（Claude Code、Codex 等）设计：

> 让 AI 编码代理**不必每次从零 grep、重读、再忘掉代码库**，而是一次建索引、持续查询。

工作流：

1. 给定一个代码库，跑一次**索引构建**（解析、抽取、嵌入等）
2. AI 代理在后续会话里**直接查询该索引**（而不是每次重读文件）
3. 索引**持久化**，跨会话保留

## 为什么用它 / 适合什么场景
- AI 编码代理在大型代码库里频繁「瞎找」浪费上下文与延迟——索引一次长期受益。
- 想要 AI 代理对代码库有「长期记忆」，而非每次会话都重头熟悉。
- 想在多个 AI 工具之间共享同一份代码库索引。

## 关键能力
| 能力 | 说明 |
|------|------|
| 核心机制 | 代码库持久索引 |
| 服务对象 | AI 编码代理 |
| 节省 | 上下文 token + 时间 |
| 索引生命周期 | 一次构建、长期查询 |
| 适配 | Claude Code / Codex 等 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 主要服务对象之一
- [Codex Standard DevFlow](playbook-codex-standard-devflow.md) — Codex 工作流；repowise 能作为其代码库准备阶段的工具
- [OKF Enrichment Agent](tool-okf-enrichment-agent.md) — OKF 富化 agent 也是「索引 + 检索」模式；repowise 的代码索引思路与之同构

## 媒体
- 架构示意图：<https://pbs.twimg.com/media/HPkUyjkbkAAWyg5.png>

## 项目链接
- 项目主页：<https://github.com/repowise-dev/repowise>