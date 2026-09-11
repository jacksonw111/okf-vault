---
type: "Tool"
title: "Pocket Battle Lab / pokemonlive（本地宝可梦对战 + AI 表现层）"
description: "本地运行的宝可梦对战原型：纯 JavaScript 规则引擎判定命中 / 伤害 / 属性克制 / 异常状态，AI 只负责表现层；DeepSeek 规划分镜，fal 系列模型生成战斗片段，三槽播放器边播边预热。"
resource: "https://github.com/xflare-bot/pokemonlive"
tags: "[game, pokemon, ai-video, javascript, rule-engine]"
timestamp: "2026-09-11T22:00:00Z"
---

# Pocket Battle Lab / pokemonlive

## 它是什么

[xflare-bot/pokemonlive](https://github.com/xflare-bot/pokemonlive) 是一个**本地运行的宝可梦对战原型**，特色是把「**规则**」与「**表现**」彻底分离：

- **规则层**：纯 JavaScript 规则引擎处理命中判定、伤害公式、属性克制、异常状态——所有战斗数据可复算、可回放、可审计。
- **表现层**：玩家选招后，DeepSeek 规划分镜脚本，fal 的 MiniMax H3 Max 系列模型生成攻击、收回、登场与收尾片段，MiniMax 语音合成训练家喊招。
- **三槽播放器**：边播一段边预热下一段，体感流畅不卡顿。

## 为什么用它 / 适合什么场景

- 想学「**规则 / 表现分离**」架构：游戏逻辑用确定性引擎，AI 只负责「好看 / 好看听」。
- 想做 AI 驱动玩法的实验性 demo（不需要真发行，但要有可玩骨架）。
- 想研究 fal / DeepSeek / MiniMax 三家模型在游戏叙事里的分工协作。

## 关键能力

| 能力 | 说明 |
|------|------|
| 规则引擎 | 纯 JS 实现命中 / 伤害 / 属性 / 状态，可复算可审计 |
| AI 分镜 | DeepSeek 把「选招」转成「镜头列表」 |
| AI 视频生成 | fal 系列模型生成攻击 / 收回 / 登场 / 收尾片段 |
| 语音合成 | MiniMax 合成训练家喊招 |
| 三槽播放器 | 边播边预热下一段，避免卡顿 |
| 本地运行 | 整套在本地跑，离线可用 |

## 参考链接

- 项目仓库：<https://github.com/xflare-bot/pokemonlive>

## 媒体

- ![](https://pbs.twimg.com/media/HRvf4_7aEAAgVPA.jpg)

## 相关概念

- [Gorest](./tool-gorest.md) — Codex 驱动的 2D 动画精灵表生成与场景合成
- [mewu-ai](./tool-mewu-ai.md) — 截图 + AI 配套（OCR / 翻译 / 表格提取 / AI 讲解）
</content>
</invoke>