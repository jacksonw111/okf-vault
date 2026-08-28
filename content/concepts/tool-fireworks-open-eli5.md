---
type: Tool
title: "fireworks-open-eli5（带证据链的离线 HTML 讲解生成 Agent Skill）"
description: "yizhiyanhua-ai/fireworks-open-eli5：开源 Agent Skill，装进 Codex 或 Claude Code 后，agent 能把复杂系统讲成带证据、可交互的视觉故事，产出单个离线 HTML 文件；每个结论旁有来源与支持范围，读者可顺着链路核查。"
resource: "https://github.com/yizhiyanhua-ai/fireworks-open-eli5"
tags: [agent-skill, explanation, offline-html, evidence-chain, eli5, storytelling]
timestamp: "2026-08-27T15:46:00Z"
---

# fireworks-open-eli5

## 它是什么
[yizhiyanhua-ai/fireworks-open-eli5](https://github.com/yizhiyanhua-ai/fireworks-open-eli5) 是一个**开源 Agent Skill**——装进 **Codex** 或 **Claude Code** 等 Coding Agent 后，agent 能：

- 把**复杂系统**讲成**带证据、可交互的视觉故事**；
- 最终产出**单个离线 HTML 文件**（自带依赖、可直接分享）；
- 每个结论旁标注**来源**与**支持范围**——读者可顺着链路核查，不只是"信不信由你"。

## 为什么用它 / 适合什么场景
- 想让 AI 把一段复杂概念 / 系统讲清楚给非专业读者（团队新人 / 客户 / 学生）；
- 输出的讲解**带证据链**——可被审计 / 复核，不只是"AI 说了"；
- 想要**单个 HTML 文件**就能分享的产物——邮件附件、Slack 拖拽、内网传阅都方便；
- 想给 Coding Agent 加一个「教学 / 文档化」维度的能力。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill |
| 载体 | Codex / Claude Code 等 Coding Agent |
| 输入 | 任意复杂系统 / 概念 |
| 输出 | 单个离线 HTML 文件 |
| 视觉故事 | 可交互（节点 / 链路 / 注释） |
| 证据链 | 每结论旁标来源 |
| 支持范围 | 标注每个结论的可信度边界 |
| 可核查 | 读者顺着链接自查 |

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念本身
- [Story Engine](term-story-engine.md) — 把信息讲成故事 / 叙事的引擎；fireworks-open-eli5 是 Story Engine 在「带证据的离线讲解」方向的特化
- [Fact-Anchored Discovery Learning](playbook-fact-anchored-discovery-learning.md) — 教学法 playbook；fireworks-open-eli5 是 Skill 形态的"证据化讲解器"

## 参考链接
- 项目链接：<https://github.com/yizhiyanhua-ai/fireworks-open-eli5>
