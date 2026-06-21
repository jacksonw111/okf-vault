---
type: "Tool"
title: "Obscura（Rust 写的反检测无头浏览器）"
description: "专为 AI Agent 与爬虫设计的 Rust 无头浏览器，仅 30MB 内存、秒级启动、完全兼容 CDP、内置指纹随机化与 MCP Server，可直接替换 Puppeteer/Playwright。"
resource: "https://github.com/nicedoc/obscura"
tags: "[browser, rust, mcp, agent, scraping, anti-detect]"
timestamp: "2026-06-21T00:55:00Z"
---

# Obscura（Rust 写的反检测无头浏览器）

## 它是什么

Obscura 是 `@gaoren7716` 在 2026-06 推荐的开源无头浏览器，定位「Playwright 替代品，专为 AI Agent 打造」：Rust 写的极轻量二进制 + 自带反检测能力 + 内置 MCP Server，让 Claude / Cursor 这类 Agent 直接「驾驶」它跑网页任务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 体积 / 启动 | 仅 30MB 内存占用，秒级启动；远低于 Chromium |
| 协议 | 100% 兼容 CDP，Puppeteer / Playwright 脚本几乎零改动迁移 |
| 反检测 | 内置指纹随机化（GPU / Canvas / Audio / Battery 全覆盖） |
| 隐私 | 自动屏蔽 3500+ 追踪域名 |
| MCP | 内置 MCP Server，Claude / Cursor 等 Agent 直接调用 |
| 代理 | 支持 HTTP / SOCKS5 代理，并发多进程 |

## 适用场景

- AI Agent 想操控浏览器但被 Cloudflare / DataDome 拦下 —— Obscura 的指纹随机化可绕过大部分反爬。
- 大规模爬虫想降低单机内存占用 —— Rust 实现把内存从几百 MB 压到 30MB。
- 不想自己搭 CDP 隧道 —— 内置 MCP Server，AI Agent 一步接入。

## 媒体

![Obscura 截图](https://pbs.twimg.com/media/HLOLtKDa8AAEnih.jpg)

## 相关概念

- [forkd](tool-forkd.md) — 另一个面向 Agent 的 microVM 沙箱路线
- [Agent Skills（代理技能包）](term-agent-skills.md) — MCP + Skill 是 Agent 操控外部世界的事实标准
- [shadcn/improve](tool-shadcn-improve.md) — 同为「让 AI 更好用工具」的工程化思路