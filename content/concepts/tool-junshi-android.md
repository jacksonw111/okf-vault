---
type: Tool
title: "军师 (Junshi) Android"
description: "面向个人使用的关系分析与沟通辅助 Android App，档案、聊天、图片、API 配置默认存在设备本地，只有主动调用 AI 时内容才发到用户自己填写的服务地址；先把事实 / 情绪 / 未知分开，再决定下一步怎么做。"
resource: "https://github.com/SouthautumnYa/junshi-android"
tags: [android, relationship, ai-assistant, local-first, privacy]
timestamp: "2026-08-03T13:18:00Z"
---

# 军师 (Junshi) Android

## 它是什么
军师（`SouthautumnYa/junshi-android`）是一个面向个人使用的关系分析与沟通辅助 Android App。**档案、聊天、图片和 API 配置默认都存在设备本地**，只有主动调用 AI 功能时，内容才会发到用户自己填写的服务地址。

核心思路：先把关系里的**事实、情绪和未知分开**，再决定下一步怎么做——而不是直接给「勇敢追 / 赶紧分」二选一的情绪化建议。

![军师界面](https://pbs.twimg.com/media/HOsyTPlaEAAoA_8.jpg)

## 为什么用它 / 适合什么场景
- **本地优先 + 隐私优先**：数据默认不上云，AI 调用走用户自配服务。
- **分层分析**：把事实 / 情绪 / 未知解耦，分别给出可执行建议。
- **个人而非企业**：面向单人使用，不做团队协作 / CRM 之类的功能。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先存储 | 档案、聊天、图片、API 配置默认在设备本地 |
| 自配 AI 服务 | AI 调用由用户填写的服务地址处理 |
| 事实 / 情绪 / 未知拆分 | 关系分析显式分三层，避免情绪化判断 |
| 行动建议 | 输出「下一步做什么」，而非笼统建议 |
| 聊天复盘 | 导入沟通记录后做结构化分析 |

## 项目链接
- <https://github.com/SouthautumnYa/junshi-android>

## 相关概念
- [goutoujunshi (狗头军师)](./tool-goutoujunshi.md) — 同为「先共情再分析」的关系向 AI Skill，本工具是 Android 客户端形态
- [Dating Coach Skill](./tool-dating-coach-skill.md) — Claude Skill 的聊天记录分析向路线
- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的概念元定义
