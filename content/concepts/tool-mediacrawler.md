---
type: "Tool"
title: "MediaCrawler（多平台自媒体数据采集工具）"
description: "基于 Python 的多平台自媒体数据采集工具，支持小红书 / 抖音 / 快手 / B 站 / 微博 / 百度贴吧 / 知乎七个平台的内容和评论爬取，利用 Playwright + JS 表达式签名参数，无需逆向加密算法。"
tags: "[crawler, scraper, social-media, python, playwright]"
timestamp: "2026-06-26T23:42:00.000Z"
resource: "https://github.com/NanmiCoder/MediaCrawler"
---

# MediaCrawler（多平台自媒体数据采集工具）

## 它是什么

[`MediaCrawler`](https://github.com/NanmiCoder/MediaCrawler) 是一个**基于 Python 的多平台自媒体数据采集工具**，支持**小红书、抖音、快手、B 站、微博、百度贴吧、知乎**七个平台的内容和评论爬取。它利用 Playwright 浏览器自动化框架登录并保存登录态，通过 JS 表达式获取签名参数，**避免了复杂的加密算法逆向**。

![MediaCrawler 演示](https://pbs.twimg.com/media/HLtQPktaMAAU_Q2.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 七平台覆盖 | 小红书 / 抖音 / 快手 / B 站 / 微博 / 贴吧 / 知乎 |
| 内容 + 评论 | 帖子正文与评论一起爬 |
| Playwright | 浏览器自动化框架登录并保存登录态 |
| JS 表达式签名 | 通过执行 JS 表达式获取签名参数 |
| 无需逆向 | 不用逆向复杂的加密算法 |
| 登录态持久化 | 一次登录，多次复用 |

## 适用场景

- 自媒体运营 / 内容研究需要批量拉取多平台公开数据
- 数据分析师做社媒舆情 / 热点 / 用户研究
- 想给数据集 / RAG 喂入社媒公开内容做实验

## 注意事项

> ⚠️ 抓取行为需遵守各平台的使用条款与当地法规，仅用于合法合规的研究与分析目的。

## 参考链接

- [项目链接](https://github.com/NanmiCoder/MediaCrawler)

## 相关概念

- [browser-search-agent](tool-browser-search-agent.md) — 自托管 AI 代理搜索栈，处理反爬
- [Obscura（Rust 无头浏览器）](tool-obscura-headless-browser.md) — 反检测 + CDP 兼容的无头浏览器