---
type: "Note"
title: "OCR is Dead, Long Live Agentic OCR（LlamaIndex 观点）"
description: "LlamaIndex 官方博客观点：传统 OCR 流水线被 agentic OCR 取代——让 LLM Agent 主动控制截图、缩放、裁剪、调用工具，把 OCR 从「固定管线」升级为「可决策循环」，对复杂版式与多模态文档更鲁棒。"
resource: "https://www.llamaindex.ai/blog/ocr-is-dead-long-live-agentic-ocr"
tags: "[ocr, agentic, llm, llamaindex, vision, document-ai]"
timestamp: "2026-10-06T00:35:00Z"
---

# OCR is Dead, Long Live Agentic OCR

## 它是什么

[LlamaIndex 官方博客](https://www.llamaindex.ai/blog/ocr-is-dead-long-live-agentic-ocr) 提出的**观点文章**——传统 OCR（固定管线：检测 → 识别 → 后处理）被 **agentic OCR** 取代。

## 核心观点

| 维度 | 传统 OCR | Agentic OCR |
|------|----------|-------------|
| 流程 | 固定管线 | 可决策循环 |
| 输入处理 | 一次性全图 | Agent 主动截图 / 缩放 / 裁剪 |
| 工具调用 | 不支持 | 可调外部工具（搜索 / 重识别） |
| 复杂版式 | 易错 | 更鲁棒 |
| 输出 | 单次文本 | 多轮精炼 |

## 关键能力

- **主动决策**：Agent 根据已识别内容决定「再看哪里 / 调多大」
- **工具调用**：失败时主动调重识别 / 翻译 / 检索
- **多轮**：可对一份文档做多轮精炼

## 适合场景

- 复杂版式文档（表格 / 公式 / 排版混乱的扫描件）
- 想把 OCR 嵌入 RAG / Agent 工作流
- 评估传统 OCR 在垂类场景的天花板

## 参考链接

- 原始链接：<https://www.llamaindex.ai/blog/ocr-is-dead-long-live-agentic-ocr>

## 相关概念

- [RAG](./term-rag.md) — Agentic OCR 的下游场景
- [Computer Use](./term-computer-use.md) — Agentic OCR 借鉴的「让模型主动控制」思路
- [LlamaIndex](./tool-llamaindex.md) — 观点出处