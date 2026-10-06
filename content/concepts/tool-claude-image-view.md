---
type: "Tool"
title: "claude-image-view（Claude Code 粘贴图片缩略图）"
description: "jarrodwatts 出品的 Claude Code 插件：解决粘贴图片后输入框只显示 [Image #1] 标签的问题，在输入框上方画出图片缩略图，可视化确认粘贴正确。"
resource: "https://github.com/jarrodwatts/claude-image-view"
tags: "[claude-code, plugin, image, ux, editor]"
timestamp: "2026-10-06T00:35:00Z"
---

# claude-image-view

## 它是什么

[claude-image-view](https://github.com/jarrodwatts/claude-image-view) 是 **jarrodwatts** 出品的 Claude Code 插件——解决粘贴图片后**输入框只显示 `[Image #1]` 标签**看不到图的问题，在输入框上方画出缩略图。

## 痛点场景

把截图、设计稿、错误画面粘贴进 Claude Code：

- **传统**：输入框里只有 `[Image #1]` / `[Image #2]` 标签，**看不到原图**
- **风险**：可能贴错 / 顺序错 / 漏贴，等模型回复错了才发现
- **解决**：输入框上方实时画缩略图，肉眼确认

## 关键能力

| 能力 | 说明 |
|------|------|
| 缩略图渲染 | 在输入框上方画出每张已粘贴图片 |
| 多图支持 | 多张图依次排列，方便对顺序 |
| 轻量 | 仅作为可视化插件，不改 Claude Code 行为 |
| 开源 | 仓库在 GitHub |

## 适合场景

- Claude Code 高频用户，每天粘几十张截图
- 设计 / 前端 / 调试场景对「贴对图」敏感
- 想给 Claude Code 加一点点「所见即所得」感

## 参考链接

- 项目链接：<https://github.com/jarrodwatts/claude-image-view>

## 相关概念

- [Claude Code](./term-claude-code.md) — 插件宿主
- [Agent Skills](./term-agent-skills.md) — 同为 Claude Code 的扩展机制