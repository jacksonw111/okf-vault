---
type: "Tool"
title: "pstack（SpaceX 工程师开源的 AI 写代码护栏）"
description: "cursor/plugins 中的 pstack 技能集：针对「用 AI 写代码但质量难保证」的痛点，提供三个关键 Skill——自动生成 Feature Map、测算爆炸半径、严格驱动模式（含 23 套工程剧本）。"
resource: "https://github.com/cursor/plugins/tree/main/pstack"
tags: "[agent-skills, cursor, ai-coding, verification, feature-map, dev-playbook]"
timestamp: "2026-09-14T21:25:00Z"
---

# pstack（SpaceX 工程师开源的 AI 写代码护栏）

## 它是什么

[pstack](https://github.com/cursor/plugins/tree/main/pstack) 是 SpaceX 工程师在 Cursor 插件仓库里开源的 **Skills 集合**。它针对「**用 AI 写代码，但质量难保证**」这个痛点，提炼出 **3 个核心 Skill** 给 Agent 调用。

## 三个核心 Skill

### 1. 自动生成 Feature Map
扫描代码自动绘制**界面交互地图**，让 AI 能直接跑模拟器或控制台操作 UI，自测真实运行结果，而不是只看代码。

### 2. 测算爆炸半径（Blast Radius）
改代码前**强制 AI 拿运行证据自证**：不会引发连带故障，不会破坏既有功能。

### 3. 严格驱动模式（Strict Driving）
根据任务自动匹配**排障、性能分析等 23 套工程剧本**，杜绝 Agent 偷懒与废话输出。

## 为什么用它

- 思路是「**验证 > 生成**」：AI 写代码快，**但你没办法信任没验证过的代码**。pstack 给 AI 一整套**自我验证剧本**。
- 「**爆炸半径**」概念是工业级（来自 SpaceX 的工程文化），不是学院派的软件工程概念——落到 AI 编码场景里有强约束力。
- 比单条 lint 规则更系统：直接给 Agent 整套「**怎么写、怎么验、怎么不出格**」剧本。

## 关键能力

| 能力 | 说明 |
|------|------|
| Feature Map | 自动 UI 交互地图 + 自测路径 |
| Blast Radius | 改前自证不爆炸 |
| 23 套剧本 | 排障 / 性能 / 重构等可复用流程 |
| Cursor 集成 | 在 Cursor 插件仓库里直接启用 |

## 项目链接

- 仓库（子目录）：<https://github.com/cursor/plugins/tree/main/pstack>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — pstack 是 Skill 思路在 AI 编码场景的工业级实践
- [gap-trap](tool-gap-trap.md) — 同样解决「AI 写代码守规矩」，思路是合约 / 规则