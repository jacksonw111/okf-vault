---
type: "Tool"
title: "checkfleet"
description: "Allan-Nava 开源的运维检查工具集：把带领域知识的检查（TLS 到期、NATS 集群、PG 复制槽等）打包成单个静态 Go 二进制，目标机无需装 agent、无需常驻服务。"
resource: "https://github.com/Allan-Nava/checkfleet"
tags: ["ops", "monitoring", "go", "static-binary", "tls", "nats", "postgres", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# checkfleet

## 它是什么
checkfleet 把常见的「领域知识运维检查」打包成一个静态 Go 二进制：检查 TLS 证书到期、NATS 集群状态、PostgreSQL 复制槽等。它不要求目标机装 agent、也不起常驻服务，丢上去跑一次就能给运维人员返回检查报告。

## 为什么用它 / 适合什么场景
- 不希望为简单的「例行检查」部署一套 Prometheus / Zabbix / 各种 exporter。
- 临时新接管的机器需要快速跑一次「健康度体检」。
- 在 CI / 准入流程里集成发布前的「依赖项自检」（如证书是否够 30 天、PG 槽是否堆积）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 部署形态 | 静态 Go 二进制，零依赖 |
| 客户端 | 目标机无需装 agent，无守护进程 |
| 检查类型 | TLS 到期 / NATS 集群 / PG 复制槽等 |
| 风格 | 一次性 / 命令式体检 |
| 适合 | 临时检查 + CI 集成 |

## 媒体

架构示例：![架构示例](https://pbs.twimg.com/media/HPka-gibYAAbKQV.jpg)

## 相关概念
- [Timecut](./tool-timecut.md) — NAS Docker 一体化监控循环录像 + AI 挑精华，checkfleet 是其上游检查侧的更轻量版本思路
- [SoundWatch](./tool-soundwatch.md) — NetWatch 系列音频分支，把数字翻译成人话建议，与 checkfleet 的「领域知识 + 检查」思路相近
