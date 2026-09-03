---
type: Tool
title: "dsh-visual-plugin（DeepSeek Harness Web 视觉插件）"
description: "针对 DeepSeek Harness Web 推出的零运行时依赖 TypeScript 插件，图片走 DSH 自带附件通道不单独配置视觉模型，右侧面板把当前模型对每张图的回答连同缩略图整理成可展开历史，一键复制。"
resource: "https://github.com/jyh20030112/dsh-visual-plugin"
tags: [deepseek-harness, plugin, vision, typescript, image]
timestamp: "2026-09-03T00:00:00Z"
---

# dsh-visual-plugin（DeepSeek Harness Web 视觉插件）

## 它是什么

[dsh-visual-plugin](https://github.com/jyh20030112/dsh-visual-plugin) 是针对 **DeepSeek Harness Web** 推出的一款零运行时依赖的 TypeScript 插件。图片走 DSH 自带附件通道，不单独配置视觉模型；右侧面板把当前模型对每张图的回答连同缩略图整理成可展开历史，一键复制。

## 为什么用它 / 适合什么场景

- 用 DeepSeek Harness Web 但希望在多轮图片对话里集中查看每张图的提问与回答；
- 不想为视觉能力额外配置视觉模型（多模态走 DSH 自己的附件通道即可）；
- 想要可展开 / 可复制的图片-回答历史，方便做笔记 / 复用；
- 偏好零运行时依赖的轻量插件（不需要 React / Vue 等大框架）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零运行时依赖 | 不强加 React / Vue，纯 TypeScript |
| 附件通道复用 | 图片走 DSH 自带附件通道，不额外配视觉模型 |
| 右侧面板 | 把每张图的回答 + 缩略图整理成可展开历史 |
| 一键复制 | 整段回答可一键复制到剪贴板 |

## 参考链接

- 项目链接：<https://github.com/jyh20030112/dsh-visual-plugin>
- 原始推文：<https://x.com/QingQ77/status/2095477154029211806>
- 媒体：<https://pbs.twimg.com/media/HRLp43haUAAHXaO.jpg>

## 相关概念

- [deepseek-harness](./tool-deepseek-harness-core.md) — DeepSeek 官方可插拔智能体框架
- [DeepSeek Harness Desktop](./tool-deepseek-harness-desktop.md) — 把官方 Web UI 打包成桌面应用
- [plugin-deepseek-vision](./tool-plugin-deepseek-vision.md) — DeepSeek 视觉相关插件
