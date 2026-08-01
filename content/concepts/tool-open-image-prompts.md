---
type: Tool
title: "open-image-prompts"
description: "NanmiCoder/open-image-prompts，整理了上万条带参考图的 AI 图片 prompt，装个 Skill 就能直接在终端里搜，避免每次写图片 prompt 都从零试。"
resource: "https://github.com/NanmiCoder/open-image-prompts"
tags: "[ai-image, prompt-library, skill, terminal, midjourney, stable-diffusion]"
timestamp: "2026-08-01T20:30:00Z"
---

# open-image-prompts

## 它是什么

[`NanmiCoder/open-image-prompts`](https://github.com/NanmiCoder/open-image-prompts) 是一个**带参考图的 AI 图片 prompt 库**：整理了**上万条**已经验证过效果的 prompt，每条都附参考图。装成 Skill 后可以在终端里直接搜，省掉「每次写 prompt 都从零试」的盲目试错。

## 解决什么痛点

- 写 AI 图片 prompt 时不知道别人用过什么、效果如何
- 自己试错成本高（生成 + 肉眼对比）
- prompt 散落在各种博客 / Reddit / Discord 里，没法系统化检索

## 关键能力

| 能力 | 说明 |
|------|------|
| 万级 prompt 库 | 上万条带参考图的 prompt，按风格 / 主题分类 |
| 配参考图 | 每条 prompt 都附实际生成的参考图，直观看效果 |
| Skill 化 | 装成 Skill 后在终端 / IDE / Agent 里就能搜 |
| 避免试错 | 直接复用别人验证过的 prompt，省时间 |

## 适合什么场景

- 经常写 Midjourney / Stable Diffusion / DALL-E prompt 的创作者
- 想给 AI Agent / Coding 工具配「找 prompt」能力
- 想搭自己的 prompt 知识库

## 与同类工具的差异

| 工具 | 范围 | 差异 |
|------|------|------|
| [ai-video-ad-prompts](./tool-ai-video-ad-prompts.md) | 视频广告 prompt | 视频而非图片 |
| [academic-humanizer](./tool-academic-humanizer.md) | 文本 prompt | 学术写作场景 |
| [AI Video Ad Prompts 合集](./tool-ai-video-ad-prompts.md) | 视频 prompt | 不同模态 |
| open-image-prompts | 图片 prompt + 图 | 图文配对，Skill 化 |

## 媒体

![open-image-prompts 截图](https://pbs.twimg.com/media/HOhcQmjaUAAxH7b.jpg)

## 原始链接

- [项目仓库](https://github.com/NanmiCoder/open-image-prompts)
- [原始推文](https://x.com/QingQ77/status/2083574977350205599)

## 相关概念

- [ai-video-ad-prompts](./tool-ai-video-ad-prompts.md) — 同为 prompt 库思路，模态不同（视频）
- [Agent Skills（代理技能包）](./term-agent-skills.md) — open-image-prompts 本身就是按 Skill 形式封装的，可作为「Skill 是什么」的具体例子