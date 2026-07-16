---
type: "Note"
title: "《深入理解 AI Agent：设计原理与工程实践》（bojieli/ai-agent-book）"
description: "bojieli 在图灵 2025 年 8~10 月《AI Agent 实战营》课程整理的开源电子书——围绕 Agent = LLM + 上下文 + 工具 核心公式展开十章,从 Harness 工程到多 Agent 协作的全景。"
resource: "https://github.com/bojieli/ai-agent-book"
tags: "[ai-agent, book, harness, multi-agent, mcp, open-source, education]"
timestamp: "2026-07-15T19:40:00Z"
---

# 《深入理解 AI Agent：设计原理与工程实践》

[ai-agent-book](https://github.com/bojieli/ai-agent-book) 是基于 2025 年 8~10 月图灵《AI Agent 实战营》课程整理的开源电子书——围绕核心公式 **`Agent = LLM + 上下文 + 工具`** 展开十章,把 Agent 工程化的每个主要侧面系统化。

## 章节目录

| 章 | 主题 | 关键内容 |
|---|------|---------|
| 1 | Agent 基础知识 | 从「模型即 Agent」新范式出发,引入 Harness 工程概念 |
| 2 | 上下文工程 | 大模型 API 上下文结构 / KV Cache 友好设计 / 提示工程 / 动态提示词与 Agent Skills / 上下文压缩 |
| 3 | 用户记忆与知识库 | 用户记忆系统、RAG 管道、结构化索引与知识图谱 |
| 4 | 工具 | 工具分类与通用设计原则、MCP 协议、感知 / 执行 / 协作三类工具、异步 Agent |
| 5 | Coding Agent 与代码生成 | 生产级 Coding Agent 完整实现案例 |
| 6 | Agent 的评估 | 评估环境、数据集、指标体系、统计显著性、可观测性、评估驱动选型 |
| 7 | 模型后训练 | SFT / RL 三阶段,何时选 SFT、何时选 RL、RLHF 算法比较 |
| 8 | Agent 的自我进化 | 从经验中学习、主动工具发现、从工具使用者到工具创造者 |
| 9 | 多模态与实时交互 | 语音三范式、Computer Use、机器人操作 |
| 10 | 多 Agent 协作 | 协作分类框架、何时真正优于单 Agent、共享/不共享上下文、Agent 社会涌现 |

## 核心立场

- 把 Agent 视为「模型 + 上下文 + 工具」三件套,Harness 工程是真正竞争力的所在
- **上下文决定能力上限**:上下文设计比模型选型更重要
- **Coding Agent 是元能力**:可以创造新工具的工具
- **不评估 = 不可信**:评估驱动是 Agent 走向生产的必经之路

## 媒体

![](https://pbs.twimg.com/media/HNQd1tlagAA9QtI.jpg)

## 参考链接

- [项目仓库(原帖)](https://github.com/bojieli/ai-agent-book)
- [参考原始推文](https://x.com/bojie_li/status/2077318200543551502)

## 相关概念

- [Agent Skills(代理技能包)](./term-agent-skills.md) — 本书第 2、4 章专门论述的概念
- [12-Factor Agents](./tool-12-factor-agents.md) — 与本书「Agent 工程化」主线一致的另一份开源方法论
- [Claude Code](./tool-claude-code.md) — 本书第 5 章「Coding Agent」概念的工业级实现
