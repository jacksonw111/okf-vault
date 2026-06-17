---
title: "Post by @wsl8297 on X"
source: "https://x.com/wsl8297/status/2059183775213625707/photo/1"
author:
  - "[[@wsl8297]]"
published: 2026-06-17
created: 2026-06-17
description: "做 A 股数据分析，最麻烦的不是写策略，而是把数据先拿全：行情、研报、龙虎榜、北向、资金流、公告、财报，每一类接口都不一样，还经常改参数。 a-stock-data 是一个面向 AI 编程助手的 A 股全栈数据 Skill，把 13 个数据源封装成一套可直接调用的工具。 Gi"
tags:
  - "clippings"
---

做 A 股数据分析，最麻烦的不是写策略，而是把数据先拿全：行情、研报、龙虎榜、北向、资金流、公告、财报，每一类接口都不一样，还经常改参数。

a-stock-data 是一个面向 AI 编程助手的 A 股全栈数据 Skill，把 13 个数据源封装成一套可直接调用的工具。

GitHub：https://github.com/simonlin1212/a-stock-data…

它的 README 写得很实在：7 层架构、28 个端点、直连 HTTP API，V3.0 之后彻底移除了 akshare 依赖。

覆盖的数据层很全：

\- 行情层：K 线、五档盘口、逐笔成交、PE / PB / 市值、指数和 ETF

\- 研报层：东财研报、PDF 下载、同花顺一致预期、iwencai 自然语言搜索

\- 信号层：强势股、题材归因、北向资金、概念板块、资金流向、龙虎榜、解禁

\- 资金面：融资融券、大宗交易、股东户数、分红送转、120 日资金流

\- 新闻 / 公告 / 基础数据：财联社快讯、全球资讯、巨潮公告、季报 37 字段、F10

如果你想让 Claude Code、Codex、OpenClaw 这类工具帮你做 A 股研究，这个 Skill 可以直接当数据底座用。
