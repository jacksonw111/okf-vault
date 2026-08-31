---
type: "Tool"
title: "codex-with-chatgpt（让 ChatGPT 订阅当 Codex 的规划大脑）"
description: "把网页版 ChatGPT 的闲置订阅额度变成 Codex 编码会话的「规划与审查大脑」，让 Codex 只负责执行。"
resource: "https://github.com/XiaoDuoYa/codex-with-chatgpt"
tags: [codex, chatgpt, subscription, planning, coding-agent]
timestamp: "2026-08-31T16:00:00Z"
---

# codex-with-chatgpt

## 它是什么

[codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) 是 [XiaoDuoYa](https://github.com/XiaoDuoYa) 开源的小工具：

- 把**网页版 ChatGPT 的闲置订阅额度**——平时用不完的 Plus / Pro 配额——变成 **Codex 编码会话的「规划与审查大脑」**；
- 让 ChatGPT 负责**高层规划 + 审查**（更擅长 reasoning 的模型），Codex CLI 只负责**实际执行**（代码生成）。

## 为什么用它 / 适合什么场景

- **ChatGPT Plus / Pro 订阅额度闲置**：很多用户用不完，codex-with-chatgpt 让这部分额度别浪费；
- **模型分工**：规划 / 审查用强 reasoning 模型，执行用专门的代码模型；
- **降低 Codex 成本**：Codex 的执行成本不必花在自己规划上。

## 关键能力

| 能力 | 说明 |
|------|------|
| ChatGPT ↔ Codex 桥 | 闲置订阅额度转规划大脑 |
| 角色分工 | ChatGPT 规划 / 审查，Codex 执行 |
| 开源 | GitHub 仓库公开 |

## 相关概念

- [CodexPro](tool-codexpro.md) — ChatGPT Web ↔ 本地仓库 MCP 桥
- [Codex Control Plane MCP](tool-codex-control-plane-mcp.md) — Codex Desktop 任务队列 MCP
- [Codex CLI](tool-codex-cli.md) — OpenAI 官方 Codex 命令行

## 参考链接

- 项目链接：<https://github.com/XiaoDuoYa/codex-with-chatgpt>