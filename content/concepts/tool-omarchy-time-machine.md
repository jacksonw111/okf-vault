---
type: Tool
title: "omarchy-time-machine（Omarchy 顶栏的「上次备份时间」指示器）"
description: "Omarchy 平铺桌面的备份插件：按计划把主目录拷到目的地，顶栏只挂一个「上次备份时间」图标，正常时安静，超时或失败才亮红。"
resource: "https://github.com/jankeesvw/omarchy-time-machine"
tags: [omarchy, backup, waybar, tiling-wm, linux, indicator, automation]
timestamp: "2026-08-28T00:00:00Z"
---

# omarchy-time-machine

## 它是什么
[jankeesvw/omarchy-time-machine](https://github.com/jankeesvw/omarchy-time-machine) 是**给 Omarchy 平铺桌面写的备份插件**，设计哲学是「桌面栏只显示一条必要信息」。

- **按计划**把用户主目录拷到指定目的地（外部盘 / NAS / 云端挂载点等）；
- **顶栏状态条**只显示「上次备份时间」一个图标；
- **正常时**安静显示（不打扰）；
- **超时没备份**或**本次备份失败**时变红，给出告警。

## 为什么用它 / 适合什么场景
- Omarchy 用户想要一个**轻量、不打扰**的备份守护；
- 不想装完整的备份方案（Borg / Restic / Timeshift），只想定期拷一份主目录；
- 桌面状态栏空间宝贵，希望只暴露一条信息；
- 错过备份时间就心里没底，需要**被动告警**而不是主动检查。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动备份 | 按计划把主目录拷到指定目的地 |
| 状态栏指示 | 顶栏只显示「上次备份时间」图标 |
| 被动告警 | 正常安静，超时 / 失败才亮红 |
| 轻量 | 单一插件，不依赖完整备份生态 |
| 可搭配 | 外部硬盘 / NAS / rclone 挂载点均可作为目的地 |

## 相关概念
- [Btop Quattro Plugin](tool-btop-quattro-plugin.md) — 同为 Omarchy 顶栏插件（btop 摘要）；Time Machine 是**备份 / 状态指示**维度
- [Synology Hyper Backup](tool-synology-hyper-backup.md) — 群晖 NAS 原生备份方案；Time Machine 是在 Omarchy **桌面端**的轻量替代

## 参考链接
- 项目链接：<https://github.com/jankeesvw/omarchy-time-machine>
- 原始推文：<https://x.com/QingQ77/status/2093243686976946625>
- 媒体：<https://pbs.twimg.com/media/HQsnapsacAA1UWi.jpg>
