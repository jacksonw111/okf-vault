---
type: Tool
title: "ax"
description: "给 AI 用的命令行抓取工具：把\"拉网页 → 摸清结构 → 抽出结构化数据\"这套 agent 天天在做的动作，合成一条本地、确定性、还省 token 的命令。"
tags: "[cli, scraper, ai-agent, web-scraping, deterministic, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/yusukebe/ax"
---

# ax

一个**给 AI 用的命令行网页抓取工具**——把"**拉网页 → 摸清结构 → 抽出结构化数据**"这套 agent 几乎天天要做的动作，**压成一条本地、确定性、还省 token 的命令**。

## 它是什么

- 一条 CLI 命令（`ax`），用最少步骤完成"**fetch + parse + extract**"；
- 设计目标不是"给人用的浏览器替代品"，而是"**让 agent 少花 token 把网页抓下来**"——比让模型自己用 `curl` + `grep` 推理省得多。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地执行 | 不依赖云端抓取服务 |
| 确定性 | 同样输入 → 同样输出，agent 可重放 |
| 省 token | 不必把 HTML 全塞进模型上下文 |
| AI 友好 | 输出结构化数据（JSON / Markdown / 自定义 schema） |

## 为什么用它 / 适合什么场景

- agent 任务里大量出现"**抓这个网页的 X 字段**"——这条命令直接出结构化结果；
- 想把网页抓取**纳入工作流**而不是临时起一个 Python 脚本；
- 受够了让模型用 `curl` 抓网页后塞回上下文分析——慢、贵、不稳。

## 设计哲学

1. **local first** — 不把数据给第三方。
2. **deterministic** — agent 重跑同一条命令得到相同结果。
3. **token-aware** — 减少大段 HTML 进入 LLM 上下文的成本。

## 相关概念

- [QuickAI Claude Cost](tool-quickai-claude-cost.md) — 同为"AI 工具的 token 成本意识"实践
- [AI Humanizer Handbook](tool-ai-humanizer-handbook.md) — 同样强调"AI 工作流中确定性输出"的设计思路
