---
type: "Tool"
title: "pojia-next（六个 AI 客户端 persona 注入器）"
description: "z91772524-ai 开源：把 DSH / WorkBuddy / ZCode / Codex / Cursor / Claude Code 六个 AI 客户端里「用户碰不到」的内置提示词换掉，改成自己写的 persona.md；动手前留备份，出事一条命令还原。"
resource: "https://github.com/z91772524-ai/pojia-next"
tags: "[ai-client, persona, prompt-override, claude-code, codex, cursor]"
timestamp: "2026-10-08T23:50:00Z"
---

# pojia-next

## 它是什么

[pojia-next](https://github.com/z91772524-ai/pojia-next) 是 z91772524-ai 开源的「**AI 客户端 persona 注入器**」：

- 覆盖 6 个主流 AI 客户端：**DSH / WorkBuddy / ZCode / Codex / Cursor / Claude Code**
- 把这些客户端里「**用户碰不到**」的**内置提示词**（系统提示 / agent 提示 / 工具调用骨架等）一次性替换成用户自己写的 `persona.md`
- **动手前自动备份**，出事一条命令还原
- 让用户在不重写客户端的前提下，统一自家 AI 客户端的人格 / 行为

## 为什么用它 / 适合什么场景

- **不想被客户端的默认人格绑架**：统一改成自己想要的工作风格
- **跨客户端保持一致人格**：6 个客户端跑出来都是「我」的语气
- **风险可控**：原始 prompt 备份了，玩坏了随时回滚
- **安全研究员 / prompt 工程师**：观察每个客户端的内置提示词究竟写什么

## 关键能力

| 能力 | 说明 |
|------|------|
| 客户端覆盖 | DSH / WorkBuddy / ZCode / Codex / Cursor / Claude Code 6 家 |
| 提示词替换 | 把内置 prompt 换成 persona.md |
| 自动备份 | 替换前留原始 prompt |
| 一键还原 | 玩坏一条命令回滚 |
| persona.md | 用户可自由编写的注入文本 |
| 安全 | 整个过程在本地完成 |

## 参考链接

- 项目链接：<https://github.com/z91772524-ai/pojia-next>

## 媒体

![](https://pbs.twimg.com/media/HUAIaFcboAALrl0.jpg)

## 相关概念

- [Claude Code](./term-claude-code.md) — 注入目标之一
- [Codex](./term-codex.md) — 注入目标之一
- [Harness Engineering](./term-harness-engineering.md) — persona 注入是 harness engineering 的实操手段之一