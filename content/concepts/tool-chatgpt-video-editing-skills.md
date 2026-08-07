---
type: Tool
title: "ChatGPT Video Editing Skills"
description: "繁体中文 AI Agent 视频剪辑技能包：一个 Skill 管环境（video-use / FFmpeg / ffprobe / 思源黑体 TW / ElevenLabs 凭据逐项查装），另一个 Skill 管剪辑流水线（逐字转写 → 内容整理 → 剪接策略 → 粗剪 → 字幕 → 预览 → 正式输出）。"
resource: "https://github.com/Jaycheng1103/chatgpt-video-editing-skills"
tags: [agent-skills, video, ffmpeg, transcription, subtitle, editorial, traditional-chinese]
timestamp: 2026-08-06T12:00:00Z
---

# ChatGPT Video Editing Skills

## 它是什么

Jaycheng1103 发布的开源繁体中文 AI Agent 技能包，把视频剪辑拆成两条 Skill 流水线，每条都假设 agent 能读写本机文件并执行终端命令：

- **环境检查 Skill**：把 video-use、FFmpeg、ffprobe、思源黑体 TW 字体、ElevenLabs 凭据逐个查、装、修。要动配置先列清单等你确认。
- **剪辑 Skill**：视频从逐字转写、内容整理、剪接策略一路做到粗剪、字幕、预览、正式输出。

## 为什么用它 / 适合什么场景

- 想用能跑命令的 agent 直接产出可发布视频，但又不想让它乱动你机器。
- 优先需要「先列清单等你点头」式确认，避免 agent 误装 / 误覆盖配置。
- 思源黑体 TW + ElevenLabs TTS 已经预设好，繁中配音 / 字幕工作流开箱即用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 环境 Skill | video-use / FFmpeg / ffprobe / 字体 / ElevenLabs 凭据逐项查装；改配置先列清单确认 |
| 转写 → 编辑流水线 | 逐字转写 → 内容整理 → 剪接策略 → 粗剪 → 字幕 → 预览 → 正式输出 |
| 多媒体依赖预审 | 把视频编辑常用二进制 / 字体 / API key 一并收纳到一个 Skill，避免 agent 缺工具翻车 |

## 相关概念
- [video-skills-toolkit](./tool-video-skills-toolkit.md) — 把短视频生产沉淀成 6 个可复用 agent skills 的同类工作流
- [Timecode Agent](./tool-timecode-agent.md) — 长视频带时间戳证据账本，转录优先 + 按需视觉验证
- [Stickman Video Director](./tool-stickman-video-director.md) — 文案 → 一分钟火柴人视频的轻量方案