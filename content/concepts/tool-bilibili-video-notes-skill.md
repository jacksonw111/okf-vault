---
type: Tool
title: "Bilibili Video Notes Skill（B 站视频自动生成 DOCX 笔记）"
description: "投一个 B 站视频链接进去，自动生成带截图的 DOCX 笔记，不用自己边看边抄。"
resource: "https://github.com/asdhabdua/bilibili-video-notes-skill"
tags: [bilibili, video-notes, docx, agent-skill, llm, transcript]
timestamp: "2026-07-28T12:31:00.000Z"
---

# Bilibili Video Notes Skill

## 它是什么

一个把 **B 站视频链接**直接转成 **带截图的 DOCX 笔记**的 skill/工具：扔一个视频 URL 进去，自动跑完整链路，输出一份能直接打开看、可二次编辑的 Word 文档，免去边看边抄的痛苦。

![截图示例](https://pbs.twimg.com/media/HOSOYxpbsAAty3n.jpg)

## 它做了什么

1. 输入一个 B 站视频 URL
2. 自动拉取视频元数据 + 字幕 / 转录
3. 按时间轴抓取关键帧截图
4. 把字幕 + 关键帧嵌入模板化的 DOCX 笔记

## 适用场景

| 场景 | 价值 |
|------|------|
| 长视频课程（讲座 / 教程） | 自动把"看完"变成"看完且有笔记" |
| 访谈 / 播客 | 留可检索文字稿 + 关键画面 |
| 资料归档 | DOCX 便于二次编辑 / 分享 |
| Agent 工作流 | 让 LLM 自动消化 B 站长视频 |

## 关键能力

| 能力 | 说明 |
|------|------|
| URL → DOCX 一条龙 | 输入少，产出可编辑 |
| 截图嵌入 | 不只是纯文字笔记 |
| 自动转录 | 利用 B 站自身字幕 / 第三方 ASR |
| 可作为 Agent Skill | 在更大的 agent pipeline 里调用 |

## 原始链接

- [项目仓库](https://github.com/asdhabdua/bilibili-video-notes-skill)
- [推文剪藏](https://x.com/QingQ77/status/2082081385951707380)

## 相关概念

- [Obsidian Knowledge Agent](./tool-obsidian-knowledge-agent.md) — 把 PDF / 论文自动整理成 Obsidian 笔记的六阶段管道
- [SciCrucible](./tool-scicrucible.md) — 给 Claude Code 配科研文献阅读 skills
- [Anysearch Skill](./tool-anysearch-skill.md) — Agent 用的统一实时搜索 Skill
- [Claude Code Tipsy Skill](./tool-claude-code-tipsy-skill.md) — 同属 Agent Skills 生态的 Skill 包