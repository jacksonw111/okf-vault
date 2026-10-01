---
type: Tool
title: "appimg（Rust + TUI 写的 AppImage 桌面级管理器）"
description: "MrGilfy 出品的 Linux 命令行工具：带 TUI 界面，把 AppImage 当正经桌面应用来管理（搜索 / 安装 / 启动 / 更新），全部操作限制在 `$HOME` 内，不写系统目录。"
resource: "https://github.com/MrGilfy/appimg"
tags: [appimage, linux, tui, rust, home-only, package-manager]
timestamp: 2026-10-01T07:49:00Z
---

# appimg

## 它是什么

**appimg** 是 [MrGilfy](https://github.com/MrGilfy) 用 **Rust** 写的 Linux 命令行工具，带 **TUI 界面**，把 **AppImage** 当成**正经桌面应用**来管理（搜索 / 安装 / 启动 / 更新）。

最大特色：**全部操作限制在 `$HOME` 内**——不写 `/usr/bin`、`/opt`、`/etc` 等系统目录。这对「不能 root」「不想污染系统」「希望完全可移植」的用户极其友好。

## 为什么用它 / 适合什么场景

- 想用 AppImage 但不想手动 chmod + 软链 + 写 `.desktop` 文件。
- 受限环境（公司机 / 学校机 / 容器 / 共享主机）只能改 `$HOME`，希望照样管理 AppImage。
- 喜欢 TUI 工具的高效操作。
- 希望 AppImage 的元数据 / 安装信息可一键清理。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实现 | Rust |
| 界面 | TUI |
| 管理对象 | AppImage |
| 操作范围 | 全部限制在 `$HOME` 内 |
| 系统目录写入 | 否 |
| 典型动作 | 搜索 / 安装 / 启动 / 更新 |

## 参考链接

- 仓库：<https://github.com/MrGilfy/appimg>

## 媒体

- ![](https://pbs.twimg.com/media/HTdz999aAAAN3Ou.jpg)

## 相关概念

- [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher) — 同类 AppImage 桌面集成工具（外部链接，需自核）
- [Nix Package Manager](https://nixos.org/) — 同样「用户态可装」思路的更重量级方案（外部链接）
