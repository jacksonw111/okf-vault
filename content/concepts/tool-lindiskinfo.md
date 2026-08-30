---
type: "Tool"
title: "lindiskinfo（CrystalDiskInfo 启发的 Linux 磁盘健康监控）"
description: "Linux 下的磁盘健康监控工具：受 CrystalDiskInfo 启发，用图形化方式呈现 S.M.A.R.T. 与 NVMe 健康状态——给 Linux 用户一个「终于有了」的等价物。"
resource: "https://github.com/pacmanics/lindiskinfo"
tags: [linux, disk-health, smart, nvme, monitoring, crystaldiskinfo]
timestamp: "2026-08-30T21:50:00Z"
---

# lindiskinfo

## 它是什么
[pacmanics/lindiskinfo](https://github.com/pacmanics/lindiskinfo) 是**受 CrystalDiskInfo 启发**的 Linux 磁盘健康监控工具——用图形化界面呈现 **S.M.A.R.T.** 与 **NVMe** 健康状态。

Windows 用户有 CrystalDiskInfo 几十年了，Linux 上对应的「**一眼看清硬盘寿命**」的工具长期缺位。lindiskinfo 补的就是这个位置：

- 读 S.M.A.R.T. 属性（重映射扇区、温度、读写量、寿命……）；
- 读 NVMe 健康指标（Percentage Used、Media Errors、温度……）；
- 用**类似 CrystalDiskInfo 的彩色温度条**直观呈现；
- 给家用 NAS / 工作站一个轻量监控入口。

## 为什么用它 / 适合什么场景
- 跑家用 NAS / Linux 工作站，想**定期看硬盘健康**；
- 不喜欢命令行 `smartctl -a /dev/sda` 的人肉解读；
- 想给非技术家庭成员一个**「看硬盘坏没坏」**的图形化工具；
- 想要 CrystalDiskInfo 的体验，但不想开 Wine / 虚拟机跑 Windows。

## 关键能力

| 能力 | 说明 |
|------|------|
| S.M.A.R.T. 读取 | 解析 `smartctl` 输出 |
| NVMe 健康 | Percentage Used / Media Errors / 温度 |
| 图形化 | 类似 CrystalDiskInfo 的彩色温度条 |
| Linux 原生 | 无需 Wine / 虚拟机 |
| 家用友好 | 一眼判断「**健康 / 警告 / 危险**」 |

## 媒体
- ![](https://pbs.twimg.com/media/HQ-FHSUa4AAtCZF.jpg)

## 相关概念
- [Synology Hyper Backup](term-synology-hyper-backup.md) — 群晖 NAS 备份；lindiskinfo 是「**备份之前的健康监控**」配套
- [Omarchy Time Machine](tool-omarchy-time-machine.md) — 另一类「**轻量备份 / 监控**」桌面插件思路

## 参考链接
- 项目链接：<https://github.com/pacmanics/lindiskinfo>
