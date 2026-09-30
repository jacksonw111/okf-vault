---
type: Tool
title: "EverythingX（macOS / Linux 上的 Everything 复刻）"
description: "把 Windows 上著名的 Everything 极速文件搜索带到 macOS 和 Linux：常驻守护进程 everythingxd 监听文件系统变化、GUI 应用 everythingx 搜索、命令行工具 ev 也可搜索，三件套。"
resource: "https://github.com/AlanKK/everythingx"
tags: [file-search, everything, macos, linux, desktop, fts, daemon]
timestamp: 2026-09-30T10:32:00Z
---

# EverythingX

## 它是什么

**EverythingX** 是 [AlanKK](https://github.com/AlanKK) 维护的开源项目，目标是**在 macOS 和 Linux 上复刻 Windows 上 Everything 的极速文件搜索体验**。它由三个互相配合的部分组成：

| 组件 | 角色 |
|------|------|
| `everythingxd` | 常驻后台守护进程，监听文件系统变化并维护索引 |
| `everythingx` | GUI 应用，提供搜索界面 |
| `ev` | 命令行工具，脚本化使用 |

## 为什么用它 / 适合什么场景

- 从 Windows 切到 macOS / Linux 后想念 Everything 的"输完就出结果"体验。
- 想给命令行工作流（脚本、管道、自动化）配一个可调用的极速文件搜索工具。
- 不愿意用 spotlight / find 命令那种"等一下才出结果"的体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | macOS / Linux |
| 守护进程 | `everythingxd` 监听文件变化并实时更新索引 |
| GUI | `everythingx` 提供图形搜索界面 |
| CLI | `ev` 命令行搜索工具，方便脚本化 |
| 性能 | 复刻 Everything 的极速搜索体验 |

## 参考链接

- 仓库：<https://github.com/AlanKK/everythingx>

## 相关概念

- [Spotlight (macOS)](./term-apple-hide-my-email.md) — macOS 自带的搜索能力；EverythingX 的差异点是**实时索引 + 极速全文搜索**