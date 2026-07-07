---
type: Tool
title: "wenyi（Claude 长篇翻译工程）"
description: "用 Claude 翻译村上春树《夏帆》整本长篇小说的开源工程实践，主张用 LLM 重做翻译任务而非逐段润色。"
resource: "https://github.com/BigDawnGhost/wenyi"
tags: [translation, claude, long-form, llm]
timestamp: "2026-07-07T12:00:00Z"
---

# wenyi（Claude 长篇翻译工程）

## 它是什么
开源项目 `wenyi`——**用 Claude 模型完成一整本长篇小说（如村上春树《夏帆》）的翻译**，演示一种「把整本长篇视为一个工程任务」的实践：上下文分章、回写一致性、人名风格统一、专有名词表等都纳入仓库管理。

## 为什么用它 / 适合什么场景
- **"AI 翻译" 范式升级**：早期 AI 翻译按段切容易丢上下文和人物语气；wenyi 把整本视为一个 project。
- 可重放：所有 prompt、术语表、风格指南都纳入 Git 版本管理，可复现。
- 适合把任何 **长篇 / 章节结构作品**（小说 / 漫画台词 / 剧本）的翻译工作流水线化。
- 对翻译出版团队的参考价值：用 LLM 辅助时**怎么管"工程化一致性"**。

## 关键能力
| 能力 | 说明 |
|------|------|
| 整本上下文管理 | 不切碎段落，跨章节保留人物语气 / 时间线 |
| 术语 / 人名表 | 显式维护前后命名一致 |
| 风格指南嵌入 prompt | 用仓库内文控制"哪类词用哪类译法" |
| Git 可重放 | prompt 与术语表版本控制 |
| 实测作品 | 村上春树《夏帆》日文 → 简中（基于 Claude） |

## 相关概念
- [12-Factor Agents](tool-12-factor-agents.md) — HumanLayer 12 条让 Agent 从 demo 到实盘的工程原则
- [Light-skills](tool-light-skills.md) — 28 个科研全流程 AI Skill，从文献调研到投稿返修
