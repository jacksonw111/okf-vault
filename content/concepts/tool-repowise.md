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
| 服务对象 | AI 编码代理（Claude Code / Codex / Cursor 等） |
| 节省 | 上下文 token + 时间 |
| 索引生命周期 | 一次构建、长期查询 |
| MCP 工具 | 10 个按任务设计的工具（含「改了这个文件会影响谁」引用式回答） |
| 基准 | django 仓库 43 题对比：Agent 工具调用从 7.2 → 3.8 次，输出少 31.6%（样本 / 方法 / 输掉的行公开在仓库） |
| 风险评估 | 改代码前 0–10 风险分（按仓库近期提交分布排），列被波及调用方 / 应跑测试 / 历史上常一起改的文件是否漏 |
| 代码健康 | 51 个检测器按「缺陷风险 / 可维护性 / 性能」分开打分，给可执行重构方案 |
| 语言覆盖 | 26 种 |
| 隐私 | 索引留在本机，0 API Key；建图 / 风险 / 健康度 / 死代码 都不调用大模型 |
| 部署 | 一条命令装好；另有免费 PR 机器人 |

## 相关概念
- [Claude Code](tool-claude-code.md) — 主要服务对象之一
- [Codex Standard DevFlow](playbook-codex-standard-devflow.md) — Codex 工作流；repowise 能作为其代码库准备阶段的工具
- [OKF Enrichment Agent](tool-okf-enrichment-agent.md) — OKF 富化 agent 也是「索引 + 检索」模式；repowise 的代码索引思路与之同构
- [understand-anything](tool-understand-anything.md) — 同样把代码库变成可探索知识图谱的同类工具

## 媒体
- 架构示意图：<https://pbs.twimg.com/media/HPkUyjkbkAAWyg5.png>
- 风险分 + 代码健康演示：<https://pbs.twimg.com/media/HS0AeAwbwAEckyU.jpg>

## 项目链接
- 项目主页：<https://github.com/repowise-dev/repowise>