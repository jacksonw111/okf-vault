---
type: "Tool"
title: "fallow（fallow-rs：TS/JS 静态分析工具）"
description: "TypeScript / JavaScript 静态分析工具：未使用代码、循环依赖、重复代码、复杂度、架构边界违反等多种检查。"
resource: "https://github.com/fallow-rs/fallow"
tags: "[static-analysis, typescript, javascript, code-quality, dead-code]"
timestamp: "2026-09-21T22:00:00Z"
---

# fallow

## 它是什么

[fallow-rs/fallow](https://github.com/fallow-rs/fallow) 是 **TypeScript / JavaScript 静态分析工具**——用 Rust 实现，单二进制，集成多种检查维度。

## 检查维度

| 检查 | 用途 |
|------|------|
| 未使用代码 | dead code / unused export |
| 循环依赖 | 模块 import cycle |
| 重复代码 | 相似 / 重复实现 |
| 复杂度 | 圈复杂度、嵌套深度 |
| 架构边界 | 模块分层、依赖方向 |

## 为什么用它 / 适合什么场景

- 维护**中大型 TypeScript / JavaScript monorepo**——死代码 / 循环依赖不靠人肉找。
- 想**统一项目代码质量门**——把多种检查合到一个工具。
- 想要 **Rust 实现的单二进制**——快、可放进 CI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多维度检查 | 一份工具覆盖 5 类常见问题 |
| Rust 实现 | 性能 + 单二进制分发 |
| TS/JS 通用 | 不分 TS 还是 JS |
| 架构边界 | 不只查单文件，也能查模块关系 |

## 项目链接

- 仓库：<https://github.com/fallow-rs/fallow>

## 相关概念

- [Biome](./tool-biome.md) — 同样面向 TS/JS 的 Rust 工具链，但侧重 lint + formatter
- [Ultracite](./tool-ultracite.md) — 同为「一处配置、整套代码质量门」的方案
