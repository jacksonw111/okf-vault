---
type: Tool
title: "Article Format（公众号 / 头条 一键排版）"
description: "LiuZheng60 开源的工具，把自媒体文案用一句话指令转成微信公众号（内联 CSS）与今日头条（语义 HTML）排版，直接复制粘贴即可发布。"
resource: "https://github.com/LiuZheng60/article-format"
tags: "[wechat, toutiao, formatting, self-media, chinese]"
timestamp: "2026-07-11T20:00:00Z"
---

# Article Format（公众号 / 头条 一键排版）

## 它是什么

`LiuZheng60/article-format` 是一个**自媒体文案一键排版工具**：把 Markdown / 纯文本输入，按目标平台规则转成可直接粘贴发布的 HTML：

- **微信公众号**：内联 CSS（公众号编辑器对 `<style>` 不友好，必须内联）。
- **今日头条**：语义 HTML（头条对样式支持不同，需要结构化标签）。

## 为什么用它 / 适合什么场景

- 自媒体作者每次手动调字号 / 间距 / 缩进浪费时间。
- 一份稿子要同时发公众号 + 头条 + 知乎，不想分别排版。
- 想让排版风格稳定，不会每次发都漂移。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多平台 | 公众号（内联 CSS）+ 头条（语义 HTML） |
| 一句话指令 | 输入 → 目标格式 HTML |
| 可粘贴 | 输出可直接复制到对应编辑器 |
| 开源 | 规则透明，可定制 |

## 相关概念

- [GZH Design Skill](tool-gzh-design-skill.md) — 同样面向公众号的 Markdown → 编辑器内联 HTML 转换
- [Article Tools](tool-article-tools.md) — 纯前端 HTML 工具集（封面 / 二维码 / 公众号富文本）
- [Markdown Slides](tool-markdown-slides.md) — Markdown 转幻灯片

## 项目链接

- 项目仓库：<https://github.com/LiuZheng60/article-format>