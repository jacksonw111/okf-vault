---
type: Tool
title: "NeoSearch（去广告去追踪的 AI 搜索引擎）"
description: "传统搜索广告多、追踪重、结果被 SEO 污染。NeoSearch 是 C# 写的开源 AI 搜索引擎（.NET 9 + Vue Petite），不带广告和追踪，搜索时同时调 Google API 和 LLM，结果通过 SSE 实时推，AI 模块做三件事：改写标题描述、按信息源质量重排序、按视角分组。"
resource: "https://github.com/bartjellema/NeoSearch"
tags: [search-engine, ai, privacy, csharp, dotnet, sse, no-ads]
timestamp: "2026-07-30T10:59:00.000Z"
---

# NeoSearch

## 它是什么

**去广告 / 去追踪的 AI 增强搜索引擎**——传统搜索的两个痛点：

1. 广告多 + 追踪重
2. SEO 污染严重，要点一堆链接才能拼出全貌

NeoSearch 的做法：

- **后端**：C# / .NET 9 + Vue Petite
- **搜索时**：同时调 Google API（拿原始数据）+ LLM（拿整理）
- **流式**：SSE 一条条往外推，页面实时更新
- **AI 模块三件事**：
  - 改写杂乱的标题和描述（清理 SEO 话术）
  - 按信息源质量重新排序（可信源加权）
  - 按视角分组（同一话题多个立场并列）

## 关键能力

| 能力 | 说明 |
|------|------|
| 去广告 / 去追踪 | 干净结果页 |
| AI 增强摘要 | LLM 整理搜索结果 |
| 多视角分组 | 同一话题多个立场 |
| SSE 流式 | 实时更新，无需等 |
| 源质量排序 | 可信源加权 |
| 自托管 | 数据私有 |

## 适合谁

- 受够 Google ads / SEO spam 的用户
- 研究类工作（同一话题多视角对比）
- 重视隐私 / 想自托管搜索的个人 / 团队
- 想搭内部 AI 搜索的企业

## 原始链接

- [项目仓库](https://github.com/bartjellema/NeoSearch)
- [推文剪藏](https://x.com/QingQ77/status/2082783009065894237)

## 相关概念

- [Xerj](./tool-xerj.md) — Rust 从头实现的统一 AI 搜索引擎，全文 + 向量 + Agent 记忆
- [anysearch-skill](./tool-anysearch-skill.md) — 给 AI agent 用的统一实时搜索 Skill
- [browser-search](./tool-browser-search-agent.md) — SearXNG + Camofox + CloakBrowser 自托管搜索栈