---
type: Tool
title: "chippytea（macOS 原生清理小工具）"
description: "常驻菜单栏的 Mac 清理工具，SwiftUI 界面 + Rust 引擎；扫描指定文件夹里的旧缓存、日志、Xcode 产物、构建目录和大文件，删除前先展示体积与后果。要求 macOS 14+。"
resource: "https://github.com/richiemcilroy/chippytea"
tags: [macos, cleanup, disk-space, swiftui, rust, menubar]
timestamp: 2026-09-04T12:00:00Z
---

# chippytea（macOS 原生清理小工具）

## 它是什么

一个平时待在菜单栏里的 Mac 原生清理工具：界面用 SwiftUI，扫描引擎用 Rust。要求 macOS 14 以上。

![](https://pbs.twimg.com/media/HRRUqE9bIAAHoNt.jpg)

## 为什么用它 / 适合什么场景

- 开发机磁盘被 Xcode 产物 / 各语言构建目录悄悄吃满，但不敢乱删。
- 不想装商业清理套件（往往捆绑一堆用不上的「优化」功能）。
- 它**只扫你指定的文件夹**，删之前先给你看体积和后果——比一键「智能清理」可控。

## 关键能力

| 能力 | 说明 |
|------|------|
| 扫描范围 | 用户指定的文件夹，非全盘扫荡 |
| 识别目标 | 旧缓存、日志、Xcode 产物、构建目录、大文件 |
| 删除前确认 | 展示每项体积与删除后果 |
| 技术栈 | SwiftUI 界面 + Rust 引擎，常驻菜单栏 |
| 系统要求 | macOS 14 及以上 |

## 参考链接

- 项目链接：<https://github.com/richiemcilroy/chippytea>
- 原始链接：<https://x.com/QingQ77/status/2095750706355372281>

## 相关概念

- [macos-disk-cleanup](./tool-macos-disk-cleanup.md) — 同样解决 macOS 磁盘被缓存 / 构建产物吃满的问题；那个是只读扫描脚本，chippytea 是带图形界面的原生应用
