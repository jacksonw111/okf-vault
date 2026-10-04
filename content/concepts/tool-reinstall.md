---
type: "Tool"
title: "reinstall（一键重装系统脚本）"
description: "bin456789 维护的一键重装系统脚本：一条命令从 Linux 重装 Windows 或反之，覆盖 Win11/10/Server 和 Debian/Ubuntu/Alpine/Rocky/Fedora/OpenWrt，也能给无 IPMI 的 VPS 远程重装。"
resource: "https://github.com/bin456789/reinstall"
tags: "[sysadmin, reinstall, linux, windows, vps, openwrt]"
timestamp: "2026-10-04T13:00:00Z"
---

# reinstall

## 它是什么

[reinstall](https://github.com/bin456789/reinstall) 是 **bin456789** 维护的**一键重装系统**脚本——按传统流程装系统得先下镜像、刻 PE / U 盘、钻 BIOS 调启动项，整套流程对经常折腾机器的人是负担。这套脚本一条命令下去系统自己重装好。

## 关键能力

| 能力 | 说明 |
|------|------|
| 系统支持（Windows 端） | Windows 11、Windows 10、Windows Server |
| 系统支持（Linux 端） | Debian、Ubuntu、Alpine、Rocky Linux、Fedora、OpenWrt |
| 跨平台重装 | Linux → Windows、Windows → Linux 双向 |
| 远程重装 | 无 IPMI 的云服务器 / VPS 可远程操作 |
| U 盘免用 | 不需要 PE / U 盘启动盘 |
| 适合人群 | 运维 / 装机党 / VPS 用户 |

## 典型场景

- 频繁测试不同 Linux 发行版的开发者
- VPS 提供商后台装错系统 / 想换系统的自救
- 给客户 / 同事远程装机而对方不熟悉 BIOS

## 参考链接

- 项目链接：<https://github.com/bin456789/reinstall>

## 相关概念

- [ternssh](./tool-ternssh.md) — 同样免本地客户端，浏览器即 SSH 工作台