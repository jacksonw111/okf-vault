---
type: Term
title: Open Knowledge Format (OKF)
description: Google Cloud 于 2026-06-12 发布的开放规范，把「LLM-wiki」模式形式化为一种可移植、可互操作的格式：一个目录的 Markdown 文件 + YAML frontmatter，供不同生产者编写、不同 agent 消费，无需翻译。
resource: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
tags: [okf, knowledge, llm, spec]
timestamp: 2026-06-12T00:00:00Z
---

# Open Knowledge Format (OKF)

## 它解决什么问题

组织内部的知识（表 schema、指标定义、事故 runbook、系统间 join 路径、API 弃用通知……）散落在各种互不兼容的系统里：元数据目录、Wiki、代码注释、几位老员工的脑子里。每次搭一个 AI agent，都要重新从零拼装这些上下文。

> 缺的不是「又一个知识服务」，而是一个**格式**：任何人都能产、任何人都能消费、能在系统/组织/工具间迁移、能和代码一起进版本控制、人和 agent 读同一份文件无需翻译层。

## 三句话定义

- **就是 Markdown** —— 任何编辑器可读、GitHub 可渲染、任何搜索工具可索引
- **就是文件** —— 可打包成 tar、放进 git 仓库、挂载到任何文件系统
- **就是 YAML frontmatter** —— 少量需要可查询的结构化字段：`type`、`title`、`description`、`resource`、`tags`、`timestamp`

## 三条设计原则

1. **最小意见** —— 对每个概念只强制要求一件事：`type` 字段。其余全部交给生产者自由发挥。
2. **生产者/消费者独立** —— 人手写的 bundle 可被 agent 消费；导出管道生成的 bundle 可被可视化器浏览；一个 LLM 合成的 bundle 可被另一个 LLM 查询。格式即契约，两端的工具各自可替换。
3. **是格式，不是平台** —— 不绑定任何云、数据库、模型厂商或 agent 框架。永远不会要求私有账号或 SDK 才能读写。

## 一个概念文件长这样

```
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?...
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema
| Column | Type | Description |
...

# Joins
Joined with [customers](/tables/customers.md) on `customer_id`.
```

## 相关概念

- [Obsidian](./tool-obsidian.md) —— 天然的 OKF 消费/编辑端
- [在 Obsidian 里开始用 OKF](./playbook-okf-obsidian-start.md)

## 来源

- 原文：Google Cloud Blog（见 `resource`），作者 Sam McVeety / Amir Hormati
- 规范灵感来自 Andrej Karpathy 的 [LLM-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
