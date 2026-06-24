---
type: "Tool"
title: "motion-skills（iart 运动图形技能包）"
description: "iart 发布的 50 个开源运动图形 Skill 包，按 14 个分类组织：抖音短视频 / 数据动画 / WebGL 3D / 数学动画等场景，每条带 SKILL.md 与渲染验证流程。"
resource: "https://github.com/iart-ai/motion-skills"
tags: [skills, motion-graphics, animation, webgl, agent]
timestamp: "2026-06-24T15:30:00Z"
---

# motion-skills（iart 运动图形技能包）

## 它是什么

[`iart-ai/motion-skills`](https://github.com/iart-ai/motion-skills) 是一套**面向 AI 编程代理设计的开源运动图形技能包**。项目分 14 个分类共 50 个 Skill，覆盖抖音短视频、数据动画、WebGL 3D、数学动画等常见动效场景。

每个 Skill 包含：

- 一份 `SKILL.md`（操作说明 + 设计意图）
- 参考文件 / 模板代码
- **渲染验证流程** — 让 agent 能自己跑一遍检查输出是否正确

## 为什么用它 / 适合什么场景

- 让 AI 代理**自己出能播的运动图形**，而不是生成静态代码让人类手改；
- 抖音短视频、数据图表动画、3D 演示等有现成分类可挑；
- 自带验证机制，agent 输出后能自动跑一遍检查（位置 / 颜色 / 帧率等）。

## 关键能力

| 能力 | 说明 |
|---|---|
| 50 个 Skill | 覆盖短视频 / 数据动画 / WebGL 3D / 数学动画等 |
| 14 个分类 | 抖音 / 数据 / 3D / 数学 / 通用动效 |
| SKILL.md 规范 | 适配 agent skill 协议（与 Claude Skills / Codex skills 同构） |
| 自带验证 | agent 输出后自动渲染检查 |
| 配套参考 | 每个 Skill 带可直接套用的代码模板 |

## 媒体 / 参考链接

- [项目链接](https://github.com/iart-ai/motion-skills)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念元定义
- [mattpocock/skills](tool-mattpocock-skills.md) — 同类 Real Engineers 风格 Skill 合集
- [shadcn/improve](tool-shadcn-improve.md) — 用最强模型审计代码的 Skill
- [transitions.dev](tool-transitions-dev.md) — 网页过渡效果精选
- [textmotion.dev](tool-textmotion-dev.md) — 文字动效精选
