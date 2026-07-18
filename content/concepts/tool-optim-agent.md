---
type: "Tool"
title: "optim-agent（Optim-Agent/optim-agent）"
description: "Python 工具，把 Claude Code / Codex / OpenCode 等编程智能体接入超参数寻优流程：每个参数可写一段自然语言说明，智能体结合历史试验推荐下一组配置，但参数范围和最终打分仍由框架把关。"
tags: "[agent, claude-code, codex, opencode, hyperparameter, optimization, prompt-engineering]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/Optim-Agent/optim-agent"
---

# optim-agent（Optim-Agent/optim-agent）

## 它是什么

[`optim-agent`](https://github.com/Optim-Agent/optim-agent) 是 Optim-Agent 开源的「**让编程智能体替你跑超参数寻优**」工具：

- 你写一段 Python 训练 / 评估代码；
- 每个超参数可以用一段**自然语言说明**告诉智能体「这个参数大概管什么、应该怎么动」；
- 工具把任务交给 Claude Code / Codex / OpenCode 等 Agent；
- Agent 看历史试验 + 参数说明，**推荐下一组配置**；
- 但**参数范围、终止条件、最终打分仍由框架本身卡死**——不让 Agent 自由发挥跑飞。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Agent 接入 | 支持 Claude Code / Codex / OpenCode 等主流编程 Agent |
| 自然语言参数说明 | 每个超参数可附带描述，Agent 据此推理 |
| 历史试验记忆 | Agent 能看到前几轮跑了什么、效果如何 |
| 安全护栏 | 参数范围 / 终止条件 / 打分函数框架自管 |
| 闭环寻优 | 试验 → 评分 → 改参数 自动循环 |

## 解决的问题

| 痛点 | optim-agent 的应对 |
|------|--------------------|
| 工程师一遍遍手调超参数 | 让 Agent 在小循环里替你试 |
| LLM 瞎给离谱参数 | 框架强制约束范围 |
| Agent 推荐无法复现 | 每次试验都记日志，可回溯 |
| LLM 评分不客观 | 框架仍用真实代码跑打分 |

## 适合什么场景

- 训练脚本 / 评估脚本有大量「可调旋钮」；
- 调参空间不算巨大、但用人脑搜太累；
- 想把 Claude Code / Codex / OpenCode 真正「嵌进 ML pipeline」做半自动调优。

## 参考链接

- [原始链接](https://github.com/Optim-Agent/optim-agent)

## 相关概念

- [MOMO CODE](tool-momo-code.md) — 同样基于编程 Agent 的「自我进化」思路；optim-agent 走「外部寻优」路线，MOMO CODE 走「自我微调」路线
- [matterloop](tool-matterloop.md) — matterloop 提供 Agent 流程的「不跑飞」护栏，optim-agent 解决「怎么让 Agent 跑得更好」，两者互补