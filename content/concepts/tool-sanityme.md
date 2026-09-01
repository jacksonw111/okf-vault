---
type: "Tool"
title: "sanityme（一条命令装上的 Git hooks 仓库规范器）"
description: "一条命令装上 Git hooks，每次 commit 自动检查格式与拼写，让仓库历史从第一天起保持干净规范。"
resource: "https://github.com/olankens/sanityme"
tags: [git, hooks, code-quality, commit-msg, spell-check, formatter, dev-tools]
timestamp: "2026-09-01T15:55:00Z"
---

# sanityme

## 它是什么
[sanityme](https://github.com/olankens/sanityme) 是一个**一条命令就能装上的 Git hooks 工具**：装好后，每次 commit 时它会自动跑**格式检查与拼写检查**，让仓库历史从第一天起就保持干净规范。

定位介于「husky + lint-staged」与「pre-commit 框架」之间：比 husky 配置更轻，比 pre-commit 框架更聚焦——只管**commit 时**的格式与拼写门槛，不引入 Python 运行时依赖（适合前端 / Node / 任意生态）。

## 为什么用它 / 适合什么场景
- 想要**一行命令**就让团队的 commit 规范落地，而不是写一堆 husky + lint-staged 配置；
- 想要「**格式 + 拼写**」这类最常见的 commit 卫生检查，**免配置 / 免选 lint 工具**；
- 想给新仓库 / 个人项目**立刻**挂上钩子，避免历史一开始就不规范；
- 不想为了 hooks 装 Python（pre-commit 需要 Python）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一条命令安装 | 单条 CLI 把 hooks 装到 `.git/hooks/` |
| 自动格式检查 | commit 时跑格式校验 |
| 自动拼写检查 | 提交说明与代码注释拼写兜底 |
| 零 Python 依赖 | 不像 pre-commit 需要 Python 运行时 |
| 仓库级配置 | 跟着仓库走，新克隆也能直接生效 |
| 拦截坏 commit | 不通过检查就不让提交 |
| 适合新仓库 | 从第一天起就维持规范历史 |

## 媒体
![](https://pbs.twimg.com/media/HRIJIQFagAEOwrm.jpg)

## 相关概念
- [Lefthook](tool-lefthook.md) — Go 写的多语言 Git hooks 管理器，能力更通用；sanityme 聚焦「格式 + 拼写」轻量场景
- [Biome](tool-biome.md) — 单一格式化 / lint 工具，配合 hooks 做格式检查

## 参考链接
- 项目链接：<https://github.com/olankens/sanityme>