---
type: Tool
title: "wechat-style-extractor"
description: "Next.js 写的微信公众号样式提取工具，输入公众号文章链接，自动扒下字体 / 颜色 / 行高 / 版式，并清理 HTML、样式拉平、缺省值兜底。"
resource: "https://github.com/sennkuwu/wechat-style-extractor"
tags: "[wechat, mp, scraper, nextjs, css, typography]"
timestamp: "2026-09-07T13:06:00Z"
---

# wechat-style-extractor

## 它是什么
一个 Next.js 写的工具，专门抓取微信公众号文章链接并提取其版式：字体（family/size/weight）、颜色、行高、段落间距等。抓取限定只走微信文章域名，顺手把 HTML 洗干净、样式拉平；识别不出来的字段不显示，预览先套默认值。

## 工作流
1. 用户粘贴公众号文章链接
2. 服务端拉取 HTML，仅允许 `*.qq.com` / 微信文章域名
3. 解析 inline style 与外联样式表，抽取版式属性
4. 清理脚本标签、广告块等干扰内容
5. 在预览面板还原排版

## 关键能力
| 能力 | 说明 |
|------|------|
| 域白名单 | 只允许抓公众号文章，防止滥用 |
| HTML 清洗 | 移除干扰脚本与样式 |
| 样式拉平 | 把外联样式展平成 inline 便于复用 |
| 缺省兜底 | 解析不出的字段用默认值填充预览 |
| Next.js 全栈 | 前后端一套搞定 |

## 适用场景
- 内容迁移：把公众号排版复用到独立博客 / Newsletter
- 设计参考：研究公众号文章的版式系统
- 批量复刻：抽取多篇文章的视觉风格做模板

## 参考
- 项目链接：<https://github.com/sennkuwu/wechat-style-extractor>

## 相关概念
- [gzh-design-skill](tool-gzh-design-skill.md) — 反向的 Markdown → 公众号内联样式转换器
- [Article Format](tool-article-format.md) — 一句话把自媒体文案转公众号 / 头条排版