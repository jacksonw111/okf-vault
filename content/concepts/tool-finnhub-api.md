---
type: "Tool"
title: "Finnhub 美股 API"
description: "免费层 60 req/min 的美股行情 / 财报 / 新闻 REST API，开发者自建美股数据栈的常用起点。"
resource: "https://finnhub.io/docs/api/introduction"
tags: [finance, api, stock-data, us-market]
timestamp: "2026-06-24T15:30:00Z"
---

# Finnhub 美股 API

## 它是什么

[finnhub.io](https://finnhub.io/docs/api/introduction) 提供覆盖美股行情、财报、公司基本面、新闻、加密货币、外汇等数据点的 REST API，免费层每分钟最多 **60 次请求**，对个人开发者 / 小型项目做轻量美股数据接入基本够用。

## 为什么用它 / 适合什么场景

- 不想花钱：免费层就能拿到核心行情 + 财报 + 新闻数据；
- 个人项目 / 副业做美股看板、研报聚合、行情监控、量化回测时常见的入门选择；
- 跨市场数据：美股 + 港股 + 欧股 + 外汇 + 加密一站式。

## 关键能力

| 能力 | 说明 |
|---|---|
| 实时报价 | 股票 / 外汇 / 加密 C 级实时价 |
| 历史 K 线 | 多周期 OHLCV |
| 财报日历 | EPS、营收披露时间表 |
| 公司新闻 | 按 symbol 拉新闻流 |
| 基本面 | 财务指标 / 估值 |
| WebSocket | 实时行情推送（付费） |

## 限制 / 注意

- 免费层 60 req/min，超过会 429；
- 实时 tick 需付费，免费通常延后 15 分钟；
- 同一 IP 多项目共用额度，建议自己跑一层缓存代理。

## 媒体 / 参考链接

![截图](https://pbs.twimg.com/media/HLfZdw0aIAAslHg.jpg)

- [项目链接](https://finnhub.io/docs/api/introduction)

## 相关概念

- [a-stock-data](tool-a-stock-data.md) — A 股全栈数据 Skill（13 源 / 28 端点），A 股侧的对应物
- [Mira](tool-mira.md) — Agent-native 投研工作台，多数据源协作场景
