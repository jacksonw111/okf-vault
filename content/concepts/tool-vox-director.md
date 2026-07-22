---
type: Tool
title: "vox-director"
description: "Alisa0808/vox-director，你扔一句话主题就能全自动出片的端到端视频生成器：写叙事节奏 → 风格挑选 → 关键帧拼贴海报 → 动效化 → 旁白音乐 → ffmpeg 合成 mp4。"
resource: "https://github.com/Alisa0808/vox-director"
tags: "[video-generation, ai-agent, storyboard, ffmpeg, creative]"
timestamp: "2026-07-22T10:24:00Z"
---

# vox-director

## 它是什么

[`vox-director`](https://github.com/Alisa0808/vox-director) 是一个**端到端自动化视频生成器**：从一句话主题开始，**自动完成**从脚本到成片的整个流程。

## 6 步流程

1. **写叙事节奏** — 把主题拆成节奏分明的段；
2. **出几种风格让你挑** — 视觉风格候选清单；
3. **生成每段的关键帧拼贴海报** — 每段出一张拼贴海报作为「定调」图；
4. **让海报动起来** — 关键帧 → 动效（两条动效路线可选）；
5. **配上旁白和音乐** — TTS + 背景音乐；
6. **ffmpeg 合成 mp4** — 最终输出。

## 核心设计原则

> **拼贴感必须在出图阶段做好，动效只是锦上添花。**

- 视觉风格「定调」是出图阶段就锁定的，而不是动效阶段补救；
- 动效有两条路线可选（轻动效 / 重动效）；
- 流程是「分支可选 + 强制流水线」，避免「全靠 AI 自由发挥」导致风格漂移。

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [Montara](tool-montara.md) | AI 原生视频制作 OS | 偏 Timeline IR + 多模块协作 |
| [Cinema Manager](tool-cinema-manager.md) | 找片 Skill | 不是创作 |
| [video-shotcraft](tool-video-shotcraft.md) | Claude Code 视频 Skill | 镜头卡 / 动效样式更偏导演视角 |
| [autoshorts](tool-autoshorts.md) | 短视频自动生成 | 偏竖屏 / 社媒 |
| vox-director | 端到端 6 步流水线 | 拼贴海报 + 风格先定，生成确定性强 |

## 媒体

![](https://pbs.twimg.com/media/HNwFdvebgAAxltg.jpg)

## 原始链接

- [项目仓库](https://github.com/Alisa0808/vox-director)

## 相关概念

- [Montara](tool-montara.md) — AI 视频操作系统，本工具更轻量、流水线更刚性
- [video-shotcraft](tool-video-shotcraft.md) — 给 AI agent 用的镜头 / 动效库，本工具是「全流程自动化」取向
- [Cinema Manager](tool-cinema-manager.md) — 找片 / 整理媒体库，不是创作工具