---
type: Tool
title: "game-copycat"
description: "复刻休闲网页小游戏的 Agent Skill：给一句名字、推文或截图，端到端产出机制忠于原作、品牌与美术完全原创的可玩游戏。"
resource: "https://github.com/hellokaton/game-copycat"
tags: "[agent-skill, game-clone, web-game, generative, claude-code]"
timestamp: "2026-07-19T08:44:00Z"
---

# game-copycat

## 它是什么

hellokaton/game-copycat 是一个**给 Claude Code 用的 Agent Skill**：输入一句游戏名字、一段推文描述、或一张截图，端到端产出一款**机制忠于原作、品牌与美术完全原创**的可玩网页小游戏。它复刻的是「玩法的灵魂」（规则 / 循环 / 核心动作），而不是「像素级照抄」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模态输入 | 名字 / 文本描述 / 截图任选其一作 seed |
| 机制保真 | 玩法循环、胜负判定、操作手感对齐原作 |
| 资产原创 | 美术 / 角色 / 音效 / 品牌全部替换为新风格，规避 IP 风险 |
| 端到端生成 | 从需求理解到代码 + 资源 + 部署链接一条龙 |

## 适合谁

- 营销团队做怀旧主题活动，需要「灵感来自 XX 经典」的网页小游戏
- 设计 / 教学演示，把经典玩法当模板快速出原型
- 个人开发者想验证「这个经典玩法能不能加上自己的调性做成新东西」

## 与已有 Skills 的关系

- [codex-storyboard](./tool-codex-storyboard.md) — 短视频分镜台，也是「生成式 UI + 端到端」模式
- [Multi-Design PPT](./tool-multi-design-ppt.md) — 按 62 种品牌设计语言出 HTML/PPTX/PDF
- game-copycat 的差异点：**针对「游戏机制复刻」垂直场景**，从输入到可玩游戏一条龙

## 媒体预览

![](https://pbs.twimg.com/media/HNae6A3aUAExTIO.jpg)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 协议本身
- [finding-unknowns-skills](./tool-finding-unknowns-skills.md) — 8 个 Skill 套件（动手前/写时/写后）

## 参考链接

- 项目链接: <https://github.com/hellokaton/game-copycat>