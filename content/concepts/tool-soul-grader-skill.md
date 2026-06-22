---
type: "Tool"
title: "Soul Grader Skill（SOUL.md 结构化评分工具）"
description: "cobibean/soul-grader-skill —— Hermes Agent 社区技能，专门给 SOUL.md 身份文件做结构化评分（总分 100），考核使命清晰度、身份定义、核心论点、优先级排序、硬约束、权限边界、语气真实性等维度。"
tags: "[agent, hermes, soul-md, identity, scoring, skill, prompt-engineering]"
timestamp: "2026-06-22T16:04:00Z"
---

# Soul Grader Skill（SOUL.md 结构化评分工具）

## 它是什么

[`cobibean/soul-grader-skill`](https://github.com/cobibean/soul-grader-skill) 是一套 **Hermes Agent 社区技能**，专门给 `SOUL.md`（Agent 身份文件）做结构化评分，**靠评分标准说话，不靠感觉**。

评分维度（总分 100）：

| 维度 | 考察内容 |
|---|---|
| 使命清晰度 | Agent 是否清楚自己要做什么 |
| 身份定义 | 自我定位是否明确 |
| 核心论点 | 是否抓住核心立场 |
| 优先级排序 | 多个目标是否能排清主次 |
| 硬约束 | 绝对不能违反的边界 |
| 软偏好 | 风格倾向与典型选择 |
| 权限边界 | 可做 / 不可做的范围 |
| 语气真实性 | 是否与目标场景匹配 |
| 成功标准 | 怎样的输出算「合格」 |

## 为什么用它 / 适合什么场景

- **写作 SOUL.md 时反查**：写完跑一遍评分，看哪些维度欠缺。
- **审查现有 SOUL.md**：团队里多个 agent 的 SOUL.md 横向比较，找配置漏洞。
- **重写 SOUL.md**：根据评分输出定向补强。
- **教学**：把 SOUL.md 的「好」拆成可量化的 9 个维度，比纯靠感觉稳。

适合：

- Hermes Agent 用户维护自己的 SOUL.md
- 多 agent 团队的「身份治理」质量检查
- 研究 agent 行为可控性 / 可解释性的开发者

## 关键能力

| 能力 | 说明 |
|---|---|
| 结构化评分 | 总分 100 + 9 个维度打分 |
| 审查 | 发现 SOUL.md 中缺漏的边界 / 矛盾 |
| 重写建议 | 按维度给出补强方向 |
| 标准量化 | 把「好不好」变成可比较的数字 |
| Hermes Skill | 直接作为 Hermes Agent 技能挂载 |

## 与人工审查的对比

| 维度 | 人工感觉 | Soul Grader Skill |
|---|---|---|
| 一致性 | 换人换结果 | 同一份 SOUL.md 始终同分 |
| 可比较 | 难以横评 | 团队横向打分对比 |
| 颗粒度 | 「感觉差点」 | 9 维逐项诊断 |
| 教学 | 隐式经验 | 显式评分标准 |

## 参考链接

- [项目链接](https://github.com/cobibean/soul-grader-skill)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念元定义
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — filesystem-convention 的 Agent 框架（同属「agent 身份 / 配置文件约定」方向）
- [Cabinet](tool-cabinet.md) — Obsidian + AI 代理（身份文件作为 agent 上下文的实际承载方式）