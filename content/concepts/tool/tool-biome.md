---
type: Tool
title: "Biome"
description: "用 Rust 写成的「一体化 Web 工具链」——格式化、Lint、import 整理一把抓；性能远超 ESLint+Prettier 组合，是本 monorepo 主力格式化与 lint 引擎（@biomejs/biome）。"
resource: "https://biomejs.dev/"
tags: "[tool, lint, formatter, rust, code-quality]"
timestamp: 2026-06-17T00:00:00Z
---

# Biome

## 它是什么

[Biome](https://biomejs.dev/) 是一个用 Rust 编写的「一体化 Web 工具链」，目标是把 **Prettier（格式化） + ESLint（lint） + import 整理器** 合并成一个单一、极速、零配置的二进制。`@biomejs/biome` 即其 npm 包名。

## 为什么用它 / 适合什么场景

- **速度**：原生 Rust 实现，单文件/全仓库 lint 比 ESLint+Prettier 快一个数量级，适合 monorepo 大规模代码
- **零配置**：开箱即用，自带合理的格式化与 lint 规则；也可被 Ultracite 等预设覆盖
- **二合一**：一份 `biome.json` 同时管 formatter 和 linter，避免两套工具互相对抗
- **类型不感知**：与 ESLint 的核心差别——Biome 不做类型检查，因此类型相关 lint 需要 ESLint 补位

## 关键能力

| 能力 | 说明 |
|------|------|
| Formatter | tab/空格、引号风格、import 排序等，本项目用 `tab` 缩进 + 双引号 + `organizeImports: on` |
| Linter | 规则分 `correctness` / `style` / `suspicious` / `complexity` / `performance` 等组；`recommended: true` 启用全部推荐规则 |
| Import 整理 | 自动按规则排序、合并、删除未用 import |
| Tailwind 排序 | `useSortedClasses` nursery 规则，可识别 `clsx` / `cva` / `cn` |
| 多语言 | JS/TS/JSX/TSX/JSON/JSONC/CSS 等 |

## 本项目配置要点

参考 [`playbook-monorepo-code-quality-setup`](../playbook/playbook-monorepo-code-quality-setup.md) 第 2 节。核心：

- 缩进用 **tab**、JS/TS 字符串 **双引号**
- `extends: ["ultracite/biome/core", "ultracite/biome/react"]` 继承 Ultracite 严格预设
- `noExplicitAny: error` + `**/*.ts(x)` override 再次强制

## 相关概念

- [Ultracite](tool-ultracite.md) —— Biome 的零配置预设封装
- [ESLint](tool-eslint.md) —— 补位 Biome 不擅长的类型感知 lint
- [Monorepo 代码质量体系搭建](../playbook/playbook-monorepo-code-quality-setup.md) —— 完整使用场景
