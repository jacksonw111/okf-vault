---
type: "Tool"
title: "北辰 Pi / Beichen Pi（Windows 本地模型极简 Agent 桌面）"
description: "面向本地部署模型的 Windows 极简 Agent 桌面平台：让本地模型安静地把活干完，同时把上下文剩余量、Token 消耗结构都摆在明面上。"
resource: "https://github.com/opopile/beichen-pi-desktop"
tags: [windows, desktop, local-model, agent, observability, token]
timestamp: "2026-08-31T16:00:00Z"
---

# 北辰 Pi / Beichen Pi

## 它是什么

[Beichen Pi](https://github.com/opopile/beichen-pi-desktop) 是 [opopile](https://github.com/opopile) 出品的 **Windows 极简 Agent 桌面平台**，专门面向**本地部署模型**（如 Ollama / LM Studio 等）。

「让本地模型安静地把活干完」是核心设计哲学——

- 极简界面：不抢注意力，模型在背后跑；
- **可观测性**：上下文还剩多少、Token 花在哪都摆在明面上；
- 桌面优先：Windows 原生体验，不必迁就浏览器 / Web UI。

## 为什么用它 / 适合什么场景

- **本地模型重度用户**：用 Ollama 跑 70B+ 模型时想看实时剩余 context；
- **不希望被 UI 噪音打扰**：极简主义审美；
- **Windows-only 桌面党**：不打算装 WSL / Mac。

## 关键能力

| 能力 | 说明 |
|------|------|
| 极简 UI | 把屏幕还给工作，不抢注意力 |
| 本地模型优先 | 与 Ollama / LM Studio 集成 |
| 上下文仪表 | 实时显示剩余 context 窗口 |
| Token 消耗可视化 | 看清花在哪（系统 / 工具 / 用户） |
| Windows 原生 | 桌面应用，无浏览器依赖 |

## 相关概念

- [Ollama](tool-ollama.md) — 主流本地模型运行时

## 参考链接

- 项目链接：<https://github.com/opopile/beichen-pi-desktop>