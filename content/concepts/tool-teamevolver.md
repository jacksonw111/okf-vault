---
type: Tool
title: "teamEvolver"
description: "把团队真实 Agent 使用记录沉淀成可版本管理的共享 Skill 与团队 Memory，解决 Agent 能力无法在团队内复用与治理的问题。"
resource: "https://github.com/leoriczhang/teamEvolver"
tags: [agent, team, skills, memory, sharing, governance]
timestamp: "2026-08-24T13:16:00Z"
---

# teamEvolver

## 它是什么

[leoriczhang/teamEvolver](https://github.com/leoriczhang/teamEvolver) 是面向「Agent 团队协作」的 Skill 与 Memory 沉淀工具：把每个成员用 Agent 的真实记录（成功的修复、跑过的任务、踩过的坑）抽取出来，经过验证后沉淀为团队共享的 Skill 条目与团队 Memory，按版本管理的方式更新 / 复盘 / 共享。

## 为什么用它 / 适合什么场景

- 团队里多个成员都在用 Claude Code / Codex / Hermes 类 Agent，但每个人的 Skill / Memory 各自藏在本地，新成员加入要从零积累。
- 想要一个能「自动从使用记录里抽经验 → 人工验证 → 入库 → 全员共享」的闭环。
- 想让 Agent 能力可以「在公司层面治理」——知道团队都用哪些 Skill、效果如何、谁贡献的。

## 关键能力

| 能力 | 说明 |
|------|------|
| 使用记录抽取 | 从 Agent 历史会话里抽取出可复用的技能片段 |
| 验证流程 | Skill 入库前需要人工或自动验证 |
| 版本管理 | Skill / Memory 走 Git 风格的版本演进，可回滚 |
| 团队分发 | 验证通过后全团队成员下次启动 Agent 自动拉取 |
| 治理仪表盘 | 哪些 Skill 用得多、效果好、过期需要清理 |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的标准化定义
- [SkillCorpus](./tool-skillcorpus.md) — 公开 SKILL.md 的可信技能库
- [Harness Router](./tool-harness-router.md) — 多 Agent harness 统一入口

## 参考链接

- [项目链接](https://github.com/leoriczhang/teamEvolver)
- ![](https://pbs.twimg.com/media/HQdASwLbMAElGa5.jpg)