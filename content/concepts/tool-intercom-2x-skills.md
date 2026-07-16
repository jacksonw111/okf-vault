---
type: "Tool"
title: "intercom-2x-skills（intercom/2x-skills）"
description: "Intercom Fin 2x 团队开源的 Claude Code 技能合集,覆盖开发、安全、审查、测试全流程,可直接挂到 Claude Code 上使用。"
resource: "https://github.com/intercom/2x-skills"
tags: "[claude-code, agent-skills, intercom, dev-tooling, security, code-review]"
timestamp: "2026-07-16T15:20:00Z"
---

# intercom-2x-skills

[intercom-2x-skills](https://github.com/intercom/2x-skills) 是 **Intercom Fin 2x 团队开源的 Claude Code 技能合集**——将他们在生产里使用的工程 agent 技能(开发、安全、审查、测试等)整体打包,可直接挂到 Claude Code 上使用。

## 它解决了什么

Intercom 的 Fin 2x 团队是 AI 工程化重实践者,他们把「让 Claude Code 在真实生产里少出错、写好代码」的技能沉淀成开源仓库。比起单条 skill 的散落,这套合集按场景(开发 / 安全 / 审查 / 测试)集成,工程师直接拉下来就能把自家 Claude Code 提升到同级别。

## 关键能力

| 能力 | 说明 |
|------|------|
| 开发类技能 | 含编码规范、提交消息、PR 描述、文档生成等开发场景 |
| 安全类技能 | 注入漏洞识别、依赖扫描、敏感信息处理等 |
| 审查类技能 | 代码评审、架构审查、设计模式识别等 |
| 测试类技能 | 单元测试生成、覆盖策略、回归用例整理等 |
| Claude Code 集成 | 直接放进 Claude Code 的 skills 目录即可生效 |
| 生产实践 | 来自 Intercom 真实工程实践,不是 demo 级 |

## 参考链接

- [项目仓库](https://github.com/intercom/2x-skills)

## 相关概念

- [Agent Skills(代理技能包)](./term-agent-skills.md) — 本工具是该生态下 Intercom 出品的实例
- [loopkit](./tool-loopkit.md) — 同样为多个 Agent runtime 准备的开源 Skill 合集,与本工具并列参考
- [Skillspec](./tool-skillspec.md) — Skill 质量审查工具,可用来审计本套 2x-skills
