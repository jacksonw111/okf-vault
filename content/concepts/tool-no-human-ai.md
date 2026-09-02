---
type: Tool
title: "no_human"
description: "本地优先的开源 AI 编码工厂：把工单变成经过评审的 Pull Request——先出计划、对抗式评审、防篡改测试、复现门禁，全程留在你的机器上。"
resource: "https://github.com/no-human-ai/no_human"
tags: [ai-coding, agent, local-first, pull-request, code-review]
timestamp: 2026-09-02T12:00:00Z
---

# no_human

## 它是什么

`no_human` 把"AI 编码代理"从"给个 prompt 出个 patch"推进到"工单 → 经过评审的 Pull Request"的全流水线：先让代理出实现计划 → 对抗式评审（另一代理 / 自检机制挑刺）→ 防篡改测试 → 复现门禁（验证 bug 真的能复现 / 修复），最后才生成 Pull Request 形态的产出物。整个流水线跑在用户本地机器上，不依赖外部 SaaS。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工单到 PR | 一条工单描述 → 一份完整 PR 输出 |
| 对抗式评审 | 计划 / 代码阶段都有对抗式评审挑刺 |
| 防篡改测试 + 复现门禁 | 测试与复现验证联动，避免"修复"无法复现的假阳性 |
| 本地优先 | 数据与流水线都在用户机器上 |

## 项目链接

- [项目主页](https://github.com/no-human-ai/no_human)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent
- [DeepSeek Harness 核心机制](./tool-deepseek-harness-core.md) — DSH 作为可插拔智能体框架
