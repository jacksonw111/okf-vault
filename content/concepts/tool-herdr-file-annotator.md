---
type: "Tool"
title: "herdr-file-annotator（herdr 代码评审批注插件）"
description: "JonasBaeumer 写的 Rust 插件，给 herdr 工作区（Claude Code / Codex / Gemini CLI 等 MCP agent）配一个代码评审面板：选中行 → 写下意见 + 标签（fix / verify / question / nit）→ 批注带行号锚点结构化传回 agent。"
tags: "[herdr, code-review, annotation, rust, mcp, agent]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/JonasBaeumer/herdr-file-annotator"
---

# herdr-file-annotator（herdr 代码评审批注插件）

## 它是什么

[`herdr-file-annotator`](https://github.com/JonasBaeumer/herdr-file-annotator) 是 JonasBaeumer 写的 **Rust 插件**——给 [herdr 工作区](./tool-herdr-nvim.md)（Claude Code / Codex / Gemini CLI 这类 MCP agent）补一个**代码评审面板**：

- 用终端 + 编码 Agent 干活时，**想看代码就得忍受满屏 diff 和 agent 长篇文字汇报**
- 现在多一个可视的评审面板，可选中代码行、写意见、打标签
- 标签分四类：**fix / verify / question / nit**
- 批注带**行号锚点**、**结构化**传回给 agent，让 agent 能直接对照修改

## 为什么用它 / 适合什么场景

- 用终端 Agent 时不愿意再翻一长串 diff 来回叙事
- 想给团队统一「这个评审批注应该长什么样」的规范
- 想让批注能结构化传递，避免自然语言表述歧义

## 关键能力

| 能力 | 说明 |
|------|------|
| 行选中 + 评论 | 可视化批注 |
| 四类标签 | fix / verify / question / nit |
| 行号锚点 | 批注自动绑定行号 |
| 结构化传递 | agent 能直接对照 |
| Rust 实现 | 性能与稳定性 |
| herdr 集成 | 配 Claude Code / Codex / Gemini CLI |

## 媒体

![](https://pbs.twimg.com/media/HQiV7U3bwAAMcZh.jpg)

## 参考链接

- [项目链接](https://github.com/JonasBaeumer/herdr-file-annotator)

## 相关概念

- [herdr-nvim](./tool-herdr-nvim.md) — 把 Neovim 嵌入 herdr 工作区的基础插件
