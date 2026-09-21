---
type: "Tool"
title: "LocalJev（githubnext：本地版 Jev 决策模型）"
description: "GitHubNext 出的本地版 Jev：底层用 omlx 推理，覆盖 diffusiongemma、Qwen MoE、Gemma 4 MoE、Gemma 4 e4b/e2b 等多种模型，本地服务对外暴露 Jev API wrapper 标准接口。"
resource: "https://github.com/githubnext/localjev"
tags: "[local-llm, jev, githubnext, omlx, decision-model]"
timestamp: "2026-09-21T22:00:00Z"
---

# LocalJev（githubnext）

## 它是什么

[githubnext/localjev](https://github.com/githubnext/localjev) 是 **GitHubNext** 出的本地版 **Jev 决策模型**——底层用 **omlx** 做推理，对外暴露与 TypeSafe Jev **同款 API wrapper 接口**。

## 解决的问题

GitHubNext 团队提到「**Not everyone on the team has access to Jev yet**」——TypeSafe Jev 还没全团队开放，于是花了一个早上在 **omlx** 上「土法炮制」一个穷人版 Jev。

## 评测过的模型

- diffusiongemma
- Qwen MoE
- Gemma 4 MoE
- Gemma 4 e4b / e2b

评测报告放在仓库里。

## 性能参考

- 在 **m5 max 64 GB** 上速度不错。
- LocalJev server 暴露的 API 与官方 Jev wrapper libraries 兼容。

## 为什么用它 / 适合什么场景

- 想**本地拥有 Jev 类决策能力**且**不愿意花 TypeSafe 商业 API 的钱**。
- 想**评测不同模型**在 Jev 类任务上的表现。
- 已经有基于 Jev wrapper 的代码，**改个 endpoint**就能切到本地。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地推理 | omlx 后端 |
| 多模型覆盖 | diffusiongemma / Qwen / Gemma 4 MoE / e4b / e2b |
| Jev API 兼容 | 改 endpoint 即可 |
| 含评测报告 | 仓库自带 benchmark |

## 项目链接

- 仓库：<https://github.com/githubnext/localjev>

## 相关概念

- [Laya（编码器式决策引擎）](./tool-laya-decision-engine.md) — 同样是不生成文本的判断引擎
- [kev（Qwen 底座本地决策模型）](./tool-kev-decision-model.md) — 另一类 Jev 复刻
- [laya-mlx](./tool-laya-mlx.md) — 把 Laya 搬上 Apple Silicon 的 MLX 实现
