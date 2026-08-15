---
type: "Tool"
title: "md-wechat（公众号 Markdown 排版工具）"
description: "公众号写 Markdown 最烦的一步是贴进后台样式全丢；md-wechat 左侧编辑、右侧预览公众号效果，一键复制富文本直接粘进后台，格式原样保留。"
tags: "[markdown, wechat, editor, formatter]"
timestamp: "2026-08-15T04:14:00Z"
resource: "https://github.com/laogou717/md-wechat"
---

# md-wechat（公众号 Markdown 排版工具）

## 它是什么

`laogou717/md-wechat` 是一个本地（或自托管）的 Markdown 编辑器，专门解决「在公众号后台写文章样式全丢」的问题。它采用**左侧编辑 / 右侧预览**的双栏布局，预写预览直接按公众号最终样式渲染，提供**一键复制为富文本**功能——把右侧内容复制到公众号编辑器里，标题、代码块、引用、列表全部保留样式。

> ![](https://pbs.twimg.com/media/HPpf2QQb0AAu81N.jpg)

## 为什么用它 / 适合什么场景

- **保留样式**：官方编辑器对 Markdown 几乎「什么都不认」，手动调整样式耗时。
- **所见即所得**：右侧预览就是最终呈现，避免反复「复制 → 粘贴 → 预览」。
- **本地优先**：不需要把内容上送到第三方平台。

## 关键能力

| 能力 | 说明 |
|------|------|
| 左右双栏 | 左侧 Markdown 源码，右侧公众号样式实时预览 |
| 多主题 | 切换不同的样式主题（默认 / 简洁 / 自定义） |
| 代码高亮 | 多种语言代码块着色，粘到后台不丢 |
| 一键复制富文本 | 把渲染结果转成微信编辑器可识别的 HTML 片段 |
| 图片支持 | 本地 / 在线图片均可嵌入 |
| 公众号兼容 | 输出符合公众号后台允许的标签集（无 `<script>` 等） |

## 与同类工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| md-wechat | 本地编辑器 + 一键复制富文本 | 开源、可自托管；适合长期写公众号 |
| [article-tools](tool-article-tools.md) | 纯前端 HTML 工具集（MD → 公众号只是其一） | 工具更杂，但没专门优化公众号样式 |

## 适用人群

- 公众号作者 / 运营 / 自媒体。
- 想把 Markdown 当成公众号原始格式、又不想每次手动调样式的人。
- 不想把内容托管到第三方排版平台的人。

## 参考链接

- [项目链接](https://github.com/laogou717/md-wechat)

## 相关概念

- [article-tools](tool-article-tools.md) — 纯前端 HTML 工具集（含 MD → 公众号）
- [local-ops](tool-local-ops.md) — 同一作者出品的 macOS 本地服务指挥台