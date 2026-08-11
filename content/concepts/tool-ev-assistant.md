---
type: "Tool"
title: "E.V. Assistant（Ouru77/ev-assistant）"
description: "用 Python + Electron 搭的 Windows 语音助手,造型与设定取自《蜘蛛侠》新片里 Peter Parker 自制的 AI;对话链路全在本机:faster-whisper 听写、Ollama 跑本地模型(默认 gemma2:9b)、回答用浏览器自带语音或 ElevenLabs 念出,默认配置零 key、零云端。"
resource: "https://github.com/Ouru77/ev-assistant"
tags: "[voice-assistant, faster-whisper, ollama, elevenlabs, windows, electron, local-ai]"
timestamp: "2026-08-11T16:00:00Z"
---

# E.V. Assistant

[E.V. Assistant](https://github.com/Ouru77/ev-assistant) 是作者用 Python + Electron 搭的 Windows 语音助手,造型与设定取自《蜘蛛侠》新片里 Peter Parker 自制的 AI "E.V."——全程对话链路跑在本机。

项目链接：<https://github.com/Ouru77/ev-assistant>

## 它是什么

一站式**本机语音对话助手**:听写(STT)→ 本地 LLM 推理 → 语音合成(TTS)三段式全部本地化,默认零 key、零云端。

## 为什么用它 / 适合什么场景

- **完全离线**:对话链路不联网,适合隐私敏感场景。
- **零配置起步**:默认配置即可用,不必先注册各家云服务。
- **可换 TTS**:支持浏览器自带语音或 ElevenLabs。

## 关键能力

| 能力 | 说明 |
|------|------|
| faster-whisper 听写 | 本地 STT,无需云 API |
| Ollama 本地模型 | 默认 gemma2:9b,可换任何 Ollama 支持的模型 |
| 多 TTS 选项 | 浏览器自带语音 / ElevenLabs 可选 |
| Python + Electron | 桌面 GUI + Python 后端,易扩展 |
| Windows 优先 | 在 Windows 上提供完整桌面体验 |
| 零 key / 零云端 | 默认配置即可上手 |

## 媒体

![](https://pbs.twimg.com/media/HPV6mh5bYAEv9iV.jpg)

## 参考链接

- [项目仓库](https://github.com/Ouru77/ev-assistant)

## 相关概念

- [Gemma Translator](./tool-gemma-translator.md) — Google 开源的本地离线实时语音翻译器,与本项目同属"本地语音 + Gemma 模型"路线
- [Ollama](./tool-ollama.md) — 本项目默认的本地 LLM 运行时