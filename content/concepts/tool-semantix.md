---
type: Tool
title: "Semantix"
description: "编码 Agent 的会话级记忆与缓存优化器：把跑完的会话拆成可复用片段存进本地库，下次碰到相似任务自动塞回上下文，同时把注入顺序与前缀整理得逐字节稳定，让云缓存命中率提升、token 成本下降。"
resource: "https://github.com/Gnosil/semantix"
tags: [agent-memory, prompt-cache, llm-cache, code-agent, cost-reduction]
timestamp: 2026-09-02T12:00:00Z
---

# Semantix

## 它是什么

编码 Agent 关掉会话就失忆——每次新会话都从零拼上下文；而且 LLM provider 的 prompt cache 通常只对一字不差的前缀有效，头部改个标点、注入顺序换一换，整段缓存就作废。`Semantix` 解决这两个问题：把已跑完的会话按"可复用片段"切分存进本地库，下次接到相似任务时按语义检索自动塞回上下文；同时把片段的注入顺序、注入前缀整理成逐字节稳定的形式，让云缓存能命中。

## 关键能力

| 能力 | 说明 |
|------|------|
| 会话切分复用 | 跑完的会话拆成可复用片段，本地库语义检索 |
| 前缀字节稳定 | 把上下文整理成逐字节一致的注入顺序，触发云缓存 |
| 跨会话记忆 | 给"无状态 Agent"补一层轻量长期记忆 |

## 项目链接

- [项目主页](https://github.com/Gnosil/semantix)

## 相关概念

- [Perenna](./tool-perenna.md) — 跨 AI 编程客户端的长期记忆方案
