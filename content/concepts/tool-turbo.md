---
type: Tool
title: "Turborepo"
description: "Vercel 出品的 monorepo 任务编排器（turbo.json）——按 `^task` 依赖图跨包并行执行 build / lint / test / type-check，自动缓存增量结果。"
resource: "https://turborepo.com/"
tags: "[tool, monorepo, build, orchestration, turbo]"
timestamp: 2026-06-17T00:00:00Z
---

# Turborepo

## 它是什么

[Turborepo](https://turborepo.com/)（`turbo` CLI）是 Vercel 开源的 **monorepo 任务编排器**。一份根 `turbo.json` 声明各个任务（`build` / `lint` / `check-types` / `dev` 等）的依赖关系（`dependsOn: ["^task"]`）、输入指纹（`inputs`）、输出（`outputs`），然后 `turbo <task>` 会在所有 workspace 包中按图并行执行，自动做增量缓存（同样的输入+输出再跑一次是 0 成本）。

## 为什么用它 / 适合什么场景

- **跨包任务编排**：`^build` 表示「先跑所有依赖包的 build 再跑当前包的 build」，省去手写脚本
- **并行 + 缓存**：天生并行；命中缓存时输出 `cache hit, suppressing logs` 并瞬间完成
- **过滤支持**：`turbo run build --filter=@myorg/web...` 只跑某包及其依赖
- **远程缓存**（可选）：团队共享缓存，进一步缩短 CI 时间

## 关键能力

| 能力 | 说明 |
|------|------|
| `tasks.<name>.dependsOn` | `["^name"]` 表示依赖包先跑；`[]` 表示不依赖 |
| `inputs` | 触发重跑的文件指纹；本项目用 `$TURBO_DEFAULT$`（默认）+ `.env*` |
| `outputs` | 缓存目录；如 `dist/**` |
| `cache: false` | 强制重跑；常用于 `dev`（persistent: true） |
| `persistent: true` | 长期运行的任务（`dev` / `watch`） |
| `ui: tui` | 终端 UI（默认） |

## 本项目配置要点

```json
{
  "$schema": "https://turborepo.com/schema.json",
  "ui": "tui",
  "tasks": {
    "build":       { "dependsOn": ["^build"], "inputs": ["$TURBO_DEFAULT$", ".env*"], "outputs": ["dist/**"] },
    "lint":        { "dependsOn": ["^lint"] },
    "check-types": { "dependsOn": ["^check-types"] },
    "dev":         { "cache": false, "persistent": true }
  }
}
```

由 [Lefthook](tool-lefthook.md) 的 `pre-push` 钩子调用：

```bash
pnpm check-types    # 等价于 turbo check-types → 各包并行跑 tsc --noEmit
```

## 相关概念

- [Lefthook](tool-lefthook.md) —— 在 pre-push 触发 turbo 任务
- [Monorepo 代码质量体系搭建](playbook-monorepo-code-quality-setup.md) —— 完整使用场景
