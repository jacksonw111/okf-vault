---
type: "Note"
title: "Self-hosted 备份方案"
description: "在自托管环境下做备份的选型参考：3-2-1 原则 / 文件级 vs 块级 / 加密策略 / 云端 vs 本地异地，Synology Hyper Backup、rclone、borgbackup、ZFS snapshot 等工具的适用场景。"
tags: [backup, self-hosted, 3-2-1, encryption, synology, borg, zfs]
timestamp: "2026-08-09T19:30:00Z"
---

# Self-hosted 备份方案

## 它是什么

「自托管备份」通常指**自己掌控存储介质与备份链路**的备份架构：NAS / 外置硬盘 / 自建对象存储 / 第三方云端冷存储都是合法端点，但「策略与恢复流程由自己设计」。本文是一份选型参考。

## 核心原则：3-2-1

- **3** 份副本
- **2** 种介质
- **1** 份异地（offsite）

> 自托管≠不要异地。NAS 整机烧毁 / 失窃 / 勒索软件都常见，3-2-1 中的「1 份异地」必须有。

## 选型维度

| 维度 | 典型方案 | 适用场景 |
|------|---------|----------|
| 端点设备 | Synology NAS / TrueNAS / Unraid / Linux + ZFS | 个人 / 小团队主力 |
| 文件级备份 | Synology Hyper Backup / borgbackup / restic / duplicati | 跨平台、增量、加密 |
| 块级 / 镜像 | ZFS snapshot / btrfs send / LVM thin snapshot | 系统盘与卷级恢复 |
| 云端异地 | rclone 同步到 B2 / S3 Glacier / Wasabi | 冷存储、低成本异地 |
| 客户端透明加密 | rclone crypt / borg / restic（自带）| 上云前必做 |
| 还原工具 | hbkit（.hbk） / borg mount / rclone mount | 关键——选之前先演练还原 |

## 常见误区

- 「NAS = 备份」→ 不算。NAS 仍是单点，需要第二介质 + 异地。
- 不演练恢复流程 → 备份等于没备份。先做一次真实还原。
- 把云端明文上传 → 一旦泄露无挽回余地。
- 备份脚本只在生产机跑 → 生产机宕机时脚本也跟着没，必须**异地跑定时**。

## 相关概念

- [hbkit](./tool-hbkit.md) — 无 Synology 环境下还原 `.hbk` 归档的工具
- [rclone](./tool-rclone.md) — 云存储同步 / 挂载 / 加密层瑞士军刀
- [Synology Hyper Backup](./term-synology-hyper-backup.md) — Synology 自家备份产品线