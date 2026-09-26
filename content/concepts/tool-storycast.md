---
type: "Tool"
title: "Storycast（纯前端 AI 短片生成流水线）"
description: "ilkerzg 开源的 Vite 纯前端项目：用你自己的 fal key 把整套视频生成流水线串起来——挑角色 + 话题 → 导演模型写脚本 → 关键帧 / 配音 / 动画镜头 / 剪辑 / 配乐 / 片尾手写字卡 / 逐词字幕，全流程自动跑完。"
resource: "https://github.com/ilkerzg/storycast"
tags: "[storycast, video-gen, fal, vite, frontend, storyboard, ai-video, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# Storycast（纯前端 AI 短片生成流水线）

## 它是什么

[Storycast](https://github.com/ilkerzg/storycast) 是 ilkerzg 开源的 **Vite 纯前端 AI 短片生成流水线**——用你自己的 **fal key** 把「**一个话题 → 一条完整短片**」的全流程串起来，**纯前端**跑。

## 流水线步骤

1. 挑一个**角色** + 给一个**话题**
2. 导演模型**写脚本**
3. 逐段做**关键帧**、**配音**、**动画镜头**
4. **剪辑**、**配乐**
5. **片尾手写字卡** + **逐词字幕**

## 为什么用它 / 适合什么场景

- 想做「**话题 → 短视频**」自动化但**不想搭后端**——纯前端 + fal 一把梭。
- 习惯用 **fal.ai** 模型生态（图像 / 视频 / 配音）。
- 想给「**每日一条科普短片 / 解说号**」做可复用的流水线。
- 想在 Storycast 基础上二次开发——Vite 纯前端项目结构好懂。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Vite 纯前端 Web 应用 |
| API Key | 用户自己的 fal key |
| 角色库 | 自带角色可选 |
| 流水线 | 脚本 → 关键帧 → 配音 → 动画 → 剪辑 → 配乐 → 字卡 → 字幕 |
| 输出 | 一条完整短片 |

## 媒体

- ![](https://pbs.twimg.com/media/HTHoD6dbUAA1DRH.jpg)

## 相关概念

- [html-explainer](./tool-html-explainer.md) — 跨 Agent Skill，把「话题 → 调研 → 解说 → HTML → MP4」串成另一条流水线
- [open-slide](./tool-openslide.md) — 同为「为 Agent 而生」的媒体生成框架（但输出 PPTX）