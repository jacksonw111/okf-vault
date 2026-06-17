---
type: "Tool"
title: "shadcn/improve"
description: "shadcn 开源的 Claude Code skill：用「当下能拿到的最强模型」审计你的代码库、写实施计划、产出 backlog；核心思想——把智能当借来的，今天榨取它来建计划，明天用更便宜/开源/可控的模型来执行。"
tags: "[ai, agent, skills, claude-code, code-audit, planning]"
timestamp: 2026-06-17T00:00:00Z
resource: "https://github.com/shadcn/improve"
---

# shadcn/improve

## 它是什么

[`shadcn/improve`](https://github.com/shadcn/improve) 是 shadcn（[shadcn/ui](https://ui.shadcn.com) 作者）开源的一个 [Claude Code](./tool-claude-code.md) skill，本质是一段**精心调过的审计 prompt**——当你调用 `/improve` 时，它会：

1. 把整个代码库拉进上下文；
2. 用结构化方式巡检（依赖、类型、可访问性、安全、性能、可维护性…）；
3. **输出可执行清单**：每个改进点都有「问题 → 影响 → 建议改法」。

**和 [mattpocock/skills](./tool-mattpocock-skills.md) 的差别**：matt 的 skill 偏对话/工作流，improve 偏「重活一次跑完」。两者互补。

## 为什么用它的核心理由（shadcn 2026-06-14 公开说法）

> "鉴于发生的事情，我正在加倍投入到像 /improve 这样的技能上。
> 一个前沿模型被撤下了。如果它发生了一次，它就会再次发生。今天是 Fable。明天可能是 4.9，或者有一天是 gpt 6。
> 所以，把智能当作借来的东西。当它可用时就榨取智能。今天就建立一个计划目录。然后以后用更便宜的、开源的，或者你控制的模型来实施。
> 现在就建立待办事项 backlog。"

翻译成工程语言：

- **模型会下架**——把它的当下能力编码进**可复用的工件**（plan / backlog / docs），不要只存进聊天历史。
- **用最强的模型做最难的部分**：规划、审计、方向判断。
- **用便宜的模型做执行**：refactor、写测试、写样板。
- **背靠 skill 而不是 prompt**：plan 是文件、可以 review、可以 PR、可以版本管理。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全库审计 | 不是单文件 diff，是「整棵代码树」视角 |
| 结构化输出 | 改进项按类别分组，每条带严重程度 / 影响 / 建议 |
| Plan 工件 | 输出落到 `.md`，可当文档沉淀 |
| 模型无关 | prompt 设计成可换底层模型；今天用 Opus，明天可以换 Sonnet 甚至本地 |
| 集成简单 | `git clone` 之后 `/improve` 即可 |

## 典型工作流

```bash
git clone https://github.com/shadcn/improve .claude/skills/improve
claude
# 交互里：
# /improve
# 等待几分钟
# 读 .claude/improve-report.md（或类似产物）
# 把每条改成立 TODO，分批用便宜的模型执行
```

## 与本知识库的关系

- `improve` 的产物 = **「计划型概念」**——可以直接作为 [OKF](./term-okf.md) 里的 Note 或 Playbook 落进 `concepts/`。
- 配合 [PRODUCER.md 协议](./../PRODUCER.md)：把 `improve` 跑出来的 backlog 丢进 `inbox/`，由 agent 拆成多个概念执行。
- 是「前沿模型 + skill + OKF」三角闭环的典型代表。

## 相关概念

- [Agent Skills 是什么](./term-agent-skills.md)
- [Claude Code](./tool-claude-code.md)
- [mattpocock/skills](./tool-mattpocock-skills.md)
- [OKF 是什么](./term-okf.md)
- [PRODUCER.md 协议](./../PRODUCER.md)
