---
type: "Tool"
title: "Clarify"
description: "面向 MDX + OpenAPI 的开源文档发布工具，TypeScript 写的本地优先 CLI；输入 MDX 内容、OpenAPI 规范与 TypeScript 配置，输出自带全文搜索、国际化与 AI 可读 llms.txt 的静态站点。"
tags: "[docs, mdx, openapi, static-site, typescript, llm]"
timestamp: "2026-06-28T02:05:00Z"
resource: "https://github.com/taicode-labs/clarify"
---

# Clarify

## 它是什么

Clarify 是一个**开源的文档发布工具**，专为 **MDX + OpenAPI** 工作流设计。TypeScript 写就，采用本地优先 CLI 模式，把三类输入（MDX 文档、OpenAPI 规范、TypeScript 配置）拼装成一个静态站点。

典型用法：API 团队把规范文档 + 教程 + 营销文案都丢进同一个仓库，`clarify build` 一键产出可部署的官网。

## 关键能力

| 能力 | 说明 |
|------|------|
| MDX 支持 | 文档中可直接嵌入 React 组件 |
| OpenAPI 渲染 | 解析规范自动生成 API 参考页 |
| 本地优先 CLI | 无需起服务，本地构建后部署到任意 CDN |
| 全文搜索 | 内置静态索引 |
| 国际化 | 多语言内容原语支持 |
| AI 可读 llms.txt | 自带生成 `/llms.txt`，方便 LLM 一次性消费全部文档 |
| 可定制 React 渲染器 | 不喜欢默认样式时换组件即可 |

## 与同类对比

相比 Docusaurus / Nextra 等「大型文档框架」，Clarify 走**窄而精**路线：默认假设你的文档站由 API 规范驱动，OpenAPI 是一等公民，MDX 是补充而非主体。

## 界面预览

![Clarify 文档站](https://pbs.twimg.com/media/HL3KIM-bEAAQx52.jpg)

## 参考链接

- [项目仓库](https://github.com/taicode-labs/clarify)
- [原始链接](https://x.com/QingQ77/status/2071052211920986414)

## 相关概念

- [Astro 7](tool-astro-7.md) — 内容驱动 Web 框架，Clarify 可视为其上的文档站变体
- [Serenade（Nuxt 4 博客）](tool-serenade-nuxt4.md) — 同样基于 Markdown 的内容站点方案
- [Markdown→Slides](tool-markdown-slides.md) — Markdown 驱动幻灯片，思路同源