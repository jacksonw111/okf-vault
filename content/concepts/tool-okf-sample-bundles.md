---
type: Tool
title: OKF 参考示例 Bundles
description: 随 OKF v0.1 一起发布的三套可浏览的样例 bundle，由 OKF Enrichment Agent 从 BigQuery 公共数据集生成，作为「符合 OKF 规范」的真实样本——GA4 e-commerce、Stack Overflow、Bitcoin public datasets。
resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
tags: [okf, google-cloud, bigquery, sample-bundle, reference-implementation]
timestamp: 2026-06-17T00:00:00Z
---

# OKF 参考示例 Bundles

## 是什么

随 OKF v0.1 规范一起，Google Cloud 在官方仓库提交了三套**已生成的、符合规范的 OKF bundle**。它们不是教程，是用 [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) 跑真实 BigQuery 公共数据集后产出的活样本（living examples of conformant OKF）。

| Bundle | 数据源 | 用途 / 特色 |
|--------|--------|-------------|
| **GA4 e-commerce** | [Google Analytics 4 BigQuery 导出](https://developers.google.com/analytics/bigquery/web-ecommerce-demo-dataset) | 电商事件流的标准分析场景 |
| **Stack Overflow** | [`bigquery-public-data.stackoverflow`](https://console.cloud.google.com/bigquery?ws=!1m4!1m3!3m2!1sbigquery-public-data!2sstackoverflow) | 问答社区的复杂 schema + join 路径 |
| **Bitcoin public datasets** | [BigQuery 上的区块链数据集](https://cloud.google.com/blog/topics/public-datasets/bitcoin-in-bigquery-blockchain-analytics-on-public-data) | 时序/链式数据 + 大量衍生指标 |

## 价值定位

> 这三套 bundle 不是「示例文件」，而是**「规范长这样」的活证明**。

- 任何想写自己 producer 的人，可以直接打开看 OKF 文档该长什么样——表 schema、join 路径、citation、tags 怎么写
- 想做视觉/功能验证的消费者开发者，可以拿这三套做集成测试
- 规范的演进方向也会先在这三套 bundle 上试，再考虑是否推广

## 设计意图

这是「**proof of concept**」的另一半——Enrichment Agent 证明生产端怎么写，这三套 bundle 证明成品长什么样。OKF 只规定**最小互操作面**（最小意见的 frontmatter、Markdown 链接、文件名约定），具体文档的章节、表格、字段如何展开由生产者自由决定，三套样例展示了在真实数据上展开的多种风格。

## 相关概念

- [Open Knowledge Format (OKF)](./term-okf.md) —— 本样例遵守的规范
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) —— 产出本样例的参考生产者
- [OKF Static HTML Visualizer](./tool-okf-static-html-visualizer.md) —— 浏览本样例的参考消费者
