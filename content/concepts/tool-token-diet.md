---
type: "Tool"
title: "token-diet（Shell 实现的编码代理令牌优化技能）"
description: "一个 Shell 实现的令牌优化技能，适用于 Claude Code、Codex、Cursor、Windsurf、Cline 五种编码代理；从七个方面削减令牌，平均减少约 31%，输出减少 30%–81%，正确性不受影响。"
tags: "[token, optimization, shell, agent, claude-code, codex, cursor, windsurf, cline]"
timestamp: "2026-07-06T14:10:00.000Z"
resource: "https://github.com/Kulaxyz/token-diet"
---

# token-diet（Shell 实现的编码代理令牌优化技能）

## 它是什么

[`token-diet`](https://github.com/Kulaxyz/token-diet) 是一个用 **Shell 脚本**实现的「令牌减肥」技能包，给 AI 编码代理装上后自动从七个维度削减 token 消耗。它适用于 **Claude Code、Codex、Cursor、Windsurf、Cline** 五种主流编码代理。

## 它做什么

从七个方面优化：

1. **回复措辞** — 让输出更紧凑
2. **文档注释** — 收敛冗余 docstring
3. **测试用例** — 避免生成冗余/重复的测试
4. **代码生成** — 生成更精简的实现
5. **上下文读取** — 按需读取而非全量
6. **工具调用** — 合并 / 精简工具调用
7. **子代理委托** — 让子代理更高效地分工

## 效果

- 平均减少 **~31%** 的令牌消耗
- 输出减少 **30%–81%**
- 正确性不受影响

## 为什么用 Shell 实现

Shell 实现意味着：

- **零依赖**：不挑运行时，macOS / Linux / WSL 都能跑
- **可审计**：每一条规则都是一个简单脚本，可以逐条 review
- **易于修改**：团队可以基于自己的 token 计费策略微调规则

## 适用场景

- 高频使用编码代理，月度 token 账单肉疼
- 想优化代理行为让它少说废话、少写冗余测试
- 想给团队统一一套「省 token」的代理规范

## 参考链接

- [项目链接](https://github.com/Kulaxyz/token-diet)

## 相关概念

- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量与费用估算
- [kcap-cli](tool-kcap-cli.md) — 给 AI 编码助手的可观测性 CLI，捕获会话生命周期 + token 用量
- [Cliare](tool-cliare.md) — 给命令行界面打「Agent 就绪评分」的运行时审计工具