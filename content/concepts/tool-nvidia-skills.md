---
type: "Tool"
title: "NVIDIA Skills（NVIDIA 官方 Agent Skills 合集）"
description: "NVIDIA 官方出品的 AI 代理技能集合，让 agent 知道怎么正确调用 CUDA / cuOpt / NeMo 等 NVIDIA 软件工具，覆盖 CUDA-X / Jetson / NeMo / TAO / Holoscan 等产品线共 200+ 技能。"
tags: "[nvidia, agent-skills, cuda, ai, official]"
timestamp: "2026-06-27T11:26:00.000Z"
resource: "https://github.com/nvidia/skills"
---

# NVIDIA Skills（NVIDIA 官方 Agent Skills 合集）

## 它是什么

[`nvidia/skills`](https://github.com/nvidia/skills) 是 **NVIDIA 官方出的一套 AI 代理技能**，让 agent 知道**怎么正确调用 CUDA、cuOpt、NeMo 等 NVIDIA 软件工具**。每个 skill 就是一份指令集，覆盖 CUDA-X、Jetson、NeMo、TAO Toolkit、Holoscan 等几十个产品线，总共 200 多个技能。

安装方式：`npx skills add nvidia/skills`，一键装到 Claude Code、Codex、Cursor、Kiro 等主流编程代理里。

## 关键能力

| 能力 | 说明 |
|------|------|
| NVIDIA 全栈 | CUDA / cuOpt / NeMo 等 |
| 产品线覆盖 | CUDA-X / Jetson / NeMo / TAO / Holoscan |
| 200+ 技能 | 覆盖大量细分用法 |
| 标准 Skill 格式 | 每条都是一份指令集 |
| 一键安装 | `npx skills add nvidia/skills` |
| 多代理兼容 | Claude Code / Codex / Cursor / Kiro |

## 适用场景

- 用 Claude Code / Codex / Cursor 做 NVIDIA GPU 相关开发
- 需要让 agent 准确知道 cuDNN / TensorRT / NeMo 等的正确调用姿势
- 想省去手写 prompt，让 agent 直接套用 NVIDIA 的官方最佳实践

## 参考链接

- [项目链接](https://github.com/nvidia/skills)

## 相关概念

- [Agent Skills 是什么](term-agent-skills.md) — Skill 概念的元定义
- [mattpocock/skills](tool-mattpocock-skills.md) — 同类官方风格合集，偏通用 SOP
- [shadcn/improve](tool-shadcn-improve.md) — 另一种 Skill 形态：用最强模型审计代码