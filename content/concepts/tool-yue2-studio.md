---
type: Tool
title: "YuE2-Studio（YuE2 歌曲生成 Windows 桌面应用）"
description: "把 YuE2 开源歌曲生成模型包成 Windows 桌面应用：用户先给风格与歌词，工具用 ABC 记谱法把旋律与和弦写出来，再渲染成带人声的完整歌曲；改音符 / 速度 / 调都能重新渲染，乐谱与音频同步给出。"
resource: "https://github.com/timoncool/YuE2-Studio"
tags: [music-generation, abc-notation, desktop, windows, gpu, ai-music]
timestamp: 2026-09-30T13:24:01Z
---

# YuE2-Studio

## 它是什么

**YuE2-Studio** 是 [timoncool](https://github.com/timoncool) 维护的 Windows 桌面应用，把 M-A-P 开源的 **YuE2** 歌曲生成模型包成可在本地显卡上跑的图形工具。

它的核心路线是**先写谱再唱**：

1. 用户输入想要的风格与歌词。
2. 工具先用 **ABC 记谱法** 把旋律与和弦写出来。
3. YuE2 模型再把这份"乐谱"渲染成带人声的完整歌曲。
4. 同时输出乐谱与音频；改音符 / 速度 / 调都能重渲染。

## 为什么用它 / 适合什么场景

- 想用 AI 出歌但希望**可以编辑旋律 / 和弦**，而不是只能听生成结果。
- 偏好本地推理（在自己的显卡上跑），避免云端 API 配额与延迟。
- 想要一份**乐谱 + 音频**双产出，方便二次混音或学习用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型 | YuE2（M-A-P 开源） |
| 形态 | Windows 桌面应用 |
| 推理位置 | 本地显卡 |
| 输入 | 风格 + 歌词 |
| 中间表达 | ABC 记谱（旋律 + 和弦） |
| 输出 | 乐谱 + 带人声的完整歌曲 |
| 可编辑性 | 改音符 / 速度 / 调均可重渲染 |

## 参考链接

- 仓库：<https://github.com/timoncool/YuE2-Studio>

## 媒体

- ![](https://pbs.twimg.com/media/HTXOA87aMAA3ytg.jpg)

## 相关概念

- [ABC 记谱法](./term-jev.md) — YuE2-Studio 的中间表达是 ABC；这是音乐圈常见的纯文本乐谱格式