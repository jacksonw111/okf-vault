---
type: "Tool"
title: "pi-pocket（基于 Pi Durable 的持久化口袋）"
description: "TannerMidd（lovelylogicss）开源：基于 Pi Durable 做的持久化口袋，每个模型 / 工具调用都是 checkpointed 任务；进程被 kill -9 杀掉，新进程能从同一 SQLite 接续执行，崩溃后可恢复而不错位。"
resource: "https://github.com/TannerMidd/pi-pocket"
tags: "[pi-agent, durable, checkpoint, crash-recovery, sqlite]"
timestamp: "2026-10-06T00:35:00Z"
---

# pi-pocket

## 它是什么

[pi-pocket](https://github.com/TannerMidd/pi-pocket) 是 **TannerMidd**（lovelylogicss）开源的「**持久化口袋**」——基于 **Pi Durable**，把每次模型 / 工具调用变成 checkpointed 任务，进程被 `kill -9` 后新进程能从同一 SQLite 接续执行。

## 关键能力

| 能力 | 说明 |
|------|------|
| Checkpoint | 每个模型 / 工具调用都是 checkpointed 任务 |
| 崩溃恢复 | `kill -9` 后新进程接续同一 SQLite |
| 测试可靠 | 中断的测试被标记为 interrupted 并自动重跑，已完成的不会重跑 |
| Multiplayer | 多用户协作天然支持（持久化共享状态） |
| 热扩展 | 工具 / 模型可热替换 |

## 适合场景

- 想做能「扛 -9」的 Agent 应用
- 多 Agent 协作需要持久化共享状态
- 测试 Agent 时要可恢复 / 可重启

## 参考链接

- 项目链接：<https://github.com/TannerMidd/pi-pocket>

## 相关概念

- [Pi Durable](./tool-pi-durable-cloudflare.md) — 底层运行时
- [Pi Pocket（笔记）](./note-pi-pocket-durable.md) — 同项目笔记