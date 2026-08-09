---
type: "Term"
title: "Synology Hyper Backup"
description: "群晖 NAS 上的官方备份套件：把数据 / LUN / 系统配置 / 套件打包为 `.hbk` 归档，支持本地外置盘 / 远程 rsync / S3 / Google Drive / Dropbox 等多目的地，块级去重 + 版本化 + 客户端加密。"
resource: "https://www.synology.com/en-us/dsm/feature/hyper_backup"
tags: [synology, backup, hbk, nas, dedupe, encryption]
timestamp: "2026-08-09T19:30:00Z"
---

# Synology Hyper Backup

## 定义

Synology Hyper Backup（DSM 套件）是群晖 NAS 上的**官方备份解决方案**：把共享文件夹 / LUN / 套件配置 / 系统设置打包成 `.hbk`（Hyper Backup archive）归档文件，支持 **本地外置盘 / 远程 Synology NAS（rsync）/ S3 兼容 / Google Drive / Dropbox / OpenStack Swift / WebDAV / SFTP** 等多目的地。

## 要点

- **块级去重**：相同数据块只存一份，多版本备份不爆空间。
- **客户端加密 (AES-256)**：密钥可选保留在 NAS 或导出到备份目的地（丢失密钥 = 数据不可恢复）。
- **版本化**：保留多次快照，按时间点恢复。
- **完整性校验**：备份时与还原时做哈希校验（hbkit 这类第三方还原器也保留了 MD5 + CRC32 校验）。
- **`.hbk` 是私有格式**：官方恢复需依赖 Synology DSM / Hyper Backup Explorer；第三方还原（如 [hbkit](./tool-hbkit.md)）只覆盖部分配置场景。

## 为什么需要知道

- 大量中小企业 / 个人用户的 NAS 备份默认就是 Hyper Backup；离开 Synology 生态做迁移或抢救时，`.hbk` 是必须处理的格式。
- 选 Hyper Backup 之前先想清楚「换 NAS 品牌后能否还原」——这是 [hbkit](./tool-hbkit.md) 这类工具存在的原因。

## 相关概念

- [hbkit](./tool-hbkit.md) — 无 Synology 软件还原 `.hbk` 的 Python 工具
- [rclone](./tool-rclone.md) — Hyper Backup 的常见远端目的地（通过 S3 / WebDAV）
- [Self-hosted 备份方案](./note-self-hosted-backup.md) — 自托管备份选型参考