---
type: Tool
title: "kunkun SkillHub（本地 Claude Code / Codex 技能盘点工具）"
description: "kunkun SkillHub 是个本地优先的桌面小工具，专门用来盘点、搜索和管理你电脑上装好的 Claude Code / Codex 技能。用 Rust + Tauri 2 写成，纯本地运行，扫描本机装好的 Claude Code / Codex 技能，统计个数、使用频次、适配软件和来源级别。"
resource: "https://github.com/duangjaiignacy-blip/kunkun-skillhub"
tags: [tool, agent-skills, claude-code, codex, tauri, rust, desktop]
timestamp: 2026-07-12T16:30:00Z
---

# kunkun SkillHub（本地 Claude Code / Codex 技能盘点工具）

## 它是什么
本地优先的桌面小工具，专为"我已经装了一堆 Claude Code / Codex 技能，但忘了装了啥、哪个高频、哪个有用"场景设计。用 Rust + Tauri 2 写成，纯本地运行，自动扫描本机已装的 Claude Code / Codex 技能，统计个数、使用频次、适配软件和来源级别（个人 / 团队 / 官方等）。

## 为什么用它 / 适合什么场景
- Skill 越装越多，自己都忘了有哪些，急需一个"本地应用商店"管理面板。
- 想按"使用频次 / 来源 / 适配软件"等维度盘点技能，识别冷门可清理项。
- 偏好 Tauri 桌面应用（资源占用低、不上传数据）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动扫描 | 扫描本机装好的 Claude Code / Codex 技能 |
| 多维统计 | 个数 / 使用频次 / 适配软件 / 来源级别 |
| 纯本地 | Rust + Tauri 2，数据不上云 |
| 搜索 / 筛选 | 快速定位需要的技能 |

## 参考链接
- [项目链接](https://github.com/duangjaiignacy-blip/kunkun-skillhub)
- [原始链接](https://x.com/QingQ77/status/2076328981939265905)

![kunkun SkillHub 截图](https://pbs.twimg.com/media/HM--jDBagAADfGN.jpg)

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — kunkun SkillHub 是 Agent Skills 生态的"应用商店 / 仪表盘"
- [LoopKit（33 个编码 agent 实战检验的技能文件包）](tool-loopkit.md) — 同属 Claude Code / Codex 技能生态的内容侧工具