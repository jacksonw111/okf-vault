---
type: "Tool"
title: "appmop"
description: "cesarferreira 写的 macOS 应用 + 残留文件清理工具：列出 macOS 应用及其关联的 Library 残留（缓存 / 偏好 / 容器 / 支持文件），勾选后一键丢进废纸篓，无需手动翻 ~/Library。"
resource: "https://github.com/cesarferreira/appmop"
tags: [macos, cleanup, uninstaller, library, terminal]
timestamp: "2026-08-09T19:35:00Z"
---

# appmop

## 它是什么

[appmop](https://github.com/cesarferreira/appmop) 是 macOS 终端里的「应用 + 残留」清理工具：扫描 `/Applications` 里装的应用，并找出它们留在 `~/Library` 下的缓存 / 偏好 / 容器 / 支持文件，**勾选后一键丢进废纸篓**，不需要手动翻 Library。

## 为什么用它 / 适合什么场景

- 卸 macOS 应用时，常规「移到废纸篓」留下大量 Library 残留。
- 想批量清理多个应用 + 它们的关联文件，但不想装 CleanMyMac 之类的闭源软件。
- 想保留「可在废纸篓恢复」的安全网，不像 `rm -rf` 那样不可逆。
- 想在终端里完成清理，便于脚本化 / 远程操作。

## 关键能力

| 能力 | 说明 |
|------|------|
| 应用 + 残留扫描 | 自动找出应用对应的 Library 路径 |
| 勾选式 UI | 列出候选清单，用户勾选后再操作 |
| 废纸篓而非 rm | 操作可逆，安全网保留 |
| CLI 友好 | 终端操作，便于脚本 / SSH 远程 |
| 开源 | 可审计、可定制 |

## 媒体

![](https://pbs.twimg.com/media/HPMb_ATaYAAk8SO.jpg)

## 相关概念

- [macos-disk-cleanup](./tool-macos-disk-cleanup.md) — 类似的 macOS 磁盘清理工具，专注于「按危险分级扫描包管理器缓存」