---
type: Tool
title: "Dormice（本地冷冻沙箱，按需快速恢复）"
description: "云沙箱按秒收费、用完就丢、回回冷启动。Dormice 把沙箱跑在用户机器上，空闲就自动冷冻，恢复只要 50 毫秒，搁着不花钱。"
resource: "https://github.com/BitMiracle-AI/Dormice"
tags: [sandbox, local-first, agent-runtime, cgroups, freezer]
timestamp: "2026-07-29T03:40:00.000Z"
---

# Dormice

## 它是什么

一种**本地沙箱思路**：把沙箱跑在用户自己的机器上，**空闲时自动冷冻（freeze）**，**恢复只要 50 毫秒**。

> 云沙箱按秒收费，用完就丢，回回冷启动。Dormice 换了个思路。

## 与云沙箱对比

| 维度 | 云沙箱 | Dormice |
|------|--------|---------|
| 计费 | 按秒 | 零成本（本地空闲） |
| 冷启动 | 秒级 | 50ms |
| 数据落地 | 远端 | 本机 |
| 隔离 | 进程级 / 容器 | 进程级 / 容器 |
| 适合 | 一次性任务 | 长生命周期 + 频繁调度 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地运行 | 沙箱在用户机器上 |
| 空闲冷冻 | 用 Linux cgroup freezer 之类机制暂停进程 |
| 50ms 恢复 | 不重新启动，复用冻结状态 |
| 零持续成本 | 搁着不烧钱 |
| 适合 agent 频繁调用 | 调一次沙箱「唤起」、用完「冻回去」 |

## 适用场景

- **agent 工作流**：每次工具调用开一次沙箱、用完冻回去，下次再调又 50ms 唤起
- **CI / 自动化**：长生命周期 pipeline 的中间步骤
- **本地开发**：避免容器冷启动拖慢开发循环

## 原始链接

- [项目仓库](https://github.com/BitMiracle-AI/Dormice)
- [推文剪藏](https://x.com/QingQ77/status/2082310142972854357)

## 相关概念

- [Cloudflare Durable Objects Agent 运行时](./tool-cloudflare-durable-objects-agent.md) — 把沙箱搬到 Cloudflare 边缘的另一种思路
- [Forkd（microVM fork 化沙箱）](./tool-forkd.md) — 100 个 100ms 起的 microVM fork 沙箱
- [Pi-env（Pi Coding Agent 沙箱运行环境）](./tool-pi-env.md) — Pi Coding Agent 的沙箱运行环境
- [Flounder（端到端白帽安全审计）](./tool-flounder.md) — 每步沙箱隔离的 agent 安全审计