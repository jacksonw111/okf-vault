---
type: Tool
title: "browser-act/skills"
description: "BrowserAct 的 skills 仓库，用真实浏览器自动化交互与提取网页数据，供 AI agent 通过 skills 协议调用"
resource: "https://github.com/browser-act/skills"
tags: [browser, automation, scraping, skills, agent]
timestamp: 2026-09-05T15:00:00Z
---

# browser-act/skills

## 它是什么
`browser-act/skills` 是 **BrowserAct** 项目的 skills 仓库：把「**用真实浏览器自动化交互 + 抽取网页数据**」封装成可被 AI agent 加载调用的 skills，覆盖点击 / 输入 / 滚动 / 等待等真实交互动作，而非依赖脆弱的 HTML 抓取。

## 为什么用它 / 适合什么场景
- 想让 agent 操作真实网页（点击按钮、登录态、动态加载内容）而非简单 HTTP 抓取。
- 需要 skills 化封装，便于不同 agent（Claude Code / Codex / Cursor…）即插即用。
- 浏览器自动化反复重写，希望用统一 skill 复用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 真实浏览器交互 | 点击 / 输入 / 滚动 / 等待等用户级动作 |
| 网页数据提取 | 自动从页面中结构化抽取数据 |
| Skills 协议 | 按 skills 规范暴露，agent 可直接加载 |
| 复用性 | 一份 skill 多 agent 共享 |

## 媒体
- ![](https://pbs.twimg.com/media/HRbJW5-XgAQcj_v.jpg)

## 相关概念
- [原始链接](https://github.com/browser-act/skills)