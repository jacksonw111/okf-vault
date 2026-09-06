---
type: Tool
title: "ffmpeg-skill"
description: "教 AI Agent 用本地 FFmpeg 干活的 Skill：一份 SKILL.md 工作流 + 二十多个 Python 小脚本，剪切拼接、加字幕、去静音、多机位对齐、调响度、HDR 转 SDR 全流程覆盖，不联网、不用 API Key。"
resource: "https://github.com/kajisho5/ffmpeg-skill"
tags: [agent-skill, ffmpeg, video-editing, local, python]
timestamp: "2026-09-06T00:00:00Z"
---

# ffmpeg-skill

## 它是什么

[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) 是给 AI Agent 用的 **FFmpeg Skill**：核心是**一份 SKILL.md 工作流 + 二十多个 Python 小脚本**，全部调用本机安装的 ffmpeg，不联网、不消耗 API Key。

定位：

- **给 AI 看的视频后期工具集**：每个脚本都是「先试跑看命令、输出结构化结果」的可观察步骤。
- **覆盖网常见后期活**：剪切拼接、加字幕、去静音、多机位对齐、调响度、HDR → SDR、各平台导出预设。

## 为什么用它 / 适合什么场景

- 想让 AI Agent 帮你做视频剪辑，但不想让它去申请云端视频 API。
- 团队已经在用 FFmpeg，希望 Agent 在同一套命令行生态里协作。
- 每个脚本都能独立 dry-run，便于审计 Agent 的中间步骤。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工作流文档 | SKILL.md 描述完整流程，Agent 阅读即用 |
| Python 脚本 | 20+ 小脚本，每个对应一类后期操作 |
| 本地执行 | 完全依赖本机 FFmpeg，零网络、零 API Key |
| 试跑支持 | 每个脚本支持先打印命令再执行，便于审计 |
| 多平台导出 | 各平台尺寸 / 码率预设开箱可用 |
| HDR 处理 | 内置 HDR → SDR 转码 |

## 相关概念

- [FFmpegFreeUI](./tool-ffmpeg-free-ui.md) — 人类用的 FFmpeg 图形外壳；ffmpeg-skill 是给 AI 用的同类能力
- [kitter](./tool-kitter.md) — 用 kitter 管理 ffmpeg-skill 这类 Skill 的链接复用
- [Agent Skills（代理技能包）](./term-agent-skills.md) — ffmpeg-skill 是典型的「Skill 包」实例

## 项目链接

- 项目主页：<https://github.com/kajisho5/ffmpeg-skill>
