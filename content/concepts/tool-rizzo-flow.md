---
type: "Tool"
title: "Rizzo Flow（本地 Jev 替代）"
description: "Jev 是托管闭源服务，本地想拿到同一套「状态进、带概率的决策出」的接口只能自己搭——Rizzo Flow 用开源权重 + llama.cpp 补齐本地推理，改 base URL 就能对接 localhost。"
resource: "https://github.com/Rizzo-AI-Academy/rizzo-flow"
tags: "[jev, local-inference, llama-cpp, decision-model, open-weights, open-source]"
timestamp: "2026-09-23T22:35:00Z"
---

# Rizzo Flow（本地 Jev 替代）

## 它是什么

[Rizzo Flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) 是一个**本地化 Jev 替代方案**：

> Jev 是托管闭源服务，本地想拿到同一套「状态进、带概率的决策出」的接口只能自己搭，Rizzo Flow 用开源权重加 llama.cpp 把这层补上，代码里改个 base URL 就能对着 localhost 跑。

## 为什么用它 / 适合什么场景

- 想使用 Jev 类决策模型但**不能把数据发到云端**（合规 / 离线 / 隐私）。
- 想用**开源权重 + 本地推理**取代托管服务，避免 vendor lock-in。
- 已有代码调 Jev HTTP 接口，想**只改 base URL** 切换成本地实现。

## 已知边界（仓库自述）

- **概率默认没校准**：开源权重的概率输出需要自行校准。
- **缺证据时自信答错**：36 例里 6 例在缺证据场景自信地答错。
- **选项数受限**：每题只给 26 个选项，而 Jev 是 255。
- **性能**：作者 Windows + RTX 5060 Ti 跑出 49ms / 决策，换硬件表现差异未知。

## 关键能力

| 能力 | 说明 |
|------|------|
| 协议兼容 | 与 Jev 同样 HTTP 接口形状 |
| 推理后端 | llama.cpp 本地推理 |
| 权重 | 开源（仓库自发布） |
| 接入 | 改 base URL 即可对接现有 Jev 调用代码 |
| 部署 | 完全本地，无云依赖 |

## 与同类方案的差异

| 方案 | 部署 | 协议 |
|------|------|------|
| Jev | 托管 API | HTTP |
| Rizzo Flow | 本地 llama.cpp | 兼容 Jev HTTP |
| laya-mlx | 本地 MLX | Apple Silicon 优化 |

## 项目链接
- 项目主页：<https://github.com/Rizzo-AI-Academy/rizzo-flow>

## 媒体
![Rizzo Flow 截图](https://pbs.twimg.com/media/HSyhV6fbwAAxRsQ.jpg)
