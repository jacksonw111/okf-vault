---
type: "Tool"
title: "KnowClip（长视频自动切片）"
description: "把几小时长视频自动切成适合短视频平台的精彩片段，导出走 ffmpeg -c copy 流复制（不解码不编码）。桌面端 Tauri 2 + React，后端 Python FastAPI；本地 Paraformer-large 跑字级时间戳语音识别 + 用户自己的 OpenAI 兼容 API 做高光分析。"
resource: "https://github.com/KnowClip-ai/knowclip"
tags: "[video, clip, tauri, fastapi, paraformer, ffmpeg, ai, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# KnowClip（长视频自动切片）

## 它是什么

[KnowClip](https://github.com/KnowClip-ai/knowclip) 是 KnowClip AI 智能剪辑的开源核心：把几小时长视频自动切成适合短视频平台的精彩片段。导出走 `ffmpeg -c copy` 流复制，不解码不编码，**速度极快且无画质损失**。

## 技术架构

| 层 | 技术 |
|----|------|
| 桌面端 | Tauri 2 + React |
| 后端 | Python FastAPI |
| 语音识别 | 本地 Paraformer-large 模型跑字级时间戳 |
| 高光分析 | 用户填的 OpenAI 兼容 API Key |
| 导出 | ffmpeg `-c copy` 流复制 |

## 工作流

1. 本地 Paraformer-large 对长视频跑字级时间戳语音识别
2. 用用户提供的 OpenAI 兼容 API 做高光分析
3. 产出带标题、描述、话题标签、评分的片段卡片
4. 用户勾选后批量导出走 ffmpeg `-c copy`

## 关键能力

| 能力 | 说明 |
|------|------|
| 字级时间戳 | 基于 Paraformer 的细粒度转写 |
| 高光评分 | LLM 给每个候选片段打分 + 起标题 |
| 流复制导出 | 不重新编码，几乎瞬时 |
| OpenAI 兼容 API | 用户自带 Key，可换第三方模型 |

## 适用场景

- 长视频（讲座 / 直播回放 / 会议录像）转短视频
- 想本地做 ASR + 云端做高光分析的混合工作流
- 想避免「重新编码耗时 + 画质损失」的导出

## 原始链接
- 项目主页：<https://github.com/KnowClip-ai/knowclip>

## 相关概念