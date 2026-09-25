---
type: "Tool"
title: "html-explainer（HTML/CSS/GSAP 视频解说 Agent Skill）"
description: "一个跨 Agent Skill（Claude Code / OpenAI Codex / WorkBuddy / Cursor / Gemini CLI 都能加载），把调研 / 解说词 / TTS 配音 / 词级字幕 / HTML/CSS/GSAP 画面 / MP4 渲染 / 质量检查 / 封面生成串成一条本地流水线。"
resource: "https://github.com/OneMoh/html-explainer"
tags: "[agent-skill, tts, gsap, html-animation, mp4-render, claude-code, codex, cursor, gemini-cli, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# html-explainer（HTML/CSS/GSAP 视频解说 Agent Skill）

## 它是什么

[html-explainer](https://github.com/OneMoh/html-explainer) 是一个**横跨多 Agent 的 Skill**——**Claude Code / OpenAI Codex / WorkBuddy / Cursor / Gemini CLI** 都能加载。

它把做一条「**HTML 视频解说**」的整条流水线串起来：

1. **调研**
2. **解说词**撰写
3. **TTS 配音**
4. **词级字幕**生成
5. **HTML / CSS / GSAP 画面**生成
6. **MP4 渲染**
7. **质量检查**
8. **封面生成**

整条流水线在**本地**跑，不需要云端 SaaS。

## 为什么用它 / 适合什么场景

- 想做**视频解说**类内容（产品介绍 / 技术教程 / 科普），但又不想每一步都用不同 SaaS（调研 Notion / 文案 GPT / TTS 某某 / 剪辑剪映）拼起来。
- 偏好**纯 HTML/CSS/GSAP** 描述画面——版本可控、可 diff、不会丢源文件。
- 想把视频做成**可重复的 Skill**：一次跑通、复用 N 次，团队任何人都能用同一套工序出片。
- 跨 Agent 平台——在 Codex 里写的 Skill，可以直接挪到 Claude Code / Cursor / Gemini CLI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill（多平台通用） |
| 支持平台 | Claude Code / Codex / WorkBuddy / Cursor / Gemini CLI |
| 流水线 | 调研 → 解说词 → TTS → 字幕 → HTML/CSS/GSAP 画面 → MP4 → 质检 → 封面 |
| 渲染 | 本地 MP4 渲染 |
| 字幕 | 词级时间戳 |
| 配音 | TTS（可换本地 / 云端） |
| 画面 | HTML + CSS + GSAP（纯前端栈） |
| 可重复 | 一次跑通、复用 N 次 |

## 媒体

视频演示：

<https://video.twimg.com/amplify_video/2103333033659310080/vid/avc1/1280x720/GlBn0JUCZfphLDQw.mp4?tag=29>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — html-explainer 所属的技能生态
- [axichuhai-motion-video](./tool-axichuhai-motion-video.md) — 同类「动效视频 Skill 集合」，html-explainer 偏向「解说流水线」一侧
