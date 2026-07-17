---
type: "Tool"
title: "brand-loom（hogan-tech/brand-loom）"
description: "能在任意大模型上跑的开放核心营销技能库: 钩子、文案、标签、内容重组、SEO 大纲、FAQ、结构化数据和行动号召都覆盖到了。"
resource: "https://github.com/hogan-tech/brand-loom"
tags: "[marketing, seo, content-skills, agent-skills, copywriting]"
timestamp: "2026-07-17T13:49:00Z"
---

# brand-loom

[brand-loom](https://github.com/hogan-tech/brand-loom) 是一个「**在任意大模型上都能跑的开放核心营销技能库**」, 把营销 / 内容 / SEO 的常见「动作」拆成可调用的 Skill, 而非一份 prompt 模板。

## 覆盖的营销环节

| 环节 | Skill 名称 (示意) | 输入 → 输出 |
|------|------|------|
| 钩子 | hook-generator | 主题 → 3-5 个不同角度的开头 |
| 文案 | copy-writer | 平台 / 调性 → 完整文案 |
| 标签 | tag-builder | 内容 → 平台相关标签 + 热度 |
| 内容重组 | spinner | 原始内容 → 多种重组版本 |
| SEO 大纲 | seo-outline | 关键词 / 主题 → 文章大纲 |
| FAQ | faq-generator | 内容 → Q&A 列表 |
| 结构化数据 | schema-builder | 页面 → JSON-LD schema |
| 行动号召 | cta-library | 目标 / 调性 → CTA 文案 |

## 它和「一堆 prompt 模板」的差别

| 维度 | 一次性 prompt | brand-loom |
|------|------|------|
| 模型依赖 | 通常为某一家定制 | **任意大模型**可挂 (通过 Skill 协议) |
| 行为粒度 | 整段输出 | 一项任务 = 一个 Skill |
| 可审计性 | 一段 prompt 不易拆 | 每个 Skill 独立可测 |
| 复用度 | 复制粘贴 | 多项目多模型共享 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 开放核心 | 自身不锁死模型提供方 |
| Skill 化 | 每个营销动作独立封装 |
| 多模型通用 | OpenAI / Claude / 本地模型都能驱动 |
| 营销链路覆盖 | 钩子 → 文案 → 标签 → SEO → CTA |

## 媒体

![](https://pbs.twimg.com/media/HNUECtSaoAEJmyX.jpg)

## 参考链接

- [项目仓库](https://github.com/hogan-tech/brand-loom)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 协议, brand-loom 是它在营销域的实例化
- [liurun-bookwriter-skills](./tool-liurun-bookwriter-skills.md) — 中文商业写作 Skill 双件套, 思路与 brand-loom 相近
- [xiaohongshu-ai-workbench](./tool-xiaohongshu-ai-workbench.md) — 同属「内容创作 Skill 化」方向
