---
type: Tool
title: "video-shotcraft"
description: "Vincentwei1021/video-shotcraft，给 Claude Code / Codex 用的 agent skill，装上之后让 AI 自己当动效导演——106 张镜头卡 + 162 种动效样式 + 161 条动态样片，覆盖产品宣传片常用拍法。"
resource: "https://github.com/Vincentwei1021/video-shotcraft"
tags: "[agent-skill, video, cinematography, storyboard, claude-code, codex]"
timestamp: "2026-07-22T15:10:00Z"
---

# video-shotcraft

## 它是什么

[`video-shotcraft`](https://github.com/Vincentwei1021/video-shotcraft) 是一个**给 Claude Code / Codex 用的 agent skill**，装上之后让 AI 自己当动效导演，自动分镜、动效、配乐，生成电影感的产品宣传视频。

## 三块素材库

| 素材 | 数量 | 用途 |
|------|------|------|
| 镜头卡 | 106 张 | 描述每种镜头语言（推 / 拉 / 摇 / 移 / 特写 / 全景等） |
| 动效样式 | 162 种 | 关键帧 / 转场 / 节奏 |
| 动态样片 | 161 条 | 参考视频片段 |

## 设计取向

- **导演视角**：不是「加滤镜」「加转场」，而是「AI 自己当导演做分镜」；
- **素材丰富**：上千条参考样片，让 AI 不靠凭空想象；
- **产品宣传片特化**：聚焦商业视频最常用的拍法。

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [vox-director](tool-vox-director.md) | 端到端视频生成器 | 6 步流水线，本工具是 Skill 形态 |
| [Montara](tool-montara.md) | AI 视频 OS | 偏 Timeline IR，本工具偏镜头语言 |
| [Cinema Manager](tool-cinema-manager.md) | 找片 Skill | 找片不是创作 |
| video-shotcraft | Skill（导演向） | 镜头 + 动效 + 样片三合一 |

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2079759410495373312/vid/avc1/1280x720/RXJZxur0scU8mvO0.mp4?tag=29>

## 原始链接

- [项目仓库](https://github.com/Vincentwei1021/video-shotcraft)

## 相关概念

- [vox-director](tool-vox-director.md) — 同为 AI 视频生成，但 vox-director 是端到端流水线，本工具是 Skill 形态的「导演向」参考
- [Montara](tool-montara.md) — AI 视频 OS，本工具是 Skill 形态，更轻量
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 的概念元定义