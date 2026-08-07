---
type: Tool
title: "Frog"
description: "wevm 团队用 TypeScript 写的 AI Agent 摩擦日志工具：agent 卡在怪问题上时跑 `frog log` 把现场与可复现材料归到 `.agents/friction-log/`，随代码一起提交；`frog publish` 把记录提成 GitHub issue，issue 关闭后 `frog/sync` 自动开 PR 删掉对应记录。"
resource: "https://github.com/wevm/frog"
tags: [agent-tooling, friction-log, github, wevm, observability, dev-workflow]
timestamp: 2026-08-06T11:30:00Z
---

# Frog

## 它是什么

wevm（wagmi / viem 团队）开源的 AI Agent「摩擦日志」工具。专门解决 agent 卡在怪问题上时开发者的痛点：当时到底发生了什么？复现路径是什么？相关代码状态是什么？

## 为什么用它 / 适合什么场景

- 你日常让 agent（Claude Code、Codex、Cursor 等）跑代码，但 agent 经常卡在「试试改这个就能好」却说不出为什么的角落。
- 想把这些「现场」沉淀到仓库里随代码一起 review，而不是丢在对话历史里蒸发。
- 想用 GitHub issue 当协作层：摩擦被解决 = issue 关闭 = 日志自动归档。

## 关键能力

| 能力 | 说明 |
|------|------|
| `frog log` | 把当时的情况和可复现材料一起归到 `.agents/friction-log/` 目录，随代码一起提交 |
| `frog publish` | 把每条记录提成一个 GitHub issue，issue 关闭后进入归档态 |
| `frog/sync` PR | issue 一关就开一个合并请求把对应日志条目删除 |
| 闭环 | 卡住 → 记录 → 解决 → 归档，全程代码与团队同步 |

## 相关概念
- [Better Harness](./tool-better-harness.md) — 五维审计 AI 编码工作流，每项绑证据
- [Agent Manager (tmux)](./tool-agent-manager-tmux.md) — TUI 架在 tmux 上统一管 Claude Code / Codex / OpenCode / Grok Build