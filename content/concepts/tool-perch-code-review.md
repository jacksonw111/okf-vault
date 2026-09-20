---
type: "Tool"
title: "Perch（AI 代码审查：方法级逐个 + 调用上下文）"
description: "lakeday-org/perch：用模型逐个读方法、连同调用者与被调用者一起看，找出传统规则式 linter 抓不到的缺陷、漏洞和重构点。"
resource: "https://github.com/lakeday-org/perch"
tags: "[code-review, ai, static-analysis, refactoring, security]"
timestamp: "2026-09-20T18:00:00Z"
---

# Perch

## 它是什么

[lakeday-org/perch](https://github.com/lakeday-org/perch) 是一个 **AI 代码审查工具**——和传统规则式 linter 不同，它**用模型逐个读方法**，并且把**调用者与被调用者**一起看进去。

目标：找到 linter 抓不到的问题——

- **逻辑缺陷**
- **安全漏洞**
- **可被重构的点**

## 为什么用它 / 适合什么场景

- ESLint / RuboCop / golangci-lint 只能查**规则层面的问题**，跨方法 / 跨调用链的语义缺陷抓不到。
- 想做 **PR-level 语义审查**——读懂「这个方法在它的调用上下文里是不是合理」。
- 在意**漏洞挖掘**——传统 SAST 太吵，AI 阅读上下文能给出更高信号的报告。

## 关键能力

| 能力 | 说明 |
|------|------|
| 方法级逐读 | 不是扫整个仓库，是一个方法一个方法读 |
| 调用上下文 | 同时看调用者 + 被调用者，理解方法在系统里的角色 |
| 缺陷 / 漏洞 / 重构 | 覆盖三类传统 linter 抓不到的语义问题 |
| 模型驱动 | 用 LLM 做阅读与判断 |

## 项目链接

- 仓库：<https://github.com/lakeday-org/perch>

## 媒体

![](https://pbs.twimg.com/media/HSn0MwqagAAggH0.jpg)

## 相关概念

- [Cloudflare security-audit-skill](./tool-cloudflare-security-audit-skill.md) — 同为「多阶段代码 / 安全审查」类工具
- [shadcn/improve](./tool-shadcn-improve.md) — 用最强模型审计代码的另一思路
