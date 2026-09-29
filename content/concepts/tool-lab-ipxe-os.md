---
type: "Tool"
title: "lab-ipxe-os（局域网 iPXE + Cloud-Init 装机服务器）"
description: "Bun + TypeScript 写的网络装机服务器，编译成单个可执行文件，内置 Web UI + SQLite + Range 静态服务；裸机 / 虚拟机开机自动装 Ubuntu Server 24.04 LTS / Talos v1.14.0 / openSUSE Leap Micro 6.2。"
resource: "https://github.com/001123/lab-ipxe-os"
tags: "[ipxe, cloud-init, network-boot, deployment, lab, bun, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# lab-ipxe-os（局域网 iPXE + Cloud-Init 装机服务器）

## 它是什么

[lab-ipxe-os](https://github.com/001123/lab-ipxe-os) 是 001123 开源的局域网网络装机服务器：在局域网里拉起一台 iPXE + Cloud-Init 服务器，让裸机和虚拟机开机自己装系统，再也不用插 U 盘点安装向导。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单可执行文件 | Bun + TypeScript 编译成单一可执行，部署简单 |
| Web UI | 内置 Web 管理界面 |
| SQLite 数据库 | 存储装机记录 / 主机元数据 |
| Range 静态服务 | 支持 HTTP Range 的大文件下载 |
| 多系统支持 | 自动部署 Ubuntu Server 24.04 LTS / Talos v1.14.0 / openSUSE Leap Micro 6.2 |
| 无运行时依赖 | 机器上不需要装 Node.js |

## 它解决的问题

实验室 / 机房场景下：
- 批量给裸机装系统（不用每台插 U 盘）
- 想要可编程 / 可复现的装机流程
- 想用 Cloud-Init 做装机后初始化

## 媒体预览

![](https://pbs.twimg.com/media/HTWSUETaUAAB-Aw.jpg)

## 原始链接

- 项目主页：<https://github.com/001123/lab-ipxe-os>

## 相关概念

- [Amlogic Armbian](./tool-amlogic-armbian.md) — 电视盒子改造 Linux 服务器，与 lab-ipxe-os 同属「无 U 盘装机」领域
- [Self-Hosted（自托管）](./term-self-hosted.md) — 自托管基础设施背景