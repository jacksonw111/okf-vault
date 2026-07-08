---
type: "Tool"
title: "Nebula（Windows GPU 加速 / 会话持久的终端）"
description: "Nebula 是 Windows 上的 GPU 加速终端，关窗口不杀会话——重开能接回正在跑的 claude、构建、SSH 等长时间任务。"
resource: "https://github.com/Kuddev/nebula"
tags: "[terminal, windows, gpu-acceleration, session-persistence, claude-code]"
timestamp: "2026-07-08T11:25:00Z"
---

# Nebula

## 它是什么

[Nebula](https://github.com/Kuddev/nebula) 是一款 **Windows 上的 GPU 加速终端**——最大卖点是**会话持久**：

- 关闭窗口，**后台任务不死**；
- 重新打开，**正在跑的 claude / 构建 / SSH 还能接上**。

对跑 Claude Code / 长时间构建 / 长时间 SSH 会话的人来说，是「终端崩溃了任务全丢」的解药。

## 关键能力

| 能力 | 说明 |
|------|------|
| GPU 加速渲染 | 比传统 Windows Terminal 更流畅 |
| 会话持久 | 关闭窗口 ≠ 杀死进程 |
| 会话恢复 | 重开窗口无缝接回原会话 |
| 长任务友好 | claude / 构建 / SSH / watch 都不掉 |
| Windows 原生 | 针对 Windows 优化 |

## 适合谁

- 在 Windows 上跑 Claude Code 但常因「关错窗口」丢进度的用户。
- 跑长时间编译 / 测试 / 部署任务，想随时关窗走人的开发者。
- 嫌 Windows Terminal / ConEmu 渲染慢、想用 GPU 加速的玩家。

## 媒体

![Nebula 终端预览](https://pbs.twimg.com/media/HMqrqJpaYAANsO0.jpg)

## 参考链接

- [项目仓库](https://github.com/Kuddev/nebula)

## 相关概念

- [Mac Tools](./tool-mac-tools.md) — 同为「终端 / 命令行增强」类工具，但偏 macOS
- [Hermes Desktop](./tool-hermes-desktop.md) — 同为长任务 / agent 的桌面外壳