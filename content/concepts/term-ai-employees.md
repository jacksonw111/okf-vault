---
type: "Term"
title: "Aiployees / 数字员工（AI Employees）"
description: "把业务流程按岗位（销售 / 客服 / 内容等）拆解成「带日程的 AI 员工」，每天自动跑任务并交简报，对外动作（发送 / 花钱）必须人工确认。"
resource: "https://github.com/markfulton/ai-employees"
tags: "[ai-agent, workflow, scheduler, digital-employee]"
timestamp: "2026-09-23T22:00:00Z"
---

# Aiployees / 数字员工（AI Employees）

## 它是什么

**AI Employees / Aiployees / 数字员工** 是一种**「按业务岗位组织 AI Agent」的范式**：把公司常见岗位（销售、客服、内容、运营、数据等）拆成独立的「员工文件夹」，每个员工：

- 跑在一个已有 AI Agent 上（Claude Code / Codex / Cursor 等）；
- 自带日程 / 触发器，按时或按事件启动；
- 每天早晨交一份简报；
- 所有「对外发送 / 花钱」类动作卡在**待人工确认**状态。

「Aiployees」是 GitHub `markfulton/ai-employees` 仓库对这一范式的具体实现（提供 8 个业务岗位模板）。

## 为什么重要

- **降低越权风险**：所有发送 / 付款类动作必须由人审批，AI 员工不会「自己掏钱」。
- **复用已有 Agent**：不需要新做一套 agent runtime，而是把岗位编排挂到用户已经在用的 Coding / General Agent 上。
- **贴近组织形态**：用「岗位 / 部门」而不是「工具 / 流程」组织 AI，更符合业务团队的认知。

## 适用场景

- 想让 AI 按日程跑日常业务，而不是手动起会话。
- 关注 AI 越权风险，需要强制审批关键动作。
- 希望直接复用现成的岗位模板，不想从零设计工作流。

## 相关概念

- [ai-employees](tool-ai-employees.md) — 该范式的具体开源实现（8 个岗位模板）
- [Agent Skills（代理技能包）](term-agent-skills.md) — 「员工文件夹」可视为按业务场景打包的 Skills 集合
