---
type: "Tool"
title: "DeepWrite（本地 AI 写作工作台）"
description: "为写作流程设计的本地桌面工作台：把模型 / 提示词 / 技能 / 素材 / 文稿组织在同一工作台，让 AI 直接修改真实文稿并逐次审阅。"
tags: "[writing, desktop, ai-agent, local-first, editor]"
timestamp: "2026-08-15T05:30:58Z"
resource: "https://github.com/swjybky/deepwrite"
---

# DeepWrite（本地 AI 写作工作台）

## 它是什么

`swjybky/deepwrite` 是一个**本地桌面工作台**，专为「AI 辅助写作流程」设计。它把以下要素组织在同一个工作台：

- **模型**：可切换不同 LLM（OpenAI 兼容 / 本地 GGUF）。
- **提示词**：保存 / 版本化多套 prompt。
- **技能**：类似 Agent Skills 的可复用写作 skill。
- **素材**：参考资料 / 引用片段 / 个人语料库。
- **文稿**：真正在写的稿件，AI 直接在原文件上修订。

与许多 Web 端「AI 写作工具」不同，DeepWrite 是**桌面应用**，AI 修改的是磁盘上的真实文件，而不是平台内的虚拟文档。

> ![](https://pbs.twimg.com/media/HPvWYo1b0AAm7xP.jpg)

## 为什么用它 / 适合什么场景

- **文稿所有权归自己**：所有稿件存在本地，导出 Markdown / DOCX / PDF 完全可控。
- **AI 直接改稿**：不是「给我建议」，而是 AI 真的改写磁盘文件，diff 一目了然。
- **逐次审阅**：每轮 AI 修改单独留痕，方便回滚 / 比较。
- **可扩展 skill**：把常用写作模式（论文 / 公众号 / 技术文档）做成 skill 复用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型路由 | 同一工作台内可配多家 LLM，按任务切换 |
| Prompt 库 | 多套 prompt 可命名 / 版本化 |
| Skill 挂载 | 类似 Agent Skills，写作用法可复用 |
| 真实文稿编辑 | AI 直接操作磁盘文件，diff 可视化 |
| 逐次审阅 | 每轮 AI 输出单独成段，方便回滚 |
| 多文稿 | 同时管理多份稿件 |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| [Obsidian](tool-obsidian.md) + AI 插件 | 知识库 + 局部 AI 辅助 | AI 不主动改全文 |
| [Niamos](tool-niamos.md) | PARA + Claude Code 模板 | 偏「知识管理」而非「主动写作」 |
| DeepWrite | 桌面工作台 + AI 真改稿 | 强调「AI 是写作者，不是助手」 |

## 适用人群

- 长期写技术博客 / 论文 / 公众号 / 书的人。
- 想让 AI 真的「改稿」，而不是只给提纲的人。
- 想完全掌控稿件文件的本地作者。

## 参考链接

- [项目链接](https://github.com/swjybky/deepwrite)

## 相关概念

- [Obsidian](tool-obsidian.md) — Markdown 知识库编辑器
- [Niamos](tool-niamos.md) — PARA + Claude Code 第二大脑模板
- [Cabinet](tool-cabinet.md) — Obsidian + AI 代理组合