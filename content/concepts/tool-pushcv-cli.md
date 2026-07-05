---
type: "Tool"
title: "pushcv-cli（终端求职看板）"
description: "把求职流程可视化为终端内看板（Drafting → Applied → Interviewing → Closed），支持手动添加或抓取 LinkedIn 职位信息、用本地 AI 模型定制简历与求职信、并提供基于网页数据的薪资估算。"
tags: "[job-board, cli, tui, career, linkedin, ai]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/notnotparas/pushcv-cli"
---

# pushcv-cli（终端求职看板）

## 它是什么

[`pushcv-cli`](https://github.com/notnotparas/pushcv-cli) 是一个**终端内的求职看板 CLI**，把求职流程拆成四列：**Drafting → Applied → Interviewing → Closed**，让所有投递进度一目了然地跑在 TUI 里，不用再回到 Excel / Notion / Trello。

![pushcv-cli 截图](https://pbs.twimg.com/media/HMYVjuvb0AA_xNa.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端看板 | TUI 看板四列：Drafting → Applied → Interviewing → Closed |
| 手动添加 | 直接 `add` 创建求职条目 |
| LinkedIn 抓取 | 自动从 LinkedIn 拉职位信息（公司 / 岗位 / JD） |
| AI 定制简历 | 用本地 AI 模型针对每条 JD 改写简历 |
| AI 求职信 | 根据 JD 自动生成求职信初稿 |
| 薪资估算 | 基于网页公开数据估算职位薪资范围 |
| 全流程闭环 | 投递 → 跟进 → 面试 → 结果，全部在一处跟踪 |

## 适用场景

- 正在批量海投 / 精投，需要在终端里跟踪几十条进度
- 想用本地 LLM 改造简历但又不想把简历内容上传到云 API
- 重度 CLI 用户，对 Notion / Trello 的 web 体验感到疲劳
- 求职阶段希望每天打开终端时第一眼看到「今天该做什么」

## 参考链接

- [项目链接](https://github.com/notnotparas/pushcv-cli)

## 相关概念

- [resume-jd-optimizer-cn](tool-resume-jd-optimizer-cn.md) — 中文定制简历生成器，可与 pushcv-cli 的「AI 定制简历」能力互补
- [backend-agent-resume-scout](tool-backend-agent-resume-scout.md) — Codex 简历 Skill，自动搜索 + 简历生成
- [Worf](tool-worf.md) — 本地优先桌面应用，看板 + OKR + 笔记六合一