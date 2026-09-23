---
type: "Tool"
title: "YoVoice"
description: "本地文字转语音工具，macOS 与 Windows 都提供安装包——推理交给 audio.cpp，集成 IndexTTS 2.0/2.5、VoxCPM2、OmniVoice、Qwen3-TTS 等多模型，可界面与 CLI 双调用。"
resource: "https://github.com/leemysw/yovoice"
tags: "[tts, voice, audio-cpp, local-inference, open-source, multi-model]"
timestamp: "2026-09-23T22:35:00Z"
---

# YoVoice

## 它是什么

[YoVoice](https://github.com/leemysw/yovoice) 是一个**本地运行的文字转语音工具**：

> 一个跑在本机的语音工具，macOS 和 Windows 都给了安装包，写完文字直接合成有人味的声音。

底层推理由 **audio.cpp** 承担，集成了多套 TTS 模型——**IndexTTS 2.0/2.5、VoxCPM2、OmniVoice、Qwen3-TTS** 都可在界面与 CLI 中调用。

## 为什么用它 / 适合什么场景

- 需要**本地 TTS**（不出网、隐私敏感场景）。
- 想在一款工具里**横向对比多套 TTS 模型**（不必分别下载）。
- 需要 GUI + CLI 双入口（开发者 + 非技术用户都用得上）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模型 | IndexTTS 2.0/2.5、VoxCPM2、OmniVoice、Qwen3-TTS |
| 推理 | 本地 audio.cpp |
| 形态 | GUI + CLI 双入口 |
| 平台 | macOS / Windows 安装包 |
| VoxCPM2 | 48 kHz，自动识别 30 种语言 |
| Qwen3-TTS CustomVoice | 自带 9 个音色 |
| 语言支持 | 自动识别 30 种语言 |

## 项目链接
- 项目主页：<https://github.com/leemysw/yovoice>

## 媒体
![YoVoice 截图 1](https://pbs.twimg.com/media/HSyjS6gb0AAS7nq.jpg)
![YoVoice 截图 2](https://pbs.twimg.com/media/HSyjTloaMAA9Oa5.jpg)
