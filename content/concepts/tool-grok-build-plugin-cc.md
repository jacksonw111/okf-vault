---
type: "Tool"
title: "Grok Build Plugin for Claude Code"
description: "xAI 官方开源的 Claude Code 插件，聊天框里输斜杠命令就能直接调本机 grok 二进制来审查代码、挑设计毛病、派任务、把当前会话导进 Grok；不走中间服务，靠插件自己记 PID 与日志跟踪运行状态。"
resource: "https://github.com/xai-org/grok-build-plugin-cc"
tags: "[xai, grok, claude-code, plugin, coding-agent]"
timestamp: "2026-07-20T20:20:00Z"
---

# Grok Build Plugin for Claude Code

## 它是什么

[xAI 官方开源](https://github.com/xai-org/grok-build-plugin-cc)的 **Claude Code 插件**。装好后 Claude Code 聊天框里多出一组斜杠命令，能直接调本机的 [Grok Build](./tool-grok-build.md) 二进制来干活——审查代码、挑设计毛病、派任务、把当前会话塞给 Grok。不依赖中间服务，grok 命令行在本机跑，插件自己记 PID 和日志查运行状态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 斜杠命令入口 | 在 Claude Code 对话框里输入 `/xxx` 直接调 Grok Build |
| 进程自追踪 | 通过 PID + 日志监控本机 grok 进程，实时回显状态 |
| 会话迁移 | 可把当前 Claude Code 会话上下文塞给 Grok Build 继续 |
| 零中间服务 | 不走第三方代理，grok CLI 在本地跑 |

## 相关概念

- [Grok Build](./tool-grok-build.md) — xAI 官方 AI 编码 agent 运行环境，被本插件驱动
- [Claude Code](./tool-claude-code.md) — 本插件的宿主

## 参考链接

- 项目链接: <https://github.com/xai-org/grok-build-plugin-cc>
