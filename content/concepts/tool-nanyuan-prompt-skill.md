---
type: Tool
title: "南鸢写真提示词 Skill"
description: "把写真或人像摄影的想法写成能直接丢给生图模型的中文提示词，也能拿参考图反推一套可复用的视觉关键词；默认只出提示词，不负责生图。"
resource: "https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt"
tags: [ai-skill, prompt, image-gen, portrait, photography, chinese]
timestamp: "2026-08-03T11:12:00Z"
---

# 南鸢写真提示词 Skill

## 它是什么
南鸢写真提示词（`nuyoah-ai-works/nuyoah-xiezhen-prompt`）是一个面向**写真 / 人像摄影**的 AI Agent Skill。

- **正向流**：把写真或人像摄影的想法写成能直接丢给生图模型的中文提示词。
- **反向流**：拿参考图反推一套可复用的视觉关键词。
- **默认只出提示词，不负责生图**：作为 Skill 集成到 Agent，由 Agent 决定调度哪个图像生成模型。

南鸢个人维护，2026-07-24 从「生图工作知识库」迁到 GitHub 独立维护。

## 为什么用它 / 适合什么场景
- **意图到提示词的桥**：把模糊的「想要这种风格」翻译成生图模型可消费的结构化 prompt。
- **参考图反向工程**：拿到参考图后能抽出可复用的视觉关键词（光线 / 构图 / 色调 / 镜头）。
- **Agent 友好**：作为 Skill 暴露，任意支持 Skill 协议的 Agent 都能直接调用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 中文 prompt 生成 | 把摄影意图翻译成可丢给生图模型的中文提示词 |
| 参考图反推 | 拿到参考图 → 反推可复用的视觉关键词清单 |
| 写真 / 人像专属 | 提示词结构针对人像场景优化（光位 / 焦段 / 表情 / 构图） |
| 与生图解耦 | 仅输出 prompt，不绑定某一个生图服务 |

## 项目链接
- <https://github.com/nuyoah-ai-works/nuyoah-xiezhen-prompt>

## 相关概念
- [open-image-prompts](./tool-open-image-prompts.md) — 万级带参考图的 AI 图片 prompt 库
- [speaker-pptx-skill](./tool-speaker-pptx-skill.md) — 同属 Skill 形态，面向演示文档生成
- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的概念元定义
