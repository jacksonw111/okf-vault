---
type: "Tool"
title: "opencode-fusion（mihneaptu/opencode-fusion）"
description: "为 OpenCode 实现多模型协作团队：主代理（贵模型，如 Opus 5）只做规划和审查、权限层禁掉编辑工具；改代码强制走 task 工具丢给便宜副手模型（如 Grok 4.5）；Cognition 实测可省 35%–54% token；主力与副手跨厂商时附带交叉检查。"
resource: "https://github.com/mihneaptu/opencode-fusion"
tags: [opencode, multi-model, cost-saving, code-review, orchestration, agents]
timestamp: "2026-07-26T09:37:00Z"
---

# opencode-fusion（mihneaptu/opencode-fusion）

## 它是什么

`mihneaptu/opencode-fusion` 为 [OpenCode](tool-opencode-cc.md) 实现**多模型协作团队**：**主代理（贵模型，如 Opus 5）只能规划和审查**，**权限层直接把编辑工具禁了**；改代码必须通过 `task` 工具丢给**便宜的副手模型（如 Grok 4.5）**。这样贵的 token 只花在动脑子的事上，机械改代码让便宜的来——**Cognition 实测可省 35%–54%**。当主力与副手用**不同厂商**模型时，每次审查附带跨厂商交叉检查。

## 为什么用它 / 适合什么场景

- 单模型 agent 太贵，想把**规划/审查**与**机械执行**拆分到不同价位模型；
- 担心「让 GPT-5 改 50 行 Python」浪费钱——这种活 Grok 4.5 干就行；
- 想拿到**跨厂商的二次校验**，避免单一模型偏见。

## 关键能力

| 能力 | 说明 |
|------|------|
| 角色分离 | 主代理只规划/审查，副手只执行 |
| 权限层隔离 | 主代理连编辑工具都拿不到 |
| 任务路由 | 通过 task 工具强制派给副手 |
| 跨厂商校验 | 主副异厂商时附带交叉检查 |
| 实测省 token | Cognition 场景 35%–54% 节省 |

## 媒体 / 原始链接

视频：<https://video.twimg.com/amplify_video/2081010865802014721/vid/avc1/1318x688/BKejzL96iQEzql8W.mp4?tag=29>

- 项目链接：<https://github.com/mihneaptu/opencode-fusion>

## 相关概念

- [OpenCode](tool-opencode-cc.md) — 被本工具扩展的终端 AI 编码 agent
- [pi-fusion](tool-pi-fusion.md) — 同样是「多模型协同」思路（Pi 上做并行扇出 + 汇总）
