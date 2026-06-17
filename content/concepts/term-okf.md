---
type: Term
title: Open Knowledge Format (OKF)
description: Google Cloud 于 2026-06-12 发布的开放规范，把「LLM-wiki」模式形式化为一种可移植、可互操作的格式：一个目录的 Markdown 文件 + YAML frontmatter，供不同生产者编写、不同 agent 消费，无需翻译。
resource: https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing
tags: [okf, knowledge, llm, spec]
timestamp: 2026-06-17T00:00:00Z
---

# Open Knowledge Format (OKF)

## 它解决什么问题

### 碎片化的上下文地形（Fragmented Context Landscape）

组织内部喂给 foundation model 的知识绝大多数是**内部知识**：表的 schema、业务对指标的定义、事故 runbook、两个系统之间的 join 路径、旧 API 的弃用通知……这些知识的「原子」散落在各种互不兼容的载体里：

- 各家元数据目录（带着自家 API）
- 第三方 Wiki / 共享盘
- 代码注释、docstring、notebook cell
- 几位资深工程师的脑子里

当一个 AI agent 要回答「怎么从我们的事件流算 weekly active users」时，它得从这些互不兼容的载体里拼装答案。每个 vendor 都自带一套 catalog、一套 SDK、一套知识图谱 schema，知识被锁在产生它的那一层里。结果就是：**每个 agent builder 都在从零重复同一个上下文拼装问题，每个 catalog vendor 都在重造同一个数据模型，知识本身被锁死。**

### 缺的不是一个服务，是一个格式

> 答案不是「又一个知识服务」。你需要一个**格式**——能产、能消费、跨系统跨组织跨工具迁移、和代码同仓、人和 agent 读同一份文件不需要翻译层。

OKF 正是按这个需求设计的：不是平台、不是 SDK、不是私有服务，是一个目录里一堆 Markdown + YAML frontmatter，可被任意生产者和消费者读写。

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
- [LLM Wiki 模式](./term-llm-wiki.md) —— OKF 的理念先驱
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) —— 参考生产者
- [OKF Static HTML Visualizer](./tool-okf-static-html-visualizer.md) —— 参考消费者
- [OKF 参考示例 Bundles](./tool-okf-sample-bundles.md) —— GA4 / Stack Overflow / Bitcoin 三套样例

## 来源

- 原文：Google Cloud Blog（见 `resource`），作者 Sam McVeety / Amir Hormati
- 规范灵感来自 Andrej Karpathy 的 [LLM-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
