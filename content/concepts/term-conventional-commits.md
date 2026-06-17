---
type: Term
title: "Conventional Commits"
description: "一种轻量的提交信息约定规范——格式 `type(scope): description`，type 限定在 feat/fix/docs/style/refactor/perf/test/chore/revert/ci/build 等少数语义值，配合工具可自动生成 CHANGELOG 与语义化版本号。"
resource: "https://www.conventionalcommits.org/"
tags: "[term, git, commit, spec, convention]"
timestamp: 2026-06-17T00:00:00Z
---

# Conventional Commits

## 定义

[Conventional Commits](https://www.conventionalcommits.org/) 是一种**轻量的提交信息约定规范**，规定每次 `git commit -m` 必须遵循：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

通过把提交分成少量**语义 type**，让自动化工具能可靠地：自动生成 CHANGELOG、自动决定下一次版本号（semver 升 major/minor/patch）、按 type 过滤提交历史（如 `git log --grep=^feat`）。

## 标准 type 词表

| type | 用途 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复 bug |
| `docs` | 仅文档变更 |
| `style` | 不影响代码含义的格式调整（空格、分号等） |
| `refactor` | 既不是新功能也不是 bug 修复的代码改动 |
| `perf` | 性能优化 |
| `test` | 新增/修改测试 |
| `chore` | 构建流程、辅助工具、依赖升级等 |
| `revert` | 回退之前的提交 |
| `ci` | CI 配置文件与脚本变更 |
| `build` | 影响构建系统或外部依赖的变更 |

## 要点

- `type` 必填；`(scope)` 可选（如 `feat(auth):`）；`description` 简短说明，长度一般建议 **1–72** 字符
- `BREAKING CHANGE` 在 footer 或 type/scope 后加 `!`（如 `feat(api)!:`）表示破坏性变更 → 触发 semver major 版本
- **与 SemVer 100% 对应**：feat → minor，fix → patch，`!` 或 `BREAKING CHANGE` → major

## 在本项目中的强制

[`playbook-monorepo-code-quality-setup`](./playbook-monorepo-code-quality-setup.md) 在 [Lefthook](./tool-lefthook.md) 的 `commit-msg` 阶段用 `piped: true` + 正则强制：

```bash
pattern="^(feat|fix|docs|style|refactor|perf|test|chore|revert|ci|build)(\(.+\))?: .{1,72}"
```

不匹配时打印中文帮助并 `exit 1`。这种「提交前硬约束」是 Conventional Commits 在团队落地最稳的方式——光靠文档不强制，三个月后就会回到 `git commit -m "改了点东西"`。

## 相关概念

- [Lefthook](./tool-lefthook.md) —— 在 commit-msg 钩子强制执行
- [Monorepo 代码质量体系搭建](./playbook-monorepo-code-quality-setup.md) —— 完整使用场景
