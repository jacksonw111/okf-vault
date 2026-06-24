---
type: "Tool"
title: "Light-skills（科研全流程 AI 技能包）"
description: "适配 Claude Code 与 Codex 的 28 个科研 AI Skill，覆盖文献调研 → 数据分析 → 创新点 → 写作 / 绘图 / 排版 → 投稿返修全流程，背后垫 9 个可溯源知识库。"
resource: "https://github.com/Light0305/Light-skills"
tags: [skills, research, claude-code, codex, agent, academic]
timestamp: "2026-06-24T15:30:00Z"
---

# Light-skills（科研全流程 AI 技能包）

## 它是什么

[`Light0305/Light-skills`](https://github.com/Light0305/Light-skills) 是一套**适配 Claude Code 与 Codex 的科研全流程 AI 技能包**。把科研工作从「找文献」到「投稿返修」拆成 28 个互相衔接的 Skill，每个 Skill 包含：

- 可跑的脚本
- 可套的模板
- 真实范例
- 对应的可溯源知识库（共 9 个）

## 为什么用它 / 适合什么场景

- **不编造文献 / 数据**：背后垫可溯源知识库，agent 引用时不会 hallucinate 论文或数字；
- **覆盖全流程**：从文献调研 / 数据整理 / 创新点提炼 → 写论文 / 画图 / 排版 / 投稿 / 返修 → 软著 / 专利 / 答辩 PPT / 竞赛申报，每个环节都有专门 Skill；
- **跨客户端**：同一个 Skill 可以在 Claude Code 或 Codex 上跑，不需要重写。

## 关键能力

| 阶段 | 代表 Skill |
|---|---|
| 文献调研 | 检索 / 综述 / 引文管理 |
| 数据分析 | 数据清洗 / 统计 / 可视化 |
| 创新点 | 研究空白识别 / 假设生成 |
| 写作 | 论文 / 摘要 / 引言 / 方法 |
| 绘图 | 学术配图 / 流程图 / 实验图 |
| 排版 | 期刊模板 / 参考文献格式化 |
| 投稿返修 | Cover Letter / 审稿回复 |
| 软著专利 | 申请文档 / 权利要求 |
| 答辩竞赛 | 答辩 PPT / 汇报稿 |

## 媒体 / 参考链接

![流程示意](https://pbs.twimg.com/media/HLZnuwEaIAEiZU8.jpg)

- [项目链接](https://github.com/Light0305/Light-skills)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念元定义
- [Claude Code](tool-claude-code.md) — Light-skills 的目标客户端之一
- [mattpocock/skills](tool-mattpocock-skills.md) — 同类 Skill 合集
- [linXiv](tool-linxiv.md) — 本地优先学术论文管理工具，与本工具研究场景互补
- [obsidian-knowledge-agent](tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道把论文自动整理为 Obsidian 笔记
