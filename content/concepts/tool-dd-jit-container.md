---
type: Tool
title: "dd（JIT 容器）"
description: "Rust + C 写的开源项目，用 JIT 编译技术在 macOS 上直接跑 Linux 容器（无需 VM / Hypervisor / Linux 内核），兼容 Docker CLI 与 Docker Engine API。"
resource: "https://github.com/ricccrd/dd"
tags: "[jit, container, macos, linux, rust, docker]"
timestamp: "2026-07-02T04:00:00Z"
---

# dd（JIT 容器）

## 它是什么
一个用 Rust + C 写的开源项目，用 **JIT 编译技术**在 macOS 上**直接运行 Linux 容器**。不需要虚拟机、Hypervisor 或 Linux 内核——把 JIT 当作客户机的「内核」，在用户态翻译容器指令并处理系统调用。

## 为什么用它 / 适合什么场景
- 在 macOS 上跑 Linux 容器但不想开 Parallels / OrbStack / Docker Desktop 之类基于 VM 的方案。
- 想让容器在 Apple Silicon 上达到接近原生 VM 的性能。
- 想用一份 `docker` CLI 命令同时管 macOS 与 Linux 容器。
- 想在 x86-64 macOS（如 Intel Mac）上跑 x86-64 Linux 容器，且性能比 QEMU 模拟更强。

## 关键能力
| 能力 | 说明 |
|------|------|
| 架构 | Rust + C + JIT 编译 |
| 客户机运行时 | arm64 Linux、x86-64 Linux（通过 `jit86` 翻译）、macOS arm64 |
| API 兼容 | 实现 Docker Engine API，兼容现有 `docker` CLI |
| 系统调用 | 用户态翻译处理，无需 Linux 内核 |
| 性能（Apple M5 Pro） | arm64 容器计算与原生 VM 持平甚至更快；x86-64 容器九成测试超越 QEMU，浮点最高 24× |
| 形态 | GTK4 桌面应用 + CLI |
| 权限 | 无需 root |

## 相关概念
- [Single Server](tool-single-server.md) — Linux 服务器端一键部署方案；dd 是 macOS 端跨架构容器方案
- [Docker Android](tool-docker-android.md) — 同为「在受限环境跑容器」思路；dd 是反方向（macOS 跑 Linux 容器）

## 项目链接
- 项目主页：<https://github.com/ricccrd/dd>