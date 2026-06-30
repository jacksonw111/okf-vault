---
type: Tool
title: "liangmai-sdk（良买金融数据 Python SDK）"
description: "企业级金融数据平台 Python SDK，封装 105 个金融数据 API，覆盖 A 股 / 港股 / 基金 / 指数 / 龙虎榜 / 游资 / 早盘竞价等全市场数据，为量化交易和金融分析提供底层数据支撑。"
resource: "https://github.com/liangmai-sdk/liangmai"
tags: "[finance, sdk, python, stock, quant, china-market]"
timestamp: "2026-06-30T15:30:00Z"
---

# liangmai-sdk（良买金融数据 Python SDK）

## 它是什么

liangmai（良买）是一个面向企业级金融数据平台的 Python SDK，封装 105 个金融数据 API，覆盖 A 股、港股、基金、指数、龙虎榜、游资、早盘竞价等全市场数据，为量化交易和金融分析提供底层数据支撑。

## 关键能力

| 数据域 | 说明 |
|--------|------|
| A 股 | 行情、财务、公告、股本结构等 |
| 港股 | 港股全市场行情与基本面 |
| 基金 | 公募 / 私募基金数据 |
| 指数 | 沪深 / 国际指数 |
| 龙虎榜 | 营业部、机构席位动向 |
| 游资 | 短线游资跟踪 |
| 早盘竞价 | 集合竞价数据 |
| 数据 API 总数 | 105 个 |

## 适用场景

- 量化交易策略研究 / 回测的数据采集层。
- 金融分析应用（选股器、行业雷达、舆情监控等）的后端数据源。
- 把分散的金融数据源（Wind / 同花顺 / 聚宽等）统一到一套 Python 接口。

## 相关概念

- [a-stock-data](./tool-a-stock-data.md) — A 股全栈数据 Skill（13 源 / 28 端点）
- [global-stock-data](./tool-global-stock-data.md) — 美港股全栈数据 Skill
- [Finnhub](./tool-finnhub-api.md) — 美股 REST API（免费层 60 req/min）
- [chinese-buy-us-stock-guide](./tool-chinese-buy-us-stock-guide.md) — 大陆投资者美股实操指南

## 参考链接

- 项目链接：<https://github.com/liangmai-sdk/liangmai>