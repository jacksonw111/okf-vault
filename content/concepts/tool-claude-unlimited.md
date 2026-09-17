---
type: "Tool"
title: "Claude Unlimited"
description: "DevDock-AI 出的本地 Python 守护进程（127.0.0.1:4317），把多个 Claude Pro/Max、ChatGPT/Codex 订阅和 Anthropic API key 汇成账号池供 Claude Code 自动切换。"
resource: "https://github.com/DevDock-AI/claude-unlimited"
tags: "[claude-code, claude, codex, anthropic-api, account-pool, fallback, local-daemon, ai-gateway]"
timestamp: "2026-09-17T11:28:00Z"
---

# Claude Unlimited

## 它是什么

[DevDock-AI/claude-unlimited](https://github.com/DevDock-AI/claude-unlimited) 是 **DevDock-AI** 开源的一个**100% 本地运行的 Python 守护进程**（监听 `127.0.0.1:4317`）。它把多个 Claude Pro / Max 订阅、ChatGPT / Codex 订阅以及 Anthropic API key **汇成一个账号池**——当 Claude Code 会话跑到某账号用量上限时，**自动切换到下一个账号**，无需登出、无需交接、无需重启会话。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多账号池 | 统一管理 Claude / Codex / Anthropic API 多种凭证 |
| 自动切换 | 用量达到上限自动 fallback 到下一个账号 |
| 本地守护 | 跑在 `127.0.0.1:4317`，数据不出本机 |
| 无需重启 | Claude Code 会话期间无缝切换，不打断当前任务 |
| 100% 本地 | 无云依赖、无外部服务 |

## 适合什么场景

- 同时持有多个 Claude Pro / Max 订阅账号、需要把额度「拼起来」重度使用 Claude Code 的开发者。
- 想给关键编码任务加一层「单账号不够用就自动 failover」保险的个人 / 小团队。
- 想统一管理「Anthropic 订阅 + API key + 其他供应商凭证」避免重复登录的 AI 重度用户。

## 与相关概念的关系

- [Claude Code](./tool-claude-code.md) — Claude Unlimited 专门为 Claude Code 提供多账号 failover 能力，是其使用体验的扩展层。
- [Claude Account] — 同账号管理方向的工具，互为补充。

## 参考

- 项目链接：<https://github.com/DevDock-AI/claude-unlimited>

![preview](https://pbs.twimg.com/media/HSY2w3DbIAA5SLk.jpg)
