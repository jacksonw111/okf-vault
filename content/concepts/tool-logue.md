---
type: "Tool"
title: "Logue（bitwize-ai/Logue）"
description: "Bitwize 出品的 macOS 原生 AI 会议笔记与写作工具：实时录音转文字、说话人分离、会议纪要和写作编辑器集成在一个本地 App 里；AI 推理用 MLX 框架跑在 Apple Silicon 上，默认不联网，本地数据用 AES-256-GCM 加密。"
resource: "https://github.com/bitwize-ai/Logue"
tags: [macos, apple-silicon, mlx, meeting-notes, transcription, local-ai, privacy]
timestamp: "2026-07-27T20:30:00Z"
---

# Logue（bitwize-ai/Logue）

## 它是什么

`bitwize-ai/Logue` 是 Bitwize 出品的 **macOS 原生 AI 会议笔记 + 写作工具**：把**实时录音转写**、**说话人分离**、**会议纪要**、**写作编辑器**集成在同一个本地 App 中。AI 推理使用 **MLX** 框架跑在 **Apple Silicon** 上，默认**不联网**；本地数据用 **AES-256-GCM** 加密存储。

## 为什么用它 / 适合什么场景

- 不想让**会议录音 / 笔记**传到云端，需要本地 AI 跑通转写 + 摘要；
- 已经在用 Mac（Apple Silicon 必需），希望开箱即用、无需服务端；
- 想要**录音 → 转写 → 说话人区分 → 会议纪要 → 在 App 内继续写作**一条龙；
- 对**数据静止加密**（AES-256-GCM）有要求的内部团队 / 律所 / 咨询场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时录音转写 | 边录边转文字 |
| 说话人分离 | 多说话人日志式区分 |
| 会议纪要 | 自动生成结构化摘要 |
| 写作编辑器 | App 内继续二次编辑 |
| 本地 MLX 推理 | Apple Silicon 加速，无需 GPU 服务器 |
| 离线优先 | 默认不联网 |
| AES-256-GCM 加密 | 本地落盘数据加密 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOKB1Q3bEAEE0iD.jpg)

- 项目链接：<https://github.com/bitwize-ai/Logue>

## 相关概念

- [Sonor](tool-sonor.md) — 同样是「数据不出设备」的 macOS 本地语音转文字（Sonor 偏纯转录，Logue 偏会议纪要 + 编辑）
