---
type: Tool
title: "Age of Agents（AI 编码会话像素艺术可视化）"
description: "本地跑的小网页，把 Claude Code / Codex / 其他 AI 编码会话渲染成一个宁静的像素艺术王国：写代码去铁匠铺、搜网页去魔法塔、跑终端去矿井，子代理围在身边、Token 堆仓库。"
resource: "https://github.com/agentsmill/age-of-agents"
tags: [visualization, pixel-art, agent, claude-code, codex, gamification]
timestamp: 2026-06-26T16:50:00Z
---

# Age of Agents

## 它是什么

Age of Agents 是一个**本地运行的小网页**，把 AI 编码会话**实时可视化为一个像素艺术王国**——一种"用游戏画面讲 Agent 在干什么"的可视化方案。

画面元素（拟人化）：

| AI 动作 | 像素王国对应 |
|---------|-------------|
| 写代码 | 铁匠铺 |
| 搜网页 | 魔法塔 |
| 跑终端 | 矿井 |
| 子代理调度 | 围在主代理身边的小工人 |
| Token 消耗 | 仓库里堆积的"产出" |

支持的 AI 编码工具：Claude Code、Codex、其他（按本地检测到的进程识别）。

## 为什么用它

| 痛点 | Age of Agents 解法 |
|------|--------------------|
| 看着终端不知道 Agent 在干到哪一步 | 看画面就知道 |
| 多个 Agent 并行想看调度 | 主代理 + 子代理的拟人化 |
| Token 烧得不明不白 | 仓库里看堆了多少"产出" |
| 干等焦虑 | 王国"宁静"风格，看着不焦 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时可视化 | 本地监听 Agent 进程，渲染像素王国 |
| 多 Agent 支持 | Claude Code / Codex / 其他 |
| 拟人化场景 | 工具调用 → 建筑 / 角色对应 |
| 子代理可视 | 主代理身边围着小工人 |
| Token 堆栈 | 仓库拟物化"消耗了多少 Token" |
| 宁静风格 | 不闪烁不吵闹，纯治愈 |

## 原始链接

- [项目仓库](https://github.com/agentsmill/age-of-agents)
- [原始推文剪藏](https://x.com/QingQ77/status/2070415013232435517)

## 相关概念

- [PeakCode（AI 编码代理的图形界面）](./tool-peakcode.md) — 同样把 AI 编码会话图形化，但走"严肃 GUI"而非"像素艺术"
- [repotato](./tool-repotato.md) — 把 GitHub 活动 TUI 化（终端而非像素艺术）
- [lex-ghostty-shaders](./tool-lex-ghostty-shaders.md) — 给终端本身"换肤"，让 Agent 工作时看着更舒服
