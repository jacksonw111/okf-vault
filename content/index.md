---
type: Index
title: "我的 OKF 知识库"
description: "基于 Open Knowledge Format v0.1 的个人知识库根入口。本目录即一个 OKF bundle——一个由 Markdown + YAML frontmatter 组成、可被人和 AI agent 共同消费的知识目录。"
tags: "[okf, root]"
timestamp: 2026-06-17T00:00:00Z
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

- [📊 知识库仪表盘](./overview.md) ← 实时统计 / 类型分布 / 标签 / 最近更新（**从这里开始**）
- [📑 概念目录](./concepts/index.md) ← 全量概念导航
- [📥 inbox 投递区](./inbox/README.md) ← 把资料扔这里

## 核心概念

- [OKF 是什么](concepts/term/term-okf.md)
- [Agent Skills（代理技能包）](concepts/term/term-agent-skills.md)
- [LLM Wiki 模式](concepts/term/term-llm-wiki.md)
- [Conventional Commits](concepts/term/term-conventional-commits.md)

## 工具

- [Obsidian](concepts/tool/tool-obsidian.md)
- [Cabinet](concepts/tool/tool-cabinet.md)
- [Field Theory](concepts/tool/tool-field-theory.md)
- [Claude Code](concepts/tool/tool-claude-code.md)
- [Mira（Agent-native 投研）](concepts/tool/tool-mira.md)
- [WechatOnCloud / 云微](concepts/tool/tool-wechat-on-cloud.md)
- [OKF Enrichment Agent](concepts/tool/tool-okf-enrichment-agent.md)
- [OKF Static HTML Visualizer](concepts/tool/tool-okf-static-html-visualizer.md)
- [OKF 参考示例 Bundles](concepts/tool/tool-okf-sample-bundles.md)

## 网络 / NAS 工具

- [3X-UI](concepts/tool/tool-3x-ui.md)
- [Lucky](concepts/tool/tool-lucky.md)

## 代码质量 / Monorepo

- [Monorepo 代码质量体系搭建](concepts/playbook/playbook-monorepo-code-quality-setup.md)
- [Biome](concepts/tool/tool-biome.md)
- [Ultracite](concepts/tool/tool-ultracite.md)
- [Lefthook](concepts/tool/tool-lefthook.md)
- [Turborepo](concepts/tool/tool-turbo.md)
- [ESLint](concepts/tool/tool-eslint.md)

## Agent Skills 生态

- [mattpocock/skills](concepts/tool/tool-mattpocock-skills.md)
- [shadcn/improve](concepts/tool/tool-shadcn-improve.md)
- [Archify](concepts/tool/tool-archify.md)
- [JSON-Render / 生成式 UI](concepts/tool/tool-json-render.md)
- [Hyperagent 设计网格 Skill](concepts/tool/tool-hyperagent-design-skill.md)

## 前端 / 设计资源

- [transitions.dev](concepts/tool/tool-transitions-dev.md)
- [textmotion.dev](concepts/tool/tool-textmotion-dev.md)
- [index.how/to/articulate](concepts/tool/tool-index-how-articulate.md)
- [animations.dev/vocabulary](concepts/tool/tool-animations-dev-vocabulary.md)
- [Trees（@rammcodes）](concepts/tool/tool-trees-rammcodes.md)
- [前端 / 创客 资源合集](concepts/note/note-front-end-resources.md)

## AI / Agent 生态

- [CopilotKit](concepts/tool/tool-copilotkit.md)
- [ShipSwift](concepts/tool/tool-shipswift.md)
- [forkd](concepts/tool/tool-forkd.md)
- [Sophon](concepts/tool/tool-sophon-at.md)
- [云端 Agent 基础设施的设计教训（CREAO）](concepts/note/note-cloud-agent-infrastructure.md)

## 自托管 / 邮件

- [Cloud Mail](concepts/tool/tool-cloud-mail.md)

## 金融 / 数据

- [a-stock-data](concepts/tool/tool-a-stock-data.md)

## 操作手册

- [在 Obsidian 里开始用 OKF（Playbook）](concepts/playbook/playbook-okf-obsidian-start.md)
- [VLESS + WebSocket + TLS 绕过电信 QoS](concepts/playbook/playbook-vless-bypass-telecom-qos.md)

## 配套文档

- [输出模板目录](./templates/_README.md)
- [变更记录](./log.md)

## 你（人类）的日常就是

1. 把资料丢进 [`inbox/`](./inbox/README.md)
2. 对 agent 说「**处理 inbox**」
3. agent 按 PRODUCER.md 产出到 `concepts/`、更新索引与 log、归档资料
4. 去 [`overview.md`](./overview.md) 看结果
