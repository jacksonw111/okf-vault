---
type: Note
title: "ten-levels-of-jev（disler 出品的 Jev 集成示例库）"
description: "disler 把 Jev 这类「发一个 state、问几个带类型的问题、拿回带概率答案」的服务按十级三十个能跑的示例拆开，告诉工程师「该把它塞进哪一层」。是一份**架构级别的实战目录**。"
resource: "https://github.com/disler/ten-levels-of-jev"
tags: [jev, architecture, examples, decision-engine, integration-patterns]
timestamp: 2026-09-30T07:27:00Z
---

# ten-levels-of-jev

## 它是什么

**ten-levels-of-jev** 是 [disler](https://github.com/disler) 维护的示例仓库。它针对 Jev（见 [term-jev](./term-jev.md)）这类服务的工作流——"发一个 state，问几个带类型的问题，拿回带概率的答案"——用**十级、三十个**真实可跑的示例展示"该把决策层塞进系统的哪一层"。

工程师实际使用 Jev 时最常见的卡点不是「能不能调用」，而是「**该放到架构的哪一层**」——是放在客户端？后端服务？数据流水线？事件处理器？十级示例一个层级一个层级展示不同选择，附带可运行代码。

## 为什么用它 / 适合什么场景

- 想引入 Jev / 类似决策服务但不知道**在系统里放哪里**。
- 已经是 Jev 用户，想看看别人怎么把它用得更深。
- 想学一种"分层示例 + 可运行"的项目结构，作为自己写内部文档的模板。

## 关键能力

| 能力 | 说明 |
|------|------|
| 示例数 | 30 个可运行示例 |
| 组织维度 | 10 个架构层级 |
| 覆盖范围 | 客户端、后端服务、流水线、事件处理器等典型集成位置 |
| 形态 | GitHub 仓库（代码） |

## 参考链接

- 仓库：<https://github.com/disler/ten-levels-of-jev>

## 媒体

- ![](https://pbs.twimg.com/media/HTbX2ujbAAA5Ukn.jpg)

## 相关概念

- [Jev](./term-jev.md) — ten-levels-of-jev 的服务对象
- [Jev DSL 写法](./tool-docjev.md) — 同为 Jev 生态的产物，专注语法 / 文档