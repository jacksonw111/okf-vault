---
type: Playbook
title: "Orca 工单编排流程（/grill → /spec → /tickets → /orchestration）"
description: "一套把 AI 编码会话拆成讨论层与执行层的流程：先 /grill 澄清需求、/spec 写文档、/tickets 拆工单，再用 /orchestration 派工给子代理串行 / 并行推进并自动验收。"
resource: "https://x.com/taresky/status/2076137012776808745"
tags: [playbook, ai-coding, orchestration, agent-workflow, tickets]
timestamp: 2026-07-12T16:30:00Z
---

# Orca 工单编排流程

## 适用场景
- 想让 AI 编码 agent 把"讨论需求 → 写文档 → 拆工单 → 并行实现 → 自动验收"串成一条流水线，而不是每次都新开对话让单个 agent 一次性跑完全部步骤。
- 一组连续工单（#33 ~ #37）需要并行 / 串行推进，并在结束时由监工统一收口、逐一验收。

## 前置条件
- AI 编码 CLI（如 Codex、Claude Code、Codex CLI 等支持自定义命令 / 子代理的运行时）。
- 能识别 `/grill`、`/spec`、`/tickets`、`/orchestration` 等自定义 slash 命令的 agent harness。
- 仓库里有清晰的工单编号（如 `#33-#37`），子代理可按编号定位任务。

## 步骤
1. **/grill**：用提问式命令反复澄清需求边界、隐含假设、边界条件——这一阶段禁止写代码。
2. **/spec**：把讨论结果整理成结构化需求 / 设计文档（包含验收标准）。
3. **/tickets**：把 spec 拆成可独立交付的小工单，每张工单有明确输入 / 输出 / 验收条件。
4. **/orchestration**：新开对话进入监工模式，根据工单依赖关系派工给子代理（codex / claude / gpt 等）串行或并行执行；子代理完成时监工自动验收（无需人工逐张检查）。
5. **多模型分工**（可选）：讨论 / 文档 / 定票交给擅长长上下文思考的模型（如 Claude Fable 5），监工与快速执行交给响应速度快的模型（如 Grok），单票实现交给擅长编码的模型（如 gpt-sol）。

## 验证 / 自检
- [ ] /grill 阶段没有产生任何代码改动（除 prompt 文件外）。
- [ ] /spec 输出包含可测试的验收标准，而非空话。
- [ ] /tickets 拆出的工单粒度均匀，每张可在一段 agent 会话内完成。
- [ ] /orchestration 结束时所有工单状态 = 已验收 或 已驳回，没有"未知"状态。

## 角色搭配示例
| 角色 | 任务 | 推荐模型倾向 |
|------|------|---------------|
| 讨论 / 文档 / 定票 | /grill、/spec、/tickets | 长上下文、推理强（如 Claude Fable 5） |
| 监工 / 快速执行 | /orchestration | 响应快（如 Grok） |
| 单票代码实现 | /implement | 编码强（如 gpt-sol） |

## 参考链接
- [原始链接](https://x.com/taresky/status/2076137012776808745)
- [转发来源](https://x.com/Wen_Zw/status/2076157289866891564)

## 相关概念
- [Fable Harness（先取证 / 明说假设 / 求反对意见 / 用真实测试证明有效）](tool-fable-harness.md) — 同一作者团队倡导的"agent 行为协议"，与本工单编排流程配套使用
- [Agent Skills（代理技能包）](term-agent-skills.md) — /grill、/spec、/tickets 等 slash 命令本质是 Agent Skills 协议的实例