---
type: Tool
title: "docksurf"
description: "praneeth-etta/docksurf，终端里用键盘操作 Docker 的 TUI 工具：看容器 / 镜像 / 卷 / 网络的状态和实时数据（CPU / 内存 / 日志），不用切浏览器。"
resource: "https://github.com/praneeth-etta/docksurf"
tags: "[docker, tui, terminal, devops, monitoring]"
timestamp: "2026-08-01T20:30:00Z"
---

# docksurf

## 它是什么

[`praneeth-etta/docksurf`](https://github.com/praneeth-etta/docksurf) 是一个**终端里用键盘操作 Docker** 的 TUI 工具。它能在终端里看容器、镜像、卷、网络的**状态和实时数据**（CPU / 内存 / 日志流），**不用切到浏览器**或反复敲 `docker ps` / `docker logs`。

## 关键能力

| 能力 | 说明 |
|------|------|
| 键盘驱动 | 全键盘操作，vim 风格导航 |
| 多视图 | 容器 / 镜像 / 卷 / 网络分别一个面板 |
| 实时数据 | CPU / 内存 / 日志流实时刷新 |
| 替代 `docker` CLI | 图形化常见操作（start / stop / logs / exec / rm） |

## 解决什么痛点

- `docker ps` / `docker logs` / `docker stats` 命令来回敲、参数记不住
- 浏览器端的 Docker Desktop 太重，且有时延
- 想在 SSH 进服务器后直接看容器状态，不想离开终端

## 适合什么场景

- 频繁操作 Docker 的开发 / 运维
- 在远程服务器 / 容器里 SSH 后想用图形化方式管 Docker
- 想从 Docker Desktop 切到「终端原生」工具

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [lazydocker](https://github.com/jesseduffield/lazydocker) | TUI | 同样思路，社区更老 |
| [SICK](./tool-sick.md) | Linux 运维脚本 | 不限于 Docker，含硬件检测 + iperf3 |
| docksurf | TUI | Docker 全功能 + 实时数据 |

## 媒体

![docksurf 截图](https://pbs.twimg.com/media/HOhWEcYasAAxtCC.png)

## 原始链接

- [项目仓库](https://github.com/praneeth-etta/docksurf)
- [原始推文](https://x.com/QingQ77/status/2083383213725282624)

## 相关概念

- [SICK](./tool-sick.md) — Linux 服务器侧的运维脚本集，docksurf 专攻 Docker 这一块