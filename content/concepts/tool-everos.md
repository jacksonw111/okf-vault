---
type: "Tool"
title: "EverOS（EverMind-AI/EverOS）"
description: "为 AI 代理提供统一的本地长期记忆层，让不同 agent 共享并持续进化记忆；可作为 Hermes 等多代理框架的记忆底座。"
resource: "https://github.com/EverMind-AI/EverOS"
tags: [agent, memory, local-first, hermes, multi-agent]
timestamp: "2026-06-23T15:30:00Z"
---

# EverOS（EverMind-AI/EverOS）

## 它是什么

面向 AI 代理的「统一本地长期记忆层」。它把不同 agent 各自零散的记忆汇总到一处共享存储，让记忆在不同代理之间流动与进化；可作为 Hermes 等多代理框架的记忆底座使用。

## 为什么用它 / 适合什么场景

- **多代理记忆共享**：让一组 agent（Hermes、Claude、GPT 等）共用同一份长期记忆；
- **记忆可持续进化**：每次新会话都会被归档、检索、再喂回代理，避免上下文丢失；
- **本地优先**：无需把数据丢到云端 SaaS；
- **可作为框架组件**：集成到现有 agent 运行时，而不是从零搭。

## 关键能力

| 能力 | 说明 |
|------|------|
| 统一记忆层 | 不同代理共享同一份长期记忆 |
| 记忆进化 | 持续归档 / 检索 / 重喂 |
| 本地优先 | 不依赖云服务 |
| 框架适配 | 可接入 Hermes 等多代理框架 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/EverMind-AI/EverOS>

## 相关概念

- [Recall](concepts/tool-recall-claude-code.md) — 同属「为 AI 代理提供长期记忆」赛道（Recall 专攻 Claude Code，EverOS 更通用）
- [Brigade](concepts/tool-brigade.md) — 同样把多代理记忆作为核心抽象（Brigade 自带 Tideline 协议）
- [ORGII](concepts/tool-orgii.md) — 多 Agent 协作框架，可与 EverOS 配套使用
- [Agent Skills](concepts/term-agent-skills.md) — 记忆层之上的工作流打包方式