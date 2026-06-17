---
type: Playbook
title: "Monorepo 代码质量体系搭建（Biome + Ultracite + ESLint + Lefthook）"
description: "在 pnpm + turbo + tsc 的 monorepo 中，从零搭建 Biome（Ultracite 预设）+ ESLint + Lefthook（pre-commit / commit-msg / pre-push）+ 自定义 Node 检查脚本的完整代码质量体系。"
tags: "[code-quality, lint, lefthook, biome, eslint, git-hooks, monorepo, pnpm, turbo]"
timestamp: 2026-06-17T00:00:00Z
---

# Monorepo 代码质量体系搭建

> 目标：在 monorepo 中复刻与 `justsayai-finances` 项目**完全一致**的代码检查效果——
> Biome（Ultracite 预设）+ ESLint（类型感知规则）+ Lefthook（pre-commit / commit-msg / pre-push）+ 三个自定义 Node 脚本。
> 按顺序执行即可得到同样的拦截效果。

## 适用场景

- 启动一个 monorepo（pnpm workspaces + turbo），需要开箱即用的「提交即检查」质量门
- 想用 Biome 做主力格式化/lint，但需要保留 ESLint 处理它不擅长的：函数行数、圈复杂度、魔术数字、参数/嵌套深度
- 想要 conventional commits 强约束、推送前类型全检查
- 团队规则想用代码写出来（自定义脚本）而不是写文档

## 前置条件

- Node.js + Corepack（启用 `corepack enable`）
- 已 `git init`（钩子依赖 git）
- 固定版本约束：本 playbook 默认 **`package.json` 禁止 `^`、`~`、`latest`、`*` 或范围版本**，必须固定版本号（`workspace:*` / `catalog:*` 例外）

## 步骤

### 1. 锁定版本与 monorepo 骨架

| 工具 | 版本 | 作用 |
|------|------|------|
| 包管理器 | `pnpm@10.22.0` | monorepo + catalog |
| 构建编排 | `turbo@2.8.12` | 跨包任务编排 |
| 格式化/Lint 引擎 | `@biomejs/biome@2.4.15` | 主要格式化 + lint |
| Ultracite | `ultracite@7.8.1` | Biome 的零配置预设封装 |
| 类型 Lint | `eslint@10.4.1` | 类型感知规则（复杂度/行数/魔术数字） |
| TS 插件 | `@typescript-eslint@8.60.1` | TS 规则 + 解析器 |
| Git 钩子 | `lefthook@2.1.9` | pre-commit / commit-msg / pre-push |
| TypeScript | `catalog` → `typescript@6.0.3` | 类型检查 |

**关键点**：`pnpm-workspace.yaml` 里要写 `allowBuilds.lefthook: true`，否则 pnpm 10 默认拦截 lefthook 的安装脚本。

### 2. 配置 Biome（Ultracite 预设）

根目录 `biome.json`：`extends: ["ultracite/biome/core", "ultracite/biome/react"]`，项目级再加严规则（详见附录 A）。要点：

- 缩进用 **tab**，字符串用**双引号**
- 自动整理 import（`organizeImports: on`）
- Tailwind 类名排序（`useSortedClasses`，识别 `clsx` / `cva` / `cn`）
- `noExplicitAny: error`，并在 `**/*.ts`/`**/*.tsx` override 中再次强制

### 3. 配置 ESLint（类型感知规则）

Biome 不做的事交给 ESLint：`max-lines-per-function`（≤50）、`complexity`（≤10）、`no-magic-numbers`、`max-params`（≤4）、`max-depth`（≤4）、`consistent-return`、`@typescript-eslint/no-non-null-assertion`、`@typescript-eslint/prefer-readonly`。

配置用 flat config（`eslint.config.js`，ESM），顶层用 `await import(...)` 动态加载插件。

### 4. 自定义 Node 检查脚本（`scripts/*.js`）

3 个脚本，由 lefthook 传入暂存文件路径，违规 `exit 1`：

| 脚本 | 规则 |
|------|------|
| `check-file-rules.js` | `.tsx` 用 PascalCase 或简单小写；其他文件 kebab-case；任何文件 ≤ 300 行 |
| `check-package-json.js` | 依赖必须固定版本号；禁止 `^` `~` `latest` `*` 范围；`workspace:*` / `catalog:*` / `file:` / `link:` 例外 |
| `check-tailwind.js` | 禁止 `w-[96px]` / `bg-[#fff]` 这类任意值；`group-` `peer-` `variant-` 例外 |

完整源码见原 inbox 资料（已归档到 `inbox/_done/`）。

### 5. 配置 Lefthook（核心）

```yaml
pre-commit:   # 并行，6 个 job（ultracite-format 带 stage_fixed、ultracite-lint、file-rules、eslint、package-json、tailwind）
commit-msg:   # piped，强制 Conventional Commits：type(scope): description（type 限 11 种）
pre-push:     # 并行，pnpm check-types（turbo → 各包 tsc）
```

**容易漏的一步**：`pnpm exec lefthook install`，否则钩子只在配置层面，不会真的在 `.git/hooks/` 生成。验证：`ls .git/hooks/ | grep -E 'pre-commit|commit-msg|pre-push'`。

### 6. 端到端验证清单

| 场景 | 期望 |
|------|------|
| 提交缩进乱的 `.ts` | 自动 tab 格式化，重新入暂存，提交成功 |
| 提交含 `any` 的 `.ts` | `ultracite-lint` 报错，提交被拒 |
| 提交 >300 行文件 | `file-rules` 报错 |
| 提交 `myComponent.ts` | `file-rules` 报错（应 kebab） |
| `package.json` 写 `^1.0.0` | `package-json-rules` 报错 |
| `className="w-[96px]"` | `tailwind-rules` 报错 |
| `git commit -m "随便写"` | commit-msg 拒绝，打印 conventional commits 帮助 |
| 推送含类型错误代码 | pre-push 失败 |

## 验证 / 自检

- [ ] `pnpm exec biome --version` → 2.4.15
- [ ] `pnpm exec ultracite doctor` → 无冲突
- [ ] `pnpm exec eslint --version` → v10.4.1
- [ ] `pnpm exec lefthook version` → 2.1.9
- [ ] `pnpm check && pnpm lint && pnpm check-types` 全过
- [ ] `.git/hooks/` 下有 `pre-commit` / `commit-msg` / `pre-push` 三个文件

## 相关概念

- [Biome](./tool-biome.md) —— 主力格式化/Lint 引擎
- [Ultracite](./tool-ultracite.md) —— Biome 的零配置预设
- [Lefthook](./tool-lefthook.md) —— Git 钩子管理器
- [Turborepo](./tool-turbo.md) —— 跨包任务编排
- [Conventional Commits](./term-conventional-commits.md) —— 提交信息规范
