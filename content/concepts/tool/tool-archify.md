---
type: "Tool"
title: "Archify"
description: "tt-a1i 开的「自然语言 → 架构图」skill：LLM 把描述转成结构化 JSON → Node.js 渲染器用纯几何算法生成 SVG → 注入自包含 HTML；不需要文生图模型，token 友好，可代码化、可主题化、可版本化。"
tags: "[ai, svg, diagram, skill, architecture, agent]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/tt-a1i/archify"
---

# Archify

## 它是什么

[`Archify`](https://github.com/tt-a1i/archify) 是一个让 LLM **不靠文生图模型、纯靠 prompt + JSON schema + 几何算法**来画架构图 / 系统拓扑的 skill。被社区发现由 `pi + DeepSeek` 跑出效果后走红。

## 工作原理（三步）

1. **LLM 把自然语言描述转成结构化 JSON**（节点 / 边 / 布局意图的 schema）。
2. **Node.js 渲染器用纯几何算法生成 SVG**（无 ML、无第三方图库依赖）。
3. **SVG 注入自包含 HTML**——一个文件就能分享、嵌入到文档 / Obsidian / Notion。

```
"画一个前后端分离架构，前端 React，后端 Go API，DB 是 Postgres，Redis 做缓存"
        ↓ LLM
{ nodes: [...], edges: [...] }
        ↓ Node.js 几何算法
.svg + 单文件 .html
```

## 关键能力

| 能力 | 说明 |
|------|------|
| 不需要文生图模型 | 只用对话模型，token 友好；可换任意模型 |
| 输出可代码化 | JSON schema 明确、SVG 可 diff |
| 自包含 HTML | 邮件 / Obsidian / Notion 都能直接嵌 |
| 主题可换 | 几何算法解耦样式，dark / light / brand 都能改 |
| 跑在 agent 里 | 作为 [Claude Code](tool-claude-code.md) skill 时可被自动调用 |

## 为什么这个思路重要

- **避开了文生图的「幻觉 / 文字错误 / 排版不可控」**：几何算法画线/对齐是确定的，LLM 只负责「画什么」。
- **可版本管理**：JSON 中间产物可以进 git、可以做 review。
- **在 agent 流程里很合适**：skill 化后，代理读完一段代码直接出一张图，比手画快。

## 使用

```bash
# 直接装为 skill
git clone https://github.com/tt-a1i/archify .claude/skills/archify
# 在 Claude Code 里：
# /archify 描述一段架构
# 产物：当前目录 archify-*.html
```

## 与其他架构图工具的关系

| 工具 | 思路 | 适合 |
|------|------|------|
| **Archify** | LLM→JSON→几何 SVG | agent 内 / 自动化 |
| Mermaid | 文本 DSL → 渲染 | 代码注释 / PR / Markdown 嵌入 |
| D2 | 文本 DSL → 多种格式 | 工程师手画 |
| tldraw / Excalidraw | 手画 | 头脑风暴 |
| 文生图（Midjourney / DALL·E） | 自然语言 → 像素 | 视觉草图，但文字经常错 |

## 相关概念

- [Agent Skills 是什么](../term/term-agent-skills.md)
- [Claude Code](tool-claude-code.md)
- [Mermaid](https://mermaid.js.org/) — 互补的代码图工具
- [OKF 是什么](../term/term-okf.md) — 同为「markdown 文件 + frontmatter」的本地知识形态，产物可互转
