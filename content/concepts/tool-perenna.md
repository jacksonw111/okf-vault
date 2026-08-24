---
type: Tool
title: "Perenna"
description: "把跨 AI 编程客户端的长期记忆放进用户自己掌控的 Git 仓库：避免换客户端 / 换机器就把记忆丢光。"
resource: "https://github.com/scarletkc/Perenna"
tags: [agent-memory, git, portability, cross-client, open-source]
timestamp: "2026-08-24T01:31:19Z"
---

# Perenna

## 它是什么

[scarletkc/Perenna](https://github.com/scarletkc/Perenna) 是给 AI 编程客户端（Claude Code / Codex / Cursor / Continue 等）做的**用户自掌控记忆层**：把跨客户端共享的长期记忆放进用户自己的 Git 仓库里，不再依赖厂商封闭存储。换客户端 / 换机器时只要 `git pull`，记忆就回来了。

## 为什么用它 / 适合什么场景

- 痛恨「AI 编程工具的记忆各自存在厂商封闭存储里，换客户端 / 换机器就丢」。
- 想用 Git 的版本控制能力来回滚 / 审计 / diff Agent 记忆。
- 想用一个统一协议跨 Claude Code / Codex / Cursor 等多个客户端共享同一份长期记忆。
- 想完全掌控自己的 AI 编程历史，不被厂商绑定。

## 关键能力

| 能力 | 说明 |
|------|------|
| Git 仓库存储 | 记忆以 Markdown / JSON 形式存进 Git 仓库 |
| 客户端无关 | 同一个仓库可被 Claude Code / Codex / Cursor 同时读写 |
| 版本管理 | 记忆变更天然带 Git diff，可回滚 / 审计 |
| 自托管 | 仓库在自己手里，不依赖任何第三方云 |
| 跨机器同步 | 一处 push，多处 pull，记忆跟着人走 |

## 相关概念

- [KITE / memoket-kite](./tool-kite-memoket.md) — 同样强调「记忆不被厂商绑定」的非向量记忆方案
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 与 Skill 生态打通
- [Harness Router](./tool-harness-router.md) — 多个 harness 共享上下文的统一入口

## 参考链接

- [项目链接](https://github.com/scarletkc/Perenna)