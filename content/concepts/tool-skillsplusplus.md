---
type: "Tool"
title: "SkillsPlusPlus（cpcc/SkillsPlusPlus）"
description: "用 Tauri 2 打造的桌面端 Skills 管理工具, 聚合 skills.sh、LobeHub、SkillHub.cn 等来源的 AI 技能, 并一键安装/卸载/重装到 Codex、Claude、Cursor、Gemini CLI 等十余种 AI 工具的本地目录。"
resource: "https://github.com/cpcc/SkillsPlusPlus"
tags: "[skills, agent-skills, tauri2, desktop, installer, ai-tools]"
timestamp: "2026-07-17T05:41:00Z"
---

# SkillsPlusPlus

[SkillsPlusPlus](https://github.com/cpcc/SkillsPlusPlus) 是一个 **Tauri 2 桌面应用**, 用来集中管理散落在各家「技能市场」的 Agent Skills。它从 [skills.sh](https://skills.sh/)、[LobeHub](https://lobehub.com/)、[SkillHub.cn](https://skillhub.cn/) 等多个来源拉取 Skill, 然后**一键安装 / 卸载 / 重装**到 Codex、Claude、Cursor、Gemini CLI 等十余种 AI 工具的本地 skills 目录, 不再需要手动复制粘贴。

## 它解决了什么

Agent Skills 是一种「把流程 / 提示词 / 上下文封装成可分发单元」的产物, 当前痛点:

- 来源分散 (skills.sh / LobeHub / SkillHub.cn / 各 GitHub 仓库)
- 目标分散 (Codex / Claude / Cursor / Gemini CLI / Cline / OpenCode ……)
- 每多一种组合都得手动维护目录

SkillsPlusPlus 用一个 GUI 把上述三个分散统一起来:

| 分散轴 | SkillsPlusPlus 处理 |
|--------|------|
| 来源 | 多源聚合到一个列表 |
| 目标 | 选择「安装到谁」即可批量同步 |
| 行为 | 安装 / 卸载 / 重装三个动作, GUI 一键 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源聚合 | skills.sh / LobeHub / SkillHub.cn |
| 多目标同步 | Codex / Claude / Cursor / Gemini CLI 等 10+ AI 工具 |
| 一键三动作 | install / uninstall / reinstall |
| Tauri 2 桌面 | 单 binary 跨平台, 不依赖浏览器 |

## 媒体

![](https://pbs.twimg.com/media/HNRPouKaUAAgQIF.jpg)

## 参考链接

- [项目仓库](https://github.com/cpcc/SkillsPlusPlus)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的本质定义, SkillsPlusPlus 是它的桌面端管理实现
- [mattpocock/skills](./tool-mattpocock-skills.md) — Real Engineers 风格合集, 可被 SkillsPlusPlus 安装到本地
- [shadcn/improve](./tool-shadcn-improve.md) — 强模型审计 Skill, 同样可经 SkillsPlusPlus 部署
