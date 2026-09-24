---
type: "Tool"
title: "omarchy-icloud-photos（Linux 上的 iCloud 照片同步）"
description: "Linux 上没有 iCloud 照片客户端、网页版要反复重新登录——这个工具把最近一个月的 iCloud 相册同步到本地，并用 Quickshell + QML 写的原生窗口按天浏览。"
resource: "https://github.com/jankeesvw/omarchy-icloud-photos"
tags: "[linux, icloud, photos, quickshell, qml, omarchy, sync, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# omarchy-icloud-photos（Linux 上的 iCloud 照片同步）

## 它是什么

[omarchy-icloud-photos](https://github.com/jankeesvw/omarchy-icloud-photos) 是为 Omarchy 桌面做的一个 iCloud 相册同步工具：把最近一个月的 iCloud 相册同步到本地，并用 QML 写的 Quickshell 窗口按天浏览，最新的排到底部。

## 它解决的问题

- Linux 没有官方 iCloud 照片客户端
- 网页版要反复重新登录，体验差
- 想在 Linux 桌面上和 macOS 一样按天翻看最近照片

## 实现要点

| 模块 | 内容 |
|------|------|
| 界面 | Quickshell 窗口 + QML 写的按天网格 |
| 下载 | 借用 icloudpd 的 `pyicloud` 模块（不 fork 整个项目） |
| 范围 | 仅同步最近一个月 |
| 排序 | 按天排网格，最新的在底 |

## 适用场景

- Linux 桌面用户想把 iCloud 相册同步到本地浏览
- Omarchy 桌面用户（针对该桌面优化）
- 不想为「看照片」装 Wine 跑 iCloud for Windows

## 原始链接
- 项目主页：<https://github.com/jankeesvw/omarchy-icloud-photos>

## 相关概念
- [Omarchy Blue Hour Theme](./tool-omarchy-blue-hour-theme.md) — 同为 Omarchy 桌面工具