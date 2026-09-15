---
type: "Tool"
title: "Octop（腾讯云开源多用户多智能体本地 AI 平台）"
description: "TencentCloud/Octop：主打多用户、多智能体的本地私有化 AI 助手平台，单进程启动数据全存本地 SQLite，内置 16 种 MBTI 人格模板与专家库，自带 Web 控制台并原生支持飞书 / 钉钉 / 企业微信 / QQ / Discord；支持双向 ACP 协议，可直接调用 Claude Code / OpenCode 等 IDE 工具，并内置 Browser AI 与 Terminal AI。"
resource: "https://github.com/TencentCloud/Octop"
tags: "[self-hosted, multi-agent, ai-assistant, mbti, acp, tencent]"
timestamp: "2026-09-15T04:40:00Z"
---

# Octop（腾讯云开源多用户多智能体本地 AI 平台）

## 它是什么

[Octop](https://github.com/TencentCloud/Octop) 是腾讯云开源的**多用户多智能体本地私有化 AI 助手平台**。它不是单一对话框，而是给团队 / 家庭打造「**独立智能环境**」：一人单机部署，全团队或全家无缝共享多个定制化 AI 助手。

## 核心能力

| 维度 | 说明 |
|------|------|
| 多用户 | 团队 / 家庭共享同一部署 |
| 多智能体 | 内置多种 Agent，可并存 |
| 本地私有化 | 单进程启动，数据全存 `~/.octop/` SQLite |
| 人格模板 | 内置 **16 种 MBTI 人格** + 专家库 |
| 多渠道 | 自带 Web + 飞书 / 钉钉 / 企业微信 / QQ / Discord |
| ACP 协议 | 双向 Agent Client Protocol |
| IDE 集成 | 可委托 Claude Code / OpenCode 等 IDE 工具 |
| 浏览器自动化 | 内置 Browser AI |
| 终端协助 | 内置 Terminal AI |

## 关键架构亮点

### 1. 完全本地与隐私
- 单进程启动
- 数据默认全部存到本地 `~/.octop/` 的 SQLite
- 无需担心隐私泄露

### 2. 多角色无缝切换
- 内置 **16 种 MBTI 人格**模板与专家库
- 不同家庭成员 / 团队角色按需切换专属 Agent

### 3. 全渠道打通
- Web 控制台
- 飞书 / 钉钉 / 企业微信 / QQ / Discord 原生接入
- 在群聊里直接派发任务

### 4. 深度面向开发者
- **双向 ACP（Agent Client Protocol）**：既可调用外部工具，也能把复杂代码任务委托给 Claude Code / OpenCode
- 内置 **Browser AI**（网页自动化）和 **Terminal AI**（终端协助）

## 为什么用它

- 「**多用户 + 多智能体 + 本地化**」同时满足的产品不多——多数自托管 AI 平台要么不支持多用户，要么不支持多智能体。
- **MBTI 人格模板**是个有趣的产品思路：让 Agent 不只是工具，而有「**性格**」可切换。
- **ACP 协议 + 委托 Claude Code / OpenCode** 让 Octop 跟主流 IDE Agent **互通**而不是竞争。

## 适合谁

- 团队 / 家庭想本地化部署 AI 助手，又希望**多用户共享**
- 重视隐私（数据全本地 SQLite）
- 需要把 AI 助手集成进飞书 / 钉钉 / 企业微信 / QQ / Discord 群聊
- 想用 ACP 协议把 Octop 与 IDE Agent 组合起来的工程团队

## 项目链接

- 仓库：<https://github.com/TencentCloud/Octop>

## 相关概念

- [Self-Hosted（自托管）](term-self-hosted.md) — Octop 是面向 AI 助手的自托管代表
- [Multi-Agent（多智能体协作）](term-multi-agent.md) — 多个并存 Agent + 人格切换
- [MCP（Model Context Protocol）](term-mcp.md) — ACP 与 MCP 同类思想：Agent 与工具的开放协议