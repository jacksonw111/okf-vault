---
type: "Tool"
title: "Azure Skills Plugin（microsoft/azure-skills）"
description: "微软官方的 AI 代理插件：包含两层技能——其一是「Azure 工作流技能」教代理在什么时候用哪项服务、该验证什么、有哪些坑要避开；其二是「MCP Server 执行技能」配 200+ 工具覆盖 40+ 项 Azure 服务，让代理既懂做法又可直接执行。"
resource: "https://github.com/microsoft/azure-skills"
tags: [azure, mcp, agent-skills, microsoft, official, cloud, devops]
timestamp: "2026-07-27T20:30:00Z"
---

# Azure Skills Plugin（microsoft/azure-skills）

## 它是什么

`microsoft/azure-skills` 是**微软官方**出品的 AI 代理插件，主要干两件事：

1. **Azure 工作流技能**：教代理 **Azure 的工作套路**——什么时候用哪项服务、该验证什么、有哪些坑要避开；
2. **MCP Server 执行能力**：配上 **200 多个工具**，覆盖 **40+ 项 Azure 服务**，让代理不仅「知道」还能「直接做」。

## 为什么用它 / 适合什么场景

- 让通用 AI 编码代理（Claude Code / Codex / Cursor）**真正理解 Azure** 而不是只懂通用云概念；
- 希望通过 **MCP** 让代理直接调用 Azure 资源（部署、查询、监控）；
- 团队**全员上 Azure**，需要标准化的「该怎么做 / 不该怎么做」知识；
- 想用官方维护的技能集，减少自己写 SKILL.md 的维护负担。

## 关键能力

| 能力 | 说明 |
|------|------|
| Azure 工作流技能 | 教代理什么时候用什么服务、验证什么、避开什么 |
| MCP Server | 暴露 200+ 工具，覆盖 40+ 项 Azure 服务 |
| 微软官方 | 由 Microsoft 维护，跟 Azure 官方文档同步 |
| 可装多端 | 作为插件装到支持 MCP / Agent Skills 的代理 |
| 双层能力 | 既给知识（workflow）也给执行（tools） |
| 覆盖广 | 服务范围涵盖计算 / 存储 / 网络 / 数据库 / AI / DevOps |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOKBp52asAAsTOM.png)

- 项目链接：<https://github.com/microsoft/azure-skills>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Azure Skills 是一份具体的「云厂商工作流技能包」
