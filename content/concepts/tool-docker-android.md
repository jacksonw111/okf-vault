---
type: "Tool"
title: "docker-android（容器化 Android 模拟器）"
description: "把 Android 模拟器 + ADB 服务打包进 Docker 镜像，跑在容器里通过网络远程连上去操作，适合 CI 测试和远程控制。"
resource: "https://github.com/HQarroum/docker-android"
tags: [android, docker, emulator, ci, adb]
timestamp: "2026-06-24T15:30:00Z"
---

# docker-android（容器化 Android 模拟器）

## 它是什么

[`HQarroum/docker-android`](https://github.com/HQarroum/docker-android) 是一个**轻量级 Docker 镜像**，把 Android 模拟器和 ADB 服务打包进去，跑在容器里，通过网络远程连上去操作。

## 为什么用它 / 适合什么场景

- **CI 测试**：GitHub Actions / GitLab CI 上跑 Android 端到端测试；
- **远程控制**：在服务器上长期挂一个 Android 实例，从本地用 adb connect 连；
- **环境统一**：开发 / 测试 / CI 共用同一份镜像，免装 Android Studio；
- **批量并行**：用 docker-compose 拉起多台模拟器做并发测试。

## 关键能力

| 能力 | 说明 |
|---|---|
| 容器化模拟器 | 整个 Android 系统跑在 Docker 里 |
| ADB 暴露 | 通过 5555 端口远程 adb 连接 |
| CI 友好 | 镜像轻量、启动快 |
| 远程控制 | 服务器长期挂着、本地连过去用 |
| 批量并行 | docker-compose 一键起多实例 |

## 媒体 / 参考链接

![架构示意](https://pbs.twimg.com/media/HLZpKKua0AABkJP.jpg)

- [项目链接](https://github.com/HQarroum/docker-android)

## 相关概念

- [PP-OCRv6 Studio](tool-ppocrv6-studio.md) — 本地 OCR 工具，与本工具组合可做 Android 截图 OCR 自动化
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker + Kamal，可作为本工具的部署底座
