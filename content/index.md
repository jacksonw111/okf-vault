---
type: Index
title: 我的 OKF 知识库
description: 基于 Open Knowledge Format v0.1 的个人知识库根入口。本目录即一个 OKF bundle——一个由 Markdown + YAML frontmatter 组成、可被人和 AI agent 共同消费的知识目录。
tags: [okf, root]
timestamp: 2026-06-16T12:00:00Z
---

# 我的 OKF 知识库

> **一句话**：OKF = 一个目录里一堆 Markdown 文件，每个文件 = 一个「概念」；文件路径就是概念的身份证；用 YAML frontmatter 放结构化字段（`type` 是唯一必填项），用正文放其余内容，文件之间用链接互相连接，形成一个知识图谱。

## 目录约定（OKF v0.1）

| 规则 | 说明 |
|------|------|
| 一个概念 = 一个文件 | 文件路径 = 概念的唯一身份，路径要稳定、不要乱改 |
| `type` 必填 | 其余字段（title / description / resource / tags / timestamp）都可选 |
| 链接互联 | 用 Markdown 链接把概念连起来 → 形成图谱（Obsidian 图谱视图直接可用） |
| `index.md` | 每个子目录可选放一个，用于「渐进式披露」（agent 浏览层级时的导航页） |
| `log.md` | 可选，按时间记录变更 |

## 本 bundle 的概念类型（自定义，OKF 不强制）

- `Term` — 术语 / 概念定义
- `Tool` — 工具 / 软件
- `Playbook` — 操作手册 / 流程
- `Note` — 普通笔记
- `Index` — 目录导航页

## 浏览起点

- [🤖 生产者协议 PRODUCER](./PRODUCER.md) ← agent 怎么把资料变成 OKF
- [📥 inbox 投递区](./inbox/README.md) ← 把资料扔这里
- [📊 知识库仪表盘](./_dashboards/overview.md) ← 浏览所有概念
- [OKF 是什么](./concepts/term-okf.md)
- [Obsidian](./concepts/tool-obsidian.md)
- [LLM Wiki 模式](./concepts/term-llm-wiki.md)
- [OKF Enrichment Agent](./concepts/tool-okf-enrichment-agent.md)
- [OKF Static HTML Visualizer](./concepts/tool-okf-static-html-visualizer.md)
- [OKF 参考示例 Bundles](./concepts/tool-okf-sample-bundles.md)
- [Monorepo 代码质量体系搭建](./concepts/playbook-monorepo-code-quality-setup.md)
- [Biome](./concepts/tool-biome.md)
- [Ultracite](./concepts/tool-ultracite.md)
- [Lefthook](./concepts/tool-lefthook.md)
- [Turborepo](./concepts/tool-turbo.md)
- [ESLint](./concepts/tool-eslint.md)
- [Conventional Commits](./concepts/term-conventional-commits.md)
- [在 Obsidian 里开始用 OKF（Playbook）](./concepts/playbook-okf-obsidian-start.md)
- [输出模板目录](./templates/_README.md)
- [变更记录](./log.md)

## 你（人类）的日常就是

1. 把资料丢进 [`inbox/`](./inbox/README.md)
2. 对 agent 说「**处理 inbox**」
3. agent 按 [`PRODUCER.md`](./PRODUCER.md) 产出到 `concepts/`、更新索引与 log、归档资料
4. 去 [`_dashboards/overview.md`](./_dashboards/overview.md) 看结果
