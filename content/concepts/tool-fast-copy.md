---
type: Tool
title: "fast-copy (gekap)"
description: "Python 写的跨平台命令行复制工具（Linux / macOS / Windows），针对 USB 移动硬盘、NAS 备份、大文件 SSH 传输场景优化；比 scp/rsync/SFTP 快 3-5 倍，SSH 走原生 tar 管道不依赖 SFTP，支持本地↔远程和远程↔远程中继，稀疏文件只传真实占用数据。"
resource: "https://github.com/gekap/fast-copy"
tags: [python, cli, file-copy, ssh, backup, sparse-file, cross-platform]
timestamp: "2026-08-03T02:15:00Z"
---

# fast-copy (gekap)

## 它是什么
fast-copy（`gekap/fast-copy`）是一个用 Python 写的跨平台命令行复制工具，支持 Linux、macOS 和 Windows，专门针对 USB 移动硬盘、NAS 备份以及大文件 SSH 传输场景做了优化。

号称比 scp / rsync / SFTP 快 3-5 倍。SSH 传输走原生 tar 管道，不依赖 SFTP；支持本地↔远程和远程↔远程中继；稀疏文件（比如 VM 磁盘镜像）也能识别，只传真实占用的数据。

![fast-copy 终端示意](https://pbs.twimg.com/media/HOn1szZakAAWB3s.jpg)

## 为什么用它 / 适合什么场景
- **NAS / USB 大文件**：比 rsync 在跨设备 / 跨文件系统时更快。
- **VM 磁盘镜像**：稀疏文件感知，传输 qcow2 / vmdk 时只传真实占用块。
- **远程中继**：A → B → C 中继转发，无需先落本地。
- **零 SSH 协议依赖**：用 tar 管道代替 SFTP，规避 SFTP 性能瓶颈。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | Linux / macOS / Windows 同一 Python 入口 |
| tar 管道 SSH | 替代 SFTP，性能 3-5 倍 |
| 远程中继 | 本地 ↔ 远程、远程 ↔ 远程（不落本地） |
| 稀疏文件 | VM 磁盘镜像等稀疏文件只传真实占用 |
| 增量同步 | 复用 rsync 类算法的增量差异（如适用） |

## 项目链接
- <https://github.com/gekap/fast-copy>

## 相关概念
- [RatholeEngine](./tool-rathole-engine.md) — rathole + Nginx 多地点反向隧道编排（与远程中继互补）
- [sick](./tool-sick.md) — Linux 服务器运维脚本集，硬件检测 + 全球 23 节点 iperf3 测速
- [Talivia](./tool-talivia.md) — 数据可视化层面的替代品参考
