---
type: Tool
title: "consulting-deck"
description: "zairuilab/consulting-deck，给 AI Agent 用的咨询风格 PPT 工具包：跑出来的 PPTX 论据能追到来源、图表带分析逻辑、PPTX 在 PowerPoint 里还能继续编辑。"
resource: "https://github.com/zairuilab/consulting-deck"
tags: "[ppt, deck, consulting, ai-agent, pptx, slide, source-traceability]"
timestamp: "2026-08-01T20:30:00Z"
---

# consulting-deck

## 它是什么

[`zairuilab/consulting-deck`](https://github.com/zairuilab/consulting-deck) 是给 **AI Agent** 用的**咨询风格 PPT 工具包**。它输出的 PPTX 有三个硬性优势：

1. **论据可追溯**：每个数据 / 结论都能跳回来源
2. **图表带分析逻辑**：不是孤立图表，每张图都说明「为什么这样画」「说明什么」
3. **PPTX 可继续编辑**：跑出来的 `.pptx` 在 PowerPoint 里能直接接着改，不用重做

## 解决什么痛点

- Agent 生成的 PPT 数字是「幻觉」——客户问「这数据哪来的？」答不上
- 图表只是装饰，不带分析逻辑（咨询公司做的图都有「所以呢」）
- 输出是图片 / HTML，PowerPoint 里改不动

## 关键能力

| 能力 | 说明 |
|------|------|
| Agent 友好 | 提供 Skill / 模板，AI Agent 可直接调用 |
| 咨询风格 | 模仿麦肯锡 / BCG 的「结论先行 → 论据 → 图表 → 行动建议」结构 |
| 论据溯源 | 每条数据 / 结论附来源链接或脚注 |
| 图表分析 | 图表带「所以呢」的分析注释 |
| PPTX 原生 | 输出可编辑 `.pptx`，不是图片 / PDF |

## 适合什么场景

- AI Agent 给咨询 / 投行 / 战略团队出 deck
- 个人用 Agent 出 deck 但要求「数字可查、图表可解读」
- 团队对外汇报，需要 deck 接受严苛审查

## 与同类工具的差异

| 工具 | 风格 | 差异 |
|------|------|------|
| [markdown-slides](./tool-markdown-slides.md) | 通用 Markdown → Slide | 无咨询风格 |
| [bolt-slides](./tool-bolt-slides.md) | 通用 | 同上 |
| [open-ai-canvas](./tool-open-ai-canvas.md) | 影策 / AI 影视画布 | 影视分镜，非咨询 deck |
| consulting-deck | 咨询风 | 论据溯源 + 图表分析 + PPTX 可编辑 |

## 媒体

![consulting-deck 截图](https://pbs.twimg.com/media/HOhOCIrbUAAJAB_.jpg)

## 原始链接

- [项目仓库](https://github.com/zairuilab/consulting-deck)
- [原始推文](https://x.com/QingQ77/status/2083332882244968787)

## 相关概念

- [markdown-slides](./tool-markdown-slides.md) — Markdown → Slide 的通用方案，consulting-deck 是它的「咨询风格强化版」
- [Agent Skills（代理技能包）](./term-agent-skills.md) — consulting-deck 按 Skill 形态提供，可作为「Skill 即模板」的范例