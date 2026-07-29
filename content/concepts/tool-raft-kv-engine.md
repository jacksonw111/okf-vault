---
type: Tool
title: "raft-kv-engine-project（Rust 从头实现的线性化复制 KV 存储）"
description: "Rust 从头实现的线性化复制 KV 存储：LSM 存储引擎、无 IO 的 Raft 共识层、FoundationDB 风格确定性模拟器来验证正确性。"
resource: "https://github.com/arjunsood2025/raft-kv-engine-project"
tags: [rust, kv-store, raft, lsm, distributed-systems, consensus]
timestamp: "2026-07-29T07:43:00.000Z"
---

# raft-kv-engine-project

## 它是什么

**Rust 从头实现的线性化复制 KV 存储**，把分布式系统三大组件做成学习 / 参考实现：

| 组件 | 说明 |
|------|------|
| LSM 存储引擎 | 日志结构合并树 |
| 无 IO 的 Raft 共识层 | 协议本身，不带磁盘 IO（便于测试） |
| FoundationDB 风格确定性模拟器 | 注入故障、跑回归验证正确性 |

![示意图](https://pbs.twimg.com/media/HOSRGpoaYAA3qSa.jpg)

## 三组件合在一起的意义

- **LSM**：现代 KV 引擎主流实现（RocksDB / LevelDB / ScyllaDB 路线）
- **Raft**：分布式共识最易理解的算法
- **确定性模拟器**：FoundationDB 用它发现了无数 bug——同一组操作在每次跑出同样结果，注入故障验证不变量

把这三个组件**从头用 Rust 实现**，是个非常扎实的分布式系统教学 / 参考工程。

## 关键能力

| 能力 | 说明 |
|------|------|
| 线性化复制 | 强一致语义 |
| LSM 存储 | 高写入吞吐 |
| Raft 共识 | 易理解 / 易验证 |
| 确定性模拟 | FoundationDB 风格测试 |
| Rust 实现 | 性能 + 内存安全 |

## 原始链接

- [项目仓库](https://github.com/arjunsood2025/raft-kv-engine-project)
- [推文剪藏](https://x.com/QingQ77/status/2082371295883542794)

## 相关概念

- [DBOSify-py](./tool-dbosify-py.md) — Temporal Python 的 Postgres 平替，持久化工作流
- [Single Server](./tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker
- [Floci（LocalStack 免费开源替代）](./tool-floci.md) — 本地 AWS 模拟器
- [Cliare（CLI 黑盒审计工具）](./tool-cliare.md) — 给 CLI 打 Agent 就绪评分