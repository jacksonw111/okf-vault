---
type: "Tool"
title: "BeefTV（本地自由画布：多模型 + Agent 多媒体生成）"
description: "glanderness 出品：本地跑的自由画布，把文本 / 图片 / 视频 / 音频模型的生成调用都接进来，Agent 在画布上摆节点、连素材、把产出写回去接着改。"
resource: "https://github.com/glanderness/BeefTV"
tags: "[canvas, agent, multimodal, local, image-gen, video-gen, audio-gen]"
timestamp: "2026-09-28T23:50:00Z"
---

# BeefTV（本地自由画布：多模型 + Agent 多媒体生成）

## 它是什么

[BeefTV](https://github.com/glanderness/BeefTV) 是 glanderness 出品的**本地自由画布**：把**文本 / 图片 / 视频 / 音频模型的生成调用**都接进来，让 **Agent 在画布上摆节点、连素材、把产出写回去接着改**。

定位介于「**白板 / Miro 类自由画布**」与「**ComfyUI 类节点工作流**」之间——但更偏向 **Agent 驱动的多媒体生成**：每一节点都可以挂一个模型调用，结果回流到画布可继续编辑。

## 为什么用它 / 适合什么场景

- 想把多模型（文本 / 图 / 视频 / 音频）**编排进同一张画布**，让 Agent 自动推进。
- 想要**本地**的画布 + 模型调用——避免数据上传第三方云。
- 创意 / 设计 / 营销工作流：素材组合 → 生成 → 迭代 全在一张画布里完成。
- 想用 **Agent 当操作员**——节点之间的连线就是它的操作路径。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地自由画布 |
| 模型覆盖 | 文本 / 图片 / 视频 / 音频 |
| 操作方式 | Agent 在画布上摆节点、连素材、回写产出 |
| 部署 | 本地跑 |
| 出品 | glanderness |

## 媒体

- ![](https://pbs.twimg.com/media/HTRiXtva8AA7AXb.jpg)

## 相关概念

- [Toolcraft](./tool-toolcraft.md) — pixel-point 出的创意类应用 starter kit，自带 canvas + 工具栏（BeefTV 与 Toolcraft 都在「画布 + 创意工具」赛道）
- [Design Studio AI](./tool-design-studio-ai.md) — 开源设计台，人 + Agent 同一份文档（与 BeefTV 同属「画布 + Agent」思路）