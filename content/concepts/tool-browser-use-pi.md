---
type: "Tool"
title: "Browser Use Pi（Browser-Use 团队的轻量 Web Agent）"
description: "Browser-Use 团队发布的轻量 TypeScript Web Agent：由 Astra 基于真实浏览器评测驱动构建与打磨；提炼 Browser Use / Harness / BrowserCode 核心，剔除冗余启发式规则。"
resource: "https://github.com/browser-use/browser-use-pi"
tags: "[web-agent, typescript, browser, ai-agent, browser-use]"
timestamp: "2026-09-11T22:10:00Z"
---

# Browser Use Pi

## 它是什么

[browser-use/browser-use-pi](https://github.com/browser-use/browser-use-pi) 是 **Browser-Use** 团队新发布的**轻量 TypeScript Web Agent**，代号 **Pi 🥧**。

## 核心亮点

| 维度 | 做法 |
|------|------|
| 去粗取精 | 提炼 Browser Use / Harness / BrowserCode 核心，剔除冗余启发式 |
| 底层架构 | 基于 **Pi Mono + 持久化 V8 REPL + 原生 CDP** |
| 全 TypeScript | 类型友好 |
| 功能完备 | 自带云浏览器 / 持久会话 / 流式 / 步骤限制 |
| 安装 | `npm install @browser_use/pi` |

## 为什么用它 / 适合什么场景

- 想做 Web Agent 但不要 Browser-Use 完整版的复杂度。
- 想要一个 TypeScript 原生、易嵌入的 Web Agent SDK。
- 想做云浏览器 + 持久会话 + 流式传输的代理应用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 轻量 | 剔除冗余启发式 |
| Pi Mono | 基础架构 |
| 持久 V8 REPL | 长时间任务 |
| 原生 CDP | Chrome DevTools Protocol |
| 云浏览器 | 自带云端支持 |
| 持久会话 | 跨调用保持 |
| 流式 | 实时输出 |
| 步骤限制 | 防止无限循环 |

## 参考链接

- 项目仓库：<https://github.com/browser-use/browser-use-pi>

## 相关概念

- [Browser-Use Pi 同生态](./tool-cua-lite.md) — Computer-Use 全流程框架
- [Vercel Agent Browser](./tool-vercel-agent-browser.md) — Vercel Labs 让 AI agent 模拟浏览器
- [note-browserbase-stagehand-code-mode](./note-browserbase-stagehand-code-mode.md) — Browserbase 三代 computer-use 演进
</content>
</invoke>