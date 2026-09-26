---
type: "Tool"
title: "open-slide（为 Agent 设计的幻灯片框架）"
description: "1weiho 出品的「为 Agent 而生」的幻灯片框架：让 Agent 自己生成整套 deck，用户再人工微调——2.0 新增可视化编辑器、可二次编辑的 PPTX 导出和重做的 UI。"
resource: "https://github.com/1weiho/open-slide"
tags: "[slides, pptx, agent, framework, presentation, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# open-slide（为 Agent 设计的幻灯片框架）

## 它是什么

[open-slide](https://github.com/1weiho/open-slide) 是一个**为 Agent 而生**的开源幻灯片框架——核心用法是「**让 Agent 生成 deck → 用户做最后微调**」：

- 2.0 版本新增 **可视化编辑器**
- **可二次编辑的 PPTX 导出**（不是导出图片，是真 PowerPoint 文件）
- 重做的 UI

## 为什么用它 / 适合什么场景

- 想让 LLM / Agent **直接产出可演示的 deck**，但又不想放弃人工微调（AI 排版常丑）。
- 需要把 AI 生成的 slide **导回 PowerPoint** 给同事二次修改。
- 想在 Agent 工作流里搭一条「**生成 → 编辑 → 导出**」闭环，而不是「AI 一次性吐一堆 PNG」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 开源框架（JS/TS 项目） |
| 核心场景 | Agent 自动生成幻灯片 |
| 2.0 编辑器 | 可视化编辑器 |
| 导出格式 | 可二次编辑的 PPTX（不是 PNG/PDF） |
| UI | 2.0 重做 |

## 媒体

视频演示：
- <https://video.twimg.com/amplify_video/2103870129566310400/vid/avc1/3840x2160/4w-Jn8FXZLnraXs5.mp4>

## 相关概念

- [html-explainer](./tool-html-explainer.md) — 跨 Agent Skill，把调研 / 解说词 / 字幕 / HTML / MP4 串成流水线（讲解视频一类）
- [Storycast](./tool-storycast.md) — 纯前端视频生成流水线（角色 + 话题 → 完整短片）