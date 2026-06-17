---
type: "Tool"
title: "Cabinet"
description: "Obsidian + AI 代理的组合：本地 Obsidian 知识库之上挂一层带「心跳和任务」的 agent 运行时；可导入 CSV / PDF，关键是能在文档里嵌入「内联 Web 应用」，让数据 / 工具在笔记里就活起来。"
tags: "[obsidian, ai, agent, knowledge-base, local-first]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://runcabinet.com"
---

# Cabinet

## 它是什么

[`Cabinet`](https://runcabinet.com) 是由 @HilaShmuel 公布的实验性项目：**Obsidian + AI Agent** 的本地优先组合。目标是补齐「LLM 缺一个能塞 CSV、PDF，关键还要能**内联 Web 应用**」的「知识库」缺口。

> "认识 Cabinet：Obsidian + AI 代理。很长一段时间以来，我一直在思考大型语言模型（LLMs）缺少知识库——一个我可以导入 CSV、PDF 的地方，最重要的是——内联 Web 应用。在你自己的 AI 上运行，带有心跳和任务的代理。"

## 为什么值得关注

- **本地优先**：和 [Obsidian](./tool-obsidian.md) 同源哲学——数据在自己机器上，AI 跑在自己的容器里。
- **「心跳 + 任务」代理**：不是一次性问答，是常驻 agent——能后台轮询、定时总结、跨笔记串信息。
- **内联 Web 应用**：在 Markdown 笔记里嵌入一个真正能交互的小组件（图表、看板、表单），而不只是「粘一段代码高亮的 JSON」。
- **给「Obsidian 只是 markdown 记事本」加点运行时**：本地文件 + 持久进程 + AI 调用 = 个人 AI 操作系统雏形。

## 与本知识库 OKF 的关系

| 维度 | Obsidian | OKF / 本知识库 | Cabinet |
|------|----------|----------------|---------|
| 文件格式 | Markdown | Markdown + YAML frontmatter | Markdown + **内联 Web App 块** |
| 运行时 | 无（纯静态编辑器） | 无（静态 bundle） | 有（常驻 agent + 心跳） |
| AI | 通过插件 | 通过 [PRODUCER.md 协议](./../PRODUCER.md) | 内建 |
| 离线 | 完全 | 完全 | 完全 |

可以理解为：**OKF 是「数据层」规范，Cabinet 是「带 AI 运行时的数据层」实现**。两者不冲突——Cabinet 的存储格式若遵守 OKF，可以直接被本知识库消费。

## 关键能力

| 能力 | 说明 |
|------|------|
| CSV / PDF 导入 | 结构化数据进知识库 |
| 内联 Web App | 笔记里嵌入可交互组件（图表、表单、计算器） |
| 心跳代理 | 定时 / 触发式任务，不需要用户主动问 |
| 本地 AI | 模型跑在自己的机器或私有容器 |
| Obsidian 兼容 | 文件可被 Obsidian 直接打开 |

## 风险 / 未知

- 项目公开时还在早期，心跳代理的可观测性 / 资源占用 / 权限模型需要观察；
- 内联 Web App 块需要约定格式——是否会成为新「DSL」或借力 Mermaid / HTML iframe，决定生态走向。

## 相关概念

- [Obsidian](./tool-obsidian.md)
- [OKF 是什么](./term-okf.md)
- [LLM Wiki 模式](./term-llm-wiki.md)
- [Agent Skills 是什么](./term-agent-skills.md)
- [Claude Code](./tool-claude-code.md)
- [在 Obsidian 里开始用 OKF](./playbook-okf-obsidian-start.md)
