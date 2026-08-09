---
type: "Tool"
title: "k6"
description: "Grafana Labs 出的现代化负载测试工具：用 JavaScript（ES2015+）写测试脚本，单二进制执行，天然对接 Grafana / Prometheus / InfluxDB 等可观测性栈。"
resource: "https://k6.io/"
tags: [load-testing, javascript, grafana, grafana-labs, performance]
timestamp: "2026-08-09T19:30:00Z"
---

# k6

## 它是什么

[k6](https://k6.io/) 是 Grafana Labs 维护的现代化负载测试工具：测试脚本用 **JavaScript**（ES2015+ 模块化）写；执行器是 Go 单二进制，可压测 HTTP / HTTPS / WebSocket / gRPC / GraphQL / Socket.IO 等；输出天然对接 Grafana / Prometheus / InfluxDB / Datadog 等可观测性栈，提供阈值（`thresholds`）判定与 CI 集成。

## 为什么用它 / 适合什么场景

- 团队 JS/TS 栈：测试脚本跟代码共用模块与工具函数。
- 已有 Grafana 体系：想看测试期间 P95 / 错误率与生产监控同图。
- 复杂场景：`scenarios` + `executor` 支持恒定 QPS / 阶梯 / 到达率 / 共享迭代等多种负载模型。
- 需要 SLO 验证：`thresholds` 让测试在 P95 超标 / 错误率 > 0.5% 时自动非零退出。
- 想做「浏览器端」混合压测：xk6-browser 用 k6 driver 操作真实 Chrome。

## 关键能力

| 能力 | 说明 |
|------|------|
| JS 测试脚本 | ES2015+ 模块化，支持 npm 包（webpack 打包） |
| 多协议 | HTTP / HTTPS / WebSocket / gRPC / GraphQL / Socket.IO / Kafka / Redis |
| 多负载模型 | constant-arrival-rate / ramping-vus / shared-iterations 等 |
| 阈值 (thresholds) | 测试内置 SLO 判定，失败即非零退出 |
| 生态 | Grafana Cloud / Prometheus / InfluxDB / Datadog / New Relic |
| 扩展 | xk6 框架 + 官方 / 社区扩展（browser / redis / kafka / grpc 等） |

## 与同类对比

| 工具 | 写场景语言 | 适用 |
|------|-----------|------|
| [wrk2](./tool-wrk2.md) | Lua + C | 裸 HTTP 极限 / 延迟分布 |
| [Locust](./tool-locust.md) | Python | 业务流 / 团队 Python 栈 |
| k6 | JavaScript | 现代化生态 / Grafana 集成 |

## 相关概念

- [wrk2](./tool-wrk2.md) — 裸 HTTP 极限与延迟分布基准
- [Locust](./tool-locust.md) — Python 写的业务流负载测试
- [zrk](./tool-zrk.md) — wrk2 的 Zig 重写版