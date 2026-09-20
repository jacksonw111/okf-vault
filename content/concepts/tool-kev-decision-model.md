---
type: "Tool"
title: "kev（Qwen 底座本地决策模型，复刻 Jev）"
description: "jaredpalmer/kev：在 Qwen 底座（0.5B–8B）上加 LoRA + 指针读出头，复刻 Archer Hume 对 TypeSafe Jev 的逆向分析；一次前向传播里对同一份文档问好几遍拿到概率，Mac 上可服务、H100 上可重训；接口照抄 TypeSafe System One，官方 typesafe-sdk 改 base_url 即可接本地。"
resource: "https://github.com/jaredpalmer/kev"
tags: "[qwen, jev, decision-model, lora, local-llm, open-source]"
timestamp: "2026-09-20T18:00:00Z"
---

# kev

## 它是什么

[jaredpalmer/kev](https://github.com/jaredpalmer/kev) 想在本地跑一个 **Jev 那样的决策模型**：

- 一次前向传播里对**同一份文档问好几遍**拿到概率，而不是让模型写字。
- 在 **Qwen 底座**（0.5B 到 8B）上加 **LoRA + 指针读出头**。
- 架构是 **Archer Hume 对 Jev 逆向分析**的复刻。
- 接口照抄 **TypeSafe System One**——官方 `typesafe-sdk` 改个 `base_url` 就能切到本地服务。

## 部署形态

| 场景 | 怎么做 |
|------|--------|
| 本机服务 | Mac 上直接起服务，typesafe-sdk 改 `base_url` 接 |
| 重训 | H100 / 多卡重新训 LoRA 与读出头 |

## 为什么用它 / 适合什么场景

- 想**本地拥有 Jev 类决策能力**，不依赖 TypeSafe 商业 API。
- 想要「**对同一份文档一次前向问多次**」的能力——概率而不是文字。
- 已经在用 typesafe-sdk，**改一行 `base_url` 即可切换**到本地部署。

## 关键能力

| 能力 | 说明 |
|------|------|
| 底座 | Qwen 0.5B / 1.5B / 8B 等多档 |
| 微调 | LoRA + 指针读出头 |
| 一次前向多次问 | 对同一文档问多问，拿到概率 |
| Mac 可服务 | 本地起服务做推理 |
| H100 可重训 | 在大算力上重新训 |
| 协议兼容 | typesafe-sdk 改 `base_url` 即接 |

## 项目链接

- 仓库：<https://github.com/jaredpalmer/kev>

## 媒体

![](https://pbs.twimg.com/media/HSn0f8baAAAxuI-.png)

## 相关概念

- [Laya](./tool-laya-decision-engine.md) — 同为编码器式决策引擎
- [SemIf](./tool-semif.md) — 同为本地小模型做 if 决策
- [Jevbridge](./tool-jevbridge.md) — 同为「给 LLM 挂类型化决策层」的另一类实现
