---
type: Tool
title: "Microsoft Data Formulator（AI 驱动的数据分析可视化工作区）"
description: "微软开源的 AI 数据分析工具：把文件 / 数据库 / Databricks 等数据源放进同一可视化工作区，由 AI Agent 生成图表、跟踪分析上下文（Data Threads）、自定义图表主题样式，0.8 Beta 把「加载 → 提问 → 分支 → 回顾」整条分析流程串起来。"
resource: "https://github.com/microsoft/data-formulator"
tags: [data-analysis, visualization, ai-agent, microsoft, databricks, open-source]
timestamp: 2026-09-30T23:44:59Z
---

# Microsoft Data Formulator

## 它是什么

**Microsoft Data Formulator** 是微软开源的 AI 数据分析工具，目的是**让数据分析少折腾点**——把文件、数据库、Databricks 等数据源放进一个**可视化工作区**，再交给 **AI Agent** 自动生成图表、分析数据、寻找洞察。

它最实用的几个功能：

1. **AI 根据问题自动生成图表**
2. **Data Threads**：从当前分析继续分支提问，保留上下文
3. 图表支持**推荐、主题和样式自定义**
4. 从**数据加载、提问、回顾到分支**，整条分析流程都串起来了
5. 最新 **0.8 Beta** 进一步完善了整套工作流

适合「不想先折腾一堆数据处理代码、想直接用自然语言探索数据」的人。

## 为什么用它 / 适合什么场景

- 业务 / 产品分析需要快速出图，但不想在 SQL + Python + 可视化之间反复切换。
- Databricks / 数据库已经在线，希望同一界面里能引用多种数据源。
- 分析常常分叉追问，需要**保留上下文**（Data Threads）而不是每次从头开始。
- 希望让**非工程师**也能跟数据对话——自然语言提问即可。

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据源 | 文件 / 数据库 / Databricks 等 |
| 图表生成 | AI 根据自然语言问题自动生成 |
| 上下文 | Data Threads 分支追问 |
| 样式 | 推荐 / 主题 / 样式自定义 |
| 工作流 | 加载 → 提问 → 分支 → 回顾 串成一条线 |
| 版本 | 0.8 Beta |
| 出品方 | 微软 |

## 参考链接

- 仓库：<https://github.com/microsoft/data-formulator>

## 媒体

- ![](https://pbs.twimg.com/media/HTYpCFIbwAAp1xg.png)

## 相关概念

- [Databricks](https://databricks.com/) — 上游常见数据源（外部链接）
- [Databricks AI Functions](https://docs.databricks.com/) — 同类数据 → AI 的桥接思路（外部链接）
