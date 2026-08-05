---
type: "Note"
title: "CNN 恐慌贪婪指数（Fear & Greed Index）拆解"
description: "CNN 维护了二十年的市场情绪指标，由 7 个等权重子指标汇总而成；要反着看（均值回归），与 VIX 结合可作为市场情绪位置参考。"
resource: "https://www.cnn.com/markets/fear-and-greed"
tags: [finance, market-sentiment, indicator, cnn, vix, mean-reversion, fear-greed-index]
timestamp: "2026-08-05T08:35:00Z"
---

# CNN 恐慌贪婪指数（Fear & Greed Index）拆解

## 一句话

CNN 的 **Fear & Greed Index** 是一个**市场情绪温度计**：0 = 极度恐惧（往往是买入机会），100 = 极度贪婪（往往是风险信号）。它由 **7 个等权重子指标**汇总而成，每个子指标单独打 0–100 分，然后等权加总。指数已运行**二十多年**。

## 怎么看

- **要反着看（均值回归）**：极度恐惧往往是机会，极度贪婪往往见顶。
- **不能用来预测具体时间点**：只看情绪温度，不做点位预测。
- **和 VIX 结合**：VIX 看波动率绝对值，Fear & Greed 看情绪位置，两者叠加可读出「恐慌+波动爆表」或「贪婪+波动收敛」等组合状态。

## 7 个等权重子指标

| # | 指标 | 怎么算 | 解读 |
|---|------|--------|------|
| 1 | 市场动能（Market Momentum） | 标普 500 相对过去 125 日均线的位置 | 高于均线=贪婪，低于=恐惧 |
| 2 | 股价强度（Stock Price Strength） | 纽交所创 52 周新高 vs 新低的个股数量 | 多数股票新低=恐惧，新高=贪婪 |
| 3 | 市场广度（Stock Price Breadth） | 麦克莱伦累积量指标（McClellan Summation Index） | 上涨股成交量>下跌股=贪婪，反之恐惧 |
| 4 | 期权 Put/Call 比 | 5 日 Put/Call 比率（逆向指标） | <1=看多预期强（贪婪），>1=对冲心态（恐惧） |
| 5 | 市场波动率（Market Volatility） | VIX 与其 50 日移动均线 | VIX 高=恐惧 |
| 6 | 避险需求（Safe Haven Demand） | 过去 20 个交易日国债 vs 股票回报率差 | 债强股弱=避险需求高=恐惧 |
| 7 | 垃圾债需求（Junk Bond Demand） | 垃圾债与安全国债的利差 | 利差收窄=投资者在追风险=贪婪 |

## 历史片段示例

- 近期科技股暴跌时，指数一度指向「Fear（小恐慌）」，随后开始反弹。
- 反弹过后指数走向「Greed（小贪婪）」。
- 这种**恐惧→反弹→贪婪**的循环是均值回归的典型表现。

## 使用建议

- 不要单独用指数做择时。
- 与 VIX（绝对波动率）、宏观经济数据结合更可靠。
- 适合作为「市场情绪位置」的**辅助**指标，不替代基本面与估值分析。

## 参考链接

- [CNN 原始指数页](https://www.cnn.com/markets/fear-and-greed)
- 原始解读：[原帖](https://x.com/shawnyinmr/status/2084908841674907953)

## 相关概念

- [VIX](./term-x402.md) — 同属市场情绪/波动率维度（备注：VIX 在 [tool-12-factor-agents](./tool-12-factor-agents.md) 中也有引用，作为对比参考）