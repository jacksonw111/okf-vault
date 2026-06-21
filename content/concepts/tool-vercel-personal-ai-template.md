---
type: "Tool"
title: "Vercel Labs Personal AI Template（持久化个人助手模板）"
description: "Vercel Labs 出品的开源模板，用来构建持久的个人 AI 智能体：支持 Web 聊天 / Slack / iMessage / Linear 集成，长期记忆功能可手动导入或由智能体提议存储（每条需用户确认），底层基于 Eve 框架 + Nuxt + Better Auth，可一键部署到 Vercel 或自托管。"
resource: "https://github.com/vercel-labs/personal-ai-template"
tags: "[vercel, eve, nuxt, personal-assistant, template]"
timestamp: "2026-06-21T00:00:00Z"
---

# Vercel Labs Personal AI Template（持久化个人助手模板）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 **Vercel Labs** 开源模板：**Personal AI Template** —— 用来构建**持久的个人 AI 智能体**。和 Eve 框架（filesystem convention 的 Agent runtime）配套使用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 接入渠道 | Web 聊天、Slack、iMessage、Linear |
| 长期记忆 | 用户手动导入，或由智能体提议存储（**每条都需要用户明确确认**） |
| 底层框架 | **Vercel Eve** + Nuxt + Better Auth |
| 部署 | 一键部署到 Vercel，或自托管 |

## 记忆机制亮点

> 「每条记录都需要用户明确确认」—— 避免 AI 自动乱写记忆、污染上下文。

Agent 只能 **提议** 存储某条记忆，用户**显式确认**才落盘。

## 适用场景

- 想搭一个 **个人 AI 助手**，跨多个渠道（Slack / iMessage / Web）响应。
- 想要长期记忆但不愿意让 AI 自动写 —— 这个模板的「每条需确认」设计正中需求。
- 想在 Vercel 上快速 prototype。

## 相关概念

- [Vercel Eve 框架](tool-vercel-eve-framework.md) — 本模板的 Agent runtime
- [agentcn](tool-agentcn.md) — 也构建在 Eve 之上的 UI registry
- [Niamos](tool-niamos.md) — 同样把个人 AI 助手模板塞进文件夹结构（Obsidian 版）
- [Agent Skills（代理技能包）](term-agent-skills.md) — 跨渠道 / 长期记忆是 Skill 生态的标准能力