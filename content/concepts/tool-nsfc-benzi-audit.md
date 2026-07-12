---
type: Tool
title: "nsfc-benzi-audit（国自然基金申请书结构化诊断 Skill）"
description: "用于国家自然科学基金申请书初稿结构化诊断的 Agent Skill，帮申请人找逻辑断点并给出可执行的修改清单。"
resource: "https://github.com/jiankang1991/nsfc-benzi-audit"
tags: [tool, agent-skill, nsfc, proposal-audit, research]
timestamp: 2026-07-12T16:30:00Z
---

# nsfc-benzi-audit（国自然基金申请书结构化诊断 Skill）

## 它是什么
专门给国家自然科学基金（NSFC）申请书初稿做结构化诊断的 Agent Skill：把申请书按立项依据、研究内容、研究方案、可行性等标准章节拆开，自动找逻辑断点（依据与内容脱节、目标与方案错位、技术路线断裂等），并给出可执行的修改清单（"在 X 节补 Y 段""调整 Z 处表述以呼应 §3"）。

## 为什么用它 / 适合什么场景
- 写 NSFC 申请书（青年 / 面上 / 重点）初稿，想在送同行 / 导师评审前先做一轮机器辅助的"逻辑体检"。
- 团队多人合写申请书，需要统一的"质量门"（CI / 流水线形式）做最后一道审查。
- 想把"找逻辑断点"这件事从导师头脑里搬到 AI agent 上，节省沟通成本。

## 关键能力
| 能力 | 说明 |
|------|------|
| 章节级拆解 | 按 NSFC 标准章节解析申请书 |
| 逻辑断点识别 | 找出依据 → 内容 → 方案 → 可行性之间的逻辑断裂 |
| 可执行修改清单 | 输出"在哪一节补什么 / 改什么"的清单 |
| Agent Skill 打包 | 按 Agent Skills 协议分发，便于 CLI 加载 |

## 参考链接
- [项目链接](https://github.com/jiankang1991/nsfc-benzi-audit)
- [原始链接](https://x.com/QingQ77/status/2076157350730502502)

![nsfc-benzi-audit 截图](https://pbs.twimg.com/media/HM7QH1la0AE2WZf.jpg)

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — nsfc-benzi-audit 是按 Agent Skills 协议分发的领域 Skill