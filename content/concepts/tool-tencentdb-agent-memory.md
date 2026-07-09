---
type: Tool
title: "TencentDB-Agent-Memory（腾讯开源的 AI Agent 四层渐进式记忆方案）"
description: "腾讯云开源的 Agent 记忆方案，按短期/中期/长期/永久四层渐进式流水线解决 LLM Agent 的长短期记忆难题。"
resource: "https://github.com/TencentCloud/TencentDB-Agent-Memory"
tags: "[agent, memory, llm, tencent, tencentdb, long-term-memory, short-term-memory]"
timestamp: "2026-07-09T20:50:00Z"
---

# TencentDB-Agent-Memory（腾讯开源的 AI Agent 四层渐进式记忆方案）

## 它是什么
`TencentCloud/TencentDB-Agent-Memory` 是腾讯开源的 **AI Agent 长期记忆基础设施**。它把记忆拆成 **四层**，按时间尺度和稳定性渐进式沉淀，从瞬时对话上下文一直延伸到「关键决策和教训」永久层。

## 四层记忆

| 层级 | 内容 | 典型场景 |
|------|------|---------|
| 短期 | 当前对话上下文 | 一轮 / 多轮对话内的事 |
| 中期 | 最近几天的任务 | 用户偏好、工作节奏、临时任务进度 |
| 长期 | 核心知识和偏好 | 用户身份、技能栈、长期目标 |
| 永久 | 关键决策和教训 | 永久性的事实约束、踩过的坑 |

## 为什么用它 / 适合什么场景
- Agent 跑得越久**越容易丢上下文**：四层分治让 Agent 知道「什么时候忘掉 / 什么时候记住」。
- 想做「真·个人助理」Agent，不希望每次开新会话一切归零。
- 想做团队级 Agent，让不同 Agent 实例之间共享长期与永久记忆。
- 中期记忆（几天级）很少开源方案覆盖，是本项目的差异点。

## 关键能力
| 能力 | 说明 |
|------|------|
| 四层记忆管线 | 短 / 中 / 长 / 永，按时间尺度分治 |
| 渐进式沉淀 | 信息自然从短→中→长→永流转 |
| 配套 TencentDB | 后端可对接腾讯云数据库族（也可扩展到自托管） |
| GitHub 开源 | 仓库与文档在 GitHub 公开维护 |

## 相关概念
- [Recall](tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆插件，TextRank 摘要注入
- [Brigade](tool-brigade.md) — 本地 AI 代理团队 + Tideline 共享长期记忆
- [EverOS](tool-everos.md) — 统一的本地长期记忆层，让不同 agent 共享并进化记忆
- [second-brain-cloudflare](tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源共享记忆层
- [EchoesVault（OpenCode 持久记忆）](tool-echoes-vault-opencode.md) — OpenCode 持久记忆插件

## 参考链接
- 项目链接：<https://github.com/TencentCloud/TencentDB-Agent-Memory>
- 原始介绍：<https://x.com/AgentWangCN/status/2075036169067454552>
