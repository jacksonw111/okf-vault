---
type: Tool
title: "Dextop（把手机变桌面工作区的 Android 虚拟显示应用）"
description: "NarYuki 开源的 Android 应用：用虚拟显示把手机本机变成一块「桌面工作区」，1.5.0 起自带特权访问运行时（root），调用系统服务接管应用启动、窗口摆放、触摸输入和屏幕旋转。"
resource: "https://github.com/NarYuki/Dextop"
tags: [android, virtual-display, desktop, mobile, root, window-manager]
timestamp: 2026-10-01T09:24:00Z
---

# Dextop

## 它是什么

**Dextop** 是 [NarYuki](https://github.com/NarYuki) 维护的开源 Android 应用。核心思路是**用 Android 虚拟显示（VirtualDisplay）API** 把手机本机变成一块「桌面工作区」——让应用跑在虚拟显示里、由系统统一管理窗口摆放、触摸输入和屏幕旋转。

从 **1.5.0** 起它**自带特权访问运行时（root）**，直接调用系统服务接管应用启动、窗口摆放、触摸输入和屏幕旋转，把虚拟显示从「开发玩具」推向「真桌面」。

## 为什么用它 / 适合什么场景

- 旧手机 / 副机不想扔，但日常系统已经不够用，希望**复用为桌面小工作站**。
- 折腾 Android ROM / 多窗口 / 模拟桌面交互的玩家。
- 想用一台机器同时跑多个独立「桌面环境」，按场景切换。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | Android |
| 核心技术 | VirtualDisplay 虚拟显示 |
| 权限 | 自带特权访问运行时（root） |
| 接管范围 | 应用启动 / 窗口摆放 / 触摸输入 / 屏幕旋转 |
| 形态 | 一款独立 App |
| 开源协议 | 见仓库 |

## 参考链接

- 仓库：<https://github.com/NarYuki/Dextop>

## 媒体

- ![](https://pbs.twimg.com/media/HTg8SYyaoAAGS3P.jpg)

## 相关概念

- [Space 桌面](https://github.com/Space Desktop) — 同为 Android 桌面化方向的项目（外部链接，需自核）
- [Samsung DeX](https://www.samsung.com/apps/dex/) — 商业产品的同类思路（外部链接）
