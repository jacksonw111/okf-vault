---
type: Tool
title: "taste-skill / redesign-existing-projects（Agent Skill：三步改造老项目视觉）"
description: "taste-skill 下的 redesign-existing-projects Skill：把改造老项目视觉这件事编码成 Scan → Diagnose → Fix 三步流程，让 Agent 能按部就班重设既有项目的设计语言。"
resource: "https://www.skills.sh/leonxlnx/taste-skill/redesign-existing-projects"
tags: [agent-skill, redesign, design, scan-diagnose-fix, taste]
timestamp: "2026-08-27T14:01:00Z"
---

# taste-skill / redesign-existing-projects

## 它是什么
[redesign-existing-projects](https://www.skills.sh/leonxlnx/taste-skill/redesign-existing-projects) 是 `leonxlnx/taste-skill` 这个出名 Skill 仓库下的一个**子 Skill**，专门用于**改造老项目的视觉 / 设计语言**。它把"重设既有项目"这件通常要靠设计师直觉的事，拆成清晰三步：

1. **Scan** — 扫描现有 UI / 设计 token / 样式规律；
2. **Diagnose** — 诊断问题点（不一致 / 不和谐 / 缺层次等）；
3. **Fix** — 按诊断结果改造并落地。

让 Agent 装上这个 Skill 后，就能按流程去改造一个老项目的视觉，而不是凭感觉乱改。

## 为什么用它 / 适合什么场景
- 手里有个能跑但「长得像上一代」的项目，想升级视觉又没时间做完整 redesign；
- 团队使用 Codex / Claude Code 等 Coding Agent，希望让 Agent 自动按统一方法重做设计；
- 想给团队沉淀一套"redesign 标准流程"，让新人 / Agent 都能跑同一套步骤。

## 关键能力
| 能力 | 说明 |
|------|------|
| 三步流程 | Scan → Diagnose → Fix |
| 适配 Coding Agent | 装进 Codex / Claude Code 等 Skill 仓 |
| 聚焦既有项目 | 与 taste-skill 全集一样，是为「已存在代码」改造设计 |
| 视觉一致性 | 按诊断结论改造，避免随手改 |
| 可复用 | 子 Skill 形式发布，可单独用也可纳入 taste-skill 全集 |

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念本身
- [UI Skills Top 10（社区精选 UI / 设计类 Skill 清单）](note-ui-skills-top10.md) — ui-skills.com 站点上的高赞 UI/设计 Skill，redesign-existing-projects 是其中"设计类"思路的延伸
- [shadcn/improve](tool-shadcn-improve.md) — 用最强模型审计代码，与本 Skill 思路都是「给 Agent 装上方法」而非「给 Agent 装上数据」

## 参考链接
- Skill 详情：<https://www.skills.sh/leonxlnx/taste-skill/redesign-existing-projects>
