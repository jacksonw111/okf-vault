---
type: "Tool"
title: "kernwatch（Rust + Ratatui 写的 Linux TUI 内核观测器）"
description: "matthart1983/kernwatch：Linux 专用 TUI 内核观测器，x86-64 与 ARM64 都跑，官方提供 glibc 与静态 musl 两种预编译二进制；CPU / 任务调度 / 内存压力 / 块 I/O / 中断 / cgroups / 模块 / eBPF 等 14 个键盘驱动视图。"
resource: "https://github.com/matthart1983/kernwatch"
tags: "[linux, kernel, tui, ratatui, rust, observability, monitoring]"
timestamp: "2026-09-20T18:00:00Z"
---

# kernwatch

## 它是什么

[matthart1983/kernwatch](https://github.com/matthart1983/kernwatch) 是一个 **Rust + Ratatui 写的 Linux 专用 TUI 内核观测器**。它把 CPU、任务调度、内存压力、块 I/O、中断、cgroups、内核模块、eBPF 活动铺在 **14 个键盘驱动视图**里，省掉搭 Web 监控那套工序。

## 为什么用它 / 适合什么场景

- 在终端里直接看内核指标，**不需要部署 Prometheus + Grafana + 告警**那一整套。
- 远程登录服务器排查问题时，**SSH 进去就能用**——纯 TUI，不占图形栈。
- 想**轻量巡检**——单一二进制，丢到 `/usr/local/bin` 就能跑。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | Linux 专用，**x86-64 + ARM64** 均支持 |
| 二进制分发 | 官方提供 **glibc** 与 **静态 musl** 两种预编译版本 |
| UI | Rust + [Ratatui](https://github.com/ratatui/ratatui) 的 TUI |
| 视图数 | **14 个**键盘驱动视图（CPU / 调度 / 内存 / 块 I/O / 中断 / cgroups / 模块 / eBPF 等） |
| 依赖 | 单一可执行文件，零运行时依赖 |

## 项目链接

- 仓库：<https://github.com/matthart1983/kernwatch>

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HSlNsHSaUAAcM7R.mp4>

## 相关概念

- [NetFluss](./tool-netfluss.md) — 同类 macOS 菜单栏系统观测思路（macOS 平台）
- [Impasto（Arch Linux + Hyprland）](./tool-impasto-arch-hyprland.md) — 同样是面向 Linux 桌面的一体化方案
