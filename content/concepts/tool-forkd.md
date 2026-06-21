---
type: "Tool"
title: "forkd（deeplethe/forkd）"
description: "把「fork 进程」的代价套在 microVM 上：父 VM 提前预热好 snapshot，子 VM 共享内存直到写时才复制；100 个 KVM 隔离沙箱 ~100ms 全出来——为 AI agent 解决冷启动 microVM 太慢的痛点。"
tags: "[ai, agent, sandbox, microvm, kvm, fork, performance, infrastructure]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/deeplethe/forkd"
---

# forkd（deeplethe/forkd）

## 它是什么

[`forkd`](https://github.com/deeplethe/forkd) 是一个 **AI agent microVM 的「fork 化」沙箱方案**——把「父进程 fork 子进程」的低成本思路套到 KVM microVM 上：

- 提前把父 VM 预热成 snapshot；
- 启动时直接 fork，**子 VM 与父 VM 共享内存，写时复制（CoW）**；
- 100 个 KVM 隔离的沙箱 ~100ms 全部就绪。

## 解决的痛点

AI agent 要做**沙箱隔离**已经基本是共识（参考 [note-cloud-agent-infrastructure](note-cloud-agent-infrastructure.md)），但「冷启一个干净的 microVM」通常要秒级甚至更久。forkd 做的事本质就是：**把 fork 的开销（约毫秒级）套在 VM 身上**，同时**保留硬件隔离**的强保证。

## 关键能力

| 能力 | 说明 |
|------|------|
| 父 VM 预热 | 一次启动，常驻 snapshot |
| 子 VM fork | 共享内存 + CoW，几乎零拷贝 |
| KVM 隔离 | 真正的硬件级隔离（不是 container） |
| 100 个 / 100ms | 批量派生，毫秒级延迟 |
| 即用即抛 | 沙箱用完即销毁，不污染父 VM |

## 与「容器」「传统 microVM」的对比

| 维度 | 容器 | 传统 microVM | forkd |
|------|------|--------------|-------|
| 隔离强度 | 弱（共享内核） | 强（独立内核） | 强（独立内核） |
| 启动速度 | 快（<100ms） | 慢（秒级） | 快（~1ms / 子 VM） |
| 批量派生 | 容易 | 难 | 容易（共享内存） |
| 适用 | 微服务 / Web | 高隔离长时间负载 | AI agent 短任务 / 多租户 |

## 适用场景

- **AI agent SaaS**——每个 run 一个沙箱，几百并发；
- **多租户代码执行**——用户上传的代码必须隔离跑，又不能等几秒；
- **CI / 评测系统**——批量起隔离环境跑测试 / benchmark；
- **教学 / playground**——用户随手点一下，秒级得到隔离环境。

## 与本知识库其他概念的关系

- [云端 Agent 基础设施的设计教训（CREAO）](note-cloud-agent-infrastructure.md) — CREAO 文里反复提「冻结 snapshot + 派生」；forkd 是这条路在 microVM 层的极致实现。

## 参考链接

- [原始链接 1](https://x.com/vintcessun/status/2062755543811588448)

## 相关概念

- [云端 Agent 基础设施的设计教训](note-cloud-agent-infrastructure.md) — 反复提「冻结 snapshot + 派生」，forkd 是这条路在 microVM 层的极致实现
