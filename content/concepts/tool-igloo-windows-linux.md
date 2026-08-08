---
type: "Tool"
title: "iGloo"
description: "Windows to Linux 现场迁移工具：收缩分区 → 装 Linux → 搬用户数据，全程不需要 U 盘或光盘，直接在原系统里完成切换。"
resource: "https://github.com/gillesduif/iGloo"
tags: [windows, linux, migration, installer, partition]
timestamp: "2026-08-08T20:30:00Z"
---

# iGloo

## 它是什么

iGloo 是一款 Windows → Linux 现场迁移工具，把整条流程「收缩 Windows 分区 → 装 Linux → 搬用户数据」收进一个工具，全程在原 Windows 系统里跑，无需 U 盘、光盘或外部启动介质。

## 为什么用它 / 适合什么场景

- 想从 Windows 平滑过渡到 Linux，但不愿折腾 U 盘启动盘。
- 不希望手动分区、调整启动项。
- 希望保留原有 Windows 分区作为回退。
- 想在个人 PC / 老旧设备上做系统切换实验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动分区收缩 | 在原 Windows 里腾出 Linux 空间 |
| 自动装 Linux | 选定发行版后直接安装 |
| 数据搬迁 | 把用户目录 / 文档搬到新系统 |
| 无外部介质 | 不用 U 盘 / 光盘 |
| 保留回退 | Windows 分区可保留 |

## 相关概念

- [TidyFS](./tool-tidyfs.md) — Linux 智能文件整理
- [Artix TUI Installer](./tool-artix-tui-installer.md) — 给 Artix Linux 用的终端安装器
- [linux-antiquity](./tool-linux-antiquity.md) — Hyprland 古典艺术风格主题包