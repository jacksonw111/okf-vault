---
type: "Tool"
title: "explainroo（本地解说视频流水线）"
description: "本地跑的解说视频流水线：Agent 交两个文件就完事——script.md 是念出来的话，scenes.js 用 JavaScript 画图，画面能挂在旁白的某一个词上蹦出来；TTS 交给开源模型 Kokoro（28 种音色），不注册不给 key。"
resource: "https://github.com/vincentsch/explainroo"
tags: "[video, tts, kokoro, agent-pipeline, javascript, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# explainroo

## 它是什么

[explainroo](https://github.com/vincentsch/explainroo) 是 **vincentsch** 出品的**本地解说视频流水线**——让 Agent 一键从文字跑到 MP4，不必把旁白丢给云端 TTS、把分镜丢给剪辑软件。

## 流水线

```
script.md（念出来的话）
   ↓
scenes.js（JS 画图）
   ↓ 画面可挂在旁白某词上蹦出
Kokoro TTS（28 种音色，本地）
   ↓
MP4
```

## 为什么用它 / 适合什么场景

- **Agent 时代「自动出片」**：Agent 写完脚本，explainroo 一键渲染。
- **本地 + 零注册**：念稿交给 Kokoro，不上传、不注册、不给 key。
- **画面对齐旁白**：JS 画的元素能挂在某一个词上出现，节奏更精确。
- **典型场景**：教程视频、产品解说、科普短视频。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | script.md + scenes.js |
| TTS | Kokoro（开源本地，28 音色） |
| 画面 | JavaScript 程序化绘制 |
| 对齐 | 画面挂在旁白词上 |
| 输出 | MP4 |
| 部署 | 本地 |

## 参考链接

- 项目链接：<https://github.com/vincentsch/explainroo>

## 相关概念

- [LiveCanvas](./tool-livecanvas.md) — 同类「Agent 一条龙产视频」方向
- [Knowclip](./tool-knowclip.md) — 同类「本地视频处理」工具
