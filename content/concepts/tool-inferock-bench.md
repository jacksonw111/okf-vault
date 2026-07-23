---
type: "Tool"
title: "Inferock Bench（LLM API 本地成本代理）"
description: "inferock/inferock-bench，在本地跑一个代理，挡住 OpenAI / Anthropic / Gemini 等 LLM API 的调用流量，独立记录每次调用实际花多少钱、哪些调用失败、哪些失败还被收了钱。"
resource: "https://github.com/inferock/inferock-bench"
tags: "[llm, api-proxy, cost-tracking, observability, billing]"
timestamp: "2026-07-23T04:20:00Z"
---

# Inferock Bench（LLM API 本地成本代理）

## 它是什么

[`inferock/inferock-bench`](https://github.com/inferock/inferock-bench) 是个**本地代理**，把所有 LLM API（OpenAI / Anthropic / Gemini 等）的请求流量「拦在门口」，独立记账：

- **实际花了多少钱**（按 token + 价格表）
- **哪些调用失败**
- **哪些失败还被收了钱**（部分上游对失败也收费）

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地代理 | 在用户机器上跑，拦 API 请求 |
| 多供应商 | OpenAI / Anthropic / Gemini 等 |
| 成本记录 | 每次调用的实际费用 |
| 失败跟踪 | 失败 vs 成功的请求分开记 |
| 失败收费识别 | 标记「被错误收费」的请求 |

## 为什么用它

- **账单核对**：供应商给的账单 vs 自己记录对比，避免被错收费
- **失败损失可见**：识别哪些失败还收了钱，便于维权
- **成本归因**：把成本拆到项目 / 团队 / 用例
- **隐私**：本地代理不上传任何调用内容

## 适用场景

- 多供应商管理：同时用 OpenAI + Anthropic + Gemini 的团队
- 自托管 LLM 应用的生产环境
- 任何「账单焦虑」的 LLM 重度用户
- 怀疑供应商账单有误的开发者

## 媒体

![](https://pbs.twimg.com/media/HNzO1YUbYAAArRp.jpg)

## 相关概念

- [Frugon](./tool-frugon.md) — 同类「LLM 费用分析器」，但吃 OpenAI 格式 JSONL 调用日志回放
- [Token Usage Insights](./tool-token-usage-insights.md) — 读本地日志做 Token 战情室 + Session 还原
- [AI Meter](./tool-ai-meter.md) — macOS 菜单栏显示编码 Agent 剩余预算 / 重置日期
- [AI Usage Dashboard](./tool-ai-usage-dashboard.md) — 类似「本地化用量仪表盘」
- [LLM Fingerprint Detector](./tool-llm-fingerprint-detector.md) — 验证 API 实际跑的模型是否与宣传一致

## 原始链接

- [项目仓库](https://github.com/inferock/inferock-bench)