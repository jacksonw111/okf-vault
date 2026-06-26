---
type: Tool
title: "paper-lifecycle（论文写作 Codex Skills 套件）"
description: "面向学术写作的 Codex skills suite：Review Revision 像审稿人一样看初稿（问题真伪 / insight 站不站得住 / novelty / 方法 / 实验 / 写作），Rebuttal 给出审稿意见回复策略。"
resource: "https://github.com/M1n-n9/paper-lifecycle"
tags: [academic, paper, codex, skill, writing, research]
timestamp: 2026-06-26T16:50:00Z
---

# paper-lifecycle

## 它是什么

paper-lifecycle 是为学术论文写作提供的 **Codex skills 套件**，目标是把"找审稿人帮看稿 → 回复审稿意见"这一最难的两步**自动化**。包含两个核心 skill：

| Skill | 角色 | 干的活 |
|-------|------|--------|
| `Review Revision` | 审稿人 | 模拟同行评审：问题真不真、insight 站不站得住、novelty 有没有、方法跟机制对不对、实验够不够支撑、写作有没有把审稿人带偏 |
| `Rebuttal` | 作者 | 给出针对审稿意见的回复策略，怎么反驳、怎么补充实验、怎么调整话术 |

## 为什么用它

| 痛点 | paper-lifecycle 解法 |
|------|---------------------|
| 找不到同领域朋友帮看稿 | 让 Codex 扮演审稿人 |
| 担心 novelty / 方法 / 实验被审稿人挑刺 | 提前按审稿人视角体检 |
| 收到 R1 不知道怎么回 | 用 `Rebuttal` 生成回复策略草稿 |
| 写作把审稿人带偏 | 由"审稿人 Skill"指出具体偏差点 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 审稿式体检 | 六维评审：问题真伪 / insight / novelty / 方法 / 实验 / 写作 |
| Rebuttal 策略 | 把每条审稿意见变成可回复的策略 |
| Codex 原生 | 走 Codex skill 体系，配套 IDE/CLI 即用 |
| 学术场景 | 术语与判断标准都贴 ML / CS 顶会习惯 |

## 原始链接

- [项目仓库](https://github.com/M1n-n9/paper-lifecycle)
- [原始推文剪藏](https://x.com/QingQ77/status/2070382045700948287)

## 相关概念

- [Light-skills](./tool-light-skills.md) — 28 个科研全流程 AI Skill（含文献调研到投稿返修），paper-lifecycle 是"写作 + 评审"环节的精修版
- [happy-figure-skill](./tool-happy-figure-skill.md) — 同属 Codex/Skill 生态，但聚焦"科研配图"而非"科研写作"
- [ExamPrep-AI](./tool-exam-prep-ai.md) — 同样把"主观题 / 客观题自动化打分"，但场景是备考
