---
type: "Tool"
title: "Locust"
description: "Python 写的 HTTP 负载测试工具：用 Python 代码定义用户行为（`@task` 装饰器），分布式跑场景，自带 Web UI 实时显示 RPS / 失败率 / 延迟分布，适合「业务流」压测而非纯吞吐基准。"
resource: "https://locust.io/"
tags: [load-testing, python, http, distributed, web-ui]
timestamp: "2026-08-09T19:30:00Z"
---

# Locust

## 它是什么

Locust 是用 **Python** 写「用户行为」再跑负载测试的工具：一个 `Locustfile` 定义一组「User」类，每个类的方法用 `@task` 装饰，模拟真实业务流（登录 → 浏览 → 加购 → 下单），而非「无脑打 /ping」。自带 Web UI 实时显示 RPS / 失败率 / 响应时间分布；master-worker 模式可分布到多机。

## 为什么用它 / 适合什么场景

- 想压「业务流」而不是「裸 HTTP 接口」（wrk / wrk2 测的是后者的极限）。
- 团队 Python 栈：用熟悉的 Python 写场景，无需学 Lua / Go / JS。
- 需要 Web UI 实时观察：看哪个 endpoint 失败率飙升、哪个用户行为拖慢响应。
- 想在 CI 里跑：Locust 提供 `--headless` 模式 + 退出码判定。

## 关键能力

| 能力 | 说明 |
|------|------|
| Python 场景 | `class UserBehavior(TaskSet)` + `@task` 装饰器 |
| Web UI | 实时 RPS / 失败率 / 延迟 + 下载 CSV |
| 分布式 | master-worker，多机协同施压 |
| 自定义协议 | HTTP / HTTPS 之外，还能写任意客户端（gRPC / WebSocket）|
| 事件钩子 | `request_success` / `request_failure` / `test_start` 等 |
| Headless 模式 | CI 友好，按阈值退出 |

## 与同类对比

| 工具 | 写场景语言 | 适用 |
|------|-----------|------|
| [wrk2](./tool-wrk2.md) | Lua + C | 裸 HTTP 极限 / 延迟分布 |
| [k6](./tool-k6.md) | JavaScript | 现代化生态 / Grafana 集成 |
| Locust | Python | 业务流 / 团队 Python 栈 |

## 相关概念

- [wrk2](./tool-wrk2.md) — 裸 HTTP 极限与延迟分布基准
- [k6](./tool-k6.md) — JS 写的现代化负载测试工具，Grafana 生态
- [zrk](./tool-zrk.md) — wrk2 的 Zig 重写版