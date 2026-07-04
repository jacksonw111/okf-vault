---
type: Tool
title: "Agent-Reach"
description: "一行命令给 AI 编码 agent 装上「现实互联网能力」：Twitter / Reddit / YouTube 转录 / GitHub / 小红书 / B 站 / 通用网页爬取,无需 API key、无需账号。"
resource: "https://github.com/Panniantong/Agent-Reach"
tags: [agent-reach, agent, ai, web-scraping, mcp]
timestamp: "2026-07-04T15:00:00Z"
---

# Agent-Reach

## 它是什么

Agent-Reach 是 `Panniantong/Agent-Reach` 项目（47.7K Stars, MIT 协议，零依赖）在做的方向：让任意 AI 编码 agent（Claude Code、Cursor、Windsurf 等）一行命令装上「能上网」的能力,**不需要 API key、不需要登录账号、不需要服务费**。

项目链接：<https://github.com/Panniantong/Agent-Reach>

## 它能给 agent 做什么

| 渠道 | 能力 |
|------|------|
| Twitter / X | 读推文与时间线;无需 cookie 也能拿到大部分公开内容 |
| Reddit | 按关键词搜 post,把整条讨论链(含所有评论)抓回来给 agent 分析 |
| YouTube | 拉视频 transcript(字幕) — agent 不用看视频就能理解讲了什么 |
| GitHub | repo 浏览、读 README、看 issue / PR、读 diff |
| 小红书 / Bilibili | 抓笔记 / 视频元数据与评论 |
| 通用网页 | HTML → Markdown 清洗,直接喂进 agent 上下文 |

## 为什么用它

- **零配置**:不要求你注册 API key 也不用翻 cookie 找 token,极大降低「让 agent 用上真实互联网」的工程负担。
- **和主流 agent 直接打通**:官方文档列出 Claude Code / Cursor / Windsurf 的接入方式。
- **MIT + 47K+ Star**:这个方向已经有人维护并验证了。

## 安装与启用(官方一行命令)

按项目 README 的 quick start,在 agent 工作目录里执行一条命令即可完成安装与配置。

## 相关概念

- [anysearch-skill](tool-anysearch-skill.md) — 同样是给 agent 装「上网能力」的 Skill,主打搜索引擎聚合
- [browser-search](tool-browser-search-agent.md) — SearXNG + Camofox + CloakBrowser 串起来的自托管搜索栈
- [Agent-Reach 仓库](https://github.com/Panniantong/Agent-Reach) — 项目链接
