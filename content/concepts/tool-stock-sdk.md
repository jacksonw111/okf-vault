---
type: Tool
title: "stock-sdk"
description: "stock-sdk 是给前端工程师用的浏览器端股票数据库:零依赖、A 股 / 港股 / 美股 / 公募基金实时行情 + K 线,自带 CLI 和 MCP server,可接 Cursor / Claude。"
resource: "https://github.com/chengzuopeng/stock-sdk"
tags: [stock-sdk, stock, a-stock, hk-stock, us-stock, mcp, sdk]
timestamp: "2026-07-04T15:00:00Z"
---

# stock-sdk

## 它是什么

`chengzuopeng/stock-sdk` 是一款「零依赖」的前端股票数据 SDK。它给浏览器 / Node 端提供 A 股、港股、美股和公募基金的实时行情 + K 线接口,无需自建后端、无需 Python 数据管道,直接 `npm i stock-sdk` 就能用。

![截图](https://pbs.twimg.com/media/HMTUnP3aYAEsk1V.jpg)

项目链接：<https://github.com/chengzuopeng/stock-sdk>

## 为什么用它 / 适合什么场景

- **前端工程师友好**:不用搭后端、不用学 Python、不用爬数据;直接 require/import 一个 SDK 就拿到所有行情数据。
- **覆盖 A 股 + 港股 + 美股 + 基金**:写一个跨市场 dashboard 不用拼四家数据源。
- **多入口同源**:ESM + CommonJS 两种打包 + CLI + MCP Server — 给前端、Node、Cursor、Claude Code 同一份数据。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时行情 | A 股 / 港股 / 美股 / 公募基金的实时价、涨跌幅 |
| K 线 | 日 / 周 / 月 / 分钟级 K 线 |
| 零依赖 | 不依赖任何 HTTP / WebSocket 客户端库 |
| ESM + CommonJS | 任意打包工具下都能用 |
| CLI | 在终端查行情 |
| MCP Server | 接 Cursor / Claude 等 AI agent |

## 使用示例

```ts
import { StockSDK } from "stock-sdk";

const sdk = new StockSDK();

const aShare = await sdk.getQuote("600519"); // 贵州茅台
const usQuote = await sdk.getQuote("AAPL");
const kline = await sdk.getKLine("AAPL", { interval: "1d", length: 90 });
```

## 相关概念

- [a-stock-data](tool-a-stock-data.md) — 同方向的另一个 A 股数据 Skill
- [global-stock-data](tool-global-stock-data.md) — 美港股全栈数据(期权链 / 财报三表 / 503 GAAP 指标)
- [Finnhub 美股 API](tool-finnhub-api.md) — 美股 REST API
- [liangmai-sdk](tool-liangmai-sdk.md) — 良买金融数据 Python SDK(服务端方向)
- [stock-sdk 仓库](https://github.com/chengzuopeng/stock-sdk) — 项目链接
