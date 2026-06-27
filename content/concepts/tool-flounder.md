---
type: "Tool"
title: "Flounder（白帽安全审计 agent）"
description: "把编码 agent（Codex / Claude Code）包装为端到端白帽安全审计系统的 TypeScript 项目：准备目标 → 映射攻击面 → 深度审计 → 确认漏洞 → 生成报告，每一步都在沙箱隔离中执行。"
tags: "[security, audit, agent, typescript, white-hat]"
timestamp: "2026-06-27T00:57:00.000Z"
resource: "https://github.com/adshao/flounder"
---

# Flounder（白帽安全审计 agent）

## 它是什么

[`Flounder`](https://github.com/adshao/flounder) 是一个 **TypeScript 项目**，把已有的编码 agent（如 Codex、Claude Code）**包装为自主的白帽安全审计系统**。它把审计流程拆成「准备目标 → 映射攻击面 → 深度审计 → 确认漏洞 → 生成报告」五步，每一步都在沙箱隔离中执行，避免审计动作污染主环境。

![Flounder 安全审计](https://pbs.twimg.com/media/HLt87claYAALJq9.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 端到端审计 | 从目标准备到报告生成全流程 |
| 多 agent 适配 | 复用现有编码 agent（Codex / Claude Code）作为审计引擎 |
| 攻击面映射 | 系统化探索目标的可被攻击面 |
| 漏洞确认 | 在沙箱内反复验证可疑点 |
| 报告输出 | 把结果整理为可读审计报告 |
| 沙箱隔离 | 每一步都在隔离环境执行，安全可控 |

## 工作流程

1. **准备目标**：选定审计目标与范围
2. **映射攻击面**：自动探测 API / 接口 / 入口
3. **深度审计**：让 agent 在隔离沙箱中尝试攻击 / 复现
4. **确认漏洞**：二次验证可疑点，降低误报
5. **生成报告**：产出结构化审计文档

## 适用场景

- 团队需要定期对自家服务做安全体检
- 个人项目想复用现有编码 agent 的推理能力做漏洞挖掘
- 在受控沙箱里跑安全测试，避免污染开发环境

## 参考链接

- [项目链接](https://github.com/adshao/flounder)

## 相关概念

- [Claude Code](tool-claude-code.md) — Flounder 复用的编码 agent 之一
- [AgentStalker](tool-agent-stalker.md) — 另一类把 LLM Agent 当系统而非模型来审计的工具