---
type: "Tool"
title: "rclone"
description: "Rsync for cloud storage：把对象存储（S3 / Google Cloud / Dropbox / OneDrive / WebDAV 等 70+ 后端）当成本地文件系统，支持 mount / sync / copy / crypt 加密层。"
resource: "https://rclone.org/"
tags: [cloud-storage, sync, cli, s3, backup, mount]
timestamp: "2026-08-09T19:30:00Z"
---

# rclone

## 它是什么

rclone 是「云存储版的 rsync」：命令行工具，**支持 70+ 云存储后端**（S3 / Google Cloud Storage / Azure Blob / Dropbox / OneDrive / Google Drive / WebDAV / SFTP / S3-compatible 兼容存储 / Backblaze B2 等），提供 `sync` / `copy` / `mount` / `crypt`（透明加密层）/ `serve`（把任意后端暴露为 HTTP/WebDAV/SFTP/FTP）等子命令。

## 为什么用它 / 适合什么场景

- 跨云备份 / 迁移：把 S3 同步到 Google Cloud Storage 或本地 NAS，无需写胶水代码。
- 离线访问云盘：`rclone mount` 把对象存储挂载成本地目录，Finder/Explorer 直接浏览。
- 多云加密归档：rclone crypt 在客户端加密后再上传，云厂商 / 中间人看不到明文。
- 把任意对象存储改造成能被别的工具读取的「本地文件系统」（hbkit 走的就是这条路）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 70+ 后端 | S3 / GCS / Azure / Dropbox / OneDrive / GDrive / WebDAV / SFTP 等 |
| 多子命令 | sync / copy / mount / crypt / serve / ls / check / dedupe 等 |
| mount（FUSE）| 把对象存储挂载为本地目录（Linux/macOS/Windows） |
| crypt | 客户端透明加密层，可叠加在任何 backend 上 |
| 后台守护 | rclone rcd 提供 REST 控制平面，便于编程化调度 |
| 校验 / 修复 | check / cryptcheck 对比本地与远端 hash |

## 相关概念

- [hbkit](./tool-hbkit.md) — 从 rclone 挂载的对象存储读 `.hbk` 备份归档