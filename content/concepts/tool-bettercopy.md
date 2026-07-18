---
type: "Tool"
title: "BetterCopy（articulite/BetterCopy）"
description: "用 Rust 写的 Windows 文件复制/删除加速工具，让普通用户零配置就能拿到接近 robocopy 这类命令行的并行复制/删除速度。"
tags: "[rust, windows, file-copy, performance, cli, gui]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/articulite/BetterCopy"
---

# BetterCopy（articulite/BetterCopy）

## 它是什么

[`BetterCopy`](https://github.com/articulite/BetterCopy) 是 articulite 开源的 Windows 文件操作加速器，用 **Rust** 实现：

- 把普通 Explorer「复制 / 剪切 / 删除」替换成并行实现；
- 用户不需要任何命令行知识、不需要学 robocopy 的开关；
- 体验上「右键 → 复制」即获得并行 I/O 带来的速度提升。

## 解决的问题

| 痛点 | 说明 |
|------|------|
| Windows 原生复制慢 | 串行处理 + 单缓冲，大文件/大量小文件都很慢 |
| robocopy 上手难 | 命令行参数多，普通用户不愿用 |
| 删除 / 移回收站卡 | NTFS 配额或海量小文件场景下经常假死 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 并行复制 | 多线程并发读 / 写，突破单缓冲瓶颈 |
| 零配置 | 装好即用，默认参数已经覆盖大多数场景 |
| 删除加速 | 绕开「移入回收站」的串行开销 |
| 资源占用克制 | Rust 写、内存占用低，不抢系统 |

## 适合什么场景

- 经常需要搬运大目录 / 大文件集合的 Windows 用户；
- 开发机 / 备份机 / 二手数据盘整理；
- 不想学 robocopy、又想获得并行 I/O 速度的普通用户。

## 演示视频

- [原始视频](https://video.twimg.com/amplify_video/2078318332017881088/vid/avc1/1280x720/1JMb9YHtgncVv7ci.mp4?tag=29)

## 参考链接

- [原始链接](https://github.com/articulite/BetterCopy)

## 相关概念

- [undo](tool-undo.md) — 同样为命令行体验「兜底」：BetterCopy 让复制变快，undo 让误删可撤销，两者常一起部署