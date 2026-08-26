---
type: "Tool"
title: "Encephalon（Claude Code 仓库级结论持久化）"
description: "isaachinman 给 Claude Code 等编码 Agent 做的「仓库级结论持久化」层：把上次决策 / 项目背景写成跟着仓库走的 JSON 小文件，agent 随时可查，避免「上次说过的事这次又忘了」。"
tags: "[claude-code, agent, memory, persistence, json, repo-level]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/isaachinman/encephalon"
---

# Encephalon（Claude Code 仓库级结论持久化）

## 它是什么

[`Encephalon`](https://github.com/isaachinman/encephalon) 是 isaachinman 给 Claude Code 等编码 Agent 写的「**仓库级结论记忆**」：

> 让 Claude 这类编码 agent 干活，最烦的是「上次的决策这次全忘了」，又得重新解释一遍项目背景。

Encephalon 把这些「**项目级决策 / 背景结论**」写成**跟着仓库走的 JSON 小文件**（不入 .gitignore，跟随分支走），agent 任何时候都可查，**不必重新解释项目背景**。

## 为什么用它 / 适合什么场景

- 长项目里 Agent 反复失忆、反复重读代码才回忆起决策
- 想把项目的**架构定论 / 选型理由 / 已否决方案**沉淀下来
- 不想因为团队成员 / Agent 切换就丢上下文
- 多 Agent 并行开发时（不同机器）需要一份**统一的项目级记忆**

## 关键能力

| 能力 | 说明 |
|------|------|
| 仓库级 JSON | 跟仓库走，多 Agent 共享 |
| 即查即读 | Agent 不用重读代码就能回忆决策 |
| 项目记忆 | 架构 / 选型 / 否决方案沉淀 |
| 与 harness 解耦 | 可挂 Claude Code / Codex / 其他 Agent |
| 轻量 | 无服务端，纯文件 |

## 媒体

![](https://pbs.twimg.com/media/HQiPv8AaUAExAnC.png)

## 参考链接

- [项目链接](https://github.com/isaachinman/encephalon)
