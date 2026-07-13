---
type: Tool
title: "readme-roast"
description: "Claude Code 技能：用 8 种人设（戈登·拉姆齐、侦探、毒舌前任等）犀利吐槽你的 README，同时给出诚实度评分、替代版本和可立刻动手的改进建议。"
tags: "[claude-code, skill, readme, documentation, review, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/KorroAi/readme-roast"
---

# readme-roast

一个 **Claude Code 技能（Skill）**——把"审视 README"这件苦事包装成 8 种**角色扮演吐槽**（戈登·拉姆齐、侦探、毒舌前任……），输出包含**诚实度评分**、**可直接替换的备选版本**、**立刻能动手的改进建议**。

## 它是什么

- 一个 Claude Code Skill，安装后可在仓库里直接调用；
- 把 README 评审做成"**多视角毒舌 + 可执行建议**"两段式输出。

## 关键能力

| 能力 | 说明 |
|------|------|
| 8 种人设视角 | 戈登·拉姆齐、侦探、毒舌前任等不同角色轮流开炮 |
| 诚实度评分 | 给 README 一个"这人/这项目文档有多不靠谱"的量化打分 |
| 备选版本 | 直接生成**可拿来替换**的 README 改写稿 |
| 可执行改进 | 列出"今天就能动手"的具体修改项 |
| Claude Code 原生 | 装上 Skill 即可在 cc 里直接用 |

## 适合什么场景

- 项目 README **自己看不下去了**但又没空重写——让它先骂一遍逼你动手；
- 给开源项目提 PR 前想**自检 README 是否够好**；
- 团队规范要求 README 达到某条线——拿它当"发布前体检"。

## 输出结构（典型）

1. 8 段吐槽（每段以人设身份出发的反馈）
2. 诚实度评分（如 6.2 / 10）
3. 备选 README（直接覆盖即可）
4. Top-N 改进项（按优先级排序）

## 预览

![](https://pbs.twimg.com/media/HM_EbIlakAAN0XX.jpg)

## 相关概念

- [Claude Code Tipsy Skill](tool-claude-code-tipsy-skill.md) — 同为 Claude Code Skill，针对"提示词调优"
- [Claude Code Best Practice](tool-claude-code-best-practice.md) — Skill 写法与使用最佳实践
- [Fable Method](tool-fable-method.md) — 把模型解题方式工程化为通用 Skill 的另一类思路
