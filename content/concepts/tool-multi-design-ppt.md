---
type: Tool
title: "Space Multi-Design PPT（品牌设计驱动幻灯片 Skill）"
description: "SpaceZephyr 开源的基于 Agent Skills 协议的幻灯片生成 Skill，把文章 / BP / 周报等内容按 62 种真实品牌设计语言生成可交付的 HTML / PPTX / PDF 演示稿。"
resource: "https://github.com/SpaceZephyr/space-multi-design-ppt"
tags: "[ppt, slides, design, skill, agent-skills, html, pptx, pdf]"
timestamp: "2026-07-11T20:00:00Z"
---

# Space Multi-Design PPT（品牌设计驱动幻灯片 Skill）

## 它是什么

`SpaceZephyr/space-multi-design-ppt` 是一个**基于 Agent Skills 协议的品牌设计驱动幻灯片 Skill**。给定一篇文章 / BP / 周报等内容，让 agent 把它按 **62 种真实品牌设计语言**（参考 62 个真实品牌的视觉风格）生成可交付的演示稿：

- 输出格式：**HTML / PPTX / PDF**
- 输入：任意文本 / Markdown
- 风格：62 种品牌设计语言可选

## 为什么用它 / 适合什么场景

- 做 BP / 周报 / 汇报时，不想用千篇一律的「白底 + 黑色无衬线标题」。
- 想要 AI 直接出能交差的演示稿，而不是「草稿」还得手工调。
- 想批量产出多版设计风格，挑一个最合适的。

## 关键能力

| 能力 | 说明 |
|------|------|
| 62 种品牌设计语言 | 风格库，不是「shadcn 默认模板」翻版 |
| Agent Skills 协议 | 跟 Claude Code / Codex / Cursor 等 agent 集成 |
| 多格式输出 | HTML / PPTX / PDF |
| 多场景输入 | 文章 / BP / 周报等任意文本 |
| 可交付 | 输出直接发，无需再调 |

## 媒体参考

- 项目截图：

![Space Multi-Design PPT](https://pbs.twimg.com/media/HM1N50PbUAAuJ0l.jpg)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — 本概念遵循的协议
- [Hallmark](tool-hallmark-skill.md) — 通用设计纪律 skill
- [Apple Design Skill](tool-apple-design-skill.md) — Apple 平台专属设计原则 skill
- [Markdown Slides](tool-markdown-slides.md) — 另一款 Markdown 转幻灯片工具

## 项目链接

- 项目仓库：<https://github.com/SpaceZephyr/space-multi-design-ppt>