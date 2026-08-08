---
type: "Tool"
title: "hbkit"
description: "Python 写的 Synology Hyper Backup（.hbk）归档还原工具：不装 Synology 软件也能从 .hbk 恢复文件，支持本地磁盘、外置硬盘、rclone 挂载的对象存储，每个数据块都过 MD5 + CRC32 校验。"
resource: "https://github.com/YordiLorenzo/hbkit"
tags: [synology, hyper-backup, restore, python, cli, tui]
timestamp: "2026-08-08T20:30:00Z"
---

# hbkit

## 它是什么

hbkit 是一个 Python 写的命令行 / TUI 工具，专门用来在没有 Synology 软件的机器上从 Synology Hyper Backup 生成的 `.hbk` 归档里恢复文件。它支持从本地磁盘、外置硬盘，甚至 rclone 挂载的对象存储直接读取，并对吐出的每个数据块做 MD5 + CRC32 校验。

## 为什么用它 / 适合什么场景

- 不再拥有 Synology NAS，但仍需恢复 `.hbk` 备份。
- 想在通用 Linux / macOS / Windows 上直接解压 Synology 备份。
- 需要从云端对象存储（通过 rclone）取回备份。
- 想逐数据块校验还原过程的完整性。

## 关键能力

| 能力 | 说明 |
|------|------|
| 无 Synology 依赖 | 不需要装 DSM 或 Hyper Backup 客户端 |
| 多源读取 | 本地盘 / 外置盘 / rclone 挂载的对象存储 |
| CLI + TUI | 命令行与终端界面两种使用方式 |
| 双算法校验 | 每个数据块 MD5 + CRC32 双重校验 |
| 跨平台 | Python 实现的轻量还原流程 |

## 相关概念

- [rclone](./tool-rclone.md) — 把对象存储挂载成本地文件系统的瑞士军刀
- [Self-hosted 备份方案](./note-self-hosted-backup.md) — 自托管备份选型参考
- [Synology Hyper Backup](./term-synology-hyper-backup.md) — 备份原始格式的来源