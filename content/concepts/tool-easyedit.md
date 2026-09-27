---
type: "Tool"
title: "easyedit（电影独白自动卡点混剪工具）"
description: "blixvip 出品的纯本地命令行 + Web 工具：输入电影名 → 自动挑出该电影最著名的独白 → faster-whisper 出逐词时间轴 → LLM 截取 9–24 秒连续段落并标重音词 → 输出社交平台常见的「字幕演讲 + 卡点混剪」视频。"
resource: "https://github.com/blixvip/easyedit"
tags: "[video-editing, ffmpeg, faster-whisper, llm, short-video, local]"
timestamp: "2026-09-27T21:55:00Z"
---

# easyedit（电影独白自动卡点混剪工具）

## 它是什么

[easyedit](https://github.com/blixvip/easyedit) 是 blixvip 出品的**纯本地命令行 + Web 工具**：你给它一个电影名，它会：

1. **挑出这部电影最有名的那段独白**
2. 用 **faster-whisper** 打出**逐词时间轴**
3. 让 **LLM** 截取 **9 到 24 秒的连续段落**、标出**重音词**
4. 产出社交平台上常见的**「字幕演讲 + 卡点混剪」视频**

## 为什么用它 / 适合什么场景

- 想批量产出「**金句卡点混剪**」类短视频（YouTube Shorts / TikTok / 抖音）。
- **不联网**：纯本地（whisper + LLM + ffmpeg），敏感素材不外传。
- 想要**流水线自动化**：电影名 → 选段 → 字幕 → 卡点 → 成片一气呵成。
- 想用 LLM 选高光，而不只是机械切时间段。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 命令行 + Web |
| 输入 | 电影名 |
| 输出 | 卡点字幕短视频 |
| ASR | faster-whisper 逐词时间轴 |
| 选段 | LLM 选 9–24 秒高光 + 标重音词 |
| 隐私 | 全本地，不上传源视频 |
| 依赖 | ffmpeg / whisper / LLM |

## 媒体

- ![](https://pbs.twimg.com/media/HTH5_NQacAASYgv.png)

## 相关概念

- [autoshorts](./tool-autoshirts.md) — Tauri 2 长视频 / 音频转竖屏短视频 + AI 选爆款段（同领域但定位不同）
- [AI Media Assistant](./tool-ai-media-assistant.md) — 中文创作者本地短视频生成 Web 工具