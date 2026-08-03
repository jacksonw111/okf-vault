---
type: Tool
title: "OpenDisk"
description: "免费开源的 macOS 磁盘空间分析器（MIT 协议），把整个磁盘映射成交互式旭日图，每一圈代表一层目录深度，悬停扇区可查看精确大小，点击缩放进入，扫描过程中结果实时流入图表和列表。"
resource: "https://github.com/137137137/OpenDisk"
tags: [macos, disk, sunburst, visualization, open-source, daisydisk-alternative]
timestamp: "2026-08-03T16:09:00Z"
---

# OpenDisk

## 它是什么
OpenDisk（`137137137/OpenDisk`）是一款免费开源的 macOS 磁盘空间分析器，MIT 协议发布，是 DaisyDisk 的开源替代品。它把整个磁盘映射为交互式旭日图，每一圈代表一层目录深度，悬停任一扇区可查看精确大小，点击即可缩放进入该子目录，扫描过程中结果会实时流入图表和列表。

![OpenDisk 旭日图示例](https://pbs.twimg.com/media/HOzsjktaQAEvhlI.jpg)

## 为什么用它 / 适合什么场景
- **开源 MIT 协议**：商业可用、可审计，DaisyDisk 是闭源付费的。
- **直观可视化**：旭日图比饼图 / 树状图更适合表达多层目录嵌套。
- **实时反馈**：扫描过程中结果实时流入，无需等完整扫描结束。
- **macOS 原生**：针对 macOS 文件系统（APFS、HFS+）优化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 旭日图映射 | 整盘映射为多层圆环，每圈代表一层目录深度 |
| 实时扫描 | 扫描过程中结果持续流入图表与列表 |
| 点击缩放 | 点击任一扇区即缩放进入该子目录 |
| 悬停信息 | 鼠标悬停显示精确大小、文件 / 目录占比 |
| 双视图 | 旭日图 + 列表同屏，方便对照核对 |

## 项目链接
- <https://github.com/137137137/OpenDisk>

## 相关概念
- [FolderSizeExplorer](./tool-folder-size-explorer.md) — Windows 等价方案：边浏览文件边递归统计文件夹大小
- [StorageUI](./tool-storageui.md) — 自托管 S3/Cloudflare R2 文件浏览器，四种视图
- [Talivia](./tool-talivia.md) — 网站分析 + 支付数据并到一图，同属「可视化 + 占用分析」思路
