---
type: "Note"
title: "AI 语音呼吸 / 亲吻 / 水声补全"
description: "sanqianzilanyue 实操踩坑：用 ElevenLabs + ffmpeg + whisper 在 Mac mini 上给 AI 语音补上呼吸 / 亲吻 / 水声，并解释为什么这些响动不该交给 TTS 去念、给出具体参数。"
resource: "https://github.com/sanqianzilanyue/ai-voice-breath-kiss-water"
tags: "[voice, elevenlabs, ffmpeg, whisper, audio-post, tts, sound-effect]"
timestamp: "2026-10-07T03:50:00Z"
---

# AI 语音呼吸 / 亲吻 / 水声补全

## 它是什么

[ai-voice-breath-kiss-water](https://github.com/sanqianzilanyue/ai-voice-breath-kiss-water) 是 **sanqianzilanyue** 写的实操踩坑记录——用 **ElevenLabs**（捏音色、念台词）、**ffmpeg**（拼接叠轨）和 **whisper**（当验声探针）在 Mac mini 上给 AI 语音配上 **呼吸 / 亲吻 / 水声**。

仓库本身只有 **一个 README** 和 **一个排好版的 index.html 网页**，不写工程代码——重点是**判断依据与具体参数**。

## 核心观点

### 1. 这些响动不该交给 TTS 去念

- **TTS 的目标**：把「字」念成「话」
- **呼吸 / 亲吻 / 水声** 本质是 **生理 / 物理音效**，不是文字内容
- 让 TTS 念会失真（要么机械、要么完全听不到）

### 2. 解法：单独录 + 后期叠轨

- **ElevenLabs**：只管「字」的音色 + 台词
- **ffmpeg**：把呼吸声 / 亲吻声 / 水声作为单独音轨叠上去
- **whisper**：合成后用 whisper 反过来验证「字」是否清晰（验声探针）

### 3. 关键参数

仓库给出了具体的 ffmpeg 叠轨参数 / 呼吸声采集建议 / ElevenLabs 的 SSML 控制点。

## 为什么值得参考

- **打破「TTS = 一切声音」的迷思**：好的 AI 语音是「**TTS + 后期音效**」组合
- **whisper 验声**：用同一类模型反验合成质量的方法值得借鉴
- **零代码可读**：仓库本身是文档，对工程师 / 内容创作者都好用

## 参考链接

- 项目仓库：<https://github.com/sanqianzilanyue/ai-voice-breath-kiss-water>

## 媒体

- ![](https://pbs.twimg.com/media/HT6pORFa0AE0nGS.jpg)

## 相关概念

无相关概念需要链入。
