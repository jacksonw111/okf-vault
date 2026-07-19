---
type: Tool
title: "Yace"
description: "不到 2KB（gzip）的浏览器代码编辑器组件，用透明 textarea 叠高亮 pre 的思路，在不引入 Monaco、CodeMirror 等大体量库的情况下实现语法高亮和扩展编辑。"
resource: "https://github.com/petersolopov/yace"
tags: "[browser-editor, code-editor, lightweight, syntax-highlight, zero-deps]"
timestamp: "2026-07-19T13:57:30Z"
---

# Yace

## 它是什么

petersolopov/yace 是一个**不到 2KB（gzip）的浏览器代码编辑器组件**：用「透明 textarea + 高亮 pre」叠层思路实现语法高亮与编辑，**不引入 Monaco / CodeMirror 等大体量库**。适合对包体积敏感、希望给网页或文档站加一个轻量代码编辑框的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| < 2KB gzip | 极小体积，几乎不影响页面加载 |
| 零依赖 | 无外部运行时，浏览器原生 textarea + pre 叠层 |
| 语法高亮 | 通过自定义 token 规则实现高亮 |
| 可扩展 | 自定义语言、快捷键、Tab 行为 |

## 适合谁

- 文档站 / 博客 / 在线教程需要嵌入代码编辑框的开发者
- 对包体积敏感的前端项目（landing page、嵌入式小工具）
- 想做「轻量代码片段编辑器」但不想引入 CodeMirror 的产品

## 与已有代码编辑器组件的差别

- [codemark](./tool-codemark.md) — Rust 写的代码书签工具（命令行侧定位）
- [arlan-vault](./tool-arlan-vault.md) — 炫酷前端 / AI 效果合集（含编辑器演示）
- Yace 的差异点：**唯一聚焦「< 2KB 浏览器内可编辑代码块」**，与 Monaco / CodeMirror 完全不在一个量级

## 媒体预览

![](https://pbs.twimg.com/media/HNlNqcHbcAArBZd.jpg)

## 相关概念

- [codemark](./tool-codemark.md) — Rust 写的代码书签工具
- [lengyi-markdown-editor](./tool-lengyi-markdown-editor.md) — 纯前端单 HTML Markdown 编辑器

## 参考链接

- 项目链接: <https://github.com/petersolopov/yace>