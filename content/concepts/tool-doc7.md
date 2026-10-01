---
type: Tool
title: "doc7（多种格式文档整页转 Markdown 的本地化方案）"
description: "magicrew 出品的本地文档预处理工具：把 PDF / Office / 邮件 / EPUB / Jupyter / 截图等异构文档**逐页渲染成图片**，再交给能看图的本地模型读出 Markdown，给下游 AI 检索 / 引用 / 推理；不依赖独立 OCR，也不按页收费。"
resource: "https://github.com/magicrew/doc7"
tags: [document, ocr, markdown, ai-pipeline, pdf, office, llm-vision, local]
timestamp: 2026-10-01T12:37:45Z
---

# doc7

## 它是什么

**doc7** 是 [magicrew](https://github.com/magicrew) 开源的本地文档→Markdown 预处理工具。它针对一个常见的痛点：把一堆格式杂乱的资料（PDF、Word、扫描件、邮件附件、截图……）丢给 AI 用之前，光整理格式就要耗半天。

doc7 的核心思路是**反直觉但实用**：不依赖独立的 OCR 工具，而是把每一页渲染成图片，**直接让能看图的 AI 模型去读懂整页内容**，输出为干净的 Markdown。

- **模型自带 OCR 能力**，省掉 OCR pipeline 的复杂度。
- 用**本地部署**的视觉模型，不按页收费，跑多少文档看机器性能上限。
- 输出干净的 Markdown，下游 RAG / 引用 / 推理都能直接接。

## 为什么用它 / 适合什么场景

- 想把内部文档、合同、书籍、邮件快速灌进向量库或 Agent 上下文。
- OCR 工具识别效果差（公式 / 表格 / 多栏排版），希望由多模态模型直接读。
- 想统一多源文档（PDF + Word + 邮件 + 截图）到一个 Markdown 中间层。
- 不想按页付费，希望把处理成本压在自己机器上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 思路 | 整页渲染 → 多模态模型读图 → Markdown |
| 输入格式 | PDF / Office / 邮件 / EPUB / Jupyter / 网页截图 |
| 运行时 | 本地模型，不按页计费 |
| 输出 | 干净的 Markdown，可直接喂给 RAG / Agent |
| 许可 | 开源（详见仓库） |

## 参考链接

- 仓库：<https://github.com/magicrew/doc7>

## 媒体

- ![](https://pbs.twimg.com/media/HTW6dKVaUAA6RQy.jpg)

## 相关概念

- [OCR](./term-okf.md) — doc7 是「让多模态模型兼任 OCR」的实践
- [RAG](./term-okf.md) — 下游典型消费方式
