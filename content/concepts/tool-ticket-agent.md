---
type: Tool
title: "ticket-agent（黄牛票截图自动解析与比价）"
description: "把黄牛票报价截图扔进去自动解析、比价、追踪价格波动与加价倍数，每个数字都能点回原图。"
resource: "https://github.com/wxyyb00/ticket-agent"
tags: [ticket, scalper, ocr, price-tracking, image-parse]
timestamp: "2026-07-24T00:00:00Z"
---

# ticket-agent

[ticket-agent](https://github.com/wxyyb00/ticket-agent) 是给演出 / 赛事**黄牛票报价截图**做自动解析、比价与价格波动的工具——把格式各异的报价图扔进去，它负责 OCR、归一化、比价、追踪加价倍数。

## 它解决的问题

买黄牛票（或反过来挂票）的痛点：
- **格式乱**：每个卖家截图都不一样（聊天记录、表格、报价单），手动抄数字既慢又易错。
- **加价倍数看不准**：原价 / 卖价 / 手续费一混，肉眼难判断真实溢价。
- **价格波动**：同一个卖家可能一小时一变，想盯盘只能反复回去看聊天。

ticket-agent 把这一套做成可点回溯的视图：每个数字都能点回去看截图原始位置。

## 关键能力

| 能力 | 说明 |
|------|------|
| 截图 OCR | 把聊天截图 / 报价单里的数字识别出来 |
| 自动比价 | 同一场次多个卖家按价格 / 区域 / 票档排序 |
| 价格波动追踪 | 跨时间记录同一卖家报价变化 |
| 加价倍数 | 自动算相对票面价的溢价倍数 |
| 数字可点回原图 | 每个解析出的数字都能反查截图原位置，便于核对 |

## 适用场景

- 追星 / 看演唱会 / 跨城看球赛需要买黄牛票的人
- 做票务倒卖或代抢的中间商，需要盯同行报价
- 票务平台数据团队做调研

## 参考链接

- 项目仓库: <https://github.com/wxyyb00/ticket-agent>

## 媒体

![](https://pbs.twimg.com/media/HN9P5tIboAAdfNr.jpg)
![](https://pbs.twimg.com/media/HN9P7Jma0AADQNn.jpg)

## 相关概念

- [light-ocr](tool-light-ocr.md) — 原生 / Node.js 离线 OCR 引擎，ticket-agent 截图解析可能的底层依赖
- [creatorhub](tool-creatorhub.md) — 多平台内容监控采集工具，同样处理「截图里挖数据」类场景