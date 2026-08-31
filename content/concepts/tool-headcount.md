---
type: "Tool"
title: "Headcount（Claude Code 技能公司化组织）"
description: "把 Claude Code 的 agent 技能组织成一家\"公司\"：16 个部门、146 项技能，每个部门都能独立安装，项目只需加载真正用到的部分。"
resource: "https://github.com/cbrock84/headcount"
tags: [claude-code, agent-skills, organization, modular, plugin]
timestamp: "2026-08-31T16:00:00Z"
---

# Headcount

## 它是什么

[Headcount](https://github.com/cbrock84/headcount) 是 [cbrock84](https://github.com/cbrock84) 维护的 **Claude Code 技能组织框架**——把零散的 agent 技能组织成一家「**公司**」：

- **16 个部门**：HR / 财务 / 法务 / 工程 / 设计 / 营销……每个部门是一个独立可安装的包；
- **146 项技能**：分布在这些部门里；
- **按需加载**：项目只需 `install` 真正会用到的部门，不会拖一堆冗余技能。

## 为什么用它 / 适合什么场景

- **Claude Code 技能管理**：默认技能混在一个目录里、难以分类，Headcount 给了一套**企业组织架构**式管理；
- **避免 context 污染**：不用的技能不会被加载，节省 context；
- **跨项目复用**：同一套部门结构在多个项目里都能用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 16 个部门 | 模拟公司架构的功能分组 |
| 146 项技能 | 跨部门完整技能库 |
| 部门级安装 | 按需 `install <dept>`，不拖冗余 |
| Claude Code 集成 | 与 Anthropic Claude Code 工具链无缝配合 |

## 媒体

- 项目截图：![](https://pbs.twimg.com/media/HRBEpz0bEAA6ocd.jpg)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念的元定义
- [Matt Pocock Skills](tool-mattpocock-skills.md) — 另一类 Claude Code 技能合集
- [Claude Code](tool-claude-code.md) — Anthropic 终端 AI 编码 agent

## 参考链接

- 项目链接：<https://github.com/cbrock84/headcount>