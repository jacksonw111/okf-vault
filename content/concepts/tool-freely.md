---
type: Tool
title: "Freely"
description: "本地运行的实时对话助手，定位为月费 150 美元的 Cluely 的免费替代：监听会议 / 面试 / 通话，本地 Whisper 转写并把建议悄悄浮窗提示。"
resource: "https://github.com/KMalek101/Freely"
tags: [tool, meeting-assistant, whisper, privacy, realtime, ai-assistant]
timestamp: 2026-07-09T23:45:00.000Z
---

# Freely

## 它是什么
本地运行的实时对话助手，常驻终端与桌面悬浮窗，监听麦克风 → 本地 Whisper 转写对方说的话 → 把转写后的文本和截图发给大模型 → 在屏幕上悄悄浮窗提示你该怎么接话。

## 为什么用它 / 适合什么场景
- 想要 Cluely 类"隐形会议提示"体验但不愿付 150 美元/月。
- 隐私敏感：音频采集、人声检测、语音转文字全程本地，只有文本 / 截图才走云端。
- 已经有 Gemini / Claude / OpenAI 的 API key，希望把成本压到接近零。

## 关键能力
| 能力 | 说明 |
|------|------|
| 实时监听 | 麦克风捕获会议 / 面试 / 通话语音 |
| 本地 Whisper | 转写与语音活动检测全部本地完成 |
| 多家 LLM | 转写结果可送 Gemini / Claude / OpenAI |
| 浮窗建议 | 在屏幕角落实时显示建议回复 |
| 隐私优先 | 仅转写文本 + 截图上云，原始音频不出本机 |

## 媒体
![Freely 预览](https://pbs.twimg.com/media/HMr7IeobYAAbw1i.jpg)

## 相关概念
- [MCP](note-front-end-resources.md) — Freely 走"自己写 API key + 本地转发"路线，是 MCP 之外更轻的 LLM 调用路径