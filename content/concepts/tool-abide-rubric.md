---
type: "Tool"
title: "Abide / quietglass（用 Jev 决策模型做 Agent 软规则检查）"
description: "QuietGlass 项目的 Abide 模块：把 Claude Code / Codex / OpenCode Agent 的 AGENTS.md / CLAUDE.md 软规则编译成 .abide/rubric.json，每次编辑和回合结束对每条规则向 Jev 决策模型问一个问题，Jev 只返回校准概率——0.8 以上当场修复、0.5–0.8 给用户看 note、0.5 以下静默。"
resource: "https://github.com/clintonimaroo/quietglass"
tags: "[agent-skills, jev, hooks, soft-rules, claude-code, codex, opencode]"
timestamp: "2026-10-03T00:00:00Z"
---

# Abide / quietglass

## 它是什么

[Abide](https://github.com/clintonimaroo/quietglass) 是 **clintonimaroo** 在 [QuietGlass](./tool-quietglass.md) 项目里的 Agent 软规则检查模块——把项目里的 `AGENTS.md` / `CLAUDE.md` **软规则**（lint 查不掉的「风格 / 命名 / 边界」类规则）编译成 `.abide/rubric.json`，**每次 Agent 编辑 / 每回合结束**，对每条规则向 TypeSafe 的 **Jev 决策模型**问一个问题；**Jev 只返回校准概率**，根据阈值决定后续动作。

## 阈值与动作

| 校准概率 | 动作 |
|---------|------|
| ≥ 0.8 | 让 Agent 在**同一回合修复** |
| 0.5 – 0.8 | 给用户看一条 note（不强制修复） |
| < 0.5 | 静默（不打扰） |

## 为什么用它 / 适合什么场景

- **Linter 抓不住「软规则」**：风格 / 一致性 / 命名习惯这些只能靠人审，Agent 写完代码常常「不漂亮但能用」。
- **决策模型便宜快速**：Jev 比调 LLM 便宜得多，可以每回合跑。
- **三档阈值减少打扰**：高确定违规立即修，不确定只提示，确定对的静默。
- **典型场景**：个人 / 团队的 Agent 工作流，让 AI 写代码同时守住风格底线。

## 关键能力

| 能力 | 说明 |
|------|------|
| 规则源 | AGENTS.md / CLAUDE.md |
| 编译产物 | `.abide/rubric.json` |
| 触发时机 | 每次编辑 + 回合结束 |
| 判定模型 | Jev（TypeSafe） |
| 输出 | 校准概率 |
| 兼容 Agent | Claude Code / Codex / OpenCode |

## 参考链接

- 项目链接：<https://github.com/clintonimaroo/quietglass>

## 相关概念

- [Jev（TypeSafe 结构化判定模型家族）](./term-jev.md) — Abide 用的判定模型
- [OneJev](./tool-onejev.md) — Jev 家族的多模态变体
- [QuietGlass](./tool-quietglass.md) — 同一仓库的 macOS 屏幕保护应用
