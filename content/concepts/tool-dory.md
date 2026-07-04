---
type: Tool
title: "Dory"
description: "Dory 是 macOS 上 Docker Desktop / OrbStack 的开源替代品:一台共享 Linux VM 跑所有容器、空闲 RAM 减 ~4.7 倍、真 docker socket、一键 Kubernetes、~6 MB 单二进制、零账号。"
resource: "https://augani.github.io/dory"
tags: [dory, docker, macos, container, kubernetes, vm]
timestamp: "2026-07-04T15:00:00Z"
---

# Dory

## 它是什么

Dory(`augani/dory`)是 macOS 上对标 Docker Desktop 与 OrbStack 的免费开源替代品。它用一台共享 Linux VM 跑所有容器,而不是每容器起一个独立 VM,所以空闲 RAM 比「每个容器一 VM」的方案少 ~4.7 倍;同时仍保留对标准 docker socket / docker CLI / docker-compose 的兼容 — 你的 `docker build` / `docker run` / `docker-compose up` 原封不动。

项目链接：<https://augani.github.io/dory>

## 为什么用它

| 痛点 | Dory 的解法 |
|------|-----------|
| Docker Desktop 又重又慢 | 单二进制 ~6 MB |
| OrbStack 收费版限制 | MIT / GPL-3.0,完全免费无功能阉割 |
| 每容器一 VM 浪费内存 | 一台共享 VM 跑全部容器 |
| Linux 开发机体验差 | 自带完整 Linux 机器做所有 dev work |
| K8s 部署麻烦 | 一键 Kubernetes |
| Electron 套壳占资源 | 非 Electron |
| 强迫登录账号 | 无需账号、无需云同步 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 共享 Linux VM | 所有容器跑在一台精简 Linux VM 内,内存开销大幅下降 |
| 真 docker socket | 兼容 docker CLI、docker-compose |
| 一键 Kubernetes | 集成 K8s 本地集群 |
| 完整 Linux 工作机 | 给开发用,不是只跑容器 |
| 极小体积 | ~6 MB,远小于 Docker Desktop |
| 无 Electron | 原生客户端,启动更快更轻 |
| GPL-3.0 | 自由使用 |

## 适用人群

- macOS 上写 Go / Rust / Node / Python 后端,要本地容器跑服务的开发者
- 想跑 Kubernetes 本地集群做联调,但 OrbStack / Docker Desktop 太重的人
- 不想被 license / 升级订阅约束的人

## 相关概念

- [Dory 官网](https://augani.github.io/dory) — 原始链接
- [dd(JIT 容器)](tool-dd-jit-container.md) — 在 macOS 上用 JIT 直接跑 Linux 容器,无需 VM/Hypervisor
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker + Kamal 一键部署
