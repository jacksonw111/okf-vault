---
type: Tool
title: "Mobile Harness"
description: "安卓端原生 AI 编码 agent 套件：Kotlin + Jetpack Compose 写界面、PRoot 跑 Ubuntu 20.04，内置 Claude Code CLI；项目、聊天、文件上下文跨会话保留。"
resource: "https://github.com/techjarves/Mobile-Harness"
tags: [android, mobile, claude-code, proot, coding-agent]
timestamp: "2026-09-08T00:00:00Z"
---

# Mobile Harness

## 它是什么
Mobile Harness 是 techjarves 开源的**安卓原生 AI 编码套件**：界面用 Kotlin + Jetpack Compose 写，底层在 PRoot 用户空间跑 Ubuntu 20.04（无需 root），内置 Claude Code 官方 CLI；项目、聊天记录、文件上下文跨会话保留。

## 为什么用它 / 适合什么场景
- 想在手机上直接做 vibe coding / 改代码 / 看仓库。
- 想避免切到多个 App（终端、编辑器、AI）之间来回跳。
- 安卓用户、无 root 环境，仍想跑完整 Linux 工具链。

## 关键能力
| 能力 | 说明 |
|------|------|
| Android 原生 | Kotlin + Jetpack Compose |
| 内置 Linux | PRoot + Ubuntu 20.04，无 root |
| Claude Code 内置 | 官方 CLI 安装在容器内 |
| 跨会话状态 | 项目 / 聊天 / 文件上下文持久 |
| 一体化 | 终端 + 编辑器 + AI 集成一个 App |

## 参考
- 原始链接：<https://github.com/techjarves/Mobile-Harness>

## 媒体
- ![](https://pbs.twimg.com/media/HRlDkKlbEAEgbWC.jpg)

## 相关概念
- [Claude Code](./tool-claude-code.md) — 内置的 AI 编码 CLI
- [PRoot](https://proot-me.github.io/) — 用户态 root 模拟
