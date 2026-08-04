---
type: "Tool"
title: "Sol Advisor (DannyMac180/sol-advisor)"
description: "用 Codex 原生 subagent 把活分给两个角色——Sol 管架构和验收、Terra 负责实现；交差前再用一个全新上下文的 Sol 复审把关，没通过就不往下走。"
resource: "https://github.com/DannyMac180/sol-advisor"
tags: "[codex, subagent, agent-orchestration, code-review, architecture, ai-coding]"
timestamp: "2026-08-04T20:30:00Z"
---

# Sol Advisor (DannyMac180/sol-advisor)

## 它是什么

[Sol Advisor](https://github.com/DannyMac180/sol-advisor) 是一个**用 Codex 原生 subagent 编排双角色协作的模板**：

- **Sol**：管架构 + 验收
- **Terra**：负责实现
- **复审 Sol（全新上下文）**：交差前用一份全新上下文的 Sol 复审把关，**没通过就不往下走**

## 为什么用它 / 适合什么场景

- **角色清晰**：架构 / 验收 / 实现分三人，避免单一 agent 既写又审的盲区。
- **复审独立性**：复审 Sol 是**全新上下文**，不会受实现过程的 bias 影响。
- **硬闸门**：复审不过就停，符合"先把关再推进"的工程纪律。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双角色分工 | Sol（架构+验收） / Terra（实现） |
| 全新上下文复审 | 复审 Sol 不在实现上下文里，避免 confirmation bias |
| 硬闸门 | 复审不过不往下走 |
| Codex 原生 | 直接用 Codex 的 subagent 机制，不引入外部编排器 |

## 角色分工

| 角色 | 职责 |
|------|------|
| Sol | 架构 + 验收 |
| Terra | 实现 |
| 复审 Sol | 全新上下文复审，硬闸门 |

## 参考链接

- [项目仓库](https://github.com/DannyMac180/sol-advisor)

## 相关概念

- [Spec Superflow](./tool-spec-superflow.md) — AI 编码规划 → 实现硬闸，先想清楚再动手
- [Metis Coding Layer](./tool-metis-coding-layer.md) — 编程模型外层包装：改前查资料 + 改后自动构建测试
- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 6-Skill 编程纪律流水线
