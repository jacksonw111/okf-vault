---
type: "Tool"
title: "omarchy-meeting-recorder（Omarchy 会议录音 + 转写应用）"
description: "jankeesvw 开源：给 Omarchy（Hyprland + Arch）做的会议录音应用，Rust + GTK 4 / libadwaita。麦克风与系统声音**分轨**录制，结束后自动生成带**说话人 / 章节 / 播放器**的转写稿。"
resource: "https://github.com/jankeesvw/omarchy-meeting-recorder"
tags: "[omarchy, hyprland, arch, meeting-recorder, transcription, rust, gtk, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# omarchy-meeting-recorder（Omarchy 会议录音 + 转写应用）

## 它是什么

[omarchy-meeting-recorder](https://github.com/jankeesvw/omarchy-meeting-recorder) 是 jankeesvw 开源的 **Omarchy 专用会议录音应用**——给「**Hyprland + Arch**」桌面环境做的原生应用：

- 语言：**Rust**
- 界面：**GTK 4 / libadwaita**

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | Omarchy（Hyprland + Arch） |
| 技术栈 | Rust + GTK 4 / libadwaita |
| **分轨录制** | 麦克风、系统声音**分开**录 |
| **说话人分离** | 自动识别不同说话人 |
| **章节** | 自动生成章节分段 |
| **播放器** | 内置带转写稿的播放界面 |

## 为什么用它 / 适合什么场景

- 用 **Omarchy / Hyprland / Arch** 桌面环境——通用会议录音工具要么不支持 Linux，要么不支持 Wayland。
- 想要**分轨**录制（后期可单独提取麦克风 / 系统声音）。
- 想要**自动说话人分离 + 章节 + 播放器** 的转写稿——开会后直接看回放 + 跳章节。

## 媒体

- ![](https://pbs.twimg.com/media/HTHxwxdbQAASwOx.jpg)

## 相关概念

- [Verenu](./tool-verenu.md) — Tauri + Svelte 按住说话听写（专注输入场景）
- [Purr](./tool-purr.md) — macOS Apple Silicon 菜单栏按住说话听写（端侧听写）