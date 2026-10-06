---
type: "Tool"
title: "Codex Attachment Manager（Codex 图片附件勾选器）"
description: "chipfighter 出品的 Codex 插件——Codex 每次请求都重发任务历史里的全部图片，长图像任务请求膨胀到几十 MB 后连接反复失败；这个插件让你**逐轮勾选哪些图片继续发给模型**，把请求体压回可控范围。"
resource: "https://github.com/chipfighter/codex-attachment-manager"
tags: "[codex, attachment, image, plugin, ai-coding-agent]"
timestamp: "2026-10-06T22:51:00Z"
---

# Codex Attachment Manager（Codex 图片附件勾选器）

## 它是什么

**Codex Attachment Manager** 是 chipfighter 出品的 Codex 插件——针对 Codex **每次请求都重发任务历史里全部图片**的问题，让你**逐轮勾选哪些图片继续发给模型**，把请求体压回可控范围。

## 为什么用它 / 适合什么场景

- **图像任务省 token**：只发当轮相关的图片，不把旧图片全塞请求
- **请求体减肥**：避免请求膨胀到几十 MB 后连接反复失败
- **人工控制**：敏感图片（个人照片 / 截图里带 token）不外发
- **Codex 友好**：作为 Codex 插件直接加载

## 关键能力

| 能力 | 说明 |
|------|------|
| 逐轮勾选 | 上一轮历史图片单独勾选 |
| 请求体瘦身 | 只勾选的图片进新请求 |
| 上下文保持 | 不勾选的图片仍留在上下文视图里供参考 |
| 图片预览 | 在勾选界面预览 |
| 开源 | 可改默认行为 |

## 参考链接

- 项目链接：<https://github.com/chipfighter/codex-attachment-manager>

## 相关概念

- [Codex](./term-codex.md) — 主要宿主
- [Claude Code](./term-claude-code.md) — 也有类似附件管理需求
