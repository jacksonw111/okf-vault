---
type: Tool
title: "reverify"
description: "让 AI 只负责提假设、由确定性工具对二进制实物逐条裁决，从根上杜绝模型一本正经地编造 API、偏移和函数行为。"
resource: "https://github.com/2akouwu/reverify"
tags: [verification, deterministic, ai-testing, anti-hallucination]
timestamp: "2026-09-06T00:00:00Z"
---

# reverify

## 它是什么

[2akouwu/reverify](https://github.com/2akouwu/reverify) 是一套**反幻觉验证框架**：让 AI 只负责**提假设**（比如「这个函数的返回值应该是 X」），由**确定性工具对二进制实物逐条裁决**——例如直接跑目标二进制、读目标文件、做 SHA256 校验——再把裁决结果回喂给 AI。

定位：

- **AI 提假设、机器做证据**：把「判断真假」从 LLM 转移到外部确定性程序。
- **专注二进制 / 实物**：特别适合「AI 解释一段机器码 / 一个固件 / 一个二进制格式」这类容易编造的领域。

## 为什么用它 / 适合什么场景

- 反编译 / 逆向 / 固件分析：AI 经常凭空编 API 签名、偏移、函数行为。
- 想给 AI 套上「不准瞎猜」的可验证约束。
- 需要审计痕迹：每次裁决都基于真实工具调用，结果可复现。

## 关键能力

| 能力 | 说明 |
|------|------|
| AI 假设 | 模型只生成可证伪的假设 |
| 确定性裁决 | 用本地工具对二进制 / 实物逐条验证 |
| 反幻觉 | 从源头避免模型编造 API / 偏移 / 函数行为 |
| 可复现 | 验证步骤都是程序化调用，结果可重放 |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — reverify 可作为 Agent 工具集中的一类 Skill
- [Claude Code](./tool-claude-code.md) — 典型可应用 reverify 模式的工作环境

## 项目链接

- 项目主页：<https://github.com/2akouwu/reverify>
