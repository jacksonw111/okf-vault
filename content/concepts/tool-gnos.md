---
type: "Tool"
title: "Gnos（把编码 agent 改造成定制课程老师）"
description: "madhvantyagi 出品的开源工具：把编码 agent（Claude Code / Codex 等）改造成会为你定制课程的老师——规划学习路线、出课、跟踪薄弱点，并生成视频、模拟、图片与 PDF 等教学物料。"
resource: "https://github.com/madhvantyagi/Gnos"
tags: "[education, ai-tutor, learning-path, agent, code-agent]"
timestamp: "2026-09-27T21:55:00Z"
---

# Gnos（把编码 agent 改造成定制课程老师）

## 它是什么

[Gnos](https://github.com/madhvantyagi/Gnos) 是 madhvantyagi 出品的开源工具：**把编码 agent 改造成会为你定制课程的老师**。

它不是另起一个 LLM，而是**复用现有编码 agent**（Claude Code / Codex 等）作为底层执行器，在其之上叠一层「教学脚手架」：

- **规划学习路线**（按目标拆解章节 / 知识点）
- **出课**（生成讲义 / 练习题）
- **跟踪薄弱点**（记录学员错题 / 卡点）
- **生成多媒体教学物料**（视频 / 模拟 / 图片 / PDF）

## 为什么用它 / 适合什么场景

- 想让**自家编码 agent 多一份教学职能**（给新人 onboarding / 给团队内训）。
- 比起「通用 LLM 问答」，更想要**结构化课程**（路线 / 出课 / 复盘三件套）。
- 想要**多媒体教学物料**一次性产出（讲义 PDF + 示意图 + 短视频）。
- 想**复用 agent 的工具栈**（文件系统 / Shell / 包管理），而不是从零写 LMS。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 编码 agent 上的教学脚手架 |
| 底层 | 复用现有编码 agent（Claude Code / Codex 等） |
| 路线 | 规划学习路径 |
| 出课 | 自动生成讲义 / 练习 |
| 跟踪 | 薄弱点分析 + 进度记录 |
| 物料 | 视频 / 模拟 / 图片 / PDF |
| 开源 | 全部代码可二开 |

## 媒体

- ![](https://pbs.twimg.com/media/HTH5bd0aoAAJN5W.jpg)
- ![](https://pbs.twimg.com/media/HTH5cKvbsAA4B_w.jpg)

## 相关概念

- [Claude Code](./tool-claude-code.md) — Gnos 的底层 agent 之一
- [Study Dost AI](./tool-study-dost-ai.md) — STEM 学习助手，每个概念同时给分步走 / 生活类比 / 视觉提示三种讲法