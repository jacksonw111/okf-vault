---
type: Tool
title: "icloud-md（coddingtonbear/icloud-md）"
description: "把 Apple Notes 的每条笔记变成磁盘上一份真实 Markdown 文件，任意编辑器改完后再双向同步回 iCloud"
resource: "https://github.com/coddingtonbear/icloud-md"
tags: "[apple-notes, icloud, markdown, sync, editor-agnostic]"
timestamp: "2026-08-22T04:19:00Z"
---

# icloud-md

## 它是什么
[`coddingtonbear/icloud-md`](https://github.com/coddingtonbear/icloud-md) 把 Apple Notes 的笔记**透明地**投影成磁盘上的 Markdown 文件：在 Linux / Windows / macOS 上用任何编辑器（VS Code、Vim、Obsidian、Emacs）改这些 .md，改完后再双向同步回 iCloud，让你像「一直在 Notes app 里输入」一样地把笔记迁出 Apple 生态。

## 为什么用它 / 适合什么场景
- 笔记锁在 Apple Notes 里，但需要版本控制 / Git / 任何外部工具处理。
- 想用 Obsidian / VS Code 编辑 Notes 内容，又不想手动复制粘贴。
- 想跨设备跨平台（Windows / Linux）访问同一份 Apple Notes。

## 关键能力
| 能力 | 说明 |
|------|------|
| 双向同步 | 本地 .md 改动回写 iCloud，iCloud 新增映射到本地 |
| 跨平台 | Linux / Windows / macOS 同款体验 |
| 编辑器自由 | 任意 Markdown 编辑器都能读写，不绑定 Apple 工具链 |
| 文件即笔记 | 每条 Notes 对应磁盘上一份真实 .md，便于 Git / 搜索 / 备份 |
| 透明代理 | 平时操作流程不变，「像一直在 Notes 里输入」 |

## 媒体
（无媒体）

## 相关概念
- [OpenMac](./tool-openmac.md) — macOS 本地 HTTP 服务，把 Vision / Translation 等系统能力暴露成 JSON API，同属「把 Apple 生态锁定的能力解锁出来」
- [Open Knowledge（Inkeep）](./tool-open-knowledge.md) — WYSIWYG Markdown 编辑器 + LLM 知识库，另一种 Markdown-as-knowledge 思路
