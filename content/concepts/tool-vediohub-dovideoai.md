---
type: Tool
title: "VedioHub / DoVideoAI（长视频分析 Agent 引擎）"
description: "dirge2024 开源：把小时级长视频拆成带时间戳的音画片段交给 Agent 处理，结论都挂上可回放的证据，同一视频还能反复追问。"
resource: "https://github.com/dirge2024/VedioHub"
tags: [video, ai, agent, rag, long-video, timestamps]
timestamp: 2026-08-21T10:23:00Z
---

# VedioHub / DoVideoAI（长视频分析 Agent 引擎）

## 它是什么
VedioHub / DoVideoAI 解决一个具体痛点：「几小时长的视频内容分散，无法直接丢给 LLM 分析」。它先把音画按场景 / 说话轮次 / 镜头变化拆成带时间戳的片段，每一段都能被 agent 单独取用；分析结论不是「一段总结文本」，而是「每条结论都挂上可点击跳转回原视频对应时间点的证据」；同一份视频可以反复追问，agent 会重新查表再回答。

## 为什么用它 / 适合什么场景
- 课程 / 培训 / 会议 / 直播录像几小时，想让 agent 帮你做内容复盘 / 章节提取 / QA。
- 法务 / 媒体 / 行业研究需要逐条可追溯的「证据链」，结论必须能点回原片断。
- 想做「可对话视频」体验：边看边问，agent 跨问题保留上下文。

## 关键能力
| 能力 | 说明 |
|------|------|
| 音画分片 | 按场景 / 镜头 / 说话轮次切出时间戳片段 |
| 时间戳证据 | 每条结论挂可点击跳转回原视频位置 |
| 反复追问 | 同一视频多轮 Q&A，agent 持续保留上下文 |
| Agent 友好 | 片段可直接喂给 LLM 而非整段送进上下文 |
| 长视频可处理 | 几小时内容拆成可管理的小单元 |

## 一句话总结
**「把几小时视频切成可回放证据链」——让 agent 看视频并给出每条都能点回去的结论。**

## 原始链接
- [dirge2024/VedioHub](https://github.com/dirge2024/VedioHub) — 原始仓库

## 媒体
- ![VedioHub 界面](https://pbs.twimg.com/media/HQNlLsTaEAAbGsM.jpg)

## 相关概念
- [claude-real-video](./concepts/tool-claude-real-video.md) — 同样解决「AI 真正看懂视频」，思路是智能抽帧
- [AI Media Assistant](./concepts/tool-ai-media-assistant.md) — 中文创作者短视频生成