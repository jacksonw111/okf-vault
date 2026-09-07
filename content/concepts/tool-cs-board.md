---
type: Tool
title: "cs-board"
description: "本地运行的 AI 视频工作台，给一段参考音频 + 中文文案就能产出 MP4 口播视频：克隆音色 / 拆镜 / 画插画 / 手写笔迹 / 配字幕一条龙，12 套画风可选。"
resource: "https://github.com/ChenShuo2004/cs-board"
tags: "[ai-video, white-board, voice-clone, tts, video-generation]"
timestamp: "2026-09-07T13:11:00Z"
---

# cs-board

## 它是什么
本地运行的 AI 视频工作台（白板动画生成器）。输入参考音频 + 中文文案，选模板就自动做完整条流水线：克隆音色 → 拆镜 → 画插画 → 手写笔迹 → 配字幕 → 合成 MP4。12 套画风从极简白板到国风、赛博霓虹都能选，还可上传风格图锁定整片画风。动态信息图模式按真实旁白时间逐条展开。

## 流水线
1. 音频输入 → 音色克隆
2. 文案输入 → 按句拆分镜
3. 每镜生成对应插画
4. 手写笔迹动画
5. 自动字幕 + 时间轴对齐
6. 合成 MP4 输出

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地运行 | 无云端依赖 |
| 12 套画风 | 极简白板 / 国风 / 赛博霓虹等 |
| 自定义画风 | 上传风格图锁定整体风格 |
| 动态信息图模式 | 按旁白节奏逐条展开 |
| 一条龙合成 | 音 / 镜 / 画 / 字幕自动组合 |

## 适用场景
- 短视频自媒体口播视频快速生产
- 知识科普类白板动画
- 配音文案 → 视频批量出片

## 参考
- 项目链接：<https://github.com/ChenShuo2004/cs-board>

## 相关概念
- [AI Media Assistant](tool-ai-media-assistant.md) — 中文创作者本地短视频生成 Web 工具
- [OpenMontage](tool-openmontage.md) — 自然语言到成片的开源 agentic 视频制作系统
- [OmniVoice-Studio](tool-omnivoice-studio.md) — 3 秒样本开源语音克隆