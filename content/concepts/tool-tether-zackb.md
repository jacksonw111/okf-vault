---
type: "Tool"
title: "Tether（iPhone ↔ Linux 桥接套件）"
description: "C++ 实现的 iPhone 与 Linux 桌面桥接套件：tetherd 守护进程 + tether CLI + tether-gtk 图形界面 + iOS App + 浏览器/邮件扩展五件套，iOS 端已上架 App Store。"
resource: "https://github.com/zackb/tether"
tags: [ios, linux, bridge, integration, desktop, mobile, cpp]
timestamp: "2026-08-31T16:00:00Z"
---

# Tether

## 它是什么

[Tether](https://github.com/zackb/tether) 是 [zackb](https://github.com/zackb) 用 **C++** 实现的 **iPhone 与 Linux 桌面桥接套件**。整套由五个互相协作的部分组成：

| 组件 | 角色 |
|------|------|
| `tetherd` | Linux 端守护进程，常驻后台 |
| `tether` | Linux 端 CLI 命令 |
| `tether-gtk` | Linux 端 GTK 图形界面 |
| iOS App | iPhone 端入口，已上架 App Store |
| 浏览器 / 邮件扩展 | 把内容推到 Linux 端的便捷通道 |

## 为什么用它 / 适合什么场景

- **iPhone 与 Linux 互传文件 / 链接 / 剪贴板**；
- **不想装 KDE Connect / KDE 生态**：Tether 是更轻量的替代；
- **iOS App + Linux 桌面一体化**：iOS 端已上架，开箱即用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文件互传 | iPhone ↔ Linux |
| 剪贴板同步 | 双向 |
| 链接推送 | 从浏览器 / 邮件扩展推送到桌面 |
| GTK GUI | 图形化操作 |
| iOS 已上架 | App Store 官方应用 |

## 媒体

- 项目截图：![](https://pbs.twimg.com/media/HQ-qaweawAAxsIb.jpg)

## 相关概念

（暂无关联项目可链。）

## 参考链接

- 项目链接：<https://github.com/zackb/tether>