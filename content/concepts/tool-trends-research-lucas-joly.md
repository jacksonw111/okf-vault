---
type: "Tool"
title: "trends-research（Lucas Joly 期货趋势持续性研究）"
description: "INSEEC 金融硕士 Lucas Joly 的毕业论文项目：研究全球期货的趋势持续性，代码与结果公开。S183 策略在 62 个期货、36 年数据上原始 Sharpe 0.97，最严修正后仍有 0.78。"
resource: "https://github.com/Lucas-Joly-GH/trends-research"
tags: "[quant, futures, trend, sharpe, research, open-source, thesis]"
timestamp: "2026-09-13T06:09:00Z"
---

# trends-research（Lucas Joly 期货趋势持续性研究）

## 它是什么

[Lucas-Joly-GH/trends-research](https://github.com/Lucas-Joly-GH/trends-research) 是 INSEEC 金融硕士 **Lucas Joly** 的毕业论文项目，主题是**全球期货市场的趋势持续性（trend continuation）**。代码、回测结果与论文配套材料全部公开。

主角策略 **S183**：四个 Alpha 等权合成，在 62 个期货品种 / 36 年数据上跑下来——**原始 Sharpe 0.97，最严多重修正后仍有 0.78**。

## 配套工程

| 部件 | 说明 |
|------|------|
| 自研回测引擎 | 针对 62 个期货统一接口 |
| 45 个独立测过的 Alpha 信号库 | 可单独挑出来用 |
| WGAN 合成市场 | 抗过拟合检验 |
| 145 天模拟盘实盘跟踪 | 2026 年初跑出来的样本外结果 |
| 注意：只读展示 | 私有行情数据未公开，脚本可看但全流程跑不通 |

## 为什么看它 / 适合什么场景

- 趋势 / CTA 策略研究者：看一份**严肃做修正 + 抗过拟合 + 样本外**的开源范例。
- 想研究跨市场趋势持续性的人。
- 量化新手：可读的回测结构 + 公开 Sharpe 修正方法论。

## 媒体

- ![](https://pbs.twimg.com/media/HR_CZlEa0AAEpJw.jpg)

## 项目链接

- 仓库：<https://github.com/Lucas-Joly-GH/trends-research>

## 相关概念

- [Sharpe Ratio（夏普比率）](https://en.wikipedia.org/wiki/Sharpe_ratio) — 衡量策略风险调整后收益的标准指标（项目本身未在 concepts 收录，留百科链接）