---
type: "Tool"
title: "Birdview（AI 编码工作流的架构可视化）"
description: "面向 AI 编程工作流的架构可视化工具：配套提供 Agent Skill，把默认流程改成「先建图、再声明变更范围、最后动手改代码」——逼 AI 动手前先把架构图与变更报备摆出来。"
resource: "https://github.com/Qiuner/birdview"
tags: "[ai-coding, architecture, visualization, agent-skill, workflow]"
timestamp: "2026-09-14T22:30:00Z"
---

# Birdview（AI 编码工作流的架构可视化）

## 它是什么

[Qiuner/birdview](https://github.com/Qiuner/birdview) 是一个面向 **AI 编程工作流的架构可视化工具**。它配套提供 **Agent Skill**，把 AI 编程默认的「上来就改代码」流程改成：

1. **先建架构图** —— 看清当前结构
2. **再声明变更范围** —— 这次动哪几个模块、证据是什么
3. **最后动手改代码** —— 改完对照声明验证

## 为什么用它

- AI 直接改代码最容易改崩，因为它不知道「动哪儿会影响哪儿」
- 逼 AI 先把架构图画出来、要动哪几个模块先报备、证据摆出来再动手
- 减少大代码库下 AI 改错的概率

## 关键能力

| 能力 | 说明 |
|------|------|
| 架构可视化 | AI 工作流里先有图 |
| 变更范围声明 | 改之前先报备动哪儿 |
| 证据驱动 | 每个变更都要给出依据 |
| Agent Skill 配套 | 直接接入 Claude Code 等 agent |
| 适配多 agent | 主流 AI 编程 agent 都能用 |

## 项目链接

- 仓库：<https://github.com/Qiuner/birdview>
