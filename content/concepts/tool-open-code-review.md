---
type: "Tool"
title: "open-code-review（阿里 AI 代码审查助手）"
description: "阿里把内部用了两年的 AI 代码审查助手开源出来：不是通用 coding agent，而是专门做 review 的 harness。支持 BYOK 接入，也支持 Delegation Mode 把审查委托给别的 agent。"
resource: "https://github.com/alibaba/open-code-review"
tags: "[code-review, ai-review, harness, alibaba, byok, delegation]"
timestamp: "2026-09-13T08:50:00Z"
---

# open-code-review（阿里 AI 代码审查助手）

## 它是什么

[alibaba/open-code-review](https://github.com/alibaba/open-code-review) 是**阿里开源**的 AI 代码审查助手——**不是通用 coding agent**，定位是**专门做 review 的 harness**：只负责选文件 / 匹配规则 / 准备 diff，**审查动作本身**交给别的 agent。

## 为什么用它 / 适合什么场景

- AI 生成代码越来越多，需要**专门的 review 工具**而不是通用 agent。
- 想换模型 / 多模型轮换，但不想改 review 流程。
- 想把 review 流程**结构化**：选文件 → 匹配规则 → 准备 diff → 交给审查者。

## 关键能力

| 能力 | 说明 |
|------|------|
| BYOK（Bring Your Own Key） | 自带 API Key 接入 |
| Delegation Mode | 不需要 key，把 review 委托给已有 agent |
| 文件挑选 | 自动选要 review 的文件 |
| 规则匹配 | 按规则匹配审查重点 |
| Diff 准备 | 把上下文差量化准备 |
| 不是通用 agent | 专做 review，不抢 coding 的活 |

## 模式选择

| 模式 | 何时用 |
|------|--------|
| BYOK | 团队有 key 配额、想直接调用大模型 |
| Delegation | 已有 Claude Code / Cursor / Codex 等，把 review 交给它们，自己只负责调度 |

## 项目链接

- 仓库：<https://github.com/alibaba/open-code-review>

## 相关概念

- [Pi Review（earendil 团队）](./tool-pi-review.md) — 同类定位，Pi 生态专属
- [Harness Engineering](./term-harness-engineering.md) — open-code-review 是「专门做 review 的 harness」典型（term 暂未独立收录，留概念链接占位）