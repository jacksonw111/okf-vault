---
type: "Tool"
title: "Astra-Ares（Codex 动态推理档位切换）"
description: "Codex 一旦开跑推理档位就钉死，读个文件也用最高强度烧 token——Astra-Ares 让 Jev 在 Codex 每次生成前重新挑档位，按子任务强度动态切到合适的模型。"
resource: "https://github.com/miuuyy/Astra-Ares"
tags: "[codex, agent, model-routing, cost, token, jev, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Astra-Ares（Codex 动态推理档位切换）

## 它是什么

[Astra-Ares](https://github.com/miuuyy/Astra-Ares) 是一个 Codex 适配器：Codex 默认一旦开跑推理档位就钉死不动，读个文件也用最高强度烧 token——Astra-Ares 在每次生成前重新挑档位，让「读文件」「跑工具」「写代码」分别用合适的强度。

## 它解决的问题

- Codex 默认推理档位是「最贵」，但很多步骤（读文件、调工具、解析结果）不需要这个强度
- 想按子任务强度动态路由模型，降低 token 成本
- 想在不动 Codex 主循环的前提下，引入动态档位切换

## 实现思路

| 元素 | 说明 |
|------|------|
| 路由模型 | 用 Jev（轻量判定模型）在每次生成前选档位 |
| Codex 适配 | 不动 Codex 主循环，只在「生成前」介入 |
| 档位粒度 | 按「读 / 跑工具 / 写」等子任务强度切档 |

## 适用场景

- Codex 重度用户，token 账单压力大
- 想把「动态档位」加进现有 Codex 工作流
- 想实验「轻量判定模型 + 重生成模型」组合的性价比

## 原始链接
- 项目主页：<https://github.com/miuuyy/Astra-Ares>

## 相关概念
- [jev-browser-use](./tool-jev-browser-use.md) — 同类「把便宜模型塞进 Codex」思路（点击交给便宜模型）
- [jevgpt](./tool-jevgpt.md) — 把判定模型当生成模型用