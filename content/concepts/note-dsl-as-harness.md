---
type: "Note"
title: "DSL-as-Harness（用 DSL 驾驭 LLM）"
description: "mulmoclaude 项目提出的核心观点——HTML、Markdown、ASD-STE100、ShapeScript 等受限 DSL 是约束 LLM 输出的天然缰绳，把表达限制在合法子集里，让模型产出更稳定、更可读、更易被工具链二次加工。"
resource: "https://github.com/receptron/mulmoclaude/blob/main/docs/papers/dsl-as-harness.md"
tags: "[llm, harness, dsl, constrained-generation, mulmoclaude, prompt-engineering]"
timestamp: "2026-10-02T12:00:00Z"
---

# DSL-as-Harness（用 DSL 驾驭 LLM）

## 核心论点

LLM 的「自由发挥」不可靠。DSL（受限领域语言，HTML、Markdown、ASD-STE100、ShapeScript 等）用语法 + 词表 + 写作约束把模型输出压到一个可被工具链二次处理的合法子集——这就是 DSL 当 harness（缰绳）的本质。

> Karpathy、snakajima 等都把它列为 LLM 时代最值得押注的范式之一。

## 为什么 DSL 比「自然语言 + 提示词约束」更稳

| 自然语言 | DSL |
|----------|-----|
| 输出格式靠 prompt 软约束 | 输出格式由语法硬约束 |
| 改 prompt 才会调整风格 | 换词表 / 文法即可调整风格 |
| 解析必须靠另一个 LLM | 用标准 parser 即可机读 |
| 失败模式：跑题、重复、幻觉 | 失败模式：语法错误（可被工具检测并重试） |
| 二次加工要重写 | 可直接喂给下一道工序（编译 / 渲染 / 转写） |

## 实战里常用的几类 LLM-harness DSL

| DSL | 用途 | 强在哪 |
|-----|------|--------|
| HTML | 落地页 / 仪表盘 | LLM 前端能力极强，HTML 即产物 |
| Markdown | 文档 / 笔记 | 与 OKF / Obsidian / GitHub 直通 |
| ASD-STE100 | 受控英语（航工维护文档） | 句长 + 词汇 + 句式有硬限制，比 LLM 默认文风更可读 |
| ShapeScript / SVG | 图示 / 几何 | 二维向量表达，几何有唯一解 |
| Mermaid / PlantUML | 图表 | 文本进、PNG / SVG 出 |

## 选 DSL 的启发式

1. **下游有 parser** → 必选（HTML / MD / SVG / SQL）
2. **下游有 LLM 二次润色** → 选受控英语类（ASD-STE100 / 简化 Markdown）
3. **下游直接渲染** → 选带官方 runtime 的（HTML / SVG / Mermaid）
4. **下游机器学习** → 选结构化 JSON / YAML Schema

## Karpathy 给出的 LLM 输出升级链

从最弱到最强：纯文本 → 受控英语（ASD-STE100）→ 图表 / 图示 → 交互式 HTML 网页 → 定制化解释视频。
**每一层都把表达压到更紧的合法子集里**，因此每一层都更稳、更可解析、更可被工具链直接消费。

## 相关概念

- [Harness Engineering](./term-harness-engineering.md) — 把 LLM 包成稳定产品的大伞概念，DSL-as-harness 是其中一支具体路径
- [Karpathy 关于 LLM 输出的层级建议](./note-karpathy-llm-output-formats.md) — 同源思路的另一种叙述
- [ASD-STE100](#) — 航工维护领域「受控英语」规范，本仓库目前未收录
