---
type: "Tool"
title: "liurun-bookwriter-skills（liangdabiao/liurun-bookwriter-skills + luozhenyu-bookwriter）"
description: "中文商业写作风格 Skill 双件套:liurun-bookwriter 学刘润式商业洞察(SCQA / 8 心法 / 7 内容块 + 12 项自检),luozhenyu-bookwriter 学罗振宇式认知启发,Agent 接到一句话指令即按风格产稿,可导 PDF。"
resource: "https://github.com/liangdabiao/liurun-bookwriter-skills"
tags: "[agent-skills, writing, chinese, business-style, prompt-engineering, pdf]"
timestamp: "2026-07-15T12:23:00Z"
---

# liurun-bookwriter-skills

[liurun-bookwriter-skills](https://github.com/liangdabiao/liurun-bookwriter-skills) 是一套**给 AI Agent 用的中文商业写作风格 Skill**,包含两个互补子包:

- `liurun-bookwriter`:学**刘润**式商业洞察和方法论(把事讲透)。
- `luozhenyu-bookwriter`:学**罗振宇**式认知启发和商业务虚(把人点醒)。

## 它是什么

把两位中国商业作者**28 年的写作经验**压成结构化模板,丢进 Agent 的 skill 仓里—— Agent 接到「用 X 风格写篇关于 Y 的 32 条评论」一句话指令后,自己挑结构、选势能、找素材、动笔,一段写完等你点头再写下一段。

## 关键能力

| 能力 | 说明 |
|------|------|
| 结构化方法论 | 8 条心法 / 3 种结构 / SCQA 三种逻辑势能 / 5 商派 SCA++ 模板 / 7 种内容块 |
| 写作前自检 | 12 项质量自检先跑一遍再动笔 |
| 段落节奏控制 | 写一段等反馈再写下一段,避免一锤子产出后大改 |
| 风格可切换 | 同一 Agent 可随时切换「刘润 / 罗振宇」两种口吻 |
| 出稿 PDF | Python 脚本接 pandoc + XeLaTeX 出 PDF |

## 适合什么场景

- 自媒体写商业分析长文,想保持稳定调性又不愿每篇重读所有范文。
- 团队内训「商业写作」课,需要可复盘的样例生成器。
- 想验证「Agent 风格化输出」的可行性——这套是把风格显式工程化的样本。

## 参考链接

- [项目仓库](https://github.com/liangdabiao/liurun-bookwriter-skills)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 本项目是 Skills 概念在「写作风格」域的具体落地
- [hallmark-skill / prompt 风格合集](./tool-hallmark-skill.md) — 另一类「把模板放回 Skill 仓」的写作类样本
