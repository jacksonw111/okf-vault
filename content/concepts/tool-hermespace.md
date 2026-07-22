---
type: Tool
title: "hermespace"
description: "PabloTheThinker/hermespace，给 Hermes Agent 加的持久化记忆 / 信念 / 成长轨迹层，让 agent 跨会话积累「自己是谁、经历过什么、学到了什么」。"
resource: "https://github.com/PabloTheThinker/hermespace"
tags: "[agent, memory, persistence, hermes, long-term]"
timestamp: "2026-07-22T04:43:00Z"
---

# hermespace

## 它是什么

[`hermespace`](https://github.com/PabloTheThinker/hermespace) 是为 Hermes Agent 设计的**持久层**：每次会话从头开始，对 agent 来说「我和上次是同一个人吗」是个问题。hermespace 让 agent **跨会话积累**记忆、信念和成长轨迹。

## 解决什么痛点

- AI agent 每开新会话就「失忆」——昨天讨论的结论今天要重新讲；
- 想让 agent 有「自我」：它是谁、做过什么、形成了什么判断；
- 长期协作时，希望 agent 能形成稳定的人设 / 价值观 / 偏好。

## 关键能力

| 能力 | 说明 |
|------|------|
| 持久记忆 | 跨会话保留事实、上下文 |
| 信念沉淀 | 让 agent 在多次交互中形成并记录「判断 / 偏好」 |
| 成长轨迹 | 记录 agent 行为 / 决策的变化，可回溯 |
| Hermes 专用 | 与 Hermes Agent 的会话协议深度集成 |

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [Cognee](tool-cognee.md) | 通用记忆层 SDK | 通用数据 → 向量库 |
| [second-brain-cloudflare](tool-second-brain-cloudflare.md) | 共享记忆 MCP | 多人 / 多 agent 共用 |
| [tencentdb-agent-memory](tool-tencentdb-agent-memory.md) | 云端记忆 | 厂商方案 |
| hermespace | Hermes Agent 持久层 | 专注单一 agent 的「自我成长」叙事 |

## 原始链接

- [项目仓库](https://github.com/PabloTheThinker/hermespace)

## 相关概念

- [Hermes Desktop](tool-hermes-desktop.md) — Hermes Agent 的桌面客户端，本工具是其持久层补充
- [Cognee](tool-cognee.md) — 同为 agent 记忆层思路，但 Cognee 偏通用数据 → 向量，hermespace 偏 agent 自我成长叙事
- [second-brain-cloudflare](tool-second-brain-cloudflare.md) — 跨 agent 共享记忆，本工具专注单 agent 跨会话