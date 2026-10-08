---
type: "Tool"
title: "plot-is-all-you-need（科研画图样板册）"
description: "liouhai 开源：给 Claude Code / Codex 用的画图技能——图库里挑几张摆成样板册让你选，agent 拿你的数据照着画；公开部分有 95 张（14 张自画 + 81 张开放获取论文引用）+ 350 条只存卡片没存图的条目。"
resource: "https://github.com/liouhai/plot-is-all-you-need"
tags: "[plot, research, agent-skill, claude-code, codex, scientific-figure]"
timestamp: "2026-10-08T23:50:00Z"
---

# plot-is-all-you-need

## 它是什么

[plot-is-all-you-need](https://github.com/liouhai/plot-is-all-you-need) 是 liouhai 开源的「**科研画图样板册**」：

- 面向 **Claude Code / Codex**
- 用法：图库里挑几张摆成样板册 → 你挑一张 → agent 拿你的数据照着画
- 公开部分 95 张图：
  - **14 张**仓库自画（带代码）
  - **81 张**摘自开放获取论文（带鉴赏卡片）
- 另有 **350 条**只存卡片没存图的条目

## 解决什么问题

科研画图的两大老问题：

1. **prompt 难写**：风格 / 配色 / 排版的描述写得再细，Agent 也未必能复刻
2. **找不到参考**：自己憋不出好图，又不知去哪儿抄

解法：**给 agent 看图，让它模仿**——比写一堆规则更直接。

## 关键能力

| 能力 | 说明 |
| ------ | ------ |
| 形态 | Claude Code / Codex 的画图技能 |
| 图库 | 95 张公开图（14 自画 + 81 论文引用）+ 350 条卡片 |
| 选图方式 | Agent 直接看图、不靠规则描述风格 |
| 鉴赏卡片 | 每张图配说明卡片 |
| 自画代码 | 自画的 14 张图全部附带代码 |

## 适合谁

- 写论文 / 投稿被审稿人吐槽「图丑」的科研人
- 想给 Agent 注入「绘图审美」的 prompt 工程师
- 缺绘图参考的实验室团队

## 参考链接

- 项目链接：<https://github.com/liouhai/plot-is-all-you-need>

## 媒体

![](https://pbs.twimg.com/media/HUEw2IJaIAADGHz.jpg)
![](https://pbs.twimg.com/media/HUEw6YdbsAAzVa5.jpg)

## 相关概念

- [figgenie-skill](./tool-figgenie-skill.md) — 同为科研绘图 Agent Skill，但按顶会规范手工写 SVG