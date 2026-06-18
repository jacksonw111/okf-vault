---
type: "Tool"
title: "Field Theory"
description: "@andrewfarah 的开源「上下文管理」应用：把写作、阅读、语音、终端、书签、剪贴板、codex 面板、markdown 等多源内容统一收纳；带 IA Writer 风格编辑器；全部本地。"
tags: "[productivity, writing, reading, bookmarks, local-first, markdown]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/andrewfarah/field-theory"
---

# Field Theory

## 它是什么

[`Field Theory`](https://github.com/andrewfarah/field-theory) 是 @andrewfarah 公布的第二个开源项目（v0.3.2）：一款**本地优先**的统一「上下文管理」应用——把日常工作中分散的内容**收拢到一个工作面**：

- IA Writer 风格编辑器
- X / Twitter 书签
- Codex 面板（代码片段 / 命令历史）
- Markdown 渲染
- 终端集成
- Gemma（推测为本地 LLM）
- CLI
- 语音输入 / 输出

定位一句话：「**写作、阅读、语音、终端、书签、剪贴板等等**」—everything-in-one-place。

## 为什么用它

- **本地优先**：所有数据在自己机器，隐私 + 离线 + 可脚本处理。
- **统一收口**：书签散在 X / 浏览器 / 笔记里、代码散在终端 / IDE / 笔记里、写作散在多个编辑器——Field Theory 想用一个面板解决。
- **Markdown 原生**：与 [OKF](term-okf.md) 生态天然兼容；保存的文件可直接被 Obsidian / 静态站点消费。
- **可扩展**：CLI + Codex 面板意味着能 shell out 给 [Claude Code](tool-claude-code.md) 之类的 agent。

## 关键能力

| 能力 | 说明 |
|------|------|
| IA Writer 风格编辑器 | 沉浸、聚焦 |
| X 书签同步 | 收藏 / 标签 / 全文搜索 |
| Codex 面板 | 命令、片段、输出可一并保存 |
| Markdown 渲染 | 与通用知识库兼容 |
| 终端集成 | 命令不离开应用 |
| 语音 | 输入 / 输出 |
| CLI | 可脚本化 |

## 与本知识库的关系

- **导出格式若为 Markdown + frontmatter**——可直接被 `PRODUCER.md 协议` 消费。
- 1.5k+ 次 commit，已经过了「玩具」门槛，是值得放进 [`overview.md`](../overview.md) 跟踪的开源项目。

## 相关概念

- [Obsidian](tool-obsidian.md)
- [Cabinet](tool-cabinet.md) — 另一款「Obsidian + 上下文」尝试
- [LLM Wiki 模式](term-llm-wiki.md)
