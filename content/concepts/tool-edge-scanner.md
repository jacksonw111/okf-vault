---
type: "Tool"
title: "Edge Scanner（美股分钟行情本机扫描器）"
description: "simonro 开源：在本机扫描美股分钟行情，交易者可自定义**Setup**组合、保存**告警规则**，再用浏览器仪表盘查看盘中信号。行情源支持 **Alpaca / Charles Schwab**。"
resource: "https://github.com/simonro/edge-scanner"
tags: "[edge-scanner, stock-scanner, alpaca, schwab, day-trading, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# Edge Scanner（美股分钟行情本机扫描器）

## 它是什么

[Edge Scanner](https://github.com/simonro/edge-scanner) 是 simonro 开源的 **美股分钟行情本机扫描器**——交易者可自定义 **Setup** 组合、保存**告警规则**，再用浏览器仪表盘查看盘中信号。

## 行情源

| 数据源 | 特点 |
|------|------|
| **Alpaca** | 免费 IEX 数据，**只一个交易所**，成交额相关设置可能更少触发 |
| **Charles Schwab** | 真实 1 分钟 K 线，覆盖流动性最高的 300 个股票 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本机扫描器 + 浏览器仪表盘 |
| 行情粒度 | 分钟级 |
| Setup 组合 | 交易者自定义 |
| 告警规则 | 可保存复用 |
| 仪表盘 | 浏览器查看盘中信号 |
| 数据源 | Alpaca / Schwab |

## 为什么用它 / 适合什么场景

- 想**本地跑**美股分钟扫描，行情数据不出本机。
- 想自己**组合 Setup**（多条件扫描）而不是用平台写死的策略。
- 想要**可保存告警规则**——一遍配置持续用。
- 行情源支持 Alpaca / Schwab——用哪家 broker 的 API 就接哪家。

## 媒体

- ![](https://pbs.twimg.com/media/HTGXHiwbUAAtVyr.jpg)

## 相关概念

- [market-echo](./tool-market-echo.md) — 本地行情形态相似度检索，最近 96 根 K 线找历史相似区间
- [Self-Hosted（自托管）](./term-self-hosted.md) — 行情本地扫描 = 自托管交易工具