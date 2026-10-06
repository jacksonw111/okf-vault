---
type: "Note"
title: "Pi Pocket（Pi Durable 上的「持久化口袋」）"
description: "lovelylogicss 基于 Pi Durable 做的 Pi Pocket 0.2.0：每个模型调用与工具调用都是 checkpointed 任务；进程被 -9 杀掉，新进程从同一 SQLite 文件接续执行；测试可从中断点恢复而不重复。"
resource: "https://earendil.com/posts/pi-durable"
tags: "[pi-agent, durable, checkpoint, crash-recovery, sqlite, agent-runtime]"
timestamp: "2026-10-06T00:35:00Z"
---

# Pi Pocket

## 它是什么

[Pi Pocket](https://github.com/TannerMidd/pi-pocket) 是 **lovelylogicss** 基于 **Pi Durable** 做的「持久化口袋」——0.2.0 版本把 **Lancet Guard 默认关掉、邀请码更易识别、官网覆盖 Pi Durable**。

## 核心特性

| 特性 | 说明 |
|------|------|
| Checkpointed | 每个模型调用与工具调用都是 checkpointed 任务 |
| 崩溃恢复 | `kill -9` 服务器后新进程从同一 SQLite 文件接续 |
| 测试可恢复 | 中断的测试被标记为 interrupted 并重跑，已完成的不会重跑 |
| 协作 | 多玩家模式（multiplayer）天然实现 |
| 扩展 | 工具可热插拔 |

## 与 Pi Durable 的关系

- **Pi Durable**：底层持久化运行时（由 earendil / pidotdev 维护）
- **Pi Pocket**：基于其上的具体产品演示 + 增强

## 适合场景

- 想做能「扛 -9」不丢进度的 Agent 应用
- 多 Agent 协作场景需要持久化共享状态
- 测试 Agent 系统时想要可恢复 / 可重启

## 参考链接

- 项目链接：<https://github.com/TannerMidd/pi-pocket>
- Pi Durable 介绍：<https://earendil.com/posts/pi-durable>

## 相关概念

- [Pi Durable](./tool-pi-durable-cloudflare.md) — 底层运行时
- [pi-durable-book](./note-pi-durable-book.md) — 中文手册