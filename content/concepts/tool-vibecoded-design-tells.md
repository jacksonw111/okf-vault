---
type: "Tool"
title: "Vibecoded Design Tells（AI 生成网站的设计特征排名）"
description: "JCarterJohnson/vibecoded-design-tells —— 用 320 万条 Reddit 帖子总结出来的「AI 生成网站一眼能看出」设计特征排名，揭示 shadcn/Tailwind 默认样式与「AI 紫」渐变为何高频出现。"
tags: "[design, ai, reddit-mining, shadcn, tailwind, anti-pattern]"
timestamp: "2026-06-22T16:00:00Z"
---

# Vibecoded Design Tells（AI 生成网站的设计特征排名）

## 它是什么

[`JCarterJohnson/vibecoded-design-tells`](https://github.com/JCarterJohnson/vibecoded-design-tells) 是一个**基于 Reddit 数据挖掘的「AI 网站视觉痕迹」调研项目**。扫描 Reddit 上 47 个 AI / SaaS 子版块的 320 万条帖子，汇总出用户用来识别 AI 生成网站的设计特征排名。

核心发现：

- **shadcn / Tailwind 默认样式**位居前列
- **"AI 紫"渐变**高频出现
- **"千篇一律"** 是最普遍的抱怨

> 截图：![](https://pbs.twimg.com/media/HLTayPPaUAAVUHH.jpg)

## 为什么用它 / 适合什么场景

- **前端工程师 / 设计师**：做产品落地页时知道「避免踩哪些坑」，**反向工程**出「不那么 AI 味」的设计。
- **AI Coding Agent 评测者**：评估 agent 生成 UI 的「品牌感」/「独特性」，可作为打分维度。
- **设计审查者**：在自己团队 / 开源项目里快速识别「未经思考就套默认主题」的情况。
- **学术 / 调研**：研究 LLM 生成内容的「视觉指纹」问题。

## 关键能力

| 能力 | 说明 |
|---|---|
| 数据规模 | 47 个 Reddit 子版块 × 320 万条帖子 |
| 排名维度 | 用户主动指认的「AI 痕迹」设计特征 |
| 社区来源 | AI / SaaS 子版块，采样有偏但量大 |
| 输出形式 | 设计特征排行榜 + 示例截图 |

## 主要发现的「AI 痕迹」设计特征

| 排名层级 | 特征类型 | 典型表现 |
|---|---|---|
| 头部 | shadcn / Tailwind 默认样式 | `rounded-xl`、阴影默认值、卡片栅格 |
| 头部 | 「AI 紫」渐变 | `#7C3AED` → `#3B82F6` 之类蓝紫渐变 |
| 普遍 | 千篇一律的「千篇一律」 | hero / 特性 / 截图三段论 |
| 普遍 | 通用 placeholder 文案 | "Empower your workflow with AI" |
| 高频 | emoji 装饰过度 | 头部每行配一个 sparkle ✨ |

## 参考链接

- [项目链接](https://github.com/JCarterJohnson/vibecoded-design-tells)

## 相关概念

- [Vercel Design System](tool-vercel-design-system.md) — vercel.com/design.md 公开设计系统页（同属「设计系统反向参考」方向）
- [DESIGN.md 最佳实践](note-design-md-best-practices.md) — 把设计系统装进 .md 喂给 AI
- [shadcn/improve](tool-shadcn-improve.md) — 用最强模型审计代码（审计 shadcn 默认样式时常用）