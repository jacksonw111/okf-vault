---
type: "Tool"
title: "SkipTheVoice"
description: "oliverjessner 写的 WhatsApp 语音转写工具：Web UI + CLI 双形态，只挑按住说话录下的语音导入，文本 / 图片 / 视频 / 表情回复一概不碰，转写靠自托管 OpenAI Whisper，Web 端 Next.js / CLI 端 Commander，共用 TypeScript 业务代码。"
resource: "https://github.com/oliverjessner/SkipTheVoice"
tags: [whatsapp, whisper, transcription, self-hosted, nextjs, typescript]
timestamp: "2026-08-09T19:35:00Z"
---

# SkipTheVoice

## 它是什么

[SkipTheVoice](https://github.com/oliverjessner/SkipTheVoice) 是给 WhatsApp 语音消息做的转写工具：分 **Web 界面**和**命令行**两种用法。它**只挑「按住说话」录下的语音导入**，文本 / 图片 / 视频 / 表情回复一概不碰——避免误转写其他媒体。转写靠**自托管的 OpenAI Whisper**，数据不出本机。Web 端 Next.js、CLI 端 Commander，**两边共用同一套 TypeScript 业务代码**。

## 为什么用它 / 适合什么场景

- WhatsApp 工作群语音消息轰炸，想批量转成文字搜索 / 归档。
- 不想用第三方云转写服务（隐私 / 成本 / 准确性）。
- 同时需要 Web 界面（一次性批量）与 CLI 自动化（脚本调用）。
- 学习 Next.js + Commander 共享 TS 业务代码的工程实践。

## 关键能力

| 能力 | 说明 |
|------|------|
| 只处理语音 | 文本 / 图片 / 视频 / 表情回复自动跳过 |
| 自托管 Whisper | 转写在本地或私有 Whisper 服务完成 |
| Web UI | Next.js 一次性批量导入与转写 |
| CLI | Commander 脚本化 / 自动化 |
| 共享代码 | TS 业务逻辑在 Web / CLI 两端复用 |
| 可部署为服务 | Docker / 任意 Node 环境运行 |

## 媒体

![](https://pbs.twimg.com/media/HPMUvWjaQAAY-CU.jpg)

## 相关概念

（暂无直接相关概念）