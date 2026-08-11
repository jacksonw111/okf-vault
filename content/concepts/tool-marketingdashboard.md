---
type: "Tool"
title: "MarketingDashboard（theBigGavin/marketingdashboard）"
description: "把指数 / 商品 / 美债 / 板块 / 资金流等多源行情塞进同一个浏览器页面，一屏实时刷新；后端 Node 代理聚合公开接口，大多数行情源免 API Key、跑起来不依赖数据库。"
resource: "https://github.com/theBigGavin/marketingdashboard"
tags: "[finance, dashboard, node, real-time, market-data, investing]"
timestamp: "2026-08-11T16:00:00Z"
---

# MarketingDashboard

[MarketingDashboard](https://github.com/theBigGavin/marketingdashboard) 是一份**多源行情聚合看板**——盯盘与产业研究同时进行时,通常要开指数、商品、美债、板块、资金流等多个页面来回切换,这个项目把所有行情源收进同一浏览器页面,一屏实时刷新。

项目链接：<https://github.com/theBigGavin/marketingdashboard>

## 它是什么

一个**单页行情聚合器**:前端浏览器页面 + 后端 Node 代理。后端做两件事——代理公开行情接口、按需聚合;前端只负责把数据画成一屏可读的卡片/表格/曲线,所见即所需的全部信息。

## 为什么用它 / 适合什么场景

- **盯盘 / 产业研究同开**:免去开多个窗口来回切。
- **零数据库**:后端不写库,刷新即拉即用,适合个人或小团队搭本地 / 局域网实例。
- **大多数接口免 API Key**:依赖公开数据源,部署摩擦最低。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源行情聚合 | 指数 / 商品 / 美债 / 板块 / 资金流统一拉取与展示 |
| 实时刷新 | 前端一屏刷新,后端按节奏轮询 |
| Node 代理层 | 跨域 / CORS / 限速 / 拼装数据格式都在服务端做 |
| 零数据库 | 跑起来不需要起 DB,适合 demo / 自部署 |
| 大多数免 API Key | 公开数据源为主,无需挨家申请配额 |

## 媒体

![](https://pbs.twimg.com/media/HPU5V03bgAEHMVM.jpg)

## 参考链接

- [项目仓库](https://github.com/theBigGavin/marketingdashboard)

## 相关概念

- [Fear & Greed Index（市场情绪指数）](./note-fear-greed-index.md) — 另一类聚合市场情绪/动量的工具,与本看板可互补
- [Gendangzou Skill(跟党走)](./tool-gendangzou-skill.md) — 把 A 股板块 / 资金 / 公司数据封装成 AI Agent 可查的 Skill,本看板是它的可视化对照面