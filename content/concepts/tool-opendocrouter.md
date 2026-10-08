---
type: "Tool"
title: "OpenDocRouter（OCR 模型的统一路由）"
description: "Jerry Liu（LlamaIndex）出品：把市面上主流 OCR / 文档理解模型装进同一套 API 与计费入口，从轻量开源（MinerU）到前沿 VLM（Opus 5.5）都能一条命令对比 / 切换。"
resource: "https://www.opendocrouter.ai/"
tags: "[ocr, document-ai, router, llm, vision, api]"
timestamp: "2026-10-08T23:50:00Z"
---

# OpenDocRouter

## 它是什么

[OpenDocRouter](https://www.opendocrouter.ai/) 把「**OCR 模型的 OpenRouter**」做成一个独立的统一入口：**LlamaIndex** 团队 Jerry Liu 出品，给文档 OCR / 文档理解场景提供 OpenRouter 那种「一个 API、一个账单、所有模型可挑」的体验。

它把市面上的 OCR 模型从轻量开源的 `MinerU`、到前沿 VLM（Opus 5.5）等都接到同一个接口下，开发者不必每个模型分别接一遍 SDK、分别结账。

## 为什么用它 / 适合什么场景

- **想横向对比 OCR 模型**，又不想每个都接一遍 SDK
- **账单统一**：一个 API key、一张发票即可覆盖多种模型
- **轻量 vs 前沿可混用**：低复杂度文档走 OSS / 便宜模型，复杂版面走前沿 VLM
- **避免厂商锁定**：模型层随时可换

## 关键能力

| 能力 | 说明 |
|------|------|
| 统一 API | 一套接口调用多家 OCR / 文档理解模型 |
| 统一计费 | 一张账单覆盖多模型 |
| 模型覆盖 | 从轻量 OSS（e.g. MinerU）到前沿 VLM（e.g. Opus 5.5） |
| 对比测试 | 同一输入可在多个模型之间切跑，看效果与花费 |
| 出品方 | LlamaIndex 团队（Jerry Liu） |

## 参考链接

- 项目链接：<https://www.opendocrouter.ai/>
- 出品方：LlamaIndex / Jerry Liu

## 媒体

视频：<https://video.twimg.com/amplify_video/2108252307712622592/vid/avc1/1920x1080/TMm6mkQdnKQ2EVfi.mp4?tag=29>

## 相关概念

- [RAG（检索增强生成）](./term-rag.md) — 文档 OCR 经常是 RAG 流水线的第一环
- [MCP（Model Context Protocol）](./term-mcp.md) — OpenDocRouter 与 MCP 是上下游工具关系：MCP 接 agent，OpenDocRouter 把文档侧统一