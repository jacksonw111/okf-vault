---
type: Tool
title: "Scientific Illustrator（可编辑科研插图 Codex 插件）"
description: "Codex 插件，让 AI 在 PowerPoint 和 draw 里逐步画出可编辑的科研插图（不是贴一张大图）。画图流程分四步：设计、绘图、审查、修正。"
resource: "https://github.com/icebird1998/scientific-illustrator"
tags: [codex-skill, scientific-figures, pptx, draw, editable, illustration]
timestamp: "2026-07-28T04:08:00.000Z"
---

# Scientific Illustrator

## 它是什么

一个 **Codex 插件**，把 AI 画的科研插图**做成 PowerPoint 和 draw 里可直接编辑的对象**，而非一张不能改的位图。

核心要求："能改"——文字、图形、表格、箭头都用**原生对象**。

## 四步流程

| 阶段 | 做什么 |
|------|--------|
| 设计 | 拆解插图元素（轴 / 数据系列 / 注释） |
| 绘图 | 在 PPT / draw 里生成原生对象 |
| 审查 | 每画完一个区域检查结构和渲染效果 |
| 修正 | 对照设计修正 |

## 它和「AI 出图」的根本区别

| AI 直接出图 | Scientific Illustrator |
|-------------|----------------------|
| 输出 PNG / JPEG | 输出可编辑原生对象 |
| 改不动 | 文字 / 颜色 / 形状都可改 |
| 学术不可二次编辑 | 学术插图可二次精修 |
| 一张图交付 | 整张 PPT 可改 |

## 关键能力

| 能力 | 说明 |
|------|------|
| Codex 插件 | 跑在 Codex 内 |
| 原生对象输出 | PowerPoint / draw 可双击编辑 |
| 四步流程 | 设计→绘图→审查→修正 |
| 区域级审查 | 每画一块都校验 |
| 学术插图友好 | 满足论文 / 海报 / 汇报需求 |

## 原始链接

- [项目仓库](https://github.com/icebird1998/scientific-illustrator)
- [推文剪藏](https://x.com/QingQ77/status/2081954801852485876)

## 相关概念

- [paper2anything](./tool-paper2anything.md) — 论文 PDF 自动生成 PPT / 海报 / 项目主页等宣传物料
- [happy-figure-skill](./tool-happy-figure-skill.md) — 科研绘图 prompt 生成 Skill（领域 × 图类型 × 模型路由）
- [GPT Image Skills](./tool-gpt-image-skills.md) — 32 个 GPT Image 2 配图 Skill 合集
- [zu-article-image-skill](./tool-zu-article-image-skill.md) — Markdown 文章配图 Skill，可编辑 prompt + 自动回插