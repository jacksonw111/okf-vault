---
type: "Tool"
title: "Tern（B0yko/tern，Apple Silicon 媒体本地搜索）"
description: "在 Apple Silicon Mac 上给播客和视频档案做本地搜索：按说了什么、屏幕上出现什么字、画面里有什么三个通道一起查，命中结果能直接剪出来导出。"
resource: "https://github.com/B0yko/tern"
tags: "[media-search, podcast, apple-silicon, multimodal, transcription, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# Tern（B0yko/tern，Apple Silicon 媒体本地搜索）

## 它是什么

[Tern](https://github.com/B0yko/tern) 是 B0yko 开源的本地媒体搜索工具：在 Apple Silicon Mac 上给播客和视频档案做本地搜索——按三个通道同时查：说了什么（语音转写）、屏幕上出现什么字（OCR）、画面里有什么（视觉）。命中结果能直接剪出来导出。

## 关键能力

| 通道 | 说明 |
|------|------|
| 语音通道 | 转写说了什么（speech-to-text） |
| 文字通道 | 屏幕上出现的文字（OCR） |
| 视觉通道 | 画面里有什么（image / scene） |
| 三通道联合 | 三个通道一起查，结果更准 |
| 直接导出 | 命中片段可剪出来导出 |

## 适用场景

- 媒体档案本地搜索（不用上传云端）
- 播客 / 长视频检索
- 内容创作者找素材 / 切片段

## 媒体预览

![](https://pbs.twimg.com/media/HTWsZHybwAAqtnx.jpg)
![](https://pbs.twimg.com/media/HTWsdMPaEAA8-OE.jpg)

## 原始链接

- 项目主页：<https://github.com/B0yko/tern>

## 相关概念

- [KnowClip](./tool-knowclip.md) — 长视频自动切片，Tauri 2 + FastAPI + 本地 Paraformer-large
- [Tern SSH](./tool-ternssh.md) — 同名工具的不同项目，本条 Tern 是媒体搜索