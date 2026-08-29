---
type: Tool
title: "WeMM-Embedding（腾讯微信通用多模态嵌入模型）"
description: "腾讯微信团队开源的通用多模态嵌入模型：文本 / 图像 / 视频 / 视觉文档 / 交错输入都能处理（暂不支持音频），2B / 4B / 9B 三档支持 Matryoshka 维度截断。"
resource: "https://github.com/Tencent/WeMM-Embedding"
tags: [embedding, multimodal, tencent, wechat, matryoshka, retrieval]
timestamp: "2026-08-29T21:30:00Z"
---

# WeMM-Embedding（腾讯微信通用多模态嵌入模型）

## 它是什么

[Tencent/WeMM-Embedding](https://github.com/Tencent/WeMM-Embedding) 是腾讯微信团队开源的**通用多模态嵌入模型**——把文本、图像、视频、视觉文档（截图 / PDF / 表格图）、交错输入（图文混排）**统一映射到同一个向量空间**；暂不支持音频。

模型规格：

| 规格 | 用途 |
|------|------|
| WeMM-2B | 轻量、可部署 |
| WeMM-4B | 平衡 |
| WeMM-9B | 强表征 |

亮点：**Matryoshka 维度截断**——2B 版砍到 256 维仍保留满维性能的 98.7%，下游可以按需选维度（速度 ↔ 精度）。

## 为什么用它 / 适合什么场景

- **统一检索**：文本 / 截图 / 视频帧 / PDF 一起搜，不必为不同模态维护多套索引；
- **RAG 升级**：多模态知识库——文档里既有正文也有图、表、公式；
- **以图搜文 / 以文搜图**：跨模态反向检索；
- **小资源部署**：用 Matryoshka 截断到低维，单机也能跑；
- 微信生态产品的嵌入能力复用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模态统一 | 文本 / 图像 / 视频 / 视觉文档 / 交错输入 |
| 三档规格 | 2B / 4B / 9B |
| Matryoshka | 维度可截断，低维保留高维性能 |
| 检索友好 | 单一向量空间，跨模态检索不用桥接模型 |
| 暂不支持音频 | 设计取舍——视觉优先 |

## 相关概念

- [Qwen MM Plugins](./tool-qwen-mm-plugins.md) — 阿里 Qwen 系列多模态插件，与 WeMM 同属多模态嵌入生态
- [Qwen Audio Agent](./tool-qwen-audio-agent.md) — 偏音频侧的多模态代理，WeMM 是视觉多模态的对照

## 参考链接

- 项目链接：<https://github.com/Tencent/WeMM-Embedding>
- 原始推文：<https://x.com/QingQ77/status/2093523279382196369>
- 媒体：<https://pbs.twimg.com/media/HQxmviyaQAAVdFm.jpg>