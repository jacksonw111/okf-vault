---
type: "Tool"
title: "brain0（Brain0-ai/brain0）"
description: "Agent 时代的 git 归因工具:被动观测 git 仓库与 agent 会话,把每次提交归因到具体意图、读过的文件和一张风险图,定位「哪句 prompt 改坏了代码」。"
resource: "https://github.com/Brain0-ai/brain0"
tags: "[agent-observability, git, attribution, risk-graph, developer-tools]"
timestamp: "2026-07-14T09:14:00Z"
---

# brain0

[brain0](https://github.com/Brain0-ai/brain0) 是面向「agent 写代码」时代的 **git 归因工具**:被动观察 git 仓库与 agent 会话,把每一次提交归因到具体的**意图、读过的文件、风险图**。

## 问题背景

> 现在大半 diff 都是 agent 写的,出了问题却查不到是哪句 prompt 动的

当 coding agent(Claude Code / Codex / Cursor 等)成为提交主力时,**prompt 与代码的因果链断了**——出问题时你既看不到是谁/什么触发的修改,也没法快速回滚至正确版本。

## 关键能力

| 能力 | 说明 |
|------|------|
| 被动观测 | 不修改 agent 行为,纯旁观 git 与会话日志 |
| 意图归因 | 每次 commit 对回具体 prompt / 会话意图 |
| 文件来源 | 标出这次改动「读过 / 修改过」的文件清单 |
| 风险图 | 给每次改动打一张风险拓扑,定位可疑变更 |
| 可审计 | 出问题时能像传统 git blame 一样看清来龙去脉 |

## 适合什么场景

- **代码评审**:Agent 提了 PR,reviewer 想直接看到对应的 prompt 历史。
- **事故复盘**:线上 bug 要回溯到「agent 何时在何 prompt 下改了哪段」。
- **团队合规**:为金融机构 / 重审计团队准备的「AI 提交可追溯」方案。
- **个人调试**:观察自己 agent 的 prompt → 行为模式,改写更高效的指令。

## 与同类资源的差别

| 资源 | 特征 | brain0 |
|------|------|--------|
| tokenscope | token 用量 / 费用 | 不观测 token,只观测 git 与会话意图 |
| kcap-cli | 会话生命周期 / 子代理树 / 工具调用 | 关注会话结构;brain0 关注「提交 ↔ 意图 ↔ 文件」的因果链 |
| AgentStalker | 把 agent 当系统来审计(污点图) | 偏安全;brain0 偏工程归因 |

## 参考链接

- [项目仓库](https://github.com/Brain0-ai/brain0)

## 相关概念

- [kcap-cli](./tool-kcap-cli.md) — 同样面向 AI 编码助手的可观测性 CLI,kcap 看会话结构,brain0 看 git 归因
- [AgentStalker](./tool-agent-stalker.md) — 偏安全的 Agent 审计工具,与 brain0 互补(安全 vs 工程)
- [Mobius](./tool-mobius-agent-os.md) — 自进化 Agent OS,brain0 是其下的归因观测组件的可能性
