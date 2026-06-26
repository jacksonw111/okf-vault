---
type: Tool
title: "Serenade（Nuxt 4 动静两栖博客系统）"
description: "基于 Nuxt 4 的博客/知识库系统，内容全部 Markdown 文件管理：既可静态导出丢到任何托管，也能跑 Node 服务提供 SSR / 搜索 / RSS 等动态功能，含文章 / 专栏 / 标签 / 友链 / 项目展示 / KaTeX / 暗黑模式，可接 OpenAI 自动生成 URL 与封面图。"
resource: "https://github.com/xurensting/serenade"
tags: [nuxt, blog, knowledge-base, markdown, ssr, static-site, katex]
timestamp: 2026-06-26T16:50:00Z
---

# Serenade（Nuxt 4 动静两栖博客）

## 它是什么

Serenade 是一个**基于 Nuxt 4 的博客 / 知识库系统**。它的关键特性是**同一套 Markdown 内容既能静态导出（随便丢到任何静态托管），也能跑 Node 服务提供 SSR、搜索、RSS 等动态能力**。

- 内容载体：全部 Markdown 文件
- 数据库：不需要
- 输出形态：
  - **静态导出**：丢到任意静态托管（GitHub Pages、Cloudflare Pages、Vercel 等）
  - **Node SSR**：自带搜索、RSS、暗黑模式、友链朋友圈等动态功能
- 内置模块：文章、专栏、标签、全文搜索、友链朋友圈、项目展示
- 排版：KaTeX 公式、暗黑模式
- 自动化：可接 OpenAI 自动生成 URL slug 与封面图
- 部署：Docker 镜像一键部署

## 为什么用它

| 需求 | Serenade 解法 |
|------|--------------|
| 想要静态站，又想后期加搜索 / RSS | 同一份内容，无痛切换 |
| 内容是 Markdown，不想要数据库 | 文件即数据 |
| 学术 / 技术博客要写公式 | 内置 KaTeX |
| 想要个友情链接圈 / 项目展示页 | 内置模块 |
| 不想手动起名 / 选封面 | 接 OpenAI 自动生成 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 动静两栖 | 同份内容，静态 / SSR 自由切换 |
| 文件即数据 | 全部 Markdown，零数据库 |
| Nuxt 4 | 当前 Nuxt 主版本，享受最新 SSR / SSG 优化 |
| KaTeX | 数学公式排版 |
| 暗黑模式 | 内置 |
| AI 命名 | 可选 OpenAI 自动 slug + 封面图 |
| Docker 一键 | 部署不用解释 |

## 原始链接

- [项目仓库](https://github.com/xurensting/serenade)
- [原始推文剪藏](https://x.com/QingQ77/status/2070345303887380715)

## 相关概念

- [Astro 7](./tool-astro-7.md) — 同样"内容驱动"的 Web 框架，Serenade 是"博客特化"形态
- [MD→Slides](./tool-markdown-slides.md) — 同一思路"Markdown → 多端呈现"，但方向是幻灯片
- [OKF 是什么](./term-okf.md) — Serenade 的"文件即数据"哲学与 OKF 一脉相承（路径即身份、内容即知识）
