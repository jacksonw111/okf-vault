---
type: Tool
title: "the-daily-diff"
description: "arpitbbhayani/the-daily-diff，每天自动汇总 arXiv 与 Hacker News 的新论文 / 技术文章，按天排好、打分排序，打开网页就能看的「技术早报」。"
resource: "https://github.com/arpitbbhayani/the-daily-diff"
tags: "[arxiv, hackernews, digest, daily, papers, automation]"
timestamp: "2026-08-01T20:30:00Z"
---

# the-daily-diff

## 它是什么

[`arpitbbhayani/the-daily-diff`](https://github.com/arpitbbhayani/the-daily-diff) 是一个**每天自动跑**的抓取与评分脚本：把 arXiv 新论文和 Hacker News 热门技术文章聚合到一份按天排好的「技术早报」里，按分数排序，**打开网页就能浏览**，不用自己挨个刷。

## 解决什么痛点

- arXiv 每天新增几百篇论文，自己刷不完
- Hacker News 首页热点噪音多（融资八卦 + 政治 + Show HN），技术含量被稀释
- 想每天只看「值得看的」10-20 条

## 核心机制

| 环节 | 说明 |
|------|------|
| 抓取 | 定时拉 arXiv（按分类）与 HN（按类型 / 分数） |
| 打分 | 用启发式分数（HN 分数、引用潜力、关键词匹配等）排序 |
| 排版 | 按天成页，HTML 静态站输出 |
| 浏览 | 打开网页就行；可部署到 GitHub Pages / 自托管 |

## 适合什么场景

- 研究者 / 学生：每天跟进自己领域的 arXiv 论文
- 工程师：不想刷 HN 浪费时间，只想看「今天真正值得读的 5 条技术」
- 想搭一个**自动化的个人技术早报**（放进自己的知识库首页 / Notion 嵌入页）

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [TrendRadar](./tool-trendradar.md) | 多平台热榜 | 更广（微博 / 知乎 / B 站等），偏社媒热榜 |
| [Ember HackerNews](./tool-ember-hackernews.md) | 客户端 | 单独 HN 阅读器，不带打分排序 |
| the-daily-diff | 服务端抓取 + 网页 | 双源 + 自动打分 + 网页成品 |

## 媒体

![the-daily-diff 截图](https://pbs.twimg.com/media/HOhazauaYAAeKZ4.jpg)

## 原始链接

- [项目仓库](https://github.com/arpitbbhayani/the-daily-diff)
- [原始推文](https://x.com/QingQ77/status/2083512818028908823)

## 相关概念

- [TrendRadar](./tool-trendradar.md) — 偏社媒热榜聚合的同类思路，平台更多但技术含量更稀