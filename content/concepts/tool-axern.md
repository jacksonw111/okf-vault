---
type: "Tool"
title: "Axern（AI agent 代码执行沙箱）"
description: "帮 AI agent 执行代码的开源沙箱：agent 生成的不可信代码进 runsc 隔离边界、可信常驻服务放 runc 运行，两套环境共用同一套资源和生命周期管理接口。"
tags: "[sandbox, agent, runsc, runc, gvisor, code-execution]"
timestamp: "2026-08-15T06:15:00Z"
resource: "https://github.com/cofy-x/axern"
---

# Axern（AI agent 代码执行沙箱）

## 它是什么

`cofy-x/axern` 是一个**双运行时**的代码执行沙箱，专门给 AI agent 用。它把运行环境分成两个边界：

- **`runsc` (gVisor)**：跑 agent 临时生成的不可信代码，做系统调用隔离。
- **`runc`（原生容器）**：跑可信常驻服务（如数据库、缓存、worker）。

两套环境**共用同一套资源和生命周期管理接口**，上层调度只需选择「用哪个边界」，不必分别维护两套编排代码。

> ![](https://pbs.twimg.com/media/HPpgNOPbYAAcj9Q.jpg)

## 为什么用它 / 适合什么场景

- **agent 代码不可信**：AI 生成的代码可能误删文件、泄漏密钥、扫端口，必须隔离。
- **常驻服务要稳定**：数据库 / Redis / API server 不必走 gVisor 的开销。
- **统一接口**：很多 agent 框架要分别接 Docker / Podman / Firecracker，Axern 把它们收敛成两个语义化的边界。

## 关键能力

| 能力 | 说明 |
|------|------|
| `runsc` 隔离边界 | gVisor 系统调用拦截，agent 不可信代码在此运行 |
| `runc` 原生容器 | 跑可信常驻服务，无 gVisor 开销 |
| 统一资源管理 | CPU / 内存 / 网络配额两套边界共用一套接口 |
| 统一生命周期 | 启动 / 停止 / 重启 / 健康检查同一套 API |
| AI agent 友好 | 上层框架只需声明「不可信 / 可信」即可调度 |

## 与相关工具的差异

| 工具 | 隔离强度 | 性能开销 | 适合 |
|------|----------|----------|------|
| Docker (`runc`) | 中 | 低 | 可信服务 |
| gVisor (`runsc`) | 高（系统调用拦截） | 中 | 不可信代码 |
| Firecracker | 极高（microVM） | 启动开销 | 短生命周期 microVM |
| **Axern** | **中 + 高 双层** | **弹性** | **同一项目内同时跑可信服务 + 不可信代码** |

## 与本知识库其它「沙箱」概念的关系

- [forkd](tool-forkd.md) — microVM fork 化沙箱，100 个 100ms。
- [pi-env](tool-pi-env.md) — Pi Coding Agent 的沙箱运行环境，定位类似但偏 Pi 单 agent。
- [pi-env](tool-pi-env.md) — Pi 的隔离宿主。
- [Flounder](tool-flounder.md) — 把编码 agent 包装为白帽安全审计，每步沙箱隔离。

## 适用人群

- 自托管 AI agent 平台的开发者。
- 给 agent 跑用户上传 / AI 生成代码的 SaaS 团队。
- 想在同一进程内同时拥有「安全边界」与「原生性能」的人。

## 参考链接

- [项目链接](https://github.com/cofy-x/axern)

## 相关概念

- [forkd](tool-forkd.md) — microVM fork 化沙箱
- [pi-env](tool-pi-env.md) — Pi Coding Agent 的沙箱运行环境
- [Flounder](tool-flounder.md) — 把编码 agent 包装为白帽安全审计，每步沙箱隔离