---
type: "Tool"
title: "pi-agenticoding（Pi 编码智能体的可组合工作流层）"
description: "为 Pi 编码智能体加一层可组合工作流层：把「哪些专家参与 / 用什么模型 / 谁能改代码 / 哪些决定要留」这类编排规则写进提示词或 Skills 里，让关键评审这类流程可以照着重复执行。"
resource: "https://github.com/agenticoding/pi-agenticoding"
tags: [agent-workflow, pi-agent, coding-agent, orchestration, skills, prompt-engineering]
timestamp: "2026-09-01T11:25:00Z"
---

# pi-agenticoding

## 它是什么
[pi-agenticoding](https://github.com/agenticoding/pi-agenticoding) 给 [Pi](note-pi-agent-core-book.md) 这类编码智能体**加一层可组合的工作流**。它把「**哪些专家参与 / 用什么模型 / 谁能改代码 / 哪些决定要留**」这些**编排规则**写成提示词或 Skill，让关键评审这类流程可以**照着重复执行**。

定位：**不是另一个 Agent 框架**，而是「在已有 Agent 之上**组织流程**」的工作流层——把单点 LLM 调用升级成可复用的、可版本化的多人协作剧本。

## 为什么用它 / 适合什么场景
- 想把「**关键代码评审**」「**架构评审**」「**安全审计**」这类**多角色流程**沉淀成可重复运行的剧本；
- 想让 Agent 的角色 / 模型 / 权限等元规则**写在文件里**（可版本化、可审计），而不是每次口头约定；
- 想给 Pi 编码智能体加一个**可组合**的工作流层，而不是重新搭一套 Agent 框架；
- 想把「专家 A 评审 → 专家 B 实现 → 主管 C 决策」这种流程用 YAML / 提示词描述出来。

## 关键能力

| 能力 | 说明 |
|------|------|
| 可组合工作流 | 把多个 Agent 步骤编排成可复用剧本 |
| 提示词 / Skills 承载 | 流程规则写在 prompt 或 Skill 文件里 |
| 角色分配 | 「哪些专家参与」可声明 |
| 模型绑定 | 不同环节可绑不同模型 |
| 权限隔离 | 「谁能改代码」可逐环节控制 |
| 决策留痕 | 「哪些决定要留」可以强制记录 |
| 关键评审脚本 | 内置可照着跑的评审剧本 |
| 版本化 | 流程本身可进版本控制 |

## 相关概念
- [Headcount](tool-headcount.md) — 同样把 Agent 能力「分部门 / 分角色」组织；Headcount 走「公司化技能框架」，pi-agenticoding 走「可组合工作流层」

## 参考链接
- 项目链接：<https://github.com/agenticoding/pi-agenticoding>