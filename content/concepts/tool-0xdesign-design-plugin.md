---
type: "Tool"
title: "0xdesign / design-plugin（设计 / 精修 Plugin）"
description: "0xdesign 开源的 Claude / Cursor / Codex 等编码 Agent 设计 Plugin：把「设计 + 反复精修」流程沉淀成可调用的 Skill，让 AI 在做 UI 时直接按资深设计师的思路迭代打磨。"
resource: "https://github.com/0xdesign/design-plugin"
tags: "[agent-skills, plugin, design, ui, claude-code, cursor, codex]"
timestamp: "2026-10-03T00:00:00Z"
---

# 0xdesign / design-plugin

## 它是什么

[0xdesign/design-plugin](https://github.com/0xdesign/design-plugin) 是 **0xdesign** 开源的 AI 编码 Agent 设计 Plugin——给 Claude / Cursor / Codex 等编码代理加载后，Agent 会按资深设计师的工作思路（设计 + 反复精修）产出并打磨 UI。

## 为什么用它 / 适合什么场景

- **避免 AI 一次出图就交差**：让 Agent 按「先设计 → 再反复精修」的两段流程输出。
- **把审美规范装进 Plugin**：不必每次再贴 prompt，把规范固化成 Plugin 装一次就能反复用。
- **团队统一设计语言**：把同一份 Plugin 装到团队成员各自的编码 Agent 里，产出的界面风格更一致。

## 关键能力

| 能力 | 说明 |
|------|------|
| 类型 | Claude / Cursor / Codex Plugin |
| 核心流程 | design + refine（设计 + 反复精修） |
| 适用对象 | 编码 Agent 在做 UI 设计时调用 |
| 开源 | GitHub 公开维护 |

## 参考链接

- 项目链接：<https://github.com/0xdesign/design-plugin>
- 配套资源：<http://prodmgmt.world/resources>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Plugin 是 Skills 的一种具体落地形态
- [Hallmark Skill](./tool-hallmark-skill.md) — 同类「把设计规范装进 Skill」思路
- [taste Skill](./tool-taste-skill-redesign.md) — 同类让 AI 培养「设计品味」的 Skill
