---
type: "Tool"
title: "get_jobs（loks666/get_jobs）"
description: "BOSS 直聘自动化投递工具合集，针对招聘网站反自动化检测做了深度对抗：CDP / 云端 bot 都会被识别为空白页，本项目用一系列「巧思」绕过反爬。"
resource: "https://github.com/loks666/get_jobs"
tags: "[job-board, automation, anti-bot, scraping, boss-zhipin, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# get_jobs（loks666/get_jobs）

## 它是什么

[get_jobs](https://github.com/loks666/get_jobs) 是 loks666 维护的 BOSS 直聘自动化投递工具合集，针对招聘网站越来越严格的反自动化检测做了深度对抗。

## 它要解决的问题

现代网站对自动化操作做了大量限制：
- 让 ChatGPT 通过 CDP 操作 Chrome → 空白页
- 让 grok bot 云端操作 → 空白页

get_jobs 项目与 GitHub Discussions 里的讨论记录了大量「AI 时代的奇淫巧技」：从浏览器指纹、cookie 处理、headless 行为模拟到反制手段的反制。

## 关键点

- 绕过 BOSS 直聘等招聘网站的反自动化检测
- 项目与 Discussions 内容都被视为「技术干货」
- 适合研究招聘场景下的 anti-bot 对抗

## 适用场景

- 想批量投递简历到 BOSS 直聘
- 研究 anti-bot / 反 anti-bot 技术
- 学习 AI agent 操作真实网站时的反制对抗

## 原始链接

- 讨论入口：<https://github.com/loks666/get_jobs/discussions/250>
- 项目主页：<https://github.com/loks666/get_jobs>

## 相关概念

- [Browsentic](./tool-browsentic.md) — 给本机已登录 Chrome 套 agent 皮，连接免 API key
- [Fast Browser Use](./tool-fast-browser-use.md) — APUS 把 Qwen3.5 搬本机做浏览器自动化