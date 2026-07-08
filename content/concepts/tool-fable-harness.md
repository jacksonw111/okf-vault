---
type: "Tool"
title: "fable-harness（Claude Code 行为协议 / 纪律化流程）"
description: "即插即用的 Claude Code 行为协议：通过 hooks、skill 和子代理，让 Opus / Sonnet / Haiku 每次会话都遵循「先取证、明说假设、重大结论前求反对意见、用真实测试证明改动有效」的纪律化流程。"
resource: "https://github.com/Miguok/fable-harness"
tags: "[claude-code, hooks, skill, sub-agent, discipline, engineering-practice]"
timestamp: "2026-07-08T12:40:00Z"
---

# fable-harness

## 它是什么

[fable-harness](https://github.com/Miguok/fable-harness) 是一套**即插即用的 Claude Code 行为协议**——通过 hooks、skill 和子代理，给 Claude Code 的每次会话**强制加上「纪律」**。

不是 prompt 调优，而是**直接在 hook 层卡流程**。

## 四大纪律

| 纪律 | 含义 |
|------|------|
| 先取证 | 任何判断必须有证据 / 引用，禁止凭空下结论 |
| 明说假设 | 不确定的事必须明示假设，不让它隐藏在结论里 |
| 重大结论前求反对意见 | 关键判断前主动找反例 / 反证 |
| 用真实测试证明改动有效 | 改动跑通测试才算「有效」，禁止「应该没问题」 |

## 关键能力

| 能力 | 说明 |
|------|------|
| Hooks | 在工具调用前 / 后强制卡流程 |
| Skill | 提供可复用的纪律子流程 |
| 子代理 | 把「找反例 / 跑测试」这类动作外包给子 agent |
| 即插即用 | 装上就生效，无需手写 prompt |
| 跨模型适用 | Opus / Sonnet / Haiku 都生效 |

## 适合谁

- 严肃工程团队，希望把 Claude Code 用得像「团队新人」一样守规矩。
- 个人深度 Claude Code 用户，希望减少「幻觉结论」「凭空修复」等常见失误。
- 任何觉得「AI 太自信」而想加约束的人。

## 参考链接

- [项目仓库](https://github.com/Miguok/fable-harness)

## 相关概念

- [Claude Code Best Practice](./tool-claude-code-best-practice.md) — 同为 Claude Code 使用规范，但偏 prompt 调优
- [Claude Code Tipsy Skill](./tool-claude-code-tipsy-skill.md) — 同为 Claude Code 增强 Skill