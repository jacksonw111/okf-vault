---
type: "Tool"
title: "Stop Slop (letideafix)"
description: "教 LLM 去掉 AI 腔的技能包，核心是 SKILL.md + references 三份——要删的短语、要避的句式、改前改后的例子；带 5 个 1-10 分的评分维度（直接度、节奏、可信、像不像人、信息密度），凑不上 35 分就重写；可挂成技能、Claude 项目知识、自定义指令或塞进 system prompt。"
resource: "https://github.com/letideafix/stop-slop"
tags: "[ai-writing, slop, skill, llm-prompt, writing-quality, no-slop]"
timestamp: "2026-08-04T20:30:00Z"
---

# Stop Slop (letideafix)

## 它是什么

[Stop Slop](https://github.com/letideafix/stop-slop) 是一个**教 LLM 去掉 AI 腔的技能包**，核心是 `SKILL.md`，配 `references/` 目录拆成三份：**要删的短语**、**要避的句式**、**改前改后的例子**。

它点名禁用的有：

- **喉塞开头**
- **强调词**
- **商业腔**
- **副词**
- **空泛论断**

结构上要砍：

- **二元对比**
- **被动语态**
- **碎片化短句**
- **煽动式排比**

此外给了**直接度、节奏、可信、像不像人、信息密度**五个 1-10 分的评分维度，**凑不上 35 分就重写**。

![Stop Slop 截图](https://pbs.twimg.com/media/HOw3O_xbQAIZqec.png)

## 为什么用它 / 适合什么场景

- **可加载到任何大模型**：不绑定特定 LLM，按 skill 加载方式注入即可。
- **结构化评分**：5 维度评分避免主观"看着像不像"。
- **多种挂法**：技能、Claude 项目知识、自定义指令、system prompt 都行。

## 评分维度（每项 1-10，凑不上 35 重写）

| 维度 | 含义 |
|------|------|
| 直接度 | 有没有绕弯子 |
| 节奏 | 句子长短有没有变化 |
| 可信 | 论断有没有证据 |
| 像不像人 | 是不是 AI 腔 |
| 信息密度 | 多少废话 |

## 禁用清单（按类别）

| 类别 | 例子 |
|------|------|
| 短语 | 喉塞开头、强调词、商业腔、副词、空泛论断 |
| 句式 | 二元对比、被动语态、碎片化短句、煽动式排比 |

## 部署方式

| 方式 | 适用 |
|------|------|
| 挂成 Skill | Claude Code / Cursor 等 |
| Claude 项目知识 | 写到 Projects 的知识库 |
| 自定义指令 | Claude.ai 自定义指令 |
| System prompt | 直接注入 API 调用 |

## 参考链接

- [项目仓库](https://github.com/letideafix/stop-slop)

## 相关概念

- [humanizer-cli](./tool-humanizer-cli.md) — 同为 AI 去痕工具，但 humanizer-cli 是命令行的离线参考 + 检查
- [No Slop 中文版](./tool-no-slop-zh.md) — 中文场景的去 AI 腔规则
- [No AI Slop](./tool-no-ai-slop.md) — AI Slop 现象的通用概念
- [AI Humanizer Handbook](./tool-ai-humanizer-handbook.md) — 系统化的 AI 去痕方法论
