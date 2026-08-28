---
type: Tool
title: "Gradio Agent Workflow Guide（agent-friendly 与 human-friendly 并重的复杂工作流 UI 设计指南）"
description: "Hugging Face 团队在 Gradio 博客上发表的复杂工作流 UI 设计指南，主张 agent 与人共用同一界面——既可由人点按，又可被 agent 解析与调用。"
resource: "https://huggingface.co/blog/gradio-workflow-guide"
tags: [gradio, agent-ui, ux, workflow, design]
timestamp: "2026-08-27T13:16:00Z"
---

# Gradio Agent Workflow Guide

## 它是什么
Hugging Face 在 [gradio-workflow-guide](https://huggingface.co/blog/gradio-workflow-guide) 中提出：在构建复杂多步工作流的 UI 时，**不要分两套界面**——一套给人类，一套给 agent。而是让两者共享同一个界面元素，使得 agent 能像人一样点按 / 输入 / 读输出。

核心理念：**agent-friendly ≈ human-friendly**。结构化表单、清晰 ID、稳定布局，让 LLM agent 能从界面直接推断出可执行步骤。

## 为什么用它 / 适合什么场景
- 构建 agent 编排平台时，想让 agent 既能调用 API 又能在「界面」上做兜底操作；
- 用 Gradio / Streamlit 等写复杂多步流程，不想为 LLM 单独再写一套工具描述；
- 想让 UI 设计原则同时照顾人类和模型——可解释、可结构化、可访问。

## 关键能力
| 能力 | 说明 |
|------|------|
| 共享界面 | 人与 agent 操作同一界面，无独立 agent UI |
| 稳定 ID | 控件 ID 稳定，agent 可直接通过 ID 点按 |
| 结构化布局 | 表单 / 分组 / 步骤清晰，LLM 可读 |
| 可解析输出 | 渲染结果同时提供文本 / 结构化两路 |
| 降低双重维护 | UI 一改两边同步生效 |

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — 把能力封装成 Skill 的思路，与本指南「让 UI 本身成为 agent 可调用的工具」思路同源
- [Toolcraft](tool-toolcraft.md) — pixel-point 出的创意类应用 starter kit，自带「让 AI 编码代理直接产出视觉工具」的指令

## 参考链接
- 原始链接：<https://huggingface.co/blog/gradio-workflow-guide>
