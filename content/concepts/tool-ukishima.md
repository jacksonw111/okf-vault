---
type: "Tool"
title: "Ukishima"
description: "Hyprland 上的动态岛式控制中心：把启动器 / 日历 / 媒体 / 混音器 / 壁纸 / 录屏 / 剪贴板 / WiFi / 蓝牙 / 电量 / 系统监控等面板全部收进屏幕顶部一条会展开的药丸状动态岛，鼠标悬停就在原地长成控制中心，不再弹独立窗口。"
resource: "https://github.com/amanhex/ukishima"
tags: ["hyprland", "wayland", "linux", "desktop-shell", "dynamic-island", "control-center"]
timestamp: "2026-08-12T04:17:00Z"
---

# Ukishima

[Ukishima](https://github.com/amanhex/ukishima) 是为 **Hyprland** 桌面打造的**动态岛式控制中心**：把启动器、日历、媒体、混音器、壁纸、录屏、剪贴板、WiFi、蓝牙、电量、系统监控等一堆面板**全部收进屏幕顶部一条药丸状"动态岛"**里，鼠标悬停就在原地展开成控制中心，不再弹独立窗口。

## 它是什么

Hyprland 桌面环境上的"全能型顶部面板"。模仿 iPhone 灵动岛 / Dynamic Island 的交互——屏幕顶部一条小条，按需展开成对应功能面板（媒体、WiFi、剪贴板等），交互后收回。

## 为什么用它 / 适合什么场景

- **Hyprland 用户**：Hyprland 默认缺少统一面板，Ukishima 填补。
- **替代多个独立组件**：以前要装 waybar + 一个启动器 + 一个混音器 + 一个剪贴板工具，Ukishima 一个搞定。
- **不抢屏幕**：悬停展开、收起恢复，避免独立窗口干扰。
- **macOS 式交互**：iPhone 灵动岛的范式移植到 Linux。

## 关键能力

| 能力 | 说明 |
|------|------|
| 顶部动态岛 | 屏幕顶部一条药丸状小条 |
| 多面板合一 | 启动器 / 日历 / 媒体 / 混音器 / 壁纸 / 录屏 / 剪贴板 / WiFi / 蓝牙 / 电量 / 系统监控 |
| 悬停展开 | 鼠标悬停在原地展开控制中心 |
| 不弹独立窗口 | 减少屏幕干扰 |
| Hyprland 集成 | 为 Hyprland 量身打造 |

## 媒体

![](https://pbs.twimg.com/media/HPaDp5WbIAApFmG.jpg)

## 参考链接

- [项目仓库](https://github.com/amanhex/ukishima)

## 相关概念

- [Caffyne Shell](./tool-caffyne-shell.md) — Python + GTK + Fabric 写的 Wayland 桌面外壳，同属 Wayland 桌面面板方案
- [Cyclop](./tool-cyclop.md) — MacBook 刘海工具面板，与 Ukishima 同属"屏幕边缘空间利用 + 多面板合一"思路