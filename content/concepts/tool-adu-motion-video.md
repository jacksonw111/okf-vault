---
type: "Tool"
title: "adu-motion-video（口播动效模板 Skill）"
description: "阿杜实验室开源的 Claude Code Skill：拍口播想加动效不用从零写模板；助手读取 SKILL.md 与 AGENTS.md 后按口播 / 文案 / 素材挑选模板、排动画，输出 MP4 与可再编辑工程目录。"
resource: "https://github.com/adunext/adu-motion-video"
tags: "[ai-agent, skill, video, motion-graphics, claude-code, template]"
timestamp: "2026-10-06T00:35:00Z"
---

# adu-motion-video

## 它是什么

[adu-motion-video](https://github.com/adunext/adu-motion-video) 是 **阿杜实验室** 开源的**动画动效模板 Skill**——给 Claude Code 等 AI Agent 用：拍口播想加动效不用从零写模板，助手读取仓库里的 `SKILL.md` 与 `AGENTS.md` 后按口播、文案、素材**挑选模板 / 排动画**，交付 MP4 + 可再编辑工程目录。

## 关键能力

| 能力 | 说明 |
|------|------|
| Skill 化 | 用 SKILL.md 描述挑选规则，AGENTS.md 描述工程约束 |
| 模板库 | 已发布 2 类模板 / 7 种风格 / 17 个镜头组 |
| 竖屏 | 11 种风格 / 39 个完整组支持竖屏 |
| 横屏 | 10 种风格 / 32 组同时支持横屏 |
| 输出 | MP4 + 可再编辑工程目录（用户可二次微调） |
| 触发 | 口播文案 + 素材作为输入 |

## 工作流

1. 用户给口播 + 素材
2. Agent 读 SKILL.md / AGENTS.md 决定模板 / 风格 / 镜头组
3. 自动排动画，渲染 MP4
4. 同时输出可再编辑工程（用户可在熟悉编辑器里继续改）

## 适合场景

- 自媒体 / 口播视频作者想快速出「动效版」
- 不想从零学 AE / Motion / 视频剪辑
- 愿意把动效设计交给 AI，但保留二次编辑能力

## 参考链接

- 项目链接：<https://github.com/adunext/adu-motion-video>

## 相关概念

- [Agent Skills](./term-agent-skills.md) — 项目采用的扩展机制
- [motion-video-skill](./tool-motion-video-skill.md) — 同为 AI 视频质量门禁 Skill