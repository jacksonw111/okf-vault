---
type: "Note"
title: "Karpathy 的 LLM 输出格式升级链"
description: "Karpathy 提出的 LLM 产物形式排序：纯文本 → ASD-STE100 受控英语 → 图表 / 图示 → 交互式 HTML 网页 → 定制化解释视频。每一层都比上一层「表达更紧、可解析更强」，是「用 LLM 帮人理解」的实战心法。"
resource: "https://x.com/karpathy/status/2105819303471976479"
tags: "[llm, karpathy, dsl, output-format, explainer, asd-ste100, html, video]"
timestamp: "2026-10-02T09:30:00Z"
---

# Karpathy 的 LLM 输出格式升级链

## 一句话

理解一件事有 5 种 LLM 产物形式，**越往上越值钱**：

> 文本 → 受控英语 → 图示 → 网页 → 视频

## 五层（按价值从低到高）

### 1) 纯文本（baseline）

LLM 默认产物。能读，但**篇幅长、靠文字描述形状和关系**，可解析性差。

### 2) 受控英语（ASD-STE100）

让 LLM 按航工维护文档的受控英语规范（ASD-STE100）输出：句长、词汇、句式都有硬约束。比 LLM 默认文风更可读。
> Tip：直接用太严，可以让 LLM 输出「80% of the way to ASD-STE100」做软化版。

### 3) 图示 / 图表（images / diagrams）

让 LLM 输出 SVG / Mermaid / 图表。**形状、关系、层级一目了然**，扫一眼胜过读三段文字。

### 4) 交互式 HTML 网页

让 LLM 直接产出 HTML 网页——动画、交互、响应式布局都行。LLM 的前端能力在 2024 之后大幅提升，已经能直接出可发布的漂亮网页。

### 5) 定制化解释视频

Karpathy 最看好的终极形态：让 LLM 输出「3b1b 风格的解释视频」，配上 ElevenLabs（或本地替代）的旁白。**最贵的认知密度**，门槛也在降。

## 为什么「越往上越值钱」

| 层 | 表达紧度 | 可解析 | 复用度 | 理解成本 |
|----|---------|--------|--------|----------|
| 文本 | 低 | 低 | 低（要二次加工） | 高 |
| 受控英语 | 中 | 中 | 中 | 中 |
| 图示 | 中高 | 高 | 高 | 低 |
| HTML | 高 | 高 | 极高（直接发布） | 低 |
| 视频 | 极高 | 中（要 ASR） | 极高（最终交付） | 最低 |

## 关键洞察

- LLM 越来越强，**人会越来越多地「上移」到监督与理解层**——具体生成交给 LLM。
- **智能 + 代码越来越便宜**——可以问 LLM 要「大件、自定义、用完即弃」的软件（web app、explainer video），这在以前没有意义。
- 「Push the boundaries here」——尝试在日常工作中尽量往上挪一档。

## 实战用法

| 你想要的效果 | 让 LLM 输出 |
|--------------|-------------|
| 一份学习笔记 | 「80% of the way to ASD-STE100」的 markdown |
| 一段流程说明 | Mermaid 流程图 |
| 一个工具演示 | HTML 单文件（含动画） |
| 一个产品介绍 | 60 秒讲解视频脚本 + 配音 + 画面 |
| 一次方案评审 | HTML dashboard，可点击、可高亮、可对比 |

## 参考链接

- 原始链接：<https://x.com/karpathy/status/2105819303471976479>
- 配图：<https://pbs.twimg.com/media/HTlaHqgbwAAS1lv.png>

## 相关概念

- [DSL-as-Harness](./note-dsl-as-harness.md) — Karpathy 思路的另一种说法，强调 DSL 本身是缰绳
- [Mermaid](#) — Karpathy 推荐的具体 DSL 之一，本仓库目前未收录
- [HTML as LLM artifact](#) — 本仓库目前未收录
