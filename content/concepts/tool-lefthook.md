---
type: Tool
title: Lefthook
description: 用 Go 写成的 Git 钩子管理器——一个 `lefthook.yml` 同时配置 pre-commit / commit-msg / pre-push，并行执行，配置和实际钩子解耦。比 husky/lint-staged 更快、更声明式。
resource: https://github.com/evilmartians/lefthook
tags: [tool, git, hooks, code-quality, lefthook]
timestamp: 2026-06-17T00:00:00Z
---

# Lefthook

## 它是什么

[Lefthook](https://github.com/evilmartians/lefthook) 是由 Evil Martians 出品的 **Git 钩子管理器**。用一个 YAML 配置文件（`lefthook.yml`）声明 pre-commit / commit-msg / pre-push 各阶段要跑哪些命令，由 Lefthook 自己负责安装（`lefthook install`）并把钩子写入 `.git/hooks/`。

## 为什么用它 / 适合什么场景

- **声明式 + 并行**：一份 YAML 覆盖三个钩子阶段，jobs 之间默认 `parallel: true`——本质串行的检查可以跑成并发
- **快**：Go 写的二进制，没有 Node 启动开销
- **stage_fixed 支持**：在 pre-commit 自动 fix 后，能把修复结果**重新加入暂存区**（Biome/ESLint fix 后不会丢失）
- **commit-msg piped 模式**：可以读 message 内容做正则校验（[Conventional Commits](./term-conventional-commits.md) 强制）
- **glob 精准过滤**：每个 job 配 `glob`，只对相关文件触发，减少浪费

## 关键能力

| 能力 | 说明 |
|------|------|
| `pre-commit` | 支持 `jobs`（声明式）和 `commands`（命令式）；`stage_fixed: true` 把 fix 后的结果入暂存 |
| `commit-msg` | `piped: true` 后可通过 `{1}` 拿到 commit message 内容做正则校验 |
| `pre-push` | 推送前钩子，本项目用于 `pnpm check-types` 全量类型检查 |
| `parallel: true` | 多 job/command 并发执行 |
| `glob` | 触发条件：本项目用 `*.{js,ts,tsx,jsx,...}` 等 |
| `{staged_files}` | 占位符：当前钩子对应的暂存文件路径列表 |

## 本项目配置要点

本项目用 Lefthook 编排三个阶段共 8 个检查项，详见 [`playbook-monorepo-code-quality-setup`](./playbook-monorepo-code-quality-setup.md) 第 5 节。最容易被遗漏的步骤是：

```bash
pnpm exec lefthook install
```

否则 `lefthook.yml` 只停留在配置文件层面，`.git/hooks/` 下不会真的生成钩子脚本。团队协作建议在 `package.json` 加 `"prepare": "lefthook install"`，让 `pnpm install` 后自动安装。

## 相关概念

- [Biome](./tool-biome.md) / [Ultracite](./tool-ultracite.md) / [ESLint](./tool-eslint.md) —— 由 Lefthook 在 pre-commit 触发
- [Conventional Commits](./term-conventional-commits.md) —— 在 commit-msg 阶段强制
- [Monorepo 代码质量体系搭建](./playbook-monorepo-code-quality-setup.md) —— 完整使用场景
