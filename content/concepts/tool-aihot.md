---
type: "Tool"
title: "AIHOT（AI 热点聚合与日报网站框架）"
description: "KKKKhazix 出品的开源热点聚合框架：每天从 6 种信源（RSS / 网页列表 / JSON / X 账号 / 公众号 / 自定义脚本）抓资料，由 LLM 预筛 + 独立打分两次，过门槛才入选，多源聚成同一事件并按独立来源数排序，每天 08:00 出日报。"
resource: "https://github.com/KKKKhazix/AIHOT"
tags: "[news-aggregator, ai, llm-filtering, daily-digest, multi-source, dedup, opensource]"
timestamp: "2026-10-02T00:35:00Z"
---

# AIHOT（AI 热点聚合与日报网站框架）

## 它是什么

[AIHOT](https://github.com/KKKKhazix/AIHOT) 是 KKKKhazix 出品的**开源热点聚合与日报框架**——把 aihot.news 的整套代码用 TypeScript 重写并完整开源。每天：

1. 从 6 种信源**抓资料**：RSS / 网页列表 / JSON 接口 / X 账号 / 微信公众号 / 自定义脚本
2. **LLM 预筛**——把所有原始资料丢给 LLM，先过一遍「值不值得写摘要」
3. **独立打分两次**——对入选条目由 LLM 独立评两次热度，过门槛才发布
4. **聚合成事件**——把同一事件的多个报道合并为一个 entry，按「独立来源数」排序热度
5. **每天 08:00 出日报**——附周报、月报自动生成

## 为什么用它 / 适合什么场景

| 场景 | AIHOT 的好处 |
|------|--------------|
| 行业监控 | 一份代码，每天出一份自己行业的 AI 摘要日报 |
| 内容运营 | 给公众号 / 知乎 / newsletter 持续供稿 |
| 投资研究 | 把关注行业的多个来源聚成事件 |
| 不写代码也能用 | 改改信源清单和精选 prompt 即可上线 |

## 6 种信源

| 信源 | 用途 |
|------|------|
| RSS | 传统博客、新闻站 |
| 网页列表 | 无 RSS 的网页（爬列表页） |
| JSON 接口 | 内部 API |
| X 账号 | 关注的 Twitter/X 列表 |
| 微信公众号 | 通过公众号爬虫或代理 |
| 自定义脚本 | 任意你想接入的信源 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源 | 6 种信源统一接入 |
| LLM 预筛 | 省下游 token，先把没价值的过滤掉 |
| 独立打分两次 | 减少单次打分偏差 |
| 事件聚合 | 多报道合并为一个事件 |
| 热度排序 | 按独立来源数排 |
| 周期输出 | 日 / 周 / 月报自动出 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105818546093596792>
- 项目链接：<https://github.com/KKKKhazix/AIHOT>

## 相关概念

- [RAG](./term-rag.md) — 检索增强生成，AIHOT 是把 LLM 用在「信源过滤」环节
- [Harness Engineering](./term-harness-engineering.md) — 大伞概念，AIHOT 是「给 LLM 接信源」的具体实例
