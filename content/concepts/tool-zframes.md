---
type: Tool
title: "zframes（自然语言生成实时行情仪表盘）"
description: "给编码智能体装一个 skill，用自然语言描述想要的仪表盘，智能体照组件目录生成 dashboard.json，由运行时渲染实时行情；内置 284 种组件、29 个免密钥数据源，全程不写 React。"
resource: "https://github.com/zentryHQ/zframes"
tags: [dashboard, agent-skill, finance, realtime, crypto, no-code]
timestamp: 2026-09-04T12:00:00Z
---

# zframes（自然语言生成实时行情仪表盘）

## 它是什么

zframes 把「做行情仪表盘」这件事从写前端代码变成**写一句话**：给编码智能体装上它提供的 skill，用自然语言描述想要看什么，智能体按组件目录生成一份 `dashboard.json`，运行时读取该 JSON 直接渲染实时行情。**不用注册账号、不用申请 API key、不用手写 React。**

![](https://pbs.twimg.com/media/HRN7RyYbQAAysKO.png)

## 为什么用它 / 适合什么场景

- 想快速拼一个盯盘面板（股票 / 加密 / 宏观），但不想为此起一个前端工程。
- 数据源都要自己申请 key 太麻烦——它内置的 29 个源均免密钥。
- 已经在用编码智能体（Claude Code / Codex 之类），希望仪表盘也走同一套 prompt 工作流。

## 关键能力

| 能力 | 说明 |
|------|------|
| 组件目录 | 内置 284 种可视化组件，智能体按目录选型组装 |
| 免密钥数据源 | 29 个，含 Hyperliquid、Nasdaq、CoinGecko、DeFiLlama、美国财政部、FRED |
| 覆盖资产 | 股票、宏观、加密货币、衍生品、贵金属 |
| 产物形态 | 单一 `dashboard.json` 描述文件，运行时负责渲染 |
| 集成方式 | 以 skill 形式挂进编码智能体 |

## 参考链接

- 项目链接：<https://github.com/zentryHQ/zframes>
- 原始链接：<https://x.com/QingQ77/status/2095656083297816664>

## 相关概念

- [Agent Skills](./term-agent-skills.md) — zframes 正是以「Skill」形态装进编码智能体，是该规范的一个具体应用
