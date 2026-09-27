---
type: "Tool"
title: "phorminx（Windows 本地优先听写与会议转写）"
description: "impossibleG 出品的 Windows 本地优先听写与会议转写应用：语音识别 + 文本格式化都在本机跑，不绑定任何付费 AI 服务。Instant 模式常驻 Vosk 边说边出字，Accurate 模式走 Whisper 可开 Vulkan 加速；两者都用带上限滚动缓冲区做增量转写。"
resource: "https://github.com/impossibleG/phorminx"
tags: "[windows, dictation, meeting-transcription, vosk, whisper, local, vulkan]"
timestamp: "2026-09-27T21:55:00Z"
---

# phorminx（Windows 本地优先听写与会议转写）

## 它是什么

[phorminx](https://github.com/impossibleG/phorminx) 是 impossibleG 出品的 **Windows** 上**本地优先**的**听写**与**会议转写**应用：**语音识别 + 文本格式化都在本机跑**，不绑定任何付费 AI 服务。

## 关键能力：两套识别引擎

| 模式 | 引擎 | 特点 |
|------|------|------|
| **Instant** | Vosk | 常驻，边说边出字 |
| **Accurate** | Whisper | 可开 **Vulkan** 加速；适合会议场景 |

两者都用**带上限的滚动缓冲区**做**增量转写**——既保留实时性，又不会无限膨胀内存。

## 为什么用它 / 适合什么场景

- **Windows 用户**不想换 macOS 也能用本地转写。
- 想要**快（Vosk）** 与**准（Whisper）** 两档可切——日常听写用 Instant，会议记录用 Accurate。
- **不想订阅** Otter / Fireflies / 飞书妙记等付费服务。
- 想要**GPU 加速**（Whisper + Vulkan），提升 Accurate 模式吞吐。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Windows 桌面应用 |
| 定位 | 听写 + 会议转写 |
| 引擎 1 | Vosk（Instant 实时） |
| 引擎 2 | Whisper + Vulkan（Accurate 模式） |
| 增量 | 滚动缓冲区（带上限） |
| 隐私 | 全本地，音频不上云 |
| 替代 | Otter / Fireflies / 飞书妙记等付费服务 |

## 媒体

- ![](https://pbs.twimg.com/media/HTH5ijqbcAAO3XX.jpg)

## 相关概念

- [Purr](./tool-purr.md) — macOS Apple Silicon 菜单栏按住说话听写
- [Verenu](./tool-verenu.md) — Tauri + Svelte 按住说话听写（跨平台）