---
type: "Tool"
title: "VoiceStudio（本地语音工作台）"
description: "debpalash 出品的本地语音工作台：语音克隆、语音设计、视频配音、听写——替代需要上传音频的云端 TTS 服务。"
resource: "https://github.com/debpalash/VoiceStudio"
tags: "[tts, voice-cloning, voice-design, voiceover, dictation, local]"
timestamp: "2026-09-27T21:55:00Z"
---

# VoiceStudio（本地语音工作台）

## 它是什么

[VoiceStudio](https://github.com/debpalash/VoiceStudio) 是 debpalash 出品的**本地语音工作台**：把**语音克隆 / 语音设计 / 视频配音 / 听写**四件事收进同一个桌面应用。

核心动机：**替代需要上传音频的云端 TTS 服务**——所有音频处理都在本机完成，不把素材传到云端。

## 为什么用它 / 适合什么场景

- 担心**音频素材外传**（版权 / 隐私 / 商业机密）。
- 想**一站式**搞定：克隆（学某人的声音）+ 设计（创造新声音）+ 配音（视频对白）+ 听写（语音转文字）。
- 想避免每个 TTS 任务都开一个云服务账号 / 付订阅费。
- 想**离线**用——出差 / 网络差环境也能用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地语音工作台 |
| 语音克隆 | 学目标说话人声音 |
| 语音设计 | 创造新声音（无需参考） |
| 视频配音 | 给视频生成对白音频 |
| 听写 | 语音转文字 |
| 隐私 | 全本地，音频不外传 |
| 替代 | 上传音频的云端 TTS 服务 |

## 媒体

- ![](https://pbs.twimg.com/media/HTMCRnTboAABT6l.jpg)

## 相关概念

- [yovoice](./tool-yovoice.md) — 本地 TTS 工具，audio.cpp 推理集成 IndexTTS / VoxCPM2 / OmniVoice / Qwen3-TTS 多模型（更偏引擎集成）
- [Purr](./tool-purr.md) — macOS Apple Silicon 菜单栏按住说话听写，全程本地推理
- [Verenu](./tool-verenu.md) — Tauri + Svelte 按住说话听写，本地优先 + 可换转写 API