---
type: "Tool"
title: "ETF Grid Design（yxcsky/etf-grid-design）"
description: "基于 Python Flask + React 的 ETF 网格交易参数生成 Web 工具：通过 tushare/akshare 拉取历史行情，自动计算日振幅、波动率、趋势等指标，并据此生成网格上下边界、网格数量、仓位分配与收益预估。"
resource: "https://github.com/yxcsky/etf-grid-design"
tags: [etf, grid-trading, flask, react, tushare, akshare, quant]
timestamp: "2026-07-26T02:26:00Z"
---

# ETF Grid Design（yxcsky/etf-grid-design）

## 它是什么

`yxcsky/etf-grid-design` 是一个**基于 Python Flask + React 的 Web 工具**，通过 `tushare` 或 `akshare` 获取 ETF 历史行情数据，自动计算 ETF 的日振幅、波动率、趋势等关键指标，并据此生成**网格交易的上下边界、网格数量、仓位分配和收益预估**。

## 为什么用它 / 适合什么场景

- 网格交易前需要先确定上下边界与格数，手工算费时且主观；
- 想基于真实历史波动率给仓位分配提供依据，而不是拍脑袋；
- 同时使用多家数据源（tushare + akshare），数据冗余更稳。

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据接入 | 支持 tushare 和 akshare 两种行情源 |
| 指标计算 | 日振幅、波动率、趋势等量化因子 |
| 边界生成 | 根据波动率自动给出网格上下边界 |
| 仓位分配 | 自动给出每格仓位建议 |
| 收益预估 | 基于历史样本预估网格收益 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOC-UllaQAAfkZz.png)

- 项目链接：<https://github.com/yxcsky/etf-grid-design>
