---
type: Tool
title: "workbuddy-xhs-skills"
description: "jackbauerxu/workbuddy-xhs-skills，10 个可执行的 Agent skill（6 内容运营 + 4 视觉）拼成的小红书全流程工作流，从变现定位、对标拆解到 3:4 封面、16:9 配图，融合 X Article / yanliudreamer / dbskill / ziguishian 等方法体系。"
resource: "https://github.com/jackbauerxu/workbuddy-xhs-skills"
tags: "[xiaohongshu, agent-skill, content-ops, social-media, visual]"
timestamp: "2026-07-22T07:50:00Z"
---

# workbuddy-xhs-skills

## 它是什么

[`workbuddy-xhs-skills`](https://github.com/jackbauerxu/workbuddy-xhs-skills) 把小红书运营从「定位 → 选题 → 写稿 → 做图」拆成 **10 个可执行的 Agent skill**，分两层：6 个内容运营技能 + 4 个视觉技能，串成完整工作流。

## 10 个 Skill

### 内容运营层（6 个）

| Skill | 职责 |
|------|------|
| 变现定位 | 从账号阶段倒推变现路径 |
| 对标拆解 | 拆解同赛道爆款账号 |
| 账号档案 | 维护人设 / 关键词矩阵 |
| 选题标题 | 选题 + 标题公式 |
| 初稿去 AI 味 | 把 AI 写的稿改回「人话」 |
| 排期复盘 | 发布日历 + 数据复盘 |

### 视觉层（4 个）

| Skill | 职责 |
|------|------|
| 路由分发 | 不同平台尺寸自动路由 |
| 3:4 封面 | 小红书竖版封面 |
| 16:9 小黑配图 | 横版配图 |
| 材质解释图 | 风格解释 / 视觉示例 |

## 方法融合

整合了 X Article、yanliudreamer、dbskill、ziguishian 等多个方法体系的内容。

## 设计原则

- **有真实工具就跑图，没工具就标 `not_called`**——绝不虚构交付；
- 视觉部分与文字部分**串联**，不是两份孤立的 skill；
- skill 之间能互相调用，构成工作流。

## 与同类资源的差异

| 资源 | 形态 | 差异 |
|------|------|------|
| [xiaohongshu-assistant](tool-xiaohongshu-assistant.md) | 桌面 Web 工作台 | 偏 GUI，单文件生成 |
| [xiaohongshu-ai-workbench](tool-xiaohongshu-ai-workbench.md) | 5 个 Skill 合集 | 偏 Codex skill，工作流粒度较粗 |
| [oil-cover](tool-oil-cover.md) | 单一封面 Skill | 只做封面 |
| workbuddy-xhs-skills | 10 个 Skill 工作流 | 覆盖运营 + 视觉全链路，粒度更细 |

## 媒体

![](https://pbs.twimg.com/media/HNuByjnaIAAX4SE.jpg)

## 原始链接

- [项目仓库](https://github.com/jackbauerxu/workbuddy-xhs-skills)

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 的概念元定义
- [xiaohongshu-ai-workbench](tool-xiaohongshu-ai-workbench.md) — 同样是小红书运营 Skill 化方案，但本工具粒度更细且包含视觉层
- [oil-cover](tool-oil-cover.md) — 单做封面的 Skill，本工具的 3:4 封面 Skill 是它的同类补充