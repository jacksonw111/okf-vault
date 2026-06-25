---
type: Tool
title: "autoshorts（长视频转竖屏短视频）"
description: "Tauri 2 + React + Rust + SQLite 桌面应用，自动把长视频/音频转竖屏短视频（9:16），AI 评估片段的病毒式传播潜力，可选 DeepSeek / Claude / 本地 Ollama 模型。"
resource: "https://github.com/JayWebtech/autoshorts"
tags: [desktop, tauri, video, shorts, ai-editing, local-llm]
timestamp: "2026-06-25T13:31:00Z"
---

# autoshorts（长视频转竖屏短视频）

## 它是什么

一个**Tauri 2 + React + Rust + SQLite** 桌面应用，专门把长视频 / 音频转成竖屏短视频。

## 流程

1. **导入素材**——视频或音频。
2. **提取音频**。
3. **Deepgram 转录**——把音频变文字 + 时间戳。
4. **AI 分析片段**——让模型挑出「**最有爆款潜力**」的部分（不是平均切，而是挑高潮）。
5. **ffmpeg 自动裁 9:16**——把挑出来的片段转竖屏。
6. **导出**——直接得到可发抖音 / TikTok / YouTube Shorts 的短视频。

## AI 引擎可选

| 模型 | 定位 |
|------|------|
| DeepSeek | 便宜又好用 |
| Claude | 写文案厉害 |
| 本地 Ollama | 完全离线 |

首次开机会有向导帮你配置 API 密钥或本地模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | macOS / Windows / Linux |
| 本地数据 | SQLite 存所有元数据与转录 |
| AI 模型可换 | DeepSeek / Claude / Ollama |
| 竖屏裁切 | ffmpeg 自动 9:16 |
| 爆款评估 | AI 选段而非平均切 |

## 媒体

![](https://pbs.twimg.com/media/HLoR65-akAALIEs.jpg)

## 相关概念

- [Local AI Workbench](./tool-local-ai-workbench.md) — 同为「本地优先 AI 桌面」形态，autoshorts 是「视频方向的具体落地」
- [AQBot](./tool-aqbot.md) — Tauri 2 桌面 AI 三件套；autoshorts 是同架构的视频向应用
- [BiliMusic](./tool-bili-music-electron.md) — Electron 把 B 站音乐包装；autoshorts 是 Tauri 把长视频包装为短视频
- [Targie](./tool-targie-similar-finder.md) — 桌面视频/图片处理工具，autoshorts 是其「处理方向」上的兄弟