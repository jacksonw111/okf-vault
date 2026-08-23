---
type: Tool
title: "OpenViking（火山引擎上下文数据库）"
description: "火山引擎开源的「上下文数据库」，把 Agent 的记忆、文档资料、技能全部挂到一个 viking:// 虚拟文件系统下，让 Agent 像操作文件一样操作自己的上下文"
resource: "https://github.com/volcengine/OpenViking"
tags: [agent, context-database, virtual-filesystem, volcengine, memory]
timestamp: "2026-08-23T05:57:00Z"
---

# OpenViking（火山引擎上下文数据库）

## 它是什么

[volcengine/OpenViking](https://github.com/volcengine/OpenViking) 是火山引擎开源的**「上下文数据库」**：核心思路是把 Agent 的记忆、文档资料、技能全部挂到一个 `viking://` 虚拟文件系统下，让 Agent 像操作本地文件一样操作自己的上下文（增删查改、目录结构、按路径引用），而不是把所有上下文都塞进 prompt 的一段 blob。

## 为什么用它 / 适合什么场景

- 想给 Agent 一个**结构化、可寻址、可管理**的上下文层，而不是平铺的向量记忆。
- 想知道 Agent 当前上下文的精确构成（哪些是记忆、哪些是文档、哪些是技能），便于排查与调试。
- 想让 Agent 按「路径 / 文件语义」引用上下文，比"取最相似 top-k"更精确、更可解释。

## 关键能力

| 能力 | 说明 |
|------|------|
| 虚拟文件系统 | 把上下文挂到 `viking://` URI 上，Agent 把它当文件操作 |
| 统一承载 | 记忆 + 文档 + 技能三类上下文在同一文件系统下共存 |
| 文件式语义 | Agent 可以 ls / cat / edit / link，不是黑盒向量检索 |
| 可解释 | 上下文来源、组成、关系可读、可审计 |

## 媒体

- ![](https://pbs.twimg.com/media/HQUGotva0AAzudL.jpg)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — OpenViking 把技能也作为一类上下文挂载，统一调度
- [AI Media Assistant](./tool-ai-media-assistant.md) — 同样关注上下文组织与记忆的同类 AI 工作台

## 参考链接

- [项目链接](https://github.com/volcengine/OpenViking)
