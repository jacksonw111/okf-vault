---
type: "Tool"
title: "PAXM（编码 Agent 跨工具持久化记忆层）"
description: "不绑定任何厂商的持久化记忆层，让 Codex、Claude Code、OpenCode、Pi、ZCode 等编码 Agent 跨会话、跨工具共享项目决策和上下文；本机即可部署。"
resource: "https://github.com/pax-beehive/paxm"
tags: "[agent, memory, persistence, cross-tool, codex, claude-code, pi]"
timestamp: "2026-07-20T20:20:00Z"
---

# PAXM（编码 Agent 跨工具持久化记忆层）

## 它是什么

[pax-beehive/paxm](https://github.com/pax-beehive/paxm) 是一个**厂商无关的持久化记忆层**，面向编码 Agent。它解决「各家编码 Agent（Codex、Claude Code、OpenCode、Pi、ZCode 等）都各自记忆、互不共享」的痛点——任何一家 agent 写入的项目决策、上下文、习惯都可被其它 agent 读到。

## 关键能力

| 能力 | 说明 |
|------|------|
| 厂商中立 | 不绑定 Codex / Claude Code / OpenCode / Pi / ZCode 任一家 |
| 跨会话 | 同一 agent 跨多次会话共享记忆 |
| 跨工具 | 不同 agent 间共享决策 / 上下文 |
| 本机部署 | 不依赖云服务，本机即可跑 |

![PAXM 截图](https://pbs.twimg.com/media/HNg7FjXa4AAMG4x.jpg)

## 相关概念

- [TencentDB Agent Memory](./tool-tencentdb-agent-memory.md) — 腾讯云四层渐进式 Agent 记忆方案
- [Notebrain CLI](./tool-notebrain-cli.md) — 把 Obsidian 笔记库离线索引到 ChromaDB，给 agent 提供语义搜索
- [AI Agent Guide](./tool-ai-agent-guide.md) — 21 章中文 Agent 教程，含 MCP / Skills / 多 Agent / RAG / 记忆章节

## 参考链接

- 项目链接: <https://github.com/pax-beehive/paxm>
