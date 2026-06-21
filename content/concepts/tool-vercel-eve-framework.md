---
type: "Tool"
title: "Vercel Eve（filesystem convention 的 Agent 框架）"
description: "Vercel 推出的 AI Agent 框架，核心思路是用文件系统约定替代复杂配置：一个 Agent = agent/ 目录下的 instructions.md / tools/ / skills/ / channels/ / schedules/ 几组文件，可维护、可扩展、持久化。"
resource: "https://eve.vercel.com"
tags: "[agent, vercel, eve, filesystem-convention, framework]"
timestamp: "2026-06-21T00:00:00Z"
---

# Vercel Eve（filesystem convention 的 Agent 框架）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐、Vercel 出品的 AI Agent 框架。它的核心信条是 **「用文件系统约定替代复杂配置」** —— 一个 Agent 就是 `agent/` 目录下的一组文件，不需要写大量 YAML、不需要 IDE 配置面板。

## 文件系统约定

```
agent/
├── instructions.md   # 系统提示词（纯 Markdown）
├── tools/            # 类型安全的工具函数
├── skills/           # 按需加载的 Skill 流程
├── channels/         # 消息接入（Slack / Web / Email……）
└── schedules/        # 定时任务
```

每个文件 / 目录的角色由 **约定（convention）** 而不是配置决定 —— 就像 Next.js 的 `app/` 目录、Rails 的 `app/controllers/`。

## 关键卖点

- **可维护**：所有 Agent 行为以文件形式存在，diff / PR / code review 都自然成立。
- **可扩展**：加一个 tool / skill / channel，就是加一个文件，不需要改主程序。
- **持久化**：Agent 状态天然落到磁盘，重启不丢。
- **类型安全**：tools/ 是类型安全的 TypeScript 函数，不是松散的脚本。

## 适用场景

- 想建「长期跑、有人维护」的 Agent，而不是一次性 demo。
- 团队里有多人协作开发 Agent —— 文件系统约定让 merge conflict 自然可处理。
- 想要「把 Agent 配置像代码一样 review」—— instructions.md 的改动可以走 PR。

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Eve 的 skills/ 目录是该概念的工程化实现
- [agentcn](tool-agentcn.md) — 构建在 Eve 之上的 shadcn 风格 UI registry
- [Vercel Labs Personal AI Template](tool-vercel-personal-ai-template.md) — 用 Eve + Nuxt 搭的开箱即用个人助手
- [Niamos](tool-niamos.md) — 同样把 AI Agent 模板塞进文件夹结构的思路（Obsidian 版）