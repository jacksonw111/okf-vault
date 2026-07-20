---
type: "Tool"
title: "RoutineOps（自托管 MDM / RMM 平台）"
description: "自托管的 MDM / RMM 平台，用常驻的 gRPC / mTLS 通道跨公网管 Windows、macOS、Linux 设备群：每台设备的 Agent 与服务器一直保持一条加密通道，走公网即可通信。"
resource: "https://github.com/Floodww/RoutineOps"
tags: "[mdm, rmm, self-hosted, fleet-management, grpc, mtls]"
timestamp: "2026-07-20T20:20:00Z"
---

# RoutineOps（自托管 MDM / RMM 平台）

## 它是什么

[Floodww/RoutineOps](https://github.com/Floodww/RoutineOps) 是**自托管的 MDM（移动设备管理）/ RMM（远程监控管理）平台**——区别于 SaaS 化的 Fleet / Jamf / Mosyle 把控制面握在第三方手里的方案，RoutineOps 把控制面整套放在自己的服务器上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 常驻加密通道 | 每台设备 Agent 与服务器保持 gRPC / mTLS 长连 |
| 跨公网 | 走公网直接通信，无需 VPN / 内网暴露 |
| 跨平台 | Windows / macOS / Linux 三端都管 |
| 自托管 | 控制面 / 状态数据全在自己服务器上 |

![RoutineOps 截图](https://pbs.twimg.com/media/HNhSgmWa0AAE8r7.jpg)

## 相关概念

- [OpenConnector](./tool-open-connector.md) — 1000+ SaaS / Action 的开源 Composio 替代品

## 参考链接

- 项目链接: <https://github.com/Floodww/RoutineOps>
