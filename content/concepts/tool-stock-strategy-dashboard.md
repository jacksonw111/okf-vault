---
type: "Tool"
title: "stock-strategy-dashboard（A股 / 美股短线波段本地只读工作台）"
description: "为 A 股与美股短线波段交易者提供的本地运行只读工作台：把全市场策略初筛、5 分钟 K 线确认、模拟成交与止损止盈提醒串成一条可追溯流程，配 7 套实验策略、0.25% 单笔风险、第三天强制走人。"
resource: "https://github.com/zc6503204-collab/stock-strategy-dashboard"
tags: "[stock, trading, backtest, a-shares, us-stocks, python]"
timestamp: "2026-09-11T22:05:00Z"
---

# stock-strategy-dashboard

## 它是什么

[zc6503204-collab/stock-strategy-dashboard](https://github.com/zc6503204-collab/stock-strategy-dashboard) 是面向 **A 股 / 美股短线波段**交易者的**本地运行只读工作台**：

| 流程节点 | 做什么 |
|---------|--------|
| **盘前** | 全市场策略初筛 |
| **盘中** | 完整 5 分钟 K 线确认 |
| **买前** | 先算仓位 |
| **买后** | 模拟成交 + 止损止盈提醒 |

每一步都**可追溯**。

## 内置策略纪律

| 维度 | 设置 |
|------|------|
| 策略数量 | 7 套实验策略 |
| 单笔风险 | 0.25% |
| 持仓周期 | 第 3 天强制走人 |
| 运行模式 | 本地 + 只读（避免误操作真账户） |

## 为什么用它 / 适合什么场景

- 做 A 股 / 美股短线波段但被情绪带着走。
- 想把「选股 → 确认 → 仓位 → 提醒」沉淀成流程。
- 不想把账户接入第三方平台（**只读 + 本地**是亮点）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全市场初筛 | 盘前跑一遍 7 套策略 |
| 5 分钟 K 线 | 盘中二次确认 |
| 仓位计算 | 买前先算 |
| 模拟成交 | 不接真账户 |
| 止损止盈 | 自动提醒 |
| 本地运行 | 数据不出本机 |
| 只读模式 | 不连真实交易接口 |

## 参考链接

- 项目仓库：<https://github.com/zc6503204-collab/stock-strategy-dashboard>

## 媒体

- ![](https://pbs.twimg.com/media/HR5hQk2bQAAEGHP.jpg)

## 相关概念

- [tickflow-stock-panel](./tool-tickflow-stock-panel.md) — 自托管 A 股量化工作台
- [a-stock-data](./tool-a-stock-data.md) — A 股数据 API
- [budget-tracker-tui](./tool-budget-tracker-tui.md) — 同为 SQLite + Python 个人理财思路
</content>
</invoke>