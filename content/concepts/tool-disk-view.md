---
type: "Tool"
title: "disk_view（Textual 磁盘分区 TUI 浏览器）"
description: "为 Linux 提供交互式磁盘分区浏览与挂载管理的终端界面：基于 Textual + Python 3.10+，可视化磁盘用量条、Vim 风格 jkhl 键盘导航、详情面板，已用/剩余空间双视图切换。"
resource: "https://github.com/Pratham-Chauhan/disk_view"
tags: "[linux, tui, disk, textual, python]"
timestamp: "2026-09-11T22:00:00Z"
---

# disk_view

## 它是什么

[Pratham-Chauhan/disk_view](https://github.com/Pratham-Chauhan/disk_view) 是一个基于 **Textual** 的 **Linux 磁盘 / 分区浏览器**（Python 3.10+），把「分区列表 + 用量条 + 详情面板 + Vim 风格导航」塞进终端 TUI：

- 每个分区展示可视化磁盘用量条
- 支持 **jkhl** Vim 风格键盘导航
- 分区详情面板查看 UUID / 挂载点 / 文件系统 / 已用 vs 剩余
- 已用空间 / 剩余空间两种视图切换

## 为什么用它 / 适合什么场景

- 远程 Linux 服务器 SSH 上去想看分区占用，又不想跑 `df -h` 反复对列。
- 想找一个比 `fdisk -l` / `lsblk` 更直观的 GUI 替代（在终端里）。
- 想学习 Textual（TUI 框架）的实战样例。

## 关键能力

| 能力 | 说明 |
|------|------|
| 分区列表 | 自动扫描所有块设备 |
| 用量条 | 每分区可视化磁盘占用 |
| Vim 键位 | jkhl 导航，零学习成本 |
| 详情面板 | UUID / 挂载点 / 文件系统 |
| 双视图 | 已用 vs 剩余空间切换 |
| TUI | 纯终端，SSH 友好 |

## 参考链接

- 项目仓库：<https://github.com/Pratham-Chauhan/disk_view>

## 媒体

- ![](https://pbs.twimg.com/media/HRx-h2IbUAAbANf.jpg)

## 相关概念

- [Pi.Alert](./tool-pi-alert.md) — 局域网设备监控与入侵检测面板
- [super-lan-cache](./tool-super-lan-cache.md) — 同为局域网 / Linux 自托管工具
</content>
</invoke>