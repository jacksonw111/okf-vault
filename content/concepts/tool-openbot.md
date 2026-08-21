---
type: Tool
title: "OpenBot（CopilotKit 出品的代理运行环境）"
description: "CopilotKit 开源的 Bot 运行时：每个 Bot 一台独立电脑（容器里的浏览器、登录态、文件），所有动作先过策略网关审批、留审计记录再执行，越权被拦、出事能查到记录。"
resource: "https://github.com/CopilotKit/OpenBot"
tags: [agent, bot, copilotkit, sandbox, audit, policy, runtime]
timestamp: 2026-08-21T12:25:00Z
---

# OpenBot（CopilotKit 出品的代理运行环境）

## 它是什么
OpenBot 是 CopilotKit 在 agent 落地过程中开出的一条产品线：把每个 Bot 都看成「一个独立的小员工」，给每只 Bot 发一台独立电脑——独立容器里的浏览器、独立登录态、独立的文件目录——并强制所有动作都要先经过策略网关（policy gateway）审批，留审计记录后才真正执行。Bot 想跑出权限 / 想越权访问会被拦下，出事后能逐条回放审计日志。

## 为什么用它 / 适合什么场景
- 想让 AI agent 真正接手「需要登录态、要操作第三方系统」的活，但不敢把真实账号直接交出去。
- 企业 / 团队场景：审计 / 合规是硬要求，agent 的每一步操作都需要可追溯。
- 已有 ChatGPT Operator / 各类 Computer-Use 但嫌权限模型粗糙，想要「一台电脑一个 Bot」的清晰边界。

## 关键能力
| 能力 | 说明 |
|------|------|
| 一 Bot 一电脑 | 每只 Bot 一个独立容器，内含独立浏览器、登录态、文件目录 |
| 策略网关 | 所有动作先经 policy gateway 审批，越权即拒绝 |
| 审计记录 | 每次动作留痕，出事可逐条回放、追责 |
| 登录态隔离 | Bot 之间账号 / Cookie 互不可见，泄漏面被收敛 |
| 与 CopilotKit 联动 | 上层 UI 仍可用 CopilotKit 的生成式 UI 能力展示 Bot 状态 |

## 一句话总结
**「一 Bot 一电脑 + 策略网关 + 审计」——把真实账号交给 AI 之前再加一层隔离与审批。**

## 原始链接
- [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) — 原始仓库

## 相关概念
- [CopilotKit](./concepts/tool-copilotkit.md) — 同团队的生成式 UI 框架，OpenBot 是它的 agent 运行时兄弟
- [AgentStalker](./concepts/tool-agent-stalker.md) — 把 LLM Agent 当系统而非模型来审计