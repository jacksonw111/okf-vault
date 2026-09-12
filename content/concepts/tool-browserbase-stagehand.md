---
type: "Tool"
title: "Stagehand（Browserbase 的 AI 浏览器自动化框架）"
description: "Browserbase 出品的浏览器自动化框架：让 AI agent 通过自然语言 / 代码混合的方式控制浏览器；最新方向是「Code Mode」，让模型直接写代码操控 DOM，替代传统预设工具调用。"
resource: "https://github.com/browserbase/stagehand"
tags: "[browser-agent, computer-use, browserbase, stagehand, automation]"
timestamp: "2026-09-12T22:00:00Z"
---

# Stagehand（Browserbase）

## 它是什么

[Browserbase](https://browserbase.com) 出品的 **AI 浏览器自动化框架**：把"自然语言意图"翻译成浏览器操作（点击 / 填表 / 抓取）。最新一代 **Code Mode** 主张：不再给模型预设一串工具，而是让模型**直接写代码**操作 DOM，绕过工具调用层。

## 核心特性

| 特性 | 说明 |
|------|------|
| 自然语言驱动 | 用 LLM 解释意图、操作浏览器 |
| 三代演进 | 纯视觉 CUA → 视觉+文本混合 → Code Mode |
| Code Mode | 让模型直接写 TypeScript / Python 操作 DOM |
| 配套云端浏览器 | Browserbase 提供可托管的浏览器实例 |

## 为什么用它 / 适合什么场景
- 想做一个能在真实网站上自主完成任务的 AI agent。
- 不想自己写 Selenium / Playwright 胶水代码。
- 想用最新 Code Mode 思路：用代码代替工具调用，让模型更灵活。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器自动化 | 点击 / 输入 / 截图 / 抓 DOM |
| 云端浏览器 | Browserbase 托管实例，无需本地启动 Chrome |
| Code Mode | 模型直接产代码操控页面 |
| 框架适配 | 与 LangChain / LlamaIndex 集成 |

## 参考链接

- 项目仓库：<https://github.com/browserbase/stagehand>
- Browserbase 官网：<https://browserbase.com>

## 相关概念

- [CUA-Lite](./tool-cua-lite.md) — 另一个轻量级 Computer-Use 框架
- [Browserbase 三代 Computer-Use 演进](./note-browserbase-stagehand-code-mode.md) — 同主题复盘长文
- [Vercel Agent Browser](./tool-vercel-agent-browser.md) — 让 AI agent 模拟浏览器行为的同类工具
