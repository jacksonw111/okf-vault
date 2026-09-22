---
type: Tool
title: "trade-journal"
description: "本地交易日志工具——把券商成交、对账单和手工录入的原始成交撮合成回合交易，生成 P&L 日历、收益统计与每日复盘，数据存自己的 SQLite，AI 复盘用自己的 API Key。"
resource: "https://github.com/LuxAlgo/trade-journal"
tags: "[trading, journaling, sqlite, ai-review, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# trade-journal

## 它是什么
一个**本地交易日志 / 复盘工具**：

> 把券商成交、对账单、手工录入的原始成交撮合成回合交易（round-trip），在本地生成 P&L 日历、收益统计与每日复盘；数据存在自己的 SQLite 里，AI 复盘用自己的 API key。

## 为什么用它 / 适合什么场景
- 想把不同来源（券商 API / 对账单 / 手工记录）的成交汇总成回合级 P&L。
- 不想把交易数据上云，希望数据留在本地 SQLite。
- 希望 AI 复盘但不想泄漏持仓 / 成交——用自己的 API Key。

## 关键能力
| 能力 | 说明 |
|------|------|
| 数据源 | 券商成交 / 对账单 / 手工录入 |
| 撮合 | 回合交易（round-trip） |
| 输出 | P&L 日历 / 收益统计 / 每日复盘 |
| 存储 | 本地 SQLite |
| AI 复盘 | 自带 API Key |

## 项目链接
- 项目主页：<https://github.com/LuxAlgo/trade-journal>

## 媒体
- 截图：<https://pbs.twimg.com/media/HSyK4SsboAAgh3Y.jpg>
