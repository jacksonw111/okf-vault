---
type: "Tool"
title: "JevAny（有限选项决策的开源工具链）"
description: "SimpleJev 开源：从有限候选项里挑一个这种活，JevAny 把数据 / 训练 / 评测包成一套开源工具链；接口收下状态 / 问题 / 候选项，吐出选中的那项 + 各项概率，置信度不够时调用方可转人工。"
resource: "https://github.com/SimpleJev/JevAny"
tags: "[decision-model, classification, jev, mvp, open-source]"
timestamp: "2026-10-06T00:35:00Z"
---

# JevAny

## 它是什么

[JevAny](https://github.com/SimpleJev/JevAny) 是 **SimpleJev** 开源的**决策工具链**——把「从有限候选项里挑一个」这件事的**数据 / 训练 / 评测**全套打包；接口收下**状态 / 问题 / 候选项**，吐出**选中的那项 + 各项概率**，置信度不够时调用方还能转人工。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | 状态 / 问题 / 候选项 |
| 输出 | 选中的项 + 各项概率 |
| 不确定转交 | 置信度不足时返回可触发人工的信号 |
| 全流程 | 数据准备 / 模型训练 / 评测一站式 |
| 与 Jev 同源 | 适配 SimpleJev 的 System One 决策模型 |

## 适合场景

- 业务里有大量「多选一」决策（路由、分类、守门、判别）
- 想自己训练专属决策模型而不是调外部 LLM
- 想要「模型没把握就交给人」的明确边界

## 参考链接

- 项目链接：<https://github.com/SimpleJev/JevAny>

## 相关概念

- [Jev 决策模型](./tool-onejev.md) — 同生态的决策小模型
- [jev-cookbook](./note-jev-cookbook.md) — 中文教程