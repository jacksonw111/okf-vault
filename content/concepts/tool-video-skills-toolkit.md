---
type: "Tool"
title: "video-skills-toolkit（liangdabiao/video-skills-toolkit）"
description: "把短视频生产流程沉淀成 6 个可复用 agent skills 的工具包：口播 / 公众号转视频 / 数学动画 / 纸片风动画等都走同一套「字幕驱动」流水线。"
resource: "https://github.com/liangdabiao/video-skills-toolkit"
tags: [video, agent-skills, content-pipeline, automation, short-video]
timestamp: "2026-08-05T13:15:00Z"
---

# video-skills-toolkit（liangdabiao/video-skills-toolkit）

## 它是什么

`video-skills-toolkit` 把**短视频生产流程**沉淀成 **6 个可复用的 agent skills**，让口播、公众号文章转视频、数学动画、纸片风动画等**各类视频**都能按同一套「**字幕驱动**」流水线**批量套模板**生产。

核心思路：**字幕是脚本与成片之间的单一事实源**——只要把字幕敲定，模板 / 分镜 / 配音 / 字幕样式都是基于字幕派生出来的。

## 为什么用它 / 适合什么场景

- **自媒体批量生产**：口播 / 图文转视频 / 教育类短视频，统一流水线。
- **模板驱动**：模板变了不改脚本，脚本变了模板自动跟随。
- **Agent 友好**：6 个 skill 可被 Claude Code / Codex 等编码 agent 直接调用，做内容流水线自动化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 字幕驱动流水线 | 脚本 = 字幕 = 成片事实源 |
| 6 个 Agent Skills | 口播 / 公众号转视频 / 数学动画 / 纸片风动画 等 |
| 模板化 | 套模板批量出片，不每个单独编排 |
| Agent 可调用 | Claude Code / Codex 等可直接调度 skill |

## 参考链接

- [GitHub 仓库](https://github.com/liangdabiao/video-skills-toolkit)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 同属「agent skills」模式，本工具包是该模式的视频生产实例
- [Bilibili Video Notes Skill](./tool-bilibili-video-notes-skill.md) — 视频 → 笔记的相反方向，可对照「视频 ↔ 文本」双向流水线