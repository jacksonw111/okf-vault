---
type: Tool
title: "Sift (macOS)"
description: "macOS 本地应用，把存储分析 / 清理 / 卸载 / 网络排查等六类操作集中到一处——扫描只读元数据，删除先进废纸篓，保证数据不出本机。"
resource: "https://github.com/rhevorn/sift"
tags: "[macos, utility, storage, cleanup, uninstaller, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# Sift (macOS)

## 它是什么
一个 **macOS 本地应用**，把 macOS 日常维护里分散在不同工具 / 设置项里的操作，集中到一个 app 里：

- 存储分析（看大文件 / 大目录）
- 清理（缓存 / 临时文件）
- 应用卸载
- 网络排查
- 其他系统级维护（具体 6 类）

**隐私姿态**：扫描只读**元数据**；删除先送**废纸篓**（不进 Finder 删除是「不可逆」）；数据**不出本机**。

## 为什么用它 / 适合什么场景
- 不想用「CleanMyMac」类闭源工具——Sift 开源 + 本地处理。
- 想把 macOS 维护工具集中到一个应用，少装几款。
- 注重数据安全：扫描只读元数据、删除可回滚（废纸篓）。
- 给 macOS 新用户一个一站式维护入口。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | macOS |
| 集中操作 | 6 类（存储分析 / 清理 / 卸载 / 网络排查等） |
| 扫描方式 | 只读元数据 |
| 删除策略 | 先废纸篓（可回滚） |
| 数据流向 | 不出本机 |
| 形态 | 本地应用 |

## 相关概念
- [synology-hyper-backup](term-synology-hyper-backup.md) — 备份工具；Sift 是「清理 / 维护」向，两者不重叠但都是「数据生命周期」工具

## 媒体
- 界面截图：<https://pbs.twimg.com/media/HPfVjGEa0AAUIPa.png>

## 项目链接
- 项目主页：<https://github.com/rhevorn/sift>