---
type: Tool
title: "NativePDF Structurer"
description: "纯 Python 数字原生 PDF 结构化工具：用 PyMuPDF 读出文字 / 字体 / 坐标 / 图片 / 矢量，重建阅读顺序、章节层级、表格与视觉区域，无 OCR / GPU / VLM。"
resource: "https://github.com/crunz-ai/nativePDF-structurer"
tags: [pdf, markdown, rag, pymupdf, document-parsing, no-ocr]
timestamp: "2026-08-25T19:30:00Z"
---

# NativePDF Structurer

## 它是什么

[crunz-ai/nativePDF-structurer](https://github.com/crunz-ai/nativePDF-structurer) 是一个**纯 Python 写**的数字原生 PDF 结构化工具，盯的场景是设备操作手册、维修手册、选型手册这类**几百页、图文混排、结构复杂**的长文档。它用 [PyMuPDF](https://pymupdf.readthedocs.io/) 读出：

- 文字
- 字体
- 坐标
- 图片对象
- 矢量路径

然后**重建阅读顺序、章节层级、表格与视觉区域**，输出可直接喂进 RAG 流程的 Markdown。

关键卖点：**OCR / GPU / VLM 一概不需要**——只依赖 PDF 内嵌结构，对「数字原生」PDF 效果最佳。

![](https://pbs.twimg.com/media/HQiBTC5aQAAQRU9.jpg)

![](https://pbs.twimg.com/media/HQiBTtba8AAwlhN.jpg)

## 为什么用它 / 适合什么场景

- **厂商技术手册 / 设备 PDF**：几百页图文混排，普通转换工具输出质量差。
- **不想花 GPU 跑 VLM / OCR**：纯 CPU 上的 PyMuPDF 即可。
- **RAG 知识库预处理**：把 PDF 转成结构化 Markdown，下游 embedding / chunking 才靠谱。
- **数字原生 PDF**（非扫描件）：本工具针对此场景设计，效果最好。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文字 / 字体 / 坐标读取 | 基于 PyMuPDF 的底层解析 |
| 图片 / 矢量保留 | 不丢视觉元素 |
| 阅读顺序重建 | 把跨栏 / 跨页内容按逻辑顺序串联 |
| 章节层级还原 | 识别标题层级，输出 Markdown 结构 |
| 表格识别 | 重建表格结构（不依赖 OCR） |
| 无 OCR / GPU / VLM | 纯 CPU 即可 |
| 输出 Markdown | 直接进 RAG 流程 |

## 相关概念

- [Open-Sheet](./tool-open-sheet.md) — 同样把「结构化文档」从异构源还原为可消费格式
- [Clarify](./tool-clarify.md) — 面向 MDX + OpenAPI 的文档发布工具，本工具是其上游结构化输入的潜在搭档

## 参考链接

- 项目链接: <https://github.com/crunz-ai/nativePDF-structurer>
- 原始链接: <https://x.com/QingQ77/status/2092260459118305610>