---
type: Tool
title: "DSH Image Gen"
description: "DeepSeek Harness 插件：在对话内直接生成图片，省去切换外部网站和手动搬运图片的步骤。"
resource: "https://github.com/shanliuling/dsh-image-gen"
tags: [dsh, deepseek-harness, image-generation, plugin]
timestamp: "2026-08-24T12:31:00Z"
---

# DSH Image Gen

## 它是什么

[shanliuling/dsh-image-gen](https://github.com/shanliuling/dsh-image-gen) 是 DeepSeek Harness 的一个插件：在 DSH 对话内直接调用图像生成模型，省去「写好 prompt → 切到外部网站 → 等出图 → 下载 → 拖回 DSH 对话框」这套繁琐流程。

## 为什么用它 / 适合什么场景

- 用 DSH 时常需要「出一张配图」，不愿离开对话窗口。
- 想把图像生成接入 DSH 的多步工作流（如「先看代码 → 画示意图 → 写文档」）。
- 想在同一个对话上下文里让文本与图像互引。

## 关键能力

| 能力 | 说明 |
|------|------|
| 对话内出图 | 在 DSH 对话界面直接生成图片 |
| 上下文引用 | 生成的图可被对话上下文继续讨论 / 编辑 |
| 可配置模型 | 接各类图像生成后端（OpenAI / SD / 第三方） |
| 插件形式 | 不修改 DSH 核心代码 |

## 相关概念

- [Plugin Deepseek Vision](./tool-plugin-deepseek-vision.md) — 给 DSH 加视觉能力的同类插件
- [DSH Vision Toolkit](./tool-dsh-vision-toolkit.md) — 同为 DSH 加视觉能力的扩展

## 参考链接

- [项目链接](https://github.com/shanliuling/dsh-image-gen)
- ![](https://pbs.twimg.com/media/HQc8a0Ka0AA4_Ts.jpg)