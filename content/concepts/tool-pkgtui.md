---
type: Tool
title: "pkgtui（padovanl/pkgtui）"
description: "htop 风格终端界面同时管理 apt 与 snap 包，搜索 / 安装 / 移除 / 升级一站完成，免背两套包管理器命令"
resource: "https://github.com/padovanl/pkgtui"
tags: "[linux, tui, apt, snap, package-manager]"
timestamp: "2026-08-19T16:00:00Z"
---

# pkgtui（padovanl/pkgtui）

## 它是什么
[`padovanl/pkgtui`](https://github.com/padovanl/pkgtui) 是一个 htop 风格的 Linux 终端 TUI：**同时**把 apt（Debian 系）和 snap（Ubuntu 默认）的搜索、安装、移除、升级全部收到同一面板里操作，免去背两套命令的麻烦。

## 为什么用它 / 适合什么场景
- Ubuntu 用户想用 apt 又偶尔要管 snap 包，命令两套记不住。
- 想要一个统一的「包管理面板」，鼠标 / 键盘方向键就能完成日常动作。
- 服务器 / WSL 里没有 GUI 桌面，又想要比纯命令更直观的交互。

## 关键能力
| 能力 | 说明 |
|------|------|
| 双后端统一 | 同时支持 apt 与 snap，结果聚合在一个列表 |
| htop 风格交互 | 上下键浏览、搜索框过滤、确认键执行 |
| 完整动作覆盖 | 搜索 / 安装 / 移除 / 升级 4 类常用操作 |
| TUI 优先 | 跑在终端里，不依赖图形环境 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HP6RUb9bwAAuXqL.mp4>

## 相关概念
- [项目仓库](https://github.com/padovanl/pkgtui) — 仓库主页
- [tuios](./tool-tuios.md) — 同样是 TUI / 终端复用器，但偏终端会话管理