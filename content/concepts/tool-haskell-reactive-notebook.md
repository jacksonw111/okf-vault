---
type: "Tool"
title: "Haskell 交互式反应式笔记本"
description: "用普通 Markdown 写文件 + 嵌入 Haskell 代码块即可跑，无需手动管理单元格执行顺序。借助 GHC 自家解析器分析代码依赖，改一处自动重算依赖它的格子；重复定义、循环引用也会显式报错 —— 让 Haskell 开发者像用 Jupyter 一样边写边看结果。"
resource: "https://t.co/aRDTheoVMd"
tags: "[haskell, jupyter, notebook, reactive, ghc, literate-programming]"
timestamp: "2026-06-21T16:03:00Z"
---

# Haskell 交互式反应式笔记本

## 它是什么

一个 Haskell 专属的**交互式 + 反应式**笔记本：你写一份普通 Markdown，在里面嵌 Haskell 代码块就能跑。它用 GHC 自己的解析器分析代码块的依赖关系，改一个格子会自动重算所有依赖它的格子，遇到重复定义、循环引用会显式报错。**不用你管「单元格谁先谁后」**。

## 为什么用它 / 适合什么场景

- 教学 / 教程场景：边讲 Haskell 概念边跑结果，像 Jupyter 一样可重现。
- 数据探索 / 库调研：快速搭原型、迭代，依赖自动追踪。
- 想要「literate programming」风格（Markdown 叙述 + 可执行代码），又不想装 Jupyter + Haskell kernel 这条崎岖路。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入格式 | 普通 Markdown 文件 + 嵌入 Haskell 代码块 |
| 执行顺序 | 不需要手动指定 —— 工具按代码依赖关系决定 |
| 反应式 | 改一格自动重算依赖它的格子 |
| 依赖分析 | 用 GHC 自家解析器，看得懂完整 Haskell 语法 |
| 错误检测 | 重复定义、循环引用显式报错，不会让 notebook 静默卡住 |

## 与传统 Jupyter 的差异

- 不用管理 cell 顺序 / 全局状态。
- 错误是「代码语义级」的（GHC 看懂的），而不是「运行时 crash」。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLK4IxgaoAA2d1A.jpg)

## 相关概念

- [LaTeX→MathML 编译器](tool-latex-mathml-compiler.md) — 同为「Markdown 内嵌富内容、用构建期处理换运行时简单」的思路