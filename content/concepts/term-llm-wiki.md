---
type: Term
title: "LLM Wiki 模式"
description: "Andrej Karpathy 提出的概念：让 LLM 作为 wiki 的维护者，承担「不会厌倦、不会遗忘、可一次修改多个文件」的文档管理工作。"
resource: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
tags: "[llm, wiki, karpathy, pattern]"
timestamp: 2026-06-17T00:00:00Z
---

# LLM Wiki 模式

## 定义

LLM Wiki 模式是 Andrej Karpathy 在 2024 年提出的 AI 辅助知识管理思路：让大语言模型替代人类承担 wikis 的「账本工作」——重复读取相同文档提取相同事实、更新交叉引用、一次修改多个文件。人类因厌倦而放弃个人 wikis 的原因，恰好是 LLM 的长项。

## 核心观点

> "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."

- **不厌倦**：LLM 可以反复读取同一份文档提取相同事实，不会有「第 15 次读这份 runbook 好无聊」的问题
- **不忘更新**：跨文件引用（如 `[customers](./customers.md)`）由 LLM 在修改时一并维护，不会漏掉
- **批量操作**：一个 prompt 可以同时修改十多个文件，人手难以做到的跨文件一致性成为可能

## 与 OKF 的关系

LLM Wiki 模式是 OKF 的**理念先驱**。OKF 将这一实践形式化为：

- 一个概念 = 一个 Markdown 文件 + YAML frontmatter
- 概念之间用 Markdown 链接互联，形成图谱
- LLM 可作为 producer（写）或 consumer（读/推理）参与

OKF = LLM Wiki 模式的**标准化产物**。Karpathy 的 gist 是点子，OKF 是把点子变成可互操作的格式。

## 常见实例

- Obsidian vault 与 coding agent 联动
- `AGENTS.md` / `CLAUDE.md` 系列约定文件
- 数据团队内部的「元数据即代码」仓库
- Hugo、Notion 等工具的 frontmatter 跨文件链接

## 相关概念

- [Open Knowledge Format (OKF)](./term-okf.md) —— LLM Wiki 模式的标准化形式
- [Obsidian](./tool-obsidian.md) —— LLM Wiki 模式的天然编辑器/消费端
