---
type: "Tool"
title: "claude-token-optimizer（Claude Code 自动加载文档精简工具）"
description: "nadimtuhin 开源的 Claude Code 上下文精简 CLI：`cto init` 给项目生成精简的 CLAUDE.md + .claudeignore + 核心文档，旧任务 / 会话记录 / 归档文件不再被自动加载；还能估算 token、压缩 CLAUDE.md、安装 12 个可选 Hooks。"
resource: "https://github.com/nadimtuhin/claude-token-optimizer"
tags: "[claude-code, token-optimization, claude-md, context-engineering, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# claude-token-optimizer（Claude Code 自动加载文档精简工具）

## 它是什么

[claude-token-optimizer](https://github.com/nadimtuhin/claude-token-optimizer) 是 nadimtuhin 开源的 **Claude Code 上下文精简 CLI**——解决「**Claude Code 自动加载的文档太多，token 占用爆炸**」问题：

跑 `cto init` 后：
- 项目得到一份**精简的 `CLAUDE.md`**
- 生成 **`.claudeignore`** 文件
- 旧任务 / 会话记录 / 归档文件**不再被自动加载**

工具还能：
- 估算当前 token 占用
- 检查文档结构
- 压缩 `CLAUDE.md`
- 归档过期内容
- 安装 **12 个可选 Hooks**

## 为什么用它 / 适合什么场景

- 用 Claude Code 一段时间后，`CLAUDE.md` 越写越长，每次启动白白烧 token。
- 团队项目积累了大量 session 记录 / 历史任务，**被自动加载但没人看**。
- 想给 Claude Code 加一条**「过期内容自动归档」** 的工程化护栏。
- 想**系统化地**估算项目文档的 token 成本，而不是凭感觉。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | CLI（`cto` 命令） |
| `cto init` | 初始化：精简 CLAUDE.md / .claudeignore / 核心文档 |
| Token 估算 | 实时估算当前自动加载文档的 token |
| 结构检查 | 检查文档结构是否合理 |
| CLAUDE.md 压缩 | 自动瘦身 |
| 归档 | 把过期内容移出自动加载区 |
| Hooks | 12 个可选 Hooks |

## 相关概念

- [Context Engineering（上下文工程）](./term-context-engineering.md) — 围绕「上下文窗口怎么选 / 排 / 省」的工程实践，本工具是其一个具体落地
- [claude-token-optimizer Skill](./tool-claude-token-optimizer.md) — 与本工具相关的 Skill 形态包装
- [Claude Account](./tool-claude-account.md) — Claude 账号与多账号管理