---
type: Tool
title: "photo-oracle"
description: "本地优先、只读、看重隐私的 AI Skill，把本地照片库变成「每日照片签」、记忆牌、三牌问题和月度星图这类带占卜感的自我回望玩法。"
resource: "https://github.com/sherrylein/photo-oracle"
tags: "[ai-skill, photo, self-reflection, local-first, privacy]"
timestamp: "2026-07-19T14:05:00Z"
---

# photo-oracle

## 它是什么

sherrylein/photo-oracle 是一个**本地优先、只读、看重隐私**的 AI Skill：把用户本机照片库作为「记忆数据库」，以**塔罗牌 / 占卜仪式**为隐喻，生成「每日照片签」「记忆牌」「三牌问题」「月度星图」等带占卜感的自我回望内容。

## 玩法

| 玩法 | 说明 |
|------|------|
| 每日照片签 | 每天抽一张过去某天的旧照 + AI 解读，作为当日「指引」 |
| 记忆牌 | 抽一张照片 + AI 把它当作牌面写一段感悟 |
| 三牌问题 | 围绕用户提问抽三张，AI 给「过去 / 现在 / 未来」式解读 |
| 月度星图 | 月底把本月照片聚成星座风格可视化，回望这个月 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先 | 照片 + 处理全在用户机器上，不上传云端 |
| 只读 | 不修改照片库原文件，避免污染素材 |
| 隐私看重 | 解读结果不分享、不外发，AI 调用可选本地模型 |
| Skill 形态 | 作为 Claude / Codex 等 Agent 的 Skill 加载，调用简单 |

## 适合谁

- 想要「日记 + 反思 + 仪式感」的个人用户
- 心理咨询 / 教练行业的辅助工具：用照片做隐喻引发来访者反思
- 重视数据主权、不愿把私人照片交给云端的本地优先用户

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 协议本身
- [finding-unknowns-skills](./tool-finding-unknowns-skills.md) — 8 个 Skill 套件

## 参考链接

- 项目链接: <https://github.com/sherrylein/photo-oracle>