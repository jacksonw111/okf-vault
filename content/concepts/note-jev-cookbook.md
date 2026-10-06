---
type: "Note"
title: "jev-cookbook（SimpleJev 中文教程）"
description: "datawhalechina 开源：给 SimpleJev 的 System One 判断模型 Jev 配一份中文教程，教开发者用 Choice / Score / Noul 三种原语把结构化概率输出接进代码，而不是解析模型生成的文本。"
resource: "https://github.com/datawhalechina/jev-cookbook"
tags: "[tutorial, chinese, jev, decision-model, typesafe]"
timestamp: "2026-10-06T00:35:00Z"
---

# jev-cookbook

## 它是什么

[jev-cookbook](https://github.com/datawhalechina/jev-cookbook) 是 **datawhalechina** 开源的 SimpleJev 中文教程——为 SimpleJev 的 System One 判断模型 **Jev** 补一份可跟做的中文资料。

## 三大原语

| 原语 | 作用 |
|------|------|
| **Choice** | 从有限候选项里选一个（带概率） |
| **Score** | 给一个候选项打 0-1 分 |
| **Noul** | 「无法判断」显式表达，转交或拒答 |

## 核心思想

- **不要解析模型生成的文本**——直接消费结构化概率输出
- 用上述三种原语把 Jev 接进业务代码（路由、守门、判别）
- 中文文档让国内开发者可以零英文门槛上手

## 适合人群

- 想给业务接入「可校准概率 + 拒答能力」的小型决策模型
- 不愿意让 LLM 自由发挥的稳定分类 / 决策场景
- 偏好中文技术教程的学习者

## 参考链接

- 项目链接：<https://github.com/datawhalechina/jev-cookbook>

## 相关概念

- [JevAny](./tool-jevany.md) — 同生态工具链
- [onejev](./tool-onejev.md) — SimpleJev 的多模态决策框架
- [datawhalechina](./term-datawhale-china.md) — 中文 AI 开源教程出品方