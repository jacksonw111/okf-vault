---
type: "Tool"
title: "MangoDisk（harry0703/MangoDisk）"
description: "macOS / Windows 上的磁盘清理与空间分析工具,清理前先按类别扫描并给用户确认,不自动删任何东西,顺带覆盖找重复文件、删大文件、干净卸载应用几个常见需求。"
resource: "https://github.com/harry0703/MangoDisk"
tags: "[disk-cleanup, storage, macos, windows, duplicate-finder, uninstaller]"
timestamp: "2026-08-11T16:00:00Z"
---

# MangoDisk

[MangoDisk](https://github.com/harry0703/MangoDisk) 是 macOS / Windows 上的**磁盘清理与空间分析工具**,区别于"一键自动清理"的同类,它要求**清理前先逐类扫描并把清单交给用户确认,不自动删任何东西**,顺带覆盖找重复文件、删大文件、干净卸载应用几个常见需求。

项目链接：<https://github.com/harry0703/MangoDisk>

## 它是什么

一站式磁盘/存储治理桌面应用,把"找大文件 / 找重复 / 清缓存 / 干净卸载"四件事收到一个 GUI 里,但所有破坏性动作必须由人点击确认才执行。

## 为什么用它 / 适合什么场景

- **想清理又怕误删**:默认不自动删除,所见即所删。
- **磁盘空间管理**:可视化按目录 / 类型看占用,定位大文件。
- **应用卸载干净**:不少应用内置卸载器留下残留,MangoDisk 提供"干净卸载"路径。
- **跨平台**:macOS 与 Windows 同款体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 分类扫描 | 缓存 / 大文件 / 重复文件 / 应用残留分别扫描 |
| 用户确认制 | 不自动删除,所有清理动作必须人工确认 |
| 重复文件查找 | 哈希比对找完全重复或近似重复 |
| 大文件定位 | 按体积排序快速找出占用大头 |
| 干净卸载 | 卸载应用时顺带清理 Library / 缓存残留 |
| macOS + Windows | 跨平台桌面应用 |

## 媒体

![](https://pbs.twimg.com/media/HPU4pXIagAAAKL9.jpg)
![](https://pbs.twimg.com/media/HPU4qZXaMAAGJnY.jpg)

## 参考链接

- [项目仓库](https://github.com/harry0703/MangoDisk)

## 相关概念

- [AppMop](./tool-appmop.md) — macOS 终端应用 + Library 残留清理工具,与本工具互补(终端 vs GUI)
- [macOS Disk Cleanup](./tool-macos-disk-cleanup.md) — 只读扫描 macOS 磁盘按危险分级