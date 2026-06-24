---
type: "Tool"
title: "DataBuff（AI Native OpenTelemetry APM）"
description: "国产开源 AI Native OpenTelemetry APM 平台，原生支持 OpenTelemetry 协议，提供分布式链路追踪、指标监控、自动拓扑图等 APM 能力，并集成 AI 智能分析能力。"
resource: "https://github.com/databufflabs/databuff"
tags: [observability, apm, opentelemetry, ai, monitoring]
timestamp: "2026-06-24T15:30:00Z"
---

# DataBuff（AI Native OpenTelemetry APM）

## 它是什么

[`databufflabs/databuff`](https://github.com/databufflabs/databuff) 是一个**国产开源 AI Native OpenTelemetry APM 平台**。原生支持 [OpenTelemetry](https://opentelemetry.io/) 协议（OTel），把 APM 该有的能力都做了：

- 分布式链路追踪（distributed tracing）
- 指标监控（metrics）
- 自动拓扑图（topology auto-discovery）

并且**额外多了 AI 能力**——用 AI 智能分析可观测数据，自动识别异常、关联事件、定位根因。

## 为什么用它 / 适合什么场景

- 想自建 APM、又不想被 vendor lock-in 绑死（OpenTelemetry 协议标准、可迁移）；
- 团队是 OpenTelemetry 派（Jaeger / Tempo / OTel Collector 生态），但想加 AI 智能分析层；
- 国产 / 国内部署友好。

## 关键能力

| 能力 | 说明 |
|---|---|
| OpenTelemetry 原生 | 协议标准、跨语言、可与 OTel Collector 互通 |
| 分布式链路追踪 | 调用链追踪 / 性能瓶颈定位 |
| 指标监控 | 系统 / 应用 / 业务多维指标 |
| 自动拓扑图 | 服务依赖自动发现 + 可视化 |
| AI 智能分析 | 异常检测 / 事件关联 / 根因定位 |

## 媒体 / 参考链接

![截图](https://pbs.twimg.com/media/HLjB0ASbIAAx6Ii.jpg)

- [项目链接](https://github.com/databufflabs/databuff)

## 相关概念

- [OPG](tool-opg-backend.md) — 一人公司多 app 后端控制面，可作为本 APM 的被观测对象
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker + Kamal，可作为本 APM 的部署形态
- [云端 Agent 基础设施的设计教训](note-cloud-agent-infrastructure.md) — 云端 Agent 可观测性设计教训，本工具可作为其实践工具
