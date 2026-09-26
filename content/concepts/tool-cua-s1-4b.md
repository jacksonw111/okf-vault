---
type: "Tool"
title: "Cua-S1-4B-0.2（开源 4B 多模态电脑操作模型）"
description: "cua-ai 开源的 4B 多模态电脑操作模型：通过屏幕画面 + 任务目标直接执行电脑操作，在真实系统环境中用任务完成奖励做强化学习训练，不依赖软件底层无障碍结构；在 168 项 GUI 基准上任务完成率 92.9%（基线 60.1%）。"
resource: "https://huggingface.co/cua-ai/cua-s1-4b-0.2"
tags: "[cua, computer-use, multimodal, gui-agent, reinforcement-learning, 4b, open-source, huggingface]"
timestamp: "2026-09-26T21:55:00Z"
---

# Cua-S1-4B-0.2（开源 4B 多模态电脑操作模型）

## 它是什么

[Cua-S1-4B-0.2](https://huggingface.co/cua-ai/cua-s1-4b-0.2) 是 [cua-ai](https://huggingface.co/cua-ai) 出品的 **4B 参数多模态电脑操作模型**——专门通过**识别屏幕画面 + 任务目标**来直接执行电脑操作（点屏幕、键鼠交互）。

## 训练方法

- 在**真实系统环境**中用**任务完成奖励**做**强化学习**训练
- **不依赖**软件底层的无障碍结构（accessibility tree）——纯视觉路线

## 性能（168 项 GUI 基准）

| 模型 | 任务完成率 |
|------|------|
| Cua-S1-4B-0.2 | **92.9%** |
| 未训练基线 | 60.1% |

> 性能差距 32.8 个百分点——证明「**视觉 + RL**」路线在 CUA 上的可行性远超传统依赖结构化信息的方案。

## 为什么用它 / 适合什么场景

- 想在**纯视觉路线**下做电脑操作 Agent（不依赖系统无障碍 / DOM）。
- 模型仅 4B，**单卡 RTX 3090/4090 就能跑**，适合本地化部署。
- 想给 [CUA-Lite](./tool-cua-lite.md) 这种框架接入一个**轻量 RL 微调过的**电脑操作模型。
- 研究「**RL + 视觉**」路线在 GUI Agent 上的有效性。

## 关键能力

| 能力 | 说明 |
|------|------|
| 参数量 | 4B |
| 输入 | 屏幕画面 + 任务目标 |
| 输出 | 键鼠动作序列 |
| 训练范式 | RL + 任务完成奖励 |
| 信息源 | 纯视觉（不读 a11y tree / DOM） |
| 性能 | GUI 基准 92.9% 任务完成率 |

## 相关概念

- [CUA-Lite](./tool-cua-lite.md) — 同一生态下的轻量电脑操作 Agent 框架（沙箱 + 数据 + 多模型接入）
- [Computer Use（计算机使用）](./term-computer-use.md) — 让 AI 直接读屏 + 模拟键鼠操作图形界面
- [Browser Use Pi](./tool-browser-use-pi.md) — Browser-Use 团队的轻量 TypeScript Web Agent