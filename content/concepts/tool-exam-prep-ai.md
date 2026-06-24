---
type: "Tool"
title: "ExamPrep-AI（PDF 笔记转考试复习材料）"
description: "基于 Streamlit 的 AI 学习助手，把 PDF 笔记自动转成摘要 / 选择题 / 闪卡 / 术语表 / 备考计划等考试复习材料，支持本地 Ollama 或 Google Gemini 后端，带输出校验和修复重试机制。"
resource: "https://github.com/suran-jeet/ExamPrep-AI"
tags: [ai, education, streamlit, pdf, ollama, gemini]
timestamp: "2026-06-24T15:30:00Z"
---

# ExamPrep-AI（PDF 笔记转考试复习材料）

## 它是什么

[`suran-jeet/ExamPrep-AI`](https://github.com/suran-jeet/ExamPrep-AI) 是一个 **Streamlit 写的 AI 学习助手**，把 PDF 笔记自动转成多种考试复习材料：

- 摘要（summary）
- 选择题（multiple choice）
- 问答题（Q&A）
- 闪卡（flashcards）
- 术语表（glossary）
- 备考计划（study plan）

## 为什么用它 / 适合什么场景

- 临考复习：把一本 PDF 课本/讲义喂进去，几分钟拿到配套闪卡 + 选择题；
- 教师出题：把课件丢进去，自动生成练习题初稿；
- 支持本地 Ollama（Gemma / Qwen / Llama / Mistral）或 Google Gemini，**数据敏感场景可完全离线**；
- 自带输出校验 + 修复重试机制，不会因为模型一次答错就崩。

## 关键能力

| 能力 | 说明 |
|---|---|
| 多材料类型 | 摘要 / 选择题 / Q&A / 闪卡 / 术语表 / 备考计划 |
| 双后端 | 本地 Ollama / Google Gemini |
| 校验重试 | 输出不合规会自动让模型改写 |
| Streamlit UI | 浏览器即开即用 |
| PDF 输入 | 适配扫描件 / 文本件 |

## 媒体 / 参考链接

![截图](https://pbs.twimg.com/media/HLi6RB1bYAAxjvf.jpg)

- [项目链接](https://github.com/suran-jeet/ExamPrep-AI)

## 相关概念

- [Datalab LIFT](tool-datalab-lift.md) — 9B 视觉语言模型，给 JSON Schema 直接从 PDF 抽出结构化 JSON
- [obsidian-knowledge-agent](tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道把论文 / PDF 自动整理为 Obsidian 笔记
- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — Electron 本地 AI 桌面工作台，可挂接本地 Ollama 后端
