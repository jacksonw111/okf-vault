---
type: "Tool"
title: "a-stock-data（A股全栈数据 Skill）"
description: "面向 AI 编程助手的 A 股全栈数据 Skill：把 13 个数据源（行情 / 研报 / 龙虎榜 / 北向 / 资金流 / 公告 / 财报）封装成 28 个直连 HTTP 端点，给 Claude Code、Codex、OpenClaw 直接当数据底座用。"
tags: "[ai, finance, a-stock, data, agent-skills, claude-code]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/simonlin1212/a-stock-data"
---

# a-stock-data（A股全栈数据 Skill）

## 它是什么

[`a-stock-data`](https://github.com/simonlin1212/a-stock-data) 是一个**面向 AI 编程助手的 A 股全栈数据 Skill**——把原本散落在 13 个数据源、各有各接口的 A 股数据，**封装成 28 个统一端点**，让 Claude Code / Codex / OpenClaw 这类 agent 直接调用做研究、写策略、做分析。

> 原话：「做 A 股数据分析，最麻烦的不是写策略，而是把数据先拿全。」

## 它替代了什么

| 旧做法 | a-stock-data |
|--------|--------------|
| 每个数据源一套 API / 鉴权 | 28 个统一端点 |
| V3 之前依赖 akshare | 直连 HTTP API，**彻底移除 akshare 依赖** |
| 13 个数据源各自文档 | 一份 README，7 层架构写清楚 |

## 数据层架构（来源推文摘录）

| 层级 | 覆盖 |
|------|------|
| 行情层 | K 线、五档盘口、逐笔成交、PE / PB / 市值、指数、ETF |
| 研报层 | 东财研报、PDF 下载、同花顺一致预期、iwencai 自然语言搜索 |
| 信号层 | 强势股、题材归因、北向资金、概念板块、资金流向、龙虎榜、解禁 |
| 资金面 | 融资融券、大宗交易、股东户数、分红送转、120 日资金流 |
| 新闻 / 公告 | 财联社快讯、全球资讯、巨潮公告 |
| 基础数据 | 季报 37 字段、F10 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 13 数据源 | 一站式收齐 A 股常见数据 |
| 28 端点 | 统一接口，agent 无需逐源学习 |
| 直连 HTTP | V3 起移除 akshare，性能 / 稳定性更可控 |
| 7 层架构 | 行情 / 研报 / 信号 / 资金 / 新闻 / 公告 / 基础 |
| 适配多 agent | Claude Code / Codex / OpenClaw |

## 适用场景

| 场景 | 价值 |
|------|------|
| 用 Claude Code 写 A 股策略 | agent 直接调端点取数，不用造轮子 |
| 量化研究 / 回测 | 28 端点够覆盖大多数 alpha / 风险因子 |
| 投研报告自动化 | 研报 + 行情 + 公告串联，agent 自动出晨报 |
| 教学 / 个人复盘 | 个人量化玩家也能低成本搭底座 |

## 与本知识库其他概念的关系

- [Agent Skills 是什么](term-agent-skills.md) — a-stock-data 是「**垂直领域数据 skill**」的代表：把领域知识 + 接口封装打包，agent 即取即用。
- [Claude Code](tool-claude-code.md) — 首批支持的目标 agent 之一。
- [mattpocock/skills](tool-mattpocock-skills.md) — 同一波「skill 仓库」生态；mattpocock 偏通用 SOP，a-stock-data 偏垂直数据接口。

## 相关概念

- [Agent Skills 是什么](term-agent-skills.md) — 垂直领域数据 skill 的典型实现
- [Claude Code](tool-claude-code.md) — a-stock-data 首批支持的目标 agent 之一
- [mattpocock/skills](tool-mattpocock-skills.md) — 同 skill 生态；通用 SOP vs 垂直数据接口的互补
