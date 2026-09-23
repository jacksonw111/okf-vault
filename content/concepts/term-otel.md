---
type: "Term"
title: "OpenTelemetry（OTel）"
description: "CNCF 旗下的可观测性开放标准——统一 traces / metrics / logs 的数据模型与采集协议，被作为 LLM Agent telemetry 的事实数据模型底座。"
resource: "https://opentelemetry.io"
tags: "[observability, tracing, cncf, telemetry, otel]"
timestamp: "2026-09-23T22:00:00Z"
---

# OpenTelemetry（OTel）

## 它是什么

**OpenTelemetry（OTel）** 是 CNCF（Cloud Native Computing Foundation）旗下的**可观测性开放标准**：通过统一的数据模型（traces / metrics / logs）和一次实现，可在不绑定厂商的前提下，把遥测数据发给任意后端。

- **Traces**：分布式请求链路，跨服务追踪一个请求的全过程。
- **Metrics**：数值型时序数据（请求量、延迟、错误率）。
- **Logs**：离散事件记录。

厂商中立（语言 SDK + OTLP 协议 + Collector），输出可同时打到 Jaeger / Prometheus / Splunk / Datadog / Elastic / CloudWatch 等后端。

## 为什么重要

- **不绑死厂商**：换后端不必改应用代码——OTel SDK → OTLP → Collector → 多路分发。
- **跨语言一致**：同一份语义约定在 Go / Java / Python / Rust / JS 等语言里行为一致。
- **AI / Agent 时代的延伸**：LLM Agent 的 prompt / tool call / 审批 / token 用量天然适合 trace 模型——已有 Agent Beacon、OpenLLMetry 等把 OTel span 当作 Agent telemetry 的统一数据模型。

## 与传统打点的差异

| 维度 | OpenTelemetry | 传统日志/打点 |
|------|---------------|---------------|
| 数据模型 | 统一的 trace / metric / log 语义 | 各系统私有 schema |
| 厂商绑定 | 一次采集多路分发 | 通常绑死单一后端 |
| 上下文传播 | W3C TraceContext / Baggage 标准 | 各家自实现 |
| Agent 适配 | OpenLLMetry / AgentOps 等直接生成 OTel span | 需要从零定义 |

## 相关概念

- [Agent Beacon](tool-agent-beacon.md) — 跨 Agent / Harness 的可观测性中台，telemetry 数据模型即基于 OTel
