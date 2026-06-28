---
type: "Tool"
title: "Study Dost AI（STEM 三视角学习助手）"
description: "STEM 学习助手，每个概念同时给出三种讲法：分步走、生活类比、视觉提示；支持南亚与全球课程、升级 / 连击 / 徽章游戏化、语音输入输出、公式与代码渲染；前后端分离 + Cloudflare Tunnel 暴露 HTTPS，AI 走 DeepSeek-V3。"
tags: "[education, ai, fastapi, stem, deepseek, cloudflare]"
timestamp: "2026-06-28T14:32:00Z"
resource: "https://github.com/samiahraf/study-dost-ai"
---

# Study Dost AI（STEM 三视角学习助手）

## 它是什么

Study Dost AI 是个**人工智能 STEM 学习助手**，对每个概念同时给**三种讲法**：

1. **分步走（Step-by-step）** — 一步步推导
2. **生活类比（Real-life analogy）** — 用日常现象类比
3. **视觉提示（Visual hint）** — 用图示辅助理解

适配南亚与全球课程，含升级 / 连击 / 徽章等游戏化设计，语音输入输出，能渲染数学公式与代码。

## 架构

| 层 | 技术 |
|----|------|
| 后端 | Python FastAPI |
| 前端 | JavaScript / HTML / CSS |
| AI 模型 | DeepSeek-V3 |
| 部署 | 后端放 RDP/VPS + Cloudflare Tunnel 暴露 HTTPS；前端放免费静态托管 |
| 数学 / 代码 | 服务端公式渲染 + 代码块高亮 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 三视角解释 | 同一概念给分步 / 类比 / 视觉三种讲法 |
| 多课程适配 | 南亚与全球课程内容对齐 |
| 游戏化 | 升级 / 连击 / 徽章 |
| 语音交互 | 输入输出双语音 |
| 公式与代码 | 渲染数学公式与代码块 |
| 前后端分离 | 静态前端 + Cloudflare Tunnel 后端 |
| DeepSeek-V3 | 默认模型走 DeepSeek |

## 参考链接

- [项目仓库](https://github.com/samiahraf/study-dost-ai)
- [原始链接](https://x.com/QingQ77/status/2071240200756638122)

## 相关概念

- [ExamPrep-AI](tool-exam-prep-ai.md) — PDF 笔记转闪卡 / 选择题 / 摘要，同属「AI 辅助学习」家族
- [happy-figure-skill](tool-happy-figure-skill.md) — 科研绘图 prompt 生成 Skill，与 Study Dost AI 的「视觉提示」思路相通
- [Kanarenshu](tool-kanarenshu.md) — 终端日语假名练习，AI 在学习场景的另一种形态