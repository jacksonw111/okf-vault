---
type: Tool
title: "Vercel Agent Browser"
description: "Vercel Labs 开源库：让 AI agent 模拟浏览器行为（点击、输入、导航），比直接驱动真实浏览器快很多；TinyShip 写 E2E 时一直在用。"
resource: "https://github.com/vercel-labs/agent-browser"
tags: [vercel, ai-agent, browser-automation, e2e, testing]
timestamp: "2026-09-08T00:00:00Z"
---

# Vercel Agent Browser

## 它是什么
Vercel Labs 开源的**让 AI agent 模拟浏览器行为的库**：让 agent 可以"假装"在浏览器里点击、输入、跳转、抓取页面元素，比直接驱动真实浏览器（Selenium/Playwright/Puppeteer）的开销小、速度更快。Vercel 的产品 [TinyShip](https://tinyship.dev) 写 E2E 时一直在用。

## 为什么用它 / 适合什么场景
- 想给 AI agent 一个轻量浏览器操作接口，而不是让 agent 反过来调 Playwright。
- 想让 LLM 主导的 UI 测试 / 回归脚本跑得更快。
- 想统一 agent 视角的"页面模型"，与人类 QA 视角解耦。

## 关键能力
| 能力 | 说明 |
|------|------|
| Agent 视角 | 接口专为 LLM agent 设计 |
| 比真实浏览器快 | 避免完整 DOM 渲染开销 |
| E2E 友好 | TinyShip 实战使用 |
| Vercel Labs 出品 | 持续维护 |

## 参考
- 原始链接：<https://github.com/vercel-labs/agent-browser>

## 相关概念
- [Vercel Portless](./tool-vercel-portless.md) — 同作者的本地多服务子域名代理
- [Playwright](https://playwright.dev/) — 通用浏览器自动化
