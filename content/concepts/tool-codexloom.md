---
type: "Tool"
title: "Codexloom (yan5xu/codexloom)"
description: "解决 Codex 任务型 Agent 每次开新线程都要重建背景、补齐旧决策、重复付出冷启动成本的问题，把一条线程延续成跨任务累积知识的领域 Agent。"
resource: "https://github.com/yan5xu/codexloom"
tags: "[codex, ai-agent, persistent-context, cold-start, domain-agent, knowledge-accumulation]"
timestamp: "2026-08-04T20:30:00Z"
---

# Codexloom (yan5xu/codexloom)

## 它是什么

[Codexloom](https://github.com/yan5xu/codexloom) 解决 **Codex 任务型 Agent 每次开新线程都要重建背景、补齐旧决策、重复付出冷启动成本**的问题——**把一条线程延续成跨任务累积知识的领域 Agent**。

![Codexloom 截图](https://pbs.twimg.com/media/HOxgFeDa0AESvgE.jpg)

## 为什么用它 / 适合什么场景

- **冷启动成本高**：每次新线程都要把背景 / 决策 / 历史决定重新塞一遍。
- **知识零散丢失**：不同任务的决策散在多个线程里，复盘困难。
- **领域 Agent**：同一领域的任务希望"越用越懂"，而不是每次都"小白"。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨任务累积 | 把一个领域的知识沉淀下来 |
| 决策可追溯 | 历史决策不丢失 |
| 线程延续 | 不再每次开新线程都重头来 |
| 冷启动成本下降 | Agent 越来越"熟"，启动成本递减 |

## 参考链接

- [项目仓库](https://github.com/yan5xu/codexloom)

## 相关概念

- [Memmy Agent](./tool-memmy-agent.md) — 跨 AI 编程代理共享长期记忆中间层
- [OptMem](./tool-optmem.md) — 426 token prompt + 脚本极简跨会话记忆
- [ZestMem](./tool-zestmem.md) — Go 写的多 Agent 分布式持久化记忆服务
- [Sol Advisor](./tool-sol-advisor.md) — Codex subagent 双角色协作
