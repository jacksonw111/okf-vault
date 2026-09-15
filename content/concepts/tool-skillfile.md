---
type: "Tool"
title: "skillfile（跨机器 AI Skills 同步工具）"
description: "eljulians/skillfile：跨多台机器和多种 AI 编程工具（Claude Code / Cursor / Codex 等）统一管理 skills 与 agents，避免手动复制导致版本混乱和本地修改在上游更新时丢失。"
resource: "https://github.com/eljulians/skillfile"
tags: "[agent-skills, sync, dotfiles, devops, claude-code, cursor, codex]"
timestamp: "2026-09-15T15:10:00Z"
---

# skillfile（跨机器 AI Skills 同步工具）

## 它是什么

[skillfile](https://github.com/eljulians/skillfile) 把 AI Agent 的 **skills / agents 配置**当成 dotfiles 一类资产来管：一份仓库，多机器多 Agent 同步，避免「**手动复制 → 版本混乱 / 本地改掉后上游更新就被覆盖**」。

## 它解决的问题

| 痛点 | skillfile 的做法 |
|------|------------------|
| skills 在多机器 / 多工具间手动复制 | 单一仓库管理，命令一键同步 |
| 本地修改后上游更新会被覆盖 | Git 化的版本控制，本地 = 分支 |
| 不知道哪台机器的哪份 skill 是最新版 | 仓库即真相（single source of truth） |
| Claude Code / Cursor / Codex 各家目录不一样 | 抽象层适配各家路径 |

## 为什么用它

- 「**Skills 是个人知识资产**」这件事越来越被接受——但**没人用 Git 管它**。skillfile 是「把 skills 当代码」的工程实践。
- 与 `chezmoi` / `yadm` 等 dotfiles 管理器思路一致，**只是作用域聚焦在 Agent skills / agents 配置**。
- 适合重度 Agent 用户：家里一台机器、公司一台机器、还有云端 sandbox——三处都需要 skills。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨机器同步 | 一份仓库同步多台设备 |
| 多 Agent 适配 | Claude Code / Cursor / Codex 等多平台目录抽象 |
| Git 化版本控制 | 本地修改即分支，避免上游覆盖 |
| 防止漂移 | 单一来源，杜绝各机器 skills 漂移 |
| 轻量部署 | 像 dotfiles 管理器一样简单 |

## 媒体

视频演示：<https://video.twimg.com/tweet_video/HSOsxf5a0AAwJKC.mp4>

## 项目链接

- 仓库：<https://github.com/eljulians/skillfile>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — 它管的就是这些 Skill 的多机同步
- [Claude Code](tool-claude-code.md) — 兼容平台之一