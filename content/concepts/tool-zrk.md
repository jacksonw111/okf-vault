---
type: "Tool"
title: "zrk"
description: "用 Zig 重写 wrk2 实现的 HTTP 压测工具：以纳秒粒度调度发包，提供恒定 / 线性吞吐量，修正协调缺失导致的延迟失真。"
resource: "https://github.com/zoxy-io/zrk"
tags: [http, load-testing, zig, wrk2, performance]
timestamp: "2026-08-08T20:30:00Z"
---

# zrk

## 它是什么

zrk 是 wrk2（HTTP 压测工具的事实标准 wrk 的吞吐恒定版）的 Zig 重写版。它以纳秒粒度调度发包，提供恒定 / 线性吞吐量选项，专门修正了原始 wrk2 中因协调缺失导致的延迟失真。

## 为什么用它 / 适合什么场景

- 需要做「恒定吞吐量」HTTP 基准测试，而非「尽力压」型测试。
- 关心 P99 / P999 长尾延迟，需要延迟分布真实可信。
- 想用 Zig 编译的单一可执行文件、零运行时依赖。
- 在 CI / 性能回归测试中跑可重复的吞吐曲线。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纳秒调度 | 以纳秒精度控制发包时间 |
| 恒定 / 线性吞吐 | 支持恒定 QPS 与线性 QPS 增长曲线 |
| 修正延迟失真 | 解决了 wrk2 协调缺失导致的 P99 假阳性 |
| Zig 实现 | 单一二进制、低开销、零运行时 |
| 兼容 wrk2 工作流 | 沿用 wrk2 的 Lua 脚本与统计输出格式 |

## 相关概念

- [wrk2](./tool-wrk2.md) — 原始被重写的对象（HTTP 压测工具）
- [Locust](./tool-locust.md) — Python 写的分布式 HTTP 负载测试
- [k6](./tool-k6.md) — Grafana Labs 出的现代化负载测试工具