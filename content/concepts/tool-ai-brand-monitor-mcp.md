---
type: Tool
title: "ai-brand-monitor-mcp"
description: "面向 AI 代理的品牌可见性监测 MCP：30 秒 OAuth 配置，一键检测品牌在 Perplexity / ChatGPT / Claude / Gemini 四大平台的提及率、位置、情感与竞品共现。"
resource: "https://github.com/khadinakbarlabs/ai-brand-monitor-mcp"
tags: "[mcp, brand-monitoring, ai-agent, seo, marketing]"
timestamp: "2026-06-29T16:00:00Z"
---

# ai-brand-monitor-mcp

## 它是什么
ai-brand-monitor-mcp 是一个面向 AI 编码 / 办公代理的品牌可见性监测 MCP（Model Context Protocol）服务器。它把 Claude / Cursor / Codex / Windsurf 这类代理接上「一键检测品牌在 Perplexity / ChatGPT / Claude / Gemini 的提及率、出现位置、引用来源、情感倾向、竞品共现」的能力，结果直接嵌入代理工作流。

## 为什么用它 / 适合什么场景
- **做 GEO（生成式引擎优化）**：想知道品牌在四个主流 AI 答案里被提到几次、出现在第几位、被怎么描述。
- **营销 / PR 想听竞品动态**：让代理每天跑一遍审计，看竞品提及变化趋势。
- **代理工作流内置**：不用打开新标签页看结果，代理在对话里直接拿到结构化数据。

## 关键能力
| 能力 | 说明 |
|------|------|
| OAuth 云服务接入 | 30 秒配置，免自托管 |
| npm 自托管 | 数据不出本地 |
| 四大 AI 平台 | Perplexity / ChatGPT / Claude / Gemini |
| 提及率 | 品牌在答案里被提到的频率 |
| 位置 | 出现在答案的第几位 |
| 引用 | 答案引用了哪些来源 |
| 情感 | 提及的情感倾向 |
| 竞品共现 | 同一答案里出现的竞品 |
| MCP 协议 | 标准协议接入各类代理 |

## 成本参考
- 单次审计（24 次检测）约 $1.92
- Apify 免费额度约 60 次检测

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071582959170412594)
- [项目链接](https://github.com/khadinakbarlabs/ai-brand-monitor-mcp)

## 相关概念
- [Proxide](./tool-proxide.md) — 让任意 Agent 经 MCP / 浏览器接 ChatGPT Pro 网页强模型，与 ai-brand-monitor-mcp 共享 MCP 接入思路
- [CodexPro](./tool-codexpro.md) — ChatGPT Web ↔ 本地仓库 MCP 桥，同属 MCP 生态工具