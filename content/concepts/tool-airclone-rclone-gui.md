---
type: "Tool"
title: "Airclone（rclone 全平台图形界面）"
description: "给命令行工具 rclone 套了一个全平台图形界面，让 70 多种云存储都能像本地文件夹一样点一点拖一拖。"
resource: "https://github.com/GigaionLLC/Airclone"
tags: "[rclone, gui, cloud-storage, sync, file-manager]"
timestamp: "2026-09-13T11:30:00Z"
---

# Airclone（rclone 全平台图形界面）

## 它是什么

[GigaionLLC/Airclone](https://github.com/GigaionLLC/Airclone) 给命令行工具 **rclone** 包了一层**全平台图形界面**。rclone 本身支持 70+ 种云存储（Google Drive / Dropbox / S3 / OneDrive / WebDAV / SFTP …），但日常管理要在终端敲 `rclone config` / `rclone sync`，Airclone 把这些操作变成点选 / 拖拽。

## 为什么用它 / 适合什么场景

- 已经在用 rclone，但希望给非工程同事一个 GUI 入口。
- 需要在多云之间频繁迁移文件（Dropbox ↔ S3 ↔ 本地 ↔ OneDrive）。
- 想批量看 70+ 种云的容量、配额、文件树。
- 想要 GUI 的同时保留 rclone 的 sync / copy / mount 命令行能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全平台 GUI | Windows / macOS / Linux 桌面端 |
| 70+ 云存储 | 复用 rclone 的全部后端 |
| 点选 / 拖拽 | 类似本地文件管理器 |
| 保留命令行能力 | 复杂任务仍可走 rclone CLI |

## 媒体

- ![](https://pbs.twimg.com/media/HR_HR7IaoAA0jSB.jpg)

## 项目链接

- 仓库：<https://github.com/GigaionLLC/Airclone>

## 相关概念

- [rclone](https://rclone.org) — Airclone 之下的命令行核心（项目本身未在 concepts 收录，留官方链接）