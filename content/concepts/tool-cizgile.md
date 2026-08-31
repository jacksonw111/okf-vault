---
type: "Tool"
title: "Cizgile（零依赖 URL slug 引擎）"
description: "纯 TypeScript 写的 URL slug 工具库：RFC 3986/3987 规范、7 种文字转写（拉丁化）、Unicode slug、IRI ↔ URI、percent-encoding，零依赖、跨运行时。"
resource: "https://github.com/productdevbook/cizgile"
tags: [typescript, slug, url, i18n, transliteration, library]
timestamp: "2026-08-31T16:00:00Z"
---

# Cizgile

## 它是什么

[Cizgile](https://github.com/productdevbook/cizgile) 是 [productdevbook](https://github.com/productdevbook) 维护的**零依赖 URL slug 引擎**，纯 TypeScript 编写。

核心覆盖：

- **RFC 3986 / 3987 规范** —— URL 与 IRI 的标准 slug 行为
- **7 种文字的转写**（拉丁化）—— CJK / 西里尔 / 阿拉伯等都能转成拉丁字母
- **Unicode slug** —— 保留非 ASCII 字符的可读 slug
- **IRI ↔ URI 双向转换** —— 国际域名 / 路径编码
- **percent-encoding** —— 安全的 URL 编码

零依赖（无 lodash / 无 node-fetch）、可在任何 JS 运行时跑。

## 为什么用它 / 适合什么场景

- **博客 / 文档系统**生成 slug：中文标题想生成 URL 友好的路径；
- **多语言站点**：希望保留 Unicode 字形而非粗暴拼音化，可切换「转写 vs 保留」模式；
- **跨运行时**：服务端（Node）、Edge worker、浏览器打包都能用；
- **替代 slugify**：原生包功能覆盖更广，无第三方依赖。

## 关键能力

| 能力 | 说明 |
|------|------|
| RFC 3986/3987 | 标准 slug 行为 |
| 7 种文字转写 | 中文 / 西里尔 / 阿拉伯 / 希腊 / 希伯来 / 日文 / 韩文 |
| Unicode slug | 保留原文可读字符 |
| IRI ↔ URI | 国际域名双向转换 |
| percent-encoding | URL 安全编码 |
| 零依赖 | 单包无任何外部依赖 |

## 媒体

- 项目截图：![](https://pbs.twimg.com/media/HRCP1qHWAAAbq_e.jpg)

## 相关概念

（暂无关联项目可链。）

## 参考链接

- 项目链接：<https://github.com/productdevbook/cizgile>