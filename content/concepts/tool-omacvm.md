---
type: "Tool"
title: "omacvm（在 Apple Silicon Mac 上以虚拟机方式跑 Omarchy）"
description: "让 Omarchy（Arch Linux ARM）在 Apple Silicon Mac 上像「原生应用一样」运行的虚拟机方案：通过 Parallels Desktop 或 UTM 5 装 Arch Linux ARM，再把 Mac 的 Wi-Fi / 音频 / 媒体键 / 触控板手势 / 显示器排列 / Night Shift / 壁纸透进虚拟机。"
resource: "https://github.com/gillesgoetsch/omacvm"
tags: "[omarchy, arch-linux, apple-silicon, vm, macos, linux-on-mac]"
timestamp: "2026-10-03T00:00:00Z"
---

# omacvm

## 它是什么

[omacvm](https://github.com/gillesgoetsch/omacvm) 是 **gillesgoetsch** 出品的「在 Apple Silicon Mac 上跑 Omarchy」虚拟机方案——通过 **Parallels Desktop** 或 **UTM 5** 建立一台跑 **Omarchy（Arch Linux ARM）** 的虚拟机，把 Mac 的硬件能力尽量透进 Linux，让 Arch 桌面在 macOS 里跑起来。

## 为什么用它 / 适合什么场景

- **想用 Omarchy 但不想放弃 macOS**：在 Mac 上开 VM 跑 Omarchy，Mac 仍可正常工作。
- **保留 Mac 体验**：Wi-Fi、音频、媒体键、触控板手势、显示器排列、Night Shift、壁纸这些 Mac 体验在 VM 内仍可用。
- **刘海友好**：用 Omanotch 把 Omarchy 的 bar 填进 Mac 刘海旁的黑条，不浪费屏幕空间。

## 关键能力

| 能力 | 说明 |
|------|------|
| 目标系统 | Omarchy（Arch Linux ARM） |
| 宿主机 | Apple Silicon Mac（M3 / M4 / M5） |
| 虚拟机平台 | Parallels Desktop 或 UTM 5 |
| 透传项 | Wi-Fi、音频、媒体键、触控板手势、显示器排列、Night Shift、壁纸 |
| 刘海适配 | 用 Omanotch 把 bar 嵌进刘海旁黑条 |

## 参考链接

- 项目链接：<https://github.com/gillesgoetsch/omacvm>

## 相关概念

- [Omarchy 桌面](./tool-impasto-arch-hyprland.md) — 类似 Arch + Hyprland 一体化桌面方向
