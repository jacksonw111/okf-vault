---
type: Tool
title: "retok（Claude Code / Codex CLI 用量与省 token 建议）"
description: "分析 Claude Code 与 OpenAI Codex CLI 的使用日志，估算 token 成本并给出可执行的省 token 建议。"
resource: "https://github.com/d-date/retok"
tags: "[claude-code, codex-cli, analytics, token-cost, optimization, transcript]"
timestamp: "2026-07-09T20:50:00Z"
---

# retok（Claude Code / Codex CLI 用量与省 token 建议）

## 它是什么
`d-date/retok` 是一个**编码 agent 用量审计与优化**工具：

- **直接读** Claude Code 与 OpenAI Codex CLI 的本地日志
- **估算** token 用量与成本
- **给出** 可执行的省 token 建议（"你这段 prompt 里 X 是冗余 / 这段工具输出可以截断 / Y 任务可以用更小模型"）

## 为什么用它 / 适合什么场景
- 想知道**一个月到底给 Claude Code 烧了多少钱**——按项目 / 任务 / 模型拆开。
- 想看到具体的**省 token 优化点**：不仅是报表，retok 会说"这里怎么改能省钱"。
- 适合：重度 Claude Code / Codex 用户、团队 AI 编码预算管理、个人开发者省钱。
- 对比：[quickai](tool-quickai-claude-cost.md) 仅做 Claude Code 静态切片报表，retok 跨 Claude Code + Codex 并能落地建议。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 CLI 支持 | Claude Code + OpenAI Codex CLI |
| 本地日志读取 | 不上传隐私 |
| token 成本估算 | 按项目 / 模型汇总 |
| 省 token 建议 | 可执行的具体建议（截断 / 改写 / 换模型） |
| 跨 CLI 对比 | 看 Claude Code vs Codex 哪个更划算 |

## 相关概念
- [quickai](tool-quickai-claude-cost.md) — 本地 Claude Code transcript 剖析工具，按任务 / 子代理 / 模型维度统计
- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量
- [kcap-cli](tool-kcap-cli.md) — 给 Claude Code / Codex CLI 的可观测性 CLI，捕获会话生命周期

## 参考链接
- 项目链接：<https://github.com/d-date/retok>
