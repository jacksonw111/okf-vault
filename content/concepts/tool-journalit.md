---
type: "Tool"
title: "Journalit（Cursivez/journalit）"
description: "交易者的多平台成交记录汇总工具,把 IBKR / Tradovate / Bybit 等平台的订单历史统一收进 Obsidian 做本地复盘,数据完全留在本机。"
resource: "https://github.com/Cursivez/journalit"
tags: "[trading, journal, obsidian, ibkr, tradovate, bybit, self-hosted]"
timestamp: "2026-07-14T19:44:19Z"
---

# Journalit

[Journalit](https://github.com/Cursivez/journalit) 是**交易者用的多平台成交记录汇总工具**——把 IBKR(盈透)、Tradovate、Bybit 等平台下单产生的成交记录**统一收进 Obsidian** 做交易复盘,**数据完全留在本机**。

## 它解决了什么

做交易的人在 3–5 个平台下单很常见,每家 API 拿到的 csv / json schema 不同,事后想复盘「这笔单子为什么下」要跨平台对账。Journalit 把多源成交记录抽出来,**统一结构化写入 Obsidian 的 vault**,得到本地、可用 Dataview / graph view 检索的交易日志。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多平台接入 | IBKR / Tradovate / Bybit 等 |
| Obsidian 落地 | 直接写进 vault,可被 Dataview 查询 |
| 数据本地化 | 不连第三方,数据留在用户机器 |
| 复盘友好 | 每笔成交对应一个 markdown 笔记 |

## 媒体

![](https://pbs.twimg.com/media/HNLC7ZAbQAAaI9i.jpg)

## 参考链接

- [项目仓库](https://github.com/Cursivez/journalit)

## 相关概念

- [Obsidian](./tool-obsidian.md) — 本工具的落地容器
- [Vibe Trading / TradingView MCP](./tool-vibe-trading.md) — 另一类让 AI/工具体系化介入交易的样本,目标不同(决策辅助 vs 复盘归集)
- [TradingView MCP](./tool-tradingview-mcp.md) — 行情 / 图表接入,本工具管成交记录侧
