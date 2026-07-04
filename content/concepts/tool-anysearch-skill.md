---
type: Tool
title: "anysearch-skill"
description: "anysearch-ai/anysearch-skill — 给 AI agent 用的统一实时搜索 Skill,把多家搜索引擎结果聚合归并,一次调用拿到综合排序后的引用列表。"
resource: "https://github.com/anysearch-ai/anysearch-skill"
tags: [anysearch, skill, search, ai, mcp]
timestamp: "2026-07-04T15:00:00Z"
---

# anysearch-skill

## 它是什么

`anysearch-ai/anysearch-skill` 是一个统一的「实时搜索」Skill,目标是让 AI 编码 agent(Claude Code、Codex 等)用**一条命令**就能同时调用多家搜索引擎,把结果聚合并重排序,得到一份对当前问题最有用的引用清单。

项目链接：<https://github.com/anysearch-ai/anysearch-skill>

## 为什么用它 / 适合什么场景

- **单一接口对应多引擎**:agent 不用集成各家 SDK,也不用记哪个 provider 限流怎么扣。
- **实时**:不是预训练语料,是当下拉取 / 排序后的搜索结果。
- **可验证**:agent 在回答前会拿到 N 条候选引用,可以挑最相关的几条展开。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多搜索引擎聚合 | 一条调用同时跑 N 家(具体名单见仓库) |
| 结果去重与重排序 | 同一网页多次出现合并 + 按相关性输出 |
| Skill 协议 | 按 Agent Skills 规范打包,可被 Claude Code / Codex 直接识别 |
| 开源 | 仓库可审阅,可自部署 |

## 与 Agent Skills 生态的对接

按照仓库的 SKILL.md 描述,装到 `.claude/skills/` 或 `~/.codex/skills/` 后,agent 在处理需要「新信息」的问题时会自动调用。也支持 MCP 模式挂载。

## 相关概念

- [Agent-Reach](tool-agent-reach.md) — 同样面向 AI agent,主打「直接上 Twitter/Reddit/YouTube/GitHub」这种**指定站点**抓取
- [browser-search](tool-browser-search-agent.md) — SearXNG + Camofox + CloakBrowser 自托管搜索栈
- [DeepSeek MCP WebSearch](tool-deepseek-mcp-websearch.md) — 基于 DeepSeek API 的 MCP 联网搜索
- [Agent Skills(代理技能包)](term-agent-skills.md) — Skill 规范本身
- [anysearch-skill 仓库](https://github.com/anysearch-ai/anysearch-skill) — 项目链接
