---
type: "Tool"
title: "gzh-design-skill（Markdown → 微信公众号排版 HTML）"
description: "把 Markdown 一键转换为样式全内联、可直接粘贴进微信公众号编辑器且不掉格式的精致 HTML，解决 Markdown 写完公众号还要手工排版的痛点。"
resource: "https://github.com/isjiamu/gzh-design-skill"
tags: "[wechat, markdown, html, formatter, publishing, gzh]"
timestamp: "2026-07-08T03:25:00Z"
---

# gzh-design-skill

## 它是什么

[gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) 是一个**Markdown → 微信公众号 HTML 排版转换工具**。

公众号编辑器对 Markdown 支持很弱：标题、代码块、引用基本都要手工排版。从 Markdown 写完到「能贴进公众号」往往隔一道工序——这就是 gzh-design-skill 要干的事：

- 输入：Markdown 源文
- 输出：**样式全内联、可直接粘贴进公众号编辑器** 的精致 HTML
- 关键点：粘贴后**不掉格式**（行内样式 + 公众号白名单标签策略）

## 为什么需要它

- 公众号编辑器本身不支持 Markdown，手工排版耗时。
- 微信编辑器对 `<style>` / `<script>` / `<link>` 等外部样式「不友好」，必须把所有样式**内联**到每个元素上才能完整生效。
- 代码块、引用、列表等元素在公众号里样式易丢失。

## 关键能力

| 能力 | 说明 |
|------|------|
| Markdown → HTML | 完整解析标题、段落、列表、代码、引用、图片 |
| 全内联样式 | 所有 CSS 内联到元素属性，适配微信编辑器 |
| 粘贴不掉格式 | 直接复制粘贴到公众号后台即可见精致排版 |
| 公众号风格模板 | 提供多种排版风格（简约 / 文艺 / 技术风 等） |
| 命令行友好 | 可脚本化集成进写作流水线 |

## 媒体

![gzh-design-skill 排版效果](https://pbs.twimg.com/media/HMrMxaCbgAAyZC1.jpg)

## 参考链接

- [项目仓库](https://github.com/isjiamu/gzh-design-skill)

## 相关概念

- [Article Tools](./tool-article-tools.md) — 同为「写作 / 文章处理」工具集，但侧重更广
- [Markdown Desktop Browser](./tool-markdown-desktop-browser.md) — 同为 Markdown 相关工具，偏阅读 / 预览