---
type: "Tool"
title: "geo-seo-claude（面向 AI 搜索的 GEO/SEO 审计工具）"
description: "用并行自动化代理审计网站在 ChatGPT、Claude、Perplexity、Google AI Overviews 中的「可被引用」分数，校验 schema markup、检查品牌权威度，给出可执行的优化建议。"
resource: "https://github.com/zubair-trabzada/geo-seo-claude"
tags: [seo, geo, ai-search, citation, schema-markup, automation, agent]
timestamp: "2026-08-30T21:50:00Z"
---

# geo-seo-claude

## 它是什么
[zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) 是一个面向「**AI 搜索 / 答案引擎优化**」(Generative Engine Optimization, GEO) 的开源审计工具，专门检查网站在 **ChatGPT、Claude、Perplexity、Google AI Overviews** 这类「带回答的搜索引擎」里能不能被引用、引用得对不对。

核心做法：

- 用**并行自动化代理**对每个目标平台分别做引用测试；
- 审计 **citation score**（被引用的频率与位次）、**schema markup**（结构化数据是否齐 / 是否准确）、**brand authority**（品牌权威信号）；
- 把分散在不同 AI 答案里的「引用证据」汇总成一张可执行清单。

## 为什么用它 / 适合什么场景
- 做 **GEO / Answer Engine Optimization**——内容站、品牌站、SaaS 落地页想让 ChatGPT / Perplexity 主动引用；
- 传统 SEO（关键词 + 外链）已稳，想**新增「AI 搜索引用」这一条战线**；
- 做品牌监控：想看自家网站在 AI 答案里出现时被怎么描述、有没有错引；
- 校验结构化数据：在 AI 时代 `JSON-LD` 不只服务 Google Rich Snippet，也直接喂给 LLM。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多平台并行代理 | 同时对 ChatGPT / Claude / Perplexity / Google AI Overviews 跑引用测试 |
| 引用分数审计 | 量化「被引用的频率 + 上下文相关度」 |
| Schema 校验 | 校验 `JSON-LD` / `Microdata` 等结构化数据是否齐、对、可用 |
| 品牌权威信号 | 评估品牌方在 AI 答案里被正面提及的强度 |
| 可执行建议 | 给出具体的修复项（缺哪类 schema、内容怎么改） |

## 媒体
- ![](https://pbs.twimg.com/media/HQ57SZXWQAAlmvE.jpg)

## 相关概念
- [Vercel Streamdown v260](tool-vercel-streamdown-v260.md) — 流式 Markdown 渲染：让 AI 输出的内容在前端可读 / 可索引；与 geo-seo-claude 同在「让内容被 AI 看见」范畴

## 参考链接
- 项目链接：<https://github.com/zubair-trabzada/geo-seo-claude>
