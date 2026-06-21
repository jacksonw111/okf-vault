---
type: "Tool"
title: "LaTeX→MathML 编译器（7.69 KB 的网页公式渲染器）"
description: "编译阶段把 LaTeX 数学公式转成浏览器原生 MathML，前端无需再加载 KaTeX / MathJax。核心包 7.69 KB（gzip 3.56 KB），零第三方依赖，30 万次/秒处理速度，比 KaTeX 快 3 倍、比 MathJax 快 40 倍以上。"
resource: "https://t.co/nnQn7lTAsV"
tags: "[latex, mathml, markdown, build-time, compiler, katex-alternative]"
timestamp: "2026-06-21T16:02:00Z"
---

# LaTeX→MathML 编译器（7.69 KB 的网页公式渲染器）

## 它是什么

一个**编译期**就把 LaTeX 数学公式转成浏览器原生 `MathML` 的轻量编译器。**前端运行时不再需要拉 KaTeX、MathJax 这类动辄几百 KB 的公式库**，浏览器自己就能渲染。代价是：编译时多做一步，输出静态页面。

## 为什么用它 / 适合什么场景

- 文档站 / 博客 / 静态站点希望首屏快、bundle 小，又不舍弃数学公式。
- 内容里 90% 的公式形态有限（行内 + 简单行间），用不着 KaTeX 全套。
- 服务端 / 构建机资源充足，可以承担一次额外的预处理。

## 关键能力

| 能力 | 说明 |
|------|------|
| 体积 | 核心包 7.69 KB（gzip 3.56 KB） |
| 依赖 | 零第三方库 |
| 速度 | 30 万次/秒以上 |
| 与 KaTeX 对比 | 快约 3× |
| 与 MathJax 对比 | 快约 40× 以上 |
| 输出格式 | 浏览器原生 `MathML` —— 不再需要公式渲染 JS 库 |

## 适用边界

- 构建管线必须能跑这一步（CI / 本地构建脚本增加一个 transform）。
- 极少数公式用了 MathML 表达不了的宏，需要事先确认覆盖范围。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLJdQ83aMAAI8OJ.jpg)

## 相关概念

- [MD→Slides](tool-markdown-slides.md) — 同为「Markdown 内嵌富内容（公式 / Mermaid / 代码）」的同款思路
- [Niamos](tool-niamos.md) — 同为「Obsidian + Dataview + Claude Code」组合下的轻量化模板