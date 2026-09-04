---
type: Tool
title: "local-llmup（本地模型可跑性评估与运行 CLI）"
description: "TypeScript 写的本地模型命令行工具，附终端交互界面与浏览器工作台；不联网扫描一遍硬件，对 66 个内置模型逐个打分，标出能跑 / 勉强跑 / 跑不动，并给出每秒 token 估算。"
resource: "https://github.com/shashankswe2020-ux/local-llmup"
tags: [local-llm, cli, typescript, hardware, benchmark, offline]
timestamp: 2026-09-04T12:00:00Z
---

# local-llmup（本地模型可跑性评估与运行 CLI）

## 它是什么

一个跑本地模型的命令行工具（TypeScript 实现），顺带提供终端交互界面和浏览器工作台。核心动作是：**不联网扫一遍你的硬件**，对内置的 66 个模型逐个打分。

![](https://pbs.twimg.com/media/HRRaOKkaYAApbax.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 硬件扫描 | 本地完成，不联网 |
| 模型评分 | 66 个内置模型逐个评估 |
| 三档结论 | 能跑 / 勉强跑 / 跑不动，直接标出 |
| 性能估算 | 附带每秒生成多少 token 的估算 |
| 交互形态 | CLI + 终端交互界面 + 浏览器工作台 |

## 为什么用它 / 适合什么场景

- 换机器或加显卡前，想先知道哪些模型真能落到这台机器上。
- 不想凭显存数字硬猜，希望有一份按本机实际配置给出的可跑清单。

## 参考链接

- 项目链接：<https://github.com/shashankswe2020-ux/local-llmup>
- 原始链接：<https://x.com/QingQ77/status/2095882075127636447>

## 相关概念

- [本地大模型硬件选型指南](./note-local-llm-hardware-guide.md) — 回答同一个问题「这台机器能跑什么模型」；指南给人读的经验法则，local-llmup 给机器跑的自动评估
