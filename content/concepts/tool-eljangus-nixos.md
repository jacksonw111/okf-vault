---
type: "Tool"
title: "Eljangus NixOS（eljangus/nixos）"
description: "把 NixOS 与 Nix-Darwin 的配置收进一份仓库,一台机器按需切 Niri / Plasma 6 / GNOME 三套桌面环境;适合想用单一配置同时管 Linux 服务器与 macOS 工作站的 Nix 用户。"
resource: "https://github.com/eljangus/nixos"
tags: "[nixos, nix-darwin, dotfiles, desktop-environment, niri, plasma, gnome]"
timestamp: "2026-08-11T16:00:00Z"
---

# Eljangus NixOS

[Eljangus NixOS](https://github.com/eljangus/nixos) 把 **NixOS 与 Nix-Darwin 的配置**收进同一份仓库,一台机器可以按需在 **Niri / Plasma 6 / GNOME** 三套桌面环境之间切换——Nix 生态下少见的"一份配置管多套桌面"实践。

项目链接：<https://github.com/eljangus/nixos>

## 它是什么

一份**统一的 Nix 配置仓库**:既管 NixOS Linux 也管 macOS(nix-darwin),用条件化切换让同一台物理机(或多台机器)在不同场景下加载不同的桌面环境。

## 为什么用它 / 适合什么场景

- **一份配置管 Linux + macOS**:Nix 生态少有的跨平台 dotfiles 范例。
- **多桌面环境自由切换**:不重装系统即可在 Niri / Plasma 6 / GNOME 之间挑当前合适的。
- **可复用的 dotfiles**:Nix 表达力强,别人 fork 即可得一套同风格的桌面。

## 关键能力

| 能力 | 说明 |
|------|------|
| NixOS + Nix-Darwin 统一 | 同一份仓库同时管 Linux 与 macOS |
| 多桌面环境 | Niri(Wayland 平铺)/ Plasma 6 / GNOME 可选 |
| 按需切换 | 不同机器 / 不同场景用同一仓库的不同 profile |
| 可复现 | 纯 Nix 表达,新机器上 checkout 即可还原 |
| 跨平台 dotfiles | macOS 用户能借鉴 Linux 上的桌面配置范式 |

## 媒体

![](https://pbs.twimg.com/media/HPU5Mdfa8AASS6m.jpg)

## 参考链接

- [项目仓库](https://github.com/eljangus/nixos)

## 相关概念

- [Dotfiles Manager](./tool-dotfiles-manager.md) — Rust 写的 dotfiles 同步工具,profile + backup/restore/check,与本工具思路互补
- [Caffyne Shell](./tool-caffyne-shell.md) — Python + GTK + Fabric 写的 Wayland 桌面外壳,也是 Niri 生态相关