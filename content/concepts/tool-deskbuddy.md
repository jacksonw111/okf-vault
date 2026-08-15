---
type: "Tool"
title: "DeskBuddy（Mac 菜单栏蓝牙升降桌控制）"
description: "在 Mac 菜单栏直接控制 IKEA IDÅSEN 这类蓝牙升降桌：常用高度存成预设一键升降，双击实体控制板切换位置，还会按坐站间隔提醒你换姿势。"
tags: "[macos, bluetooth, sit-stand-desk, menu-bar, health]"
timestamp: "2026-08-15T11:22:00Z"
resource: "https://github.com/koenigderorangen/DeskBuddy"
---

# DeskBuddy（Mac 菜单栏蓝牙升降桌控制）

## 它是什么

`koenigderorangen/DeskBuddy` 是一个 macOS 菜单栏应用，专门控制 IKEA IDÅSEN 等品牌的**蓝牙升降桌**。它把升降桌的控制从桌面下方的实体控制板搬到了 Mac 菜单栏：

- 预设常用高度（一键升降）。
- 双击实体控制板上的按钮 → 切换位置（坐 / 站）。
- 按坐 / 站间隔定时提醒你换姿势。

> ![](https://pbs.twimg.com/media/HPphw89bgAAzG2S.jpg)

## 为什么用它 / 适合什么场景

- **不用弯腰按实体控制板**：Mac 菜单栏就能升降。
- **预设高度**：站立 / 坐下各一个预设，一键切换。
- **健康提醒**：坐着超过 50 分钟 → 提醒站立。
- **多品牌支持**：除了 IDÅSEN，也支持其它用 Linak / 兼容蓝牙协议的升降桌。

## 关键能力

| 能力 | 说明 |
|------|------|
| 菜单栏 UI | 直接在 Mac 顶部菜单栏操作升降 |
| 预设高度 | 自定义坐 / 站高度，命名 + 一键到位 |
| 蓝牙直连 | 通过 Linak 蓝牙协议直连升降桌 |
| 实体控制板双击 | 双击控制板按钮 → 切换坐 / 站 |
| 坐站提醒 | 按用户设置间隔弹出通知 |
| 多品牌 | IDÅSEN 等支持 Linak 协议的升降桌 |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| 实体控制板 | 桌子自带 | 需弯腰、无预设 |
| 通用蓝牙工具 | 控制多种蓝牙设备 | 不专注升降桌 |
| **DeskBuddy** | **专为升降桌 + 菜单栏** | **预设 + 提醒 + 双击切换** |

## 适用人群

- 用 IKEA IDÅSEN / 同类蓝牙升降桌的 Mac 用户。
- 想养成「定时换姿势」习惯的人。
- 不愿反复弯腰按实体控制板的人。

## 参考链接

- [项目链接](https://github.com/koenigderorangen/DeskBuddy)

## 相关概念

- [MacTools](tool-mac-tools.md) — 免费开源 macOS 菜单栏工具集
- [CloseUp](tool-closeup.md) — 开源 macOS 原生小工具，给 Mission Control 缩略图加按钮