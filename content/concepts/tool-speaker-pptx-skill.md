---
type: Tool
title: "speaker（学术演讲 PPTX 备注生成 Skill）"
description: "面向学术演讲的 Codex skill：读取真实 PPTX，结合文本提取、幻灯片渲染、OCR 与视觉审查，逐页生成有据可查的演讲备注并注入 PowerPoint 备注栏。"
resource: "https://github.com/AI272/speaker"
tags: [codex, agent-skills, pptx, ocr, presentation]
timestamp: "2026-06-25T07:34:00Z"
---

# speaker（学术演讲 PPTX 备注生成 Skill）

## 它是什么

一个面向**学术演讲场景**的 Codex Skill，专门处理 PPTX。它不只读文本框——

1. **提取文本**：用 python-pptx 拉所有文本。
2. **渲染幻灯片**：把 PPTX 每页**渲染成 PNG**。
3. **OCR**：识别截图里**嵌在图中的小字**（公式、图表标签、参考文献截屏等）。
4. **视觉审查**：对图表、SmartArt 这类**复杂视觉内容**逐一盘查，建每页可见元素清单。
5. **生成两版备注**：
   - **排练版**：带转场标记、停顿、词汇表、计时表。
   - **注入版**：干净版本，写入 PowerPoint **备注栏**。

## 为什么用它

- 学术 PPT 里的图常带「**关键信息在图里**」的小字——纯文本提取会漏。
- 「AI 写备注」通常只剩语义层，但学术演讲需要「**有据可查**」——speaker 把所有可见元素都盘出来再生成。
- 一次产出两版：排练时用详细版，**正式演讲备注栏只留干净版**。

## 关键步骤

| 步骤 | 干什么 |
|------|--------|
| 文本提取 | python-pptx 拉所有文本 |
| 渲染 | PPTX → PNG |
| OCR | 识别嵌图里的小字 |
| 视觉审查 | 图表 / SmartArt 等 |
| 元素清单 | 每页建立完整可见元素清单 |
| 备注生成 | 排练版 + 注入版 |

## 相关概念

- [PP-OCRv6 Studio](./tool-ppocrv6-studio.md) — 本地 OCR 工具；speaker 内嵌的 OCR 思路与之一致
- [Markdown → Slides](./tool-markdown-slides.md) — 同为「演示文稿」赛道，但 MD→Slides 是**生成**幻灯片，speaker 是**给已有幻灯片加备注**
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 又一个 SKILL.md 形态的内容增强 Skill
- [happy-figure-skill](./tool-happy-figure-skill.md) — 都是「结构化地理解图像 / 文档内容」的 Skill