---
type: Tool
title: "pi-smart-web-search"
description: "Pi Coding Agent 的扩展，给智能体加一个 web_search 工具，能一次接收多个查询批量检索网页并抽取内容，让模型自己挑选要深入打开的链接。"
resource: "https://github.com/joematthews/pi-smart-web-search"
tags: "[pi, web-search, agent-extension, batch-search, multi-query]"
timestamp: "2026-07-19T02:34:00Z"
---

# pi-smart-web-search

## 它是什么

joematthews/pi-smart-web-search 是一个 [Pi Coding Agent](./tool-pi-hive.md) 的扩展，给智能体加一个 `web_search` 工具。与传统的「一次搜一个 query」的 web_search 实现不同，它**接收多个查询并批量检索**，把抽取到的内容一次性交给模型，让模型自己判断哪些链接值得深入打开。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多查询批量 | `web_search(queries: ["q1","q2",...])` 单次工具调用覆盖多个问题 |
| 内容抽取 | 拿到结果摘要，不只给 URL |
| 模型自主筛选 | 把候选链接交给 LLM，让它决定下一步深读哪些 |
| Pi 原生集成 | 作为 Pi 的扩展加载，复用 Pi 已有扩展点 |

## 适合什么场景

- **研究类任务**：需要并行查多个角度的问题，再收敛
- **事实核查 / 综述写作**：让 Agent 自己决定哪条信息更值得展开
- **Agent 自主决策链**：减少「一次搜一次问」的串行延迟

## 媒体预览

![](https://pbs.twimg.com/media/HNUpsdWawAALTRm.jpg)

## 相关概念

- [pi-task-delegation](./tool-pi-task-delegation.md) — Pi 的子任务委派扩展
- [pi-fusion](./tool-pi-fusion.md) — Pi 多模型并行扇出 + 汇总
- [pi-exa](./tool-pi-exa.md) — Pi Agent 的 Exa 扩展包
- [pi-hive](./tool-pi-hive.md) — Pi 多智能体团队协作
- [anysearch-skill](./tool-anysearch-skill.md) — 统一实时搜索 Skill

## 参考链接

- 项目链接: <https://github.com/joematthews/pi-smart-web-search>