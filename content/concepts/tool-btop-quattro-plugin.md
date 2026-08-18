---
type: Tool
title: "btop-quattro-plugin (ilyaZar/btop-quattro-plugin)"
description: "Omarchy 顶栏的 btop 系统监控插件：悬停看 CPU/内存/GPU/温度，点击图标拉起或聚焦 btop，让常驻顶栏也能实时感知系统状态"
resource: "https://github.com/ilyaZar/btop-quattro-plugin"
tags: [btop, omarchy, system-monitor, topbar, linux]
timestamp: "2026-08-18T12:00:00Z"
---

# btop-quattro-plugin (ilyaZar/btop-quattro-plugin)

## 它是什么
`ilyaZar/btop-quattro-plugin` 是 Omarchy 顶栏（Waybar 风格）的一款插件，把 btop 的核心系统监控能力**压缩到顶栏图标上**：鼠标悬停弹出 CPU / 内存 / GPU / 温度摘要，单击图标则拉起或聚焦 btop 主窗口。适合想保持顶栏极简、但又想随时感知机器负载的用户。

## 为什么用它 / 适合什么场景
- 不希望每次按快捷键看 btop，又不想塞满桌面挂件。
- 做编译 / 跑模型 / 玩游戏时，悬停顶栏即可瞥一眼 GPU 与温度。
- 想在已有 Waybar 配置里把 btop 变成「按需呼出 + 常驻摘要」组合。

## 关键能力
| 能力 | 说明 |
|------|------|
| 顶栏摘要 | 悬停顶栏图标弹出 CPU / 内存 / GPU / 温度 |
| 单击聚焦 | 点击图标拉起或聚焦 btop 主窗口 |
| Omarchy 集成 | 面向 Omarchy 顶栏配置体系 |
| btop 复用 | 数据来源复用 btop 已有的采集能力，不重复实现 |

## 媒体
- ![](https://pbs.twimg.com/media/HP5HD8VaEAAO_HZ.jpg)

## 相关概念
- [项目链接](https://github.com/ilyaZar/btop-quattro-plugin) — 仓库地址
