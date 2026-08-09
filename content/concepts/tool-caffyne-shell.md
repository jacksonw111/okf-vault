---
type: "Tool"
title: "caffyne-shell"
description: "caffyne-org 写的 Wayland 桌面外壳（Python + GTK，跑在 Fabric 框架上）：面板可拖拽调整，内置 15 个小程序管启动器 / 设置 / 通知 / 时钟 / 天气 / 媒体 / 音量 / WiFi / 蓝牙 / 电源；主题色由 Matugen 从壁纸自动生成 Material You 配色；Niri 稳定、Hyprland 与 MangoWM 还在 Beta。"
resource: "https://github.com/caffyne-org/caffyne-shell"
tags: [wayland, desktop-shell, python, gtk, fabric, matugen, material-you]
timestamp: "2026-08-09T19:35:00Z"
---

# caffyne-shell

## 它是什么

[caffyne-shell](https://github.com/caffyne-org/caffyne-shell) 是 **Wayland 桌面外壳**：用 Python + GTK 写成，跑在 [Fabric](https://github.com/Fabric-Development/fabric) 框架上。面板可拖拽调整，内置 15 个小程序（applet）覆盖日常需要：启动器、设置、通知、时钟、天气、媒体、音量、WiFi、蓝牙、电源等。主题色由 [Matugen](https://github.com/InioX/matugen) **从壁纸里取色自动生成 Material You 配色**。**Niri 支持较稳定**，**Hyprland 与 MangoWM 还在 Beta**。

## 为什么用它 / 适合什么场景

- 在 Niri / Hyprland / MangoWM 等 Wayland compositor 上想要一个比默认 bar / waybar 更完整的桌面外壳。
- 喜欢 Material You「壁纸即主题」的视觉一致性。
- 想用 Python + GTK 而非 QML / Rust 定制 Wayland 面板（学习曲线低）。
- 想在 Wayland 上得到接近 macOS Sonoma / iOS 的「面板 + 小程序」UX 范式。

## 关键能力

| 能力 | 说明 |
|------|------|
| Wayland 桌面外壳 | Python + GTK + Fabric 框架 |
| 15 个内置 applet | 启动器 / 设置 / 通知 / 时钟 / 天气 / 媒体 / 音量 / WiFi / 蓝牙 / 电源等 |
| 拖拽面板 | 面板布局可拖拽调整 |
| Material You 主题 | Matugen 从壁纸自动取色 |
| Niri 支持 | 较稳定 |
| Beta 兼容 | Hyprland / MangoWM 还在 Beta |

## 媒体

视频：
- <https://video.twimg.com/amplify_video/2086068252040630272/vid/avc1/1280x800/8BxBeUgtMbyj0Pft.mp4?tag=29>

## 相关概念

- [Denial (Wayland)](./tool-denial-wayland.md) — Flutter 写桌面图形层的 Wayland 合成器（更底层）
- [linux-antiquity](./tool-linux-antiquity.md) — Hyprland 古典艺术风格主题包