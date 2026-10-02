---
type: "Tool"
title: "Bencho（bencho.dev 基准对比工具）"
description: "在线对比不同模型、框架、硬件配置的跑分与延迟：填两份配置（比如 CPU vs GPU、不同 LLM、不同数据库），就能看到跑同一份 benchmark 的对比数据，适合选型决策。"
resource: "https://bencho.dev"
tags: "[benchmark, comparison, llm, hardware, performance, dev-tools]"
timestamp: "2026-10-02T06:00:00Z"
---

# Bencho（bencho.dev 基准对比工具）

## 它是什么

[Bencho](https://bencho.dev) 是一个**在线基准对比工具**：填两份配置（不同模型、不同框架、不同硬件、不同数据库等），就能在网页上看到它们跑同一份 benchmark 时的耗时、吞吐、内存、延迟等关键指标的横向对比。

## 为什么用它 / 适合什么场景

- **选型**——「A 卡 vs B 卡」「Llama 3 70B vs Qwen 72B」「Postgres vs ClickHouse」，Bencho 帮你跑分对比，省下自建 benchmark 的时间。
- **汇报**——给团队 / 客户做技术选型汇报时，直接拿 Bencho 的对比截图做证据。
- **预估成本**——结合吞吐数据换算每月调用成本。

## 典型对比维度

| 类别 | 可对比的轴 |
|------|-----------|
| 模型 | Llama / Qwen / Mistral / GPT / Claude |
| 推理框架 | vLLM / llama.cpp / TGI / SGLang / Ollama |
| 硬件 | Apple Silicon / NVIDIA H100 / AMD MI300 / CPU |
| 数据库 | Postgres / ClickHouse / DuckDB / SQLite |
| Web 框架 | Next.js / Remix / Astro / SolidStart |
| 浏览器引擎 | Chromium / Firefox / Safari |
| UI 交互集合 | **Bencho Finds**：单独收集网上疯狂的 UI 交互（按钮、表单、卡片等的奇异玩法）供设计 / 前端借鉴 |

## 使用方式

1. 进入 <https://bencho.dev>，挑选一个 benchmark（已收录不少）
2. 选两份配置，比如「Llama 3 70B on 2×H100」 vs 「Qwen 72B on 2×MI300」
3. 点 Run，看耗时 + 内存 + 吞吐对比
4. 把结果导出为图 / 表贴进 wiki / 报告

## 参考链接

- 原始链接：<https://x.com/scottymatt/status/2105641577469374661>
- 项目链接：<https://bencho.dev>

## 相关概念

- [OmniStudio](./tool-omnistudio.md) — 本地大模型桌面工作台，可把 Bencho 结果配套做实测
- [vLLM](#) — 高吞吐推理引擎，本仓库目前未收录
