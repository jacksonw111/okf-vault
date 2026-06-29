---
type: Tool
title: "DeepSpec"
description: "DeepSeek 开源的投机解码端到端训练与评估框架，内置 Eagle3 / DFlash / DSpark 三种草稿模型，支持 Qwen3 / Gemma 目标模型。"
resource: "https://github.com/deepseek-ai/DeepSpec"
tags: "[llm, inference, speculative-decoding, deepseek, open-source]"
timestamp: "2026-06-29T16:00:00Z"
---

# DeepSpec

## 它是什么
DeepSpec 是 DeepSeek AI 开源的「投机解码（Speculative Decoding）」全栈实现框架，覆盖数据准备、草稿模型训练、评估的完整链路。内置 Eagle3、DFlash、DSpark 三种主流草稿模型实现，可对接 Qwen3 与 Gemma 系列作为目标模型。

## 为什么用它 / 适合什么场景
- **想给本地部署的大模型加推理加速**：投机解码在保留目标模型输出分布的前提下，用小模型先猜若干 token 再让大模型一次性 verify，吞吐通常能涨 2–4 倍。
- **想自己训练草稿模型**：DeepSpec 提供数据准备 + 训练 + 评估完整 pipeline，不用自己拼。
- **研究对比不同草稿策略**：同一框架内可以切换 Eagle3 / DFlash / DSpark 做消融。

## 关键能力
| 能力 | 说明 |
|------|------|
| 数据准备 | 把目标模型语料转成草稿训练样本 |
| 草稿模型训练 | Eagle3 / DFlash / DSpark 三套实现 |
| 评估 pipeline | 与目标模型对比吞吐 / 接受率 / 输出等价性 |
| 目标模型 | Qwen3 / Gemma 系列 |
| 端到端 | 数据 → 训练 → 评估一条龙 |

## 投机解码速览
- 草稿模型（小、快）先生成 K 个候选 token
- 目标模型（大、准）一次性并行 verify 这 K 个 token
- 接受率越高，加速比越大
- 输出分布与目标模型一致（无损）

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071576667563397322)
- [项目链接](https://github.com/deepseek-ai/DeepSpec)

## 相关概念
- [llmaker](./tool-llmaker.md) — Go CLI 一条命令拉起本地 LLM 应用栈，与 DeepSpec 组合可搭出「加速推理 + 本地部署」完整方案
- [DeepSeek MCP WebSearch](./tool-deepseek-mcp-websearch.md) — 同样基于 DeepSeek 生态的工具，但定位在联网搜索而非推理加速