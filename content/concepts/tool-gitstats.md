---
type: "Tool"
title: "gitstats（开源编码统计面板：GitHub 公私仓都能看）"
description: "yaroslavhaidash 开源：把 GitHub 公开 / 私有 / 工作仓库的编码数据汇总成排行榜和趋势图；Next.js + TypeScript + Drizzle ORM + Neon Postgres。私有仓库在本机读取，服务端只收到汇总数字，按周 / 月 / 年比较代码增删量与提交数。"
resource: "https://github.com/yaroslavhaidash/gitstats"
tags: "[gitstats, github, coding-stats, dashboard, nextjs, typescript, drizzle, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# gitstats（开源编码统计面板：GitHub 公私仓都能看）

## 它是什么

[gitstats](https://github.com/yaroslavhaidash/gitstats) 是 yaroslavhaidash 开源的 **GitHub 编码统计面板**——把 GitHub 公开 / 私有 / 工作仓库的编码数据汇总成排行榜 + 趋势图。

## 关键隐私设计

- **私有仓库在本机读取**——服务端只收到**汇总数字**，**仓库名称不会默认上传**。

## 核心能力

- **周 / 月 / 年** 比较代码**增 / 删量**与**提交数**
- **个人页**：连续贡献 / 语言分布 / 活跃仓库 / 趋势图表
- **组队**：邀请码制，团队排行榜
- **技术栈**：Next.js + TypeScript + Drizzle ORM + Neon Postgres

## 为什么用它 / 适合什么场景

- 想给团队 / 自己**做编码统计**但拒绝 GitHub Insights 那种**只对公开仓**的方案。
- 担心**私有仓库代码被上传**给三方服务——gitstats 的「本地读、服务端只收汇总」是关键。
- 个人开发者想**可视化**自己的 coding 节奏（活跃仓库 / 语言偏好 / 趋势）。
- 想**团队 PK**——按周 / 月比较谁的代码增量高（注意：避免单纯按 LOC 评绩效）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Next.js Web 应用 |
| 数据源 | GitHub 公开 / 私有 / 工作仓库 |
| 隐私 | 私有仓本机读，服务端只收汇总 |
| 视图 | 排行榜 / 趋势图 / 个人页 |
| 比较粒度 | 周 / 月 / 年 |
| 技术栈 | Next.js + TypeScript + Drizzle ORM + Neon Postgres |

## 媒体

- ![](https://pbs.twimg.com/media/HTGX89PbcAAaVcV.jpg)

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — gitstats 可自托管，私有仓数据完全在本地处理
- [Obscura（Rust 无头浏览器）](./tool-obscura-headless-browser.md) — 同为隐私优先的开源工具