---
type: "Tool"
title: "build-plan（文档一键转 HTML 页）"
description: "yulonghe97/build-plan，把技术方案 / Build Plan 这类文档丢进去，一键生成带侧边栏导航 + 编号章节 + 内联 SVG 图表 + 多语言切换的可直接打开 HTML 页，不需要任何构建步骤。"
resource: "https://github.com/yulonghe97/build-plan"
tags: "[docs, html, generator, svg, build-plan, multi-language]"
timestamp: "2026-07-23T13:45:00Z"
---

# build-plan（文档一键转 HTML 页）

## 它是什么

[`yulonghe97/build-plan`](https://github.com/yulonghe97/build-plan) 是把**技术方案 / Build Plan 文档一键转成可打开 HTML 页**的工具，输出成品自带：

- 侧边栏导航
- 编号章节
- 内联 SVG 图表
- 多语言切换
- 零构建步骤（扔进 .md，直接出 .html）

## 关键能力

| 能力 | 说明 |
|------|------|
| 文档转 HTML | 把 .md / 长文档一键转 HTML |
| 侧边栏导航 | 自动生成左侧目录 |
| 编号章节 | 按文档结构编号 |
| 内联 SVG | 图表自动嵌入（不依赖外部图片） |
| 多语言 | 同一文档可切语言 |
| 零构建 | 没有 webpack / vite / build step |

## 为什么用它

- **避免构建依赖**：不需要 Node.js / 构建工具链
- **离线可用**：输出单 HTML 后不需要服务端
- **跨工具可移植**：和 GitHub README 一样只要浏览器
- **可分享**：发一个 .html 链接就能分发

## 适用场景

- 产品 / 工程团队分享 Build Plan
- 个人 / 公司内部技术方案归档
- 客户交付的技术说明
- 想让文档像「SaaS 文档站」一样体面但又不依赖 SaaS

## 媒体

![](https://pbs.twimg.com/media/HN4VnBTbAAAnjT1.jpg)

## 相关概念

- [Bento](./tool-bento-slides.md) — 同为「单 HTML 演示工具」，但侧重幻灯片
- [Arlan Vault](./tool-arlan-vault.md) — 前端 / AI 效果合集，每个效果附 Markdown 提示词让 Agent 直拷还原
- [GitHub README SVG Slides](./note-github-readme-svg-slides.md) — 让 Agent 把 README 当纵向演示文稿设计

## 原始链接

- [项目仓库](https://github.com/yulonghe97/build-plan)