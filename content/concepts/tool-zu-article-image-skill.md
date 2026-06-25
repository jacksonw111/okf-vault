---
type: Tool
title: "zu-article-image-skill（Markdown 文章配图 Skill）"
description: "给 Markdown 文章配图的 Skill：分析文章结构 → 在正文里插入可编辑的 prompt 标签 → 用户确认 → 生成图片 → 自动插回原位置。"
resource: "https://github.com/wwenj/zu-article-image-skill"
tags: [agent-skills, markdown, image-generation, claude-code, codex]
timestamp: "2026-06-25T06:34:00Z"
---

# zu-article-image-skill（Markdown 文章配图 Skill）

## 它是什么

一个面向 Markdown 文章的「**配图 Skill**」，跑在 Claude Code / Codex 上。流程是：

1. **分析文章结构**——读 Markdown，识别「这里该有图」的位置。
2. **在正文里插可编辑的 prompt 标签**——比如 `<!-- zu-image: 一张说明 XXX 概念的示意图 -->`。
3. **用户确认 / 修改**——prompt 文本可编辑、不会被神秘黑盒吞掉。
4. **生成图片**——交给下游图像生成模型。
5. **自动插回原位置**——生成完替换 tag 为真正的 `![](url)`。

## 为什么用它

- **人在 prompt 回路**：默认 prompt 可改，避免「AI 配图总是 AI 紫渐变」的同质化。
- **结构感知**：不是「往文末加张图」，而是按文章节奏在合适位置插。
- **OKF 友好**：Markdown 原生，输出可直接并入 OKF 知识库的概念文件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文章结构分析 | 识别需要配图的位置 |
| 可编辑 prompt 标签 | 人在回路（human-in-the-loop） |
| 一键生成 | 用户确认后自动调下游图像模型 |
| 自动回插 | 把生成的图插回 Markdown 对应位置 |

## 媒体

![](https://pbs.twimg.com/media/HLjI-10b0AALEZR.jpg)

## 相关概念

- [happy-figure-skill](./tool-happy-figure-skill.md) — 同为图像生成 prompt 路由 Skill，但侧重「科研语义 → 模型语义」；zu-article-image-skill 侧重「文章结构 → 配图位置」
- [GPT Image Skills](./tool-gpt-image-skills.md) — 32 个 GPT Image 2 配图 Skill 合集；zu-article-image-skill 是其中「文章配图」这条线的整合入口
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 又一个 SKILL.md 形态的图像 Skill
- [OKF 是什么](./term-okf.md) — 输出直接可并入 OKF 概念文件