---
type: "Tool"
title: "OpenObserve（Rust 写的开源可观测平台）"
description: "openobserve/openobserve：Rust 写的可观测平台，AGPL-3.0 协议，单文件部署几分钟跑起来。Parquet + S3 架构让存储成本降 140 倍，日志 / 指标 / 链路追踪 / 前端 RUM / LLM 监控全家桶，SQL 或 PromQL 直接查询，单二进制扛 TB 级数据。"
resource: "https://github.com/openobserve/openobserve"
tags: "[observability, rust, s3, parquet, logs, metrics, tracing, self-hosted]"
timestamp: "2026-09-15T04:20:00Z"
---

# OpenObserve（Rust 写的开源可观测平台）

## 它是什么

[OpenObserve](https://github.com/openobserve/openobserve) 是用 **Rust** 写的开源可观测平台，**AGPL-3.0** 协议，「专治那些贵到肉疼的日志工具」。**单文件部署**几分钟就能跑起来。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单二进制部署 | 几分钟上线 |
| 存储成本 -140× | Parquet + S3 架构 |
| 日志 | 完整日志接入与查询 |
| 指标 | Metrics 支持 |
| 链路追踪 | Distributed Tracing |
| 前端 RUM | Real User Monitoring |
| LLM 监控 | 专门的 LLM 推理 / 调用监控 |
| SQL 或 PromQL 查询 | 不学自研语法 |
| TB 级单二进制 | 单机扛 TB 数据，告别集群维护 |

## 与同类对比

| 维度 | 商业 ELK / Datadog | OpenObserve |
|------|-------------------|-------------|
| 协议 | 商业 | AGPL-3.0 开源 |
| 部署 | 集群 | 单二进制 |
| 存储 | 自带 / 贵 | Parquet + S3 |
| 查询 | 自研 / PromQL | SQL + PromQL |
| 成本 | 高 | 大幅下降 |

## 为什么用它

- 「**存储成本暴降 140 倍**」——这是用 Parquet 列存 + S3 对象存储替换传统倒排索引的结果。
- 「**全家桶打包**」让运维不必再拼 Prometheus + Loki + Tempo + Grafana + 自研 LLM 监控——**一套搞定**。
- 「**单二进制扛 TB**」对中小团队意义重大——**不必为了可观测性专门维护一个集群**。

## 适合谁

- 中小公司 / 创业团队：商业 ELK 太贵，想找替代品
- 自托管爱好者：想在自己机器上跑完整可观测栈
- SRE / 平台工程团队：想统一日志 / 指标 / 追踪 / RUM / LLM 监控
- 边缘 / 远程部署：单二进制对资源受限环境友好

## 媒体

![](https://pbs.twimg.com/media/HSFrYu0bAAAZR7P.png)

## 项目链接

- 仓库：<https://github.com/openobserve/openobserve>

## 相关概念

- [Self-Hosted（自托管）](term-self-hosted.md) — OpenObserve 是开源可观测平台的代表