---
type: Tool
title: "pi-caffeinated-linux（跑 Pi 任务时不让 Linux 睡过去）"
description: "跑 Pi 任务时用 systemd-inhibit 把 Linux 机器锁在唤醒状态，任务收尾才放手，避免长任务被挂起 / 休眠打断。"
resource: "https://github.com/nmdra/pi-caffeinated-linux"
tags: [linux, systemd, pi, power-management, caffeinate]
timestamp: "2026-09-03T00:00:00Z"
---

# pi-caffeinated-linux（跑 Pi 任务时不让 Linux 睡过去）

## 它是什么

[pi-caffeinated-linux](https://github.com/nmdra/pi-caffeinated-linux) 是一个让 Linux 电脑在跑 Pi 任务时**不会中途睡过去**的小工具：基于 systemd-inhibit 把机器锁在唤醒状态（阻止 auto-suspend / 休眠），等任务收尾才放手。

类似 macOS 的 `caffeinate` 命令，但面向 Linux + Pi 编码 Agent 场景，包装得开箱即用。

## 为什么用它 / 适合什么场景

- 在笔记本上跑 Pi 长任务（训练 / 评估 / 拉取大模型 / 长 Agent 会话），但不想一直插电、又不希望系统自动休眠打断；
- 用 systemd 桌面环境，希望有与 macOS `caffeinate` 等价的「跑任务期间别睡」一行命令；
- 想给 Pi Agent 加一个保活机制，让系统推断「还在干活」，不要走自动休眠 / 屏保 / 锁屏。

## 关键能力

| 能力 | 说明 |
|------|------|
| 保活 | 调用 systemd-inhibit 把机器锁在唤醒状态 |
| 自动释放 | 任务结束后自动放手，不影响日常电源管理 |
| 命令行 | 简单 CLI 包装 |
| Pi 场景 | 专为 Pi 编码 Agent 跑长任务设计 |

## 参考链接

- 项目链接：<https://github.com/nmdra/pi-caffeinated-linux>
- 原始推文：<https://x.com/QingQ77/status/2095515909263880529>
- 媒体：<https://pbs.twimg.com/media/HRMNKWla4AA0XaF.jpg>

## 相关概念

- [MacTools](./tool-mac-tools.md) — macOS 菜单栏工具集（含防休眠）
- [Pi Agent Desktop](./tool-pi-agent-desktop.md) — Pi Coding Agent 原生桌面外壳
