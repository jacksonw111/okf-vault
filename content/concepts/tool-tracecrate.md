---
type: "Tool"
title: "tracecrate（Agent 日志查看器）"
description: "纯前端的 Agent 日志查看工具：支持 Claude Code、Codex 和 OTLP 几种格式，解析成时间线、指标、异常模式和双会话对比；不联网、不要 key，分享前可脱敏。"
resource: "https://github.com/FankChen/tracecrate"
tags: "[agent, log-viewer, claude-code, codex, otlp, frontend]"
timestamp: "2026-09-12T22:30:00Z"
---

# tracecrate

## 它是什么

[FankChen/tracecrate](https://github.com/FankChen/tracecrate) 是**纯前端的 Agent 日志查看工具**：把 Agent 跑完产生的日志文件丢进来，本地解析成时间线、指标、异常模式、双会话对比；**不联网、不要 API Key**、分享前可脱敏。

## 核心特性

| 特性 | 说明 |
|------|------|
| 纯前端 | 浏览器里直接跑，无后端 |
| 多格式 | Claude Code / Codex / OTLP 日志 |
| 时间线 | 看 Agent 一段时间做了什么 |
| 指标聚合 | 关键指标可视 |
| 异常模式 | 高亮卡点 / 错误 |
| 双会话对比 | A / B 会话并排看 |
| 脱敏 | 分享前可一键脱敏 |

## 为什么用它 / 适合什么场景
- 想审计 Agent 跑完到底干了什么。
- 在两个会话里跑同一任务对比效果。
- 想分享日志给同事又怕泄露敏感信息。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源日志 | Claude Code / Codex / OTLP |
| 纯前端 | 不联网，隐私友好 |
| 时间线 | 看清执行顺序 |
| 双会话对比 | A/B 测试友好 |
| 脱敏 | 内置分享前处理 |

## 参考链接

- 项目仓库：<https://github.com/FankChen/tracecrate>

## 媒体

- ![](https://pbs.twimg.com/media/HR-yyhDbQAAtqeY.jpg)

## 相关概念
