---
type: Tool
title: "OKF Enrichment Agent"
description: "Google Cloud 发布的 OKF 参考实现：遍历 BigQuery 数据集，为每个表/视图起草 OKF 概念文档，再通过第二轮 LLM 爬取权威文档补充引用、schema 和 join 路径。"
resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf"
tags: "[okf, google-cloud, bigquery, agent, reference-implementation]"
timestamp: 2026-06-17T00:00:00Z
---

# OKF Enrichment Agent

## 是什么

OKF Enrichment Agent 是 Google Cloud 随 OKF v0.1 一起发布的**参考生产者实现**（reference producer）。它的作用是将 BigQuery 中的数据集批量转化为 OKF 概念文件。

## 工作流程

### 第一轮：草案生成

1. 遍历目标 BigQuery 数据集中的所有表（table）和视图（view）
2. 为每个表/视图生成一个 OKF 概念文档，包含：
   - `type`：`BigQuery Table` 或 `BigQuery View`
   - `title`：表名
   - `description`：一行描述（从 schema 推断）
   - `resource`：BigQuery 控制台链接
   - `tags`：数据集相关的标签

### 第二轮： enrichment（增强）

3. 运行第二轮 LLM pass，爬取权威文档（data catalog、dbt docs、团队 runbook 等）
4. 为每个概念补充：
   - 列级 schema 说明
   - 表间 join 路径
   - 外部引用来源（citation）

最终产出是一组符合 OKF v0.1 规范的 `.md` 文件，可直接加入任何 OKF bundle。Google 已用该 agent 跑通三套公开数据集作为样例——见 [OKF 参考示例 Bundles](./tool-okf-sample-bundles.md)。

## 设计意图

这是一个**证明概念**（proof of concept），不是为了限定生产者必须用特定框架：

- 展示了一种可能的「元数据 → OKF」的自动化路径
- 任何数据源（不限于 BigQuery）都可以参考这个模式写自己的 producer
- 格式本身不要求 SDK，enrichment agent 的代码只是参考，不是规范的一部分

## 相关概念

- [Open Knowledge Format (OKF)](./term-okf.md) —— 本 agent 的产出目标格式
- [LLM Wiki 模式](./term-llm-wiki.md) —— 启发了 OKF 的理念基础
- [OKF Static HTML Visualizer](./tool-okf-static-html-visualizer.md) —— 配套的参考消费者实现
