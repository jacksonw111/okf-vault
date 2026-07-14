---
type: "Tool"
title: "reame（swellweb/reame）"
description: "跑在廉价 CPU 上的 LLM 推理服务:用磁盘缓存把同一提示与相似回答记下来,重复请求越跑越便宜,适合自托管 / 边缘场景。"
resource: "https://github.com/swellweb/reame"
tags: "[llm, inference, caching, disk-cache, cpu, edge, self-hosted]"
timestamp: "2026-07-14T14:40:00Z"
---

# reame

[reame](https://github.com/swellweb/reame) 是一个面向**廉价 CPU**的 **LLM 推理服务**:**通过磁盘缓存命中**让重复(及相似)请求越跑越便宜。

## 关键思想

| 层 | 作用 |
|----|------|
| 磁盘缓存 | 把同一提示 + 相似提示的回答存到本地磁盘 |
| 命中即返回 | 第二次起不再调用模型,直接返回缓存 |
| 相似度匹配 | 即使措辞不同,语义相近也能命中 |
| CPU 友好 | 不依赖 GPU,普通服务器甚至家用机可跑 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 廉价 CPU 推理 | 不依赖高端 GPU,适合预算敏感的部署 |
| 磁盘缓存层 | 降低重复请求的算力开销 |
| 越用越便宜 | 缓存命中率随时间增长 |
| 自托管友好 | 数据不出端,适合隐私场景 |

## 适合什么场景

- **FAQ / 客服 / 内部知识库**:大量重复问题,缓存命中率极高。
- **边缘 / IoT**:部署在仅 CPU 的网关 / 边缘盒。
- **预算紧的副业**:想跑一个 LLM 服务但买不起 GPU 服务器。
- **个人助手**:每天问很多相似问题,缓存自然累积。

## 与同类资源的差别

| 资源 | 特征 | reame |
|------|------|-------|
| Colibri | 25GB 跑 744B MoE | 极端模型;reame 是「廉价 + 缓存」思路 |
| llmaker | Go 写的私有 LLM 应用栈编排器 | 上层编排;reame 是底层推理服务 |
| OpenGENAI | 数字厅本地化 GENAI | 全栈;reame 更轻、更聚焦 |

## 参考链接

- [项目仓库](https://github.com/swellweb/reame)

## 相关概念

- [Colibri](./tool-colibri-inference.md) — 同样是面向低资源的推理引擎,主打 MoE 大模型;reame 主打 CPU + 缓存
- [Local LLM 硬件搭建实操指南](./note-local-llm-hardware-guide.md) — 本地 LLM 部署硬件选择参考
- [Open GENAI](./tool-open-genai.md) — 全栈本地 GENAI 平台
