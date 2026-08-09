---
type: "Tool"
title: "wrk2"
description: "wrk 的「恒定吞吐量」分支：在 HdrHistogram 之上加恒定 QPS 调度器，修正 wrk 「尽力压」模式带来的延迟失真，是 HTTP 基准测试中测 P99 / P999 长尾的事实标准。"
resource: "https://github.com/wg/wrk"
tags: [http, load-testing, wrk, performance, hdrhistogram]
timestamp: "2026-08-09T19:30:00Z"
---

# wrk2

## 它是什么

[wrk2](https://github.com/giltene/wrk2) 是 [wrk](https://github.com/wg/wrk)（现代多机 C 写的 HTTP 压测工具）的**吞吐恒定分支**，由 Gil Tene（也是 HdrHistogram 作者）维护。原始 wrk 是「**尽力压**」（as many requests as possible）模式——当服务器跟不上时，wrk 实际发出去的 RPS 在抖，测出的 P99 延迟里掺杂了「队列堆积」，不可信。

wrk2 引入**精密的恒定 QPS 调度器**：到时间点就发包，不因网络 / 进程调度抖动而失真。配合 HdrHistogram 输出 P50 / P95 / P99 / P99.9 / P99.99 长尾，是测「延迟分布而非峰值吞吐」的事实标准。

## 为什么用它 / 适合什么场景

- 做 SLA 验证：业务承诺「P99 < 50ms」，必须用恒定 QPS 才能测出真实尾延迟。
- CI 性能回归：每次跑同一 QPS 曲线，对比 commit 之间的延迟漂移。
- 想看不同吞吐下的延迟曲线（自动跑 1k → 10k → 50k QPS）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 恒定 QPS 调度 | 调度器按目标 RPS 准时发包（精度远高于 wrk 的「尽力」） |
| HdrHistogram 输出 | 真实 P99 / P99.9 / P99.99 长尾延迟 |
| Lua 脚本扩展 | 沿用 wrk 的 Lua API（请求构造 / 响应校验 / 自定义 header） |
| 多线程 + epoll | 单机多核利用，事件驱动 |

## 局限 / 衍生

- 延迟失真**只在「尽力压」模式下出现**，被 wrk2 修正；之后又有 [zrk](./tool-zrk.md) 用 Zig 重写并进一步降低调度噪声。
- 想测「业务级」场景（登录 / 下单 / 复杂流程）通常会用 [Locust](./tool-locust.md) / [k6](./tool-k6.md) 这类 Python / JS 生态。

## 相关概念

- [zrk](./tool-zrk.md) — wrk2 的 Zig 重写版，进一步降低调度噪声
- [Locust](./tool-locust.md) — Python 写的分布式 HTTP 负载测试
- [k6](./tool-k6.md) — Grafana Labs 的现代化负载测试工具