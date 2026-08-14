---
type: "Tool"
title: "InsightForge"
description: "gx-ui 开源的本地 AI 视频成片引擎：把一句话 / 完整剧本 / 长篇小说拆给一串专业 Agent（叙事 / 角色 / 分镜 / 镜头 / 关键帧 / 视频片段），自动产出可控制的 AI 视频成片。"
resource: "https://github.com/gx-ui/Insightforge"
tags: ["ai-video", "agent", "storytelling", "storyboard", "open-source", "react"]
timestamp: "2026-08-14T19:50:00Z"
---

# InsightForge

## 它是什么
InsightForge 是一个本地跑的「多 Agent 协作」AI 视频成片引擎。它把视频创作流水线拆成：叙事规划 → 角色 → 分镜 → 镜头 → 关键帧 → 视频片段 → 终片，每一步由专门的 Agent 负责。可吃一句话创意（Idea2Video）、完整剧本（Script2Video）或长篇小说（Novel2Video）。Web 工作区用 React 19，CLI 与 Web 共用同一套运行时。

## 为什么用它 / 适合什么场景
- 想把「AI 自动生成视频」流程化、可控化，而不是单一 prompt 直接出片。
- 适合「短视频自动化生产」、「小说可视化改编」、「剧本 → 镜头脚本」等场景。
- 本地优先 + 多 Agent 协作让每一步都可调整，符合内容生产「分步审核」的工业流程。

## 关键能力
| 能力 | 说明 |
|------|------|
| 三类输入 | 一句话 / 完整剧本 / 长篇小说 |
| 流水线 | 叙事规划 → 角色 → 分镜 → 镜头 → 关键帧 → 视频片段 → 终片 |
| 多 Agent | 每一步有专门 Agent |
| 形态 | Web（React 19）+ 交互式 CLI |
| 运行模式 | 本地优先 |

## 媒体

工作区截图：![工作区截图](https://pbs.twimg.com/media/HPkjqkZa8AAbknf.jpg)

## 相关概念
- [Stickman Video Director](./tool-stickman-video-director.md) — 文案 / 笔记 → 一分钟火柴人视频，与 InsightForge 同属「结构化 AI 视频生产」思路但更轻量
- [Video Skills Toolkit](./tool-video-skills-toolkit.md) — 把短视频生产沉淀成 6 个可复用 agent skills，与 InsightForge 的多 Agent 设计思路一致
- [Stickman-Video-Director](./tool-stickman-video-director.md) — 同上
