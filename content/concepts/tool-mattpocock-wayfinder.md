---
type: Tool
title: "mattpocock wayfinder skill（DAG + 战争迷雾的项目规划 Skill）"
description: "mattpocock skills v1.1 中的 /wayfinder Skill：把模糊大目标拆解成 DAG 节点地图（grilling / research / prototype / task 四类），并用「战争迷雾」机制标注 Frontiers 与未知区域。"
resource: "https://github.com/mattpocock/skills"
tags: "[mattpocock, wayfinder, skill, dag, agent-skills, project-planning, claude-code]"
timestamp: "2026-07-09T20:50:00Z"
---

# mattpocock wayfinder skill（DAG + 战争迷雾的项目规划 Skill）

## 它是什么
`mattpocock/skills` v1.1 中发布的 `/wayfinder` Skill，是整个 skill 套件里**范围最大的一个**：把一个大的、模糊的想法，拆解成一张像游戏地图一样的「DAG」。这张地图不只是任务列表，更带 4 种节点类型 + 战争迷雾 + Frontiers 概念。

## 四种节点类型（Ticket）

| 类型 | 缩写 | 含义 | 谁负责 |
|------|------|------|--------|
| grilling | HITL | 需要 grill 系列 skill 拷问人来决策 | 人 |
| research | AFK | 需要 Agent 去查资料 | Agent |
| prototype | HITL | 需要 prototype 系列 Skill 做原型 | 人 + Agent |
| task | HITL/AFK | 纯粹任务，只做不决策 | Agent |

- **HITL**：Human in the loop，需要人决策。
- **AFK**：Away from keyboard，给 Agent 跑就完事了。

## 战争迷雾模型

- **边**：节点之间的 blocking 关系，**有向**，ticket 间存在依赖，必须解锁前置才能处理某节点。
- **Frontiers（疆域）**：当前"未关闭 + 无未解阻塞 + 未被认领"的节点集合——地图里已经勘探清楚、成型为 ticket 的区域，相当于游戏里的「已知领土」。
- **Fog of War**：未知的、不明确的迷雾部分——地图上的战争迷雾。

## 设计理念

> "DAG + 战争迷雾 = 整个地图"

把整个项目规划过程**做成游戏**：每个 ticket 像一个 token，被处理像占领领土。前端自由度高（grill / research / prototype 三类节点可以独立拼装），后端规则极简（DAG + 阻塞关系）。

实际践行 **「解放 Human 到决策中，剩下的交给 Agent 执行」**——与 mattpocock 其他 skill 系列保持同一设计哲学。

## 关键能力
| 能力 | 说明 |
|------|------|
| 把模糊目标拆成 DAG | 一个入口 `/wayfinder` 就能起一张地图 |
| 4 类节点 | grilling / research / prototype / task |
| HITL / AFK 区分 | 节点元数据自带"是否需要人决策" |
| 战争迷雾 | 把"未知"与"已知"在同一张地图可视化 |
| 阻塞关系有向 | ticket 间显式表达依赖 |

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 协议本身
- [mattpocock/skills](tool-mattpocock-skills.md) — Real Engineers 风格的技能合集（wayfinder 隶属此套件）
- [Loop Engineering](tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论
- [firstmate](tool-firstmate.md) — 把终端编码 AI 变成「大副」，自动派多个 crewmate 并行干活

## 参考链接
- 原始介绍：<https://x.com/ninthbit_ai/status/2074903842882527306>
- 套件主仓库：<https://github.com/mattpocock/skills>
