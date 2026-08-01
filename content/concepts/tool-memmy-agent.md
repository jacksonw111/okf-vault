---
type: Tool
title: "memmy-agent"
description: "MemTensor/memmy-agent，给所有 AI 编程代理（Claude Code / Codex / Cursor 等）共享同一套长期记忆的中间层，跨代理一次记住、到处用，避免每次切换都重新介绍自己。"
resource: "https://github.com/MemTensor/memmy-agent"
tags: "[ai-coding, long-term-memory, multi-agent, claude-code, codex, cursor, shared-memory]"
timestamp: "2026-08-01T20:30:00Z"
---

# memmy-agent

## 它是什么

[`MemTensor/memmy-agent`](https://github.com/MemTensor/memmy-agent) 是一个**跨 AI 代理的长期记忆中间层**：给 Claude Code / Codex / Cursor 等所有 AI 编程代理提供**同一套共享的长期记忆**，一次记住、到处用。解决「每次切换 AI 代理或重开会话就要重新介绍自己」的烦人问题。

## 解决什么痛点

- Claude Code 知道你的项目结构、代码风格，Codex 不知道
- 切换 AI 工具就要重新口述上下文
- 每个代理各自的 memory 文件格式互不兼容

## 关键设计

| 设计 | 说明 |
|------|------|
| 跨代理兼容 | 同时支持 Claude Code / Codex / Cursor 等主流 AI 编程工具 |
| 共享记忆库 | 一处写，多处读，所有代理共享同一份上下文 |
| 长期记忆 | 跨会话持久，不随单次对话结束丢失 |
| 中间层形态 | 不替代理执行，只是它们的「记忆外挂」 |

## 适合什么场景

- 同时用多个 AI 编程工具（Claude Code + Codex + Cursor），不想反复同步上下文
- 想让 AI 长期记住项目背景、代码风格、个人偏好
- 团队多人共用同一套「项目记忆」

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [OptMem](./tool-optmem.md) | 极简跨会话记忆 | 单文件 426 token prompt + 脚本 |
| [zestmem](./tool-zestmem.md) | 多 Agent 分布式持久化记忆服务 | Go 服务 + PostgreSQL + pgvector |
| [Agent Skills（代理技能包）](./term-agent-skills.md) | 技能包体系 | 静态「技能」而非「记忆」 |
| memmy-agent | 中间层 | 跨代理共享长期记忆 |

## 媒体

![memmy-agent 截图](https://pbs.twimg.com/media/HOhbR44acAAWdc-.jpg)

## 原始链接

- [项目仓库](https://github.com/MemTensor/memmy-agent)
- [原始推文](https://x.com/QingQ77/status/2083543520250572957)

## 相关概念

- [zestmem](./tool-zestmem.md) — 同样是多 Agent 记忆服务，zestmem 走分布式服务架构，memmy-agent 走轻中间层
- [OptMem](./tool-optmem.md) — 单文件极简方案，memmy-agent 是它的「多代理版」
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 技能 ≠ 记忆，但都是「让代理更好用」的外挂