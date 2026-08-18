---
type: Tool
title: "nopus (Vistyy/nopus)"
description: "编码助手回复的「抽象度检测器」：扫描非常用词、名词堆叠、套话式开头等特征，超阈值就要求重写为更具体的表达，避免 AI 腔"
resource: "https://github.com/Vistyy/nopus"
tags: [code-agent, code-review, anti-jargon, readability, cli]
timestamp: "2026-08-18T12:00:00Z"
---

# nopus (Vistyy/nopus)

## 它是什么
`Vistyy/nopus` 是一个针对 Pi / Claude Code / Codex 等**编码助手回复**的「抽象度检测器」：扫描模型输出，识别非常用词、抽象词句、名词堆叠、短语密度过高、套话式开头等特征；一旦超过阈值就**要求重写为更具体的表达**，减少「AI 腔 / 万能句式」对编码协作体验的污染。

## 为什么用它 / 适合什么场景
- 觉得 AI 编码 agent 的回复越来越「正确但空洞」：堆概念不点问题。
- 想把「去 AI 腔」变成**自动化、每次回复都执行的硬约束**，而不是靠人 review。
- 团队希望统一编码助手的回复风格：具体、可执行、有证据。

## 关键能力
| 能力 | 说明 |
|------|------|
| 抽象词检测 | 词频数据 + 人工评分具体性词典，量化「抽象度」 |
| 多特征打分 | 非常用词 / 名词堆叠 / 短语密度 / 套话开头一起算 |
| 按比例打分 | 比例与密度而非长度，长回复不会被误判 |
| 预处理剔除代码 | 先去掉代码块与标识符，避免误伤技术词 |
| 触发重写 | 超阈值自动要求模型重写一版 |

## 媒体
- ![](https://pbs.twimg.com/media/HPz0jXpbEAAbm61.png)

## 相关概念
- [项目链接](https://github.com/Vistyy/nopus) — 仓库地址
