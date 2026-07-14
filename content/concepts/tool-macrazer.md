---
type: "Tool"
title: "MacRazer（SorcRR/MacRazer）"
description: "macOS 菜单栏小程序,直接走 USB HID 控制 Razer 鼠标:电量 / DPI / 灯效 / 回报率都能调,绕过只认少数型号的官方 Synapse。"
resource: "https://github.com/SorcRR/MacRazer"
tags: "[macos, razer, mouse, menu-bar, usb-hid, hardware-control]"
timestamp: "2026-07-14T04:57:00Z"
---

# MacRazer

[MacRazer](https://github.com/SorcRR/MacRazer) 是 macOS 上的**菜单栏小程序**,直接走 **USB HID** 协议对 **Razer 鼠标**做底层控制:电量 / DPI / 灯效 / 回报率都能调,绕过只认少数型号的官方 Synapse。

## 关键能力

| 能力 | 说明 |
|------|------|
| 电量显示 | 当前电池余量 |
| DPI 切换 | 多档可调,即刻生效 |
| 灯效调节 | 自带光效切换 / 亮度 |
| 回报率 | 125 / 500 / 1000 Hz 等 |
| 菜单栏优先 | 不占 Dock,常驻 status bar |
| USB HID | 不依赖 Synapse / Razer Center |

## 适合什么场景

- 在 macOS 上使用 Razer 鼠标却**不想装 Synapse**(系统开销 + 模型白名单)。
- 想读鼠标**电量**等 Synapse 不暴露的状态。
- 极简工具党:**一个菜单栏图标,所有硬件控制**。

## 与同类资源的差别

| 资源 | 特征 | MacRazer |
|------|------|----------|
| MacTools | 通用 macOS 菜单栏工具集 | 通用;MacRazer 专攻 Razer 鼠标 |
| Razer Synapse | 官方软件,只支持部分型号 | MacRazer 是 Synapse 的开源补位 |
| OpenMac | 系统能力暴露 JSON API | 偏系统能力;MacRazer 偏硬件 |

## 参考链接

- [项目仓库](https://github.com/SorcRR/MacRazer)

## 相关概念

- [MacTools](./tool-mac-tools.md) — 通用 macOS 菜单栏工具集,MacRazer 是其下专攻 Razer 的子工具
- [OpenMac](./tool-openmac.md) — 同样把 macOS 系统能力开放,MacRazer 偏硬件 HID
