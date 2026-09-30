---
type: Tool
title: "habitat-cli（Codex / Claude Code 会话本地归档与审计）"
description: "把 Codex 和 Claude Code 的编码会话留存在本机 SQLite 里并可检索审计；只有需要团队共享时才有选择地上传，避免敏感代码默认上云。"
resource: "https://github.com/wusterbuilds/habitat-cli"
tags: [codex, claude-code, session-log, sqlite, privacy, audit, local-first]
timestamp: 2026-09-30T00:26:00Z
---

# habitat-cli

## 它是什么

**habitat-cli** 是 [wusterbuilds](https://github.com/wusterbuilds) 维护的命令行工具：把 **Codex** 和 **Claude Code** 的编码会话**默认留在本机**（写入 SQLite 库），并支持本地检索 / 审计；只有当用户**显式需要团队共享**时才会选择性上传。

设计思路的核心是**"敏感代码默认不上云"**——而不是默认同步到团队空间，需要分享时再由人主动选择。

## 为什么用它 / 适合什么场景

- 公司 / 团队代码涉及敏感业务（金融、医疗、内部系统），不希望编码会话默认同步到任何云端。
- 希望以后能**回查某次 Codex / Claude Code 会话做了什么**——本地 SQLite 提供可检索的归档。
- 想用同一种归档 / 审计能力覆盖多个 Agent（Codex + Claude Code）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 覆盖 Agent | Codex、Claude Code |
| 存储 | 本机 SQLite |
| 默认行为 | 留本机，不上传 |
| 共享方式 | 用户显式选择性上传 |
| 检索 | 本地可搜索 |
| 审计 | 支持 |

## 参考链接

- 仓库：<https://github.com/wusterbuilds/habitat-cli>

## 媒体

- ![](https://pbs.twimg.com/media/HTWwRAObsAAz6G5.jpg)

## 相关概念

- [Claude Code](./note-claude-code-startups-guide.md) — habitat-cli 归档的对象之一
- [Codex 标准开发流](./playbook-codex-standard-devflow.md) — 同为 Codex 生态工具