---
type: Tool
title: ESLint
description: 最流行的 JS/TS 可插拔 lint 工具。本项目用 flat config（eslint.config.js，ESM），搭配 @typescript-eslint 插件做 Biome 不擅长的类型感知规则（行数/复杂度/魔术数字/非空断言等）。
resource: https://eslint.org/
tags: [tool, lint, typescript, code-quality]
timestamp: 2026-06-17T00:00:00Z
---

# ESLint

## 它是什么

[ESLint](https://eslint.org/) 是 JS/TS 生态里最主流的**可插拔静态分析工具**。通过规则插件（`@typescript-eslint` / `eslint-plugin-import` 等）扩展能力，配合配置文件（传统 `.eslintrc` 或新 flat config）启用规则。本项目用 **flat config（`eslint.config.js`，ESM）** + **`@typescript-eslint`** 提供类型感知 lint。

## 为什么用它 / 适合什么场景

- **类型感知规则**：`@typescript-eslint` 能利用 TS 类型信息判定规则（如 `prefer-readonly` / `consistent-return`），Biome 做不到
- **补位 Biome 不擅长的领域**：函数行数（`max-lines-per-function`）、圈复杂度（`complexity`）、魔术数字、参数/嵌套深度等
- **生态最广**：规则数量最多，碰到冷门问题几乎都有现成插件

## 关键能力

| 能力 | 说明 |
|------|------|
| Flat config | v9 起默认；本项目用 `eslint.config.js` + `export default [...]` |
| 动态加载插件 | flat config 顶层 `await import("@typescript-eslint/parser")` 异步加载（需要 `"type": "module"`） |
| 类型感知 | `parserOptions.project: ["./**/tsconfig.json"]` 启用 |
| 缓存 | `--cache` 加速；pre-commit 用 `--no-cache` 强制即时结果 |

## 本项目配置要点

本项目 ESLint **只针对 `**/*.ts` / `**/*.tsx`**，规则全部围绕类型感知 + 复杂度：

| 规则 | 级别 | 阈值 / 说明 |
|------|------|-------------|
| `@typescript-eslint/no-non-null-assertion` | error | 禁止 `!` |
| `@typescript-eslint/no-explicit-any` | error | 禁止 `any`（与 Biome 双重防御） |
| `@typescript-eslint/prefer-readonly` | warn | 建议 `readonly` |
| `max-lines-per-function` | error | 单函数 ≤ 50 行（不计空行/注释） |
| `complexity` | error | 圈复杂度 ≤ 10 |
| `no-magic-numbers` | warn | 忽略 -1/0/1、数组下标、默认值、枚举 |
| `max-params` | warn | ≤ 4 |
| `max-depth` | warn | ≤ 4 |
| `no-console` | warn | 提示 `console` |
| `consistent-return` | error | 返回值一致 |

完整源码参见 [`playbook-monorepo-code-quality-setup`](./playbook-monorepo-code-quality-setup.md) 与 `inbox/_done/` 中归档的原始资料。

## 相关概念

- [Biome](./tool-biome.md) —— 主力 lint/格式化引擎，ESLint 是补位
- [Ultracite](./tool-ultracite.md) —— Biome 预设
- [Lefthook](./tool-lefthook.md) —— 在 pre-commit 触发 ESLint
- [Monorepo 代码质量体系搭建](./playbook-monorepo-code-quality-setup.md) —— 完整使用场景
