---
type: Note
title: 输出模板目录
description: agent 按 PRODUCER.md 写概念文件时，照这里的对应模板填充。也是人类偶尔手写时的起点。这些是 schema，不是成品。
tags: [okf, templates]
timestamp: 2026-06-16T12:30:00Z
---

# templates/ —— 概念输出模板

每个 `type` 一份骨架。agent 产出新概念时**复制对应模板 → 填实 → 放到 `concepts/`**，再把占位符删掉。

| 文件 | 对应 type | 用途 |
|------|-----------|------|
| [term.md](./term.md) | Term | 术语 / 概念定义 |
| [tool.md](./tool.md) | Tool | 工具 / 软件 / 服务 |
| [playbook.md](./playbook.md) | Playbook | 操作手册 / 流程 |
| [note.md](./note.md) | Note | 普通笔记 / 通用兜底 |

> 占位符约定：`<…>` 必填，`[…]` 可选。frontmatter 里只 `type` 是强制的，其余按资料情况尽量补全，尤其 `description`。

## 在 Obsidian 里用核心模板插件

已配置（见 `.obsidian/templates.json`）：模板目录 = `templates`。
在 Obsidian 里 `Cmd+P` → "Insert template" → 选对应模板，即可插入骨架（偶尔手写时用）。
