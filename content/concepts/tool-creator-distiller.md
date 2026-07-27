---
type: "Tool"
title: "Creator Distiller（lihuanihaoma-design/creator-distiller）"
description: "把博主在多平台发布的内容（视频 / 推文等）抓取下来，转成带标点的文字稿（语音内容也可带时间戳），统一喂给本地大模型当知识库使用。"
resource: "https://github.com/lihuanihaoma-design/creator-distiller"
tags: [transcription, content-pipeline, knowledge-base, local-llm, scraping]
timestamp: "2026-07-27T20:30:00Z"
---

# Creator Distiller（lihuanihaoma-design/creator-distiller）

## 它是什么

`lihuanihaoma-design/creator-distiller` 是一个**创作者内容蒸馏器**：把博主在**多个平台**发布的内容（视频、推文等）抓取下来，**转成带标点的文字稿**，统一喂给**本地大模型**做个人知识库。视频来源则调用转写，输出带**时间戳**的稿子，方便后续切片回看。

## 为什么用它 / 适合什么场景

- 想把**自己关注的一批创作者**的长视频 / 推文一次性消化成可检索知识；
- 不想手工开剪映 / Whisper / Otter 一次次转写；
- 偏好**本地 LLM + 个人知识库**路线（与 RAG、向量库配合）；
- 希望输稿**带标点、可检索**，而不是干巴巴的字幕流。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多平台抓取 | 把博主在多平台发布的内容拉下来 |
| 转文字稿 | 视频 / 语音内容转写为带标点的文本 |
| 时间戳稿 | 视频来源输出带时间戳，便于回溯原片段 |
| 喂本地 LLM | 输出格式适配本地大模型 + 知识库管线 |
| 一键蒸馏 | 从「创作者源」到「可检索文字」一步走 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/lihuanihaoma-design/creator-distiller>
