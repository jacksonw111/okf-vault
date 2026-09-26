---
type: "Note"
title: "Anthropic FDE 写的 AI 时代代码现代化最佳实践"
description: "Anthropic 官博文章：Forward Deployed Engineer 团队总结的 AI 驱动代码现代化项目准备清单——覆盖遗留代码摸底、风险评估、AI 工具链选型、迁移策略、回滚预案。"
resource: "https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects"
tags: "[anthropic, fde, code-modernization, legacy-code, ai-coding, migration, claude]"
timestamp: "2026-09-26T21:55:00Z"
---

# Anthropic FDE 写的 AI 时代代码现代化最佳实践

## 它是什么

[Anthropic 官博](https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects) 上的 FDE（Forward Deployed Engineer）总结的 **AI 驱动代码现代化项目准备清单**——面向「**用 Claude / Agent 重写 / 迁移遗留代码**」的项目负责人。

## 涵盖要点

- **遗留代码摸底**：依赖关系、调用拓扑、热点路径
- **风险评估**：哪些模块可以放手让 AI 改、哪些必须人工把关
- **AI 工具链选型**：Claude Code / Codex / Cursor 在不同迁移阶段的取舍
- **迁移策略**：绞杀者模式（Strangler Fig） / 大爆炸 / 并行切换
- **回滚预案**：每个阶段必须有可回退的快照与契约测试

## 为什么读 / 适合什么场景

- 手里有一个**多年遗留系统**想用 AI 重写——不想「**重写到一半发现跑不起来**」。
- 想给 CTO / VP 一份「**上 AI 之前要准备什么**」的清单。
- FDE 这类「**被派到客户现场解决问题**」的角色总结的实战经验比纯理论更落地。
- 和 [Claude Code 创业公司指南](./note-claude-code-startups-guide.md) 互补——后者偏「**早期怎么用 AI 写代码**」，本条目偏「**老代码怎么迁移到 AI 时代**」。

## 相关概念

- [Claude Code 创业公司指南](./note-claude-code-startups-guide.md) — 早期用 Claude Code 写新代码的实战指南
- [FDE 入门 / 实战手册](./note-fde-101-dotey.md) — FDE 这条职业路径的能力地图
- [Top 10 系统设计资源清单](./note-system-design-resources.md) — 现代化项目背后依然要遵守的系统设计原则