---
type: Tool
title: "Ultracite"
description: "Biome 的零配置严格预设，把社区最佳实践（lint 规则 + 格式化选项）打包成「一行 `extends` 即可获得」——`ultracite/biome/core` + `ultracite/biome/react`。"
resource: "https://www.ultracite.dev/"
tags: "[tool, biome, preset, lint, code-quality]"
timestamp: 2026-06-17T00:00:00Z
---

# Ultracite

## 它是什么

[Ultracite](https://www.ultracite.dev/) 是 [Biome](tool-biome.md) 之上的**零配置严格预设**——把社区共识的 lint 规则和格式化选项预先写好，让项目只需要 `extends: ["ultracite/biome/core", "ultracite/biome/react"]` 就获得一套完整的最佳实践配置。

## 为什么用它 / 适合什么场景

- **零配置起步**：不用从零选 lint 规则——覆盖默认（性能/安全/风格）已经写好
- **可叠加自定义**：Ultracite 在 `biome.json` 里是 `extends`，项目自己的 `linter.rules` 在它之上**进一步加严**
- **生态分核**：分 `core`（JS/TS 通用）和 `react`（React 生态）两个预设，按需引入

## 关键能力

| 能力 | 说明 |
|------|------|
| `ultracite/biome/core` | 核心 JS/TS 严格规则（noAny、noFloatingPromises 等） |
| `ultracite/biome/react` | React 生态补充规则（hooks 依赖完整性、key 等） |
| `ultracite check` | 只读检查命令 |
| `ultracite fix` | 自动修复命令 |
| `ultracite doctor` | 诊断 Biome 与预设间配置冲突 |

## 本项目配置要点

```json
// biome.json（节选）
{
  "extends": ["ultracite/biome/core", "ultracite/biome/react"]
}
```

搭配 Biome `@2.4.15`，由 [Lefthook](tool-lefthook.md) 在 pre-commit 调用：

```bash
pnpm dlx ultracite fix   --files-ignore-unknown=true {staged_files}
pnpm dlx ultracite check --files-ignore-unknown=true {staged_files}
```

## 相关概念

- [Biome](tool-biome.md) —— Ultracite 包装的目标引擎
- [Monorepo 代码质量体系搭建](../playbook/playbook-monorepo-code-quality-setup.md) —— 完整使用场景
