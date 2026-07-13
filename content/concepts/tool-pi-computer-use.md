---
type: Tool
title: "pi-computer-use"
description: "给 pi harness 用的 computer-use 工具，让 AI 直接操控 macOS / Windows 桌面（鼠标键盘、截屏、点击），作者逆向自 codex 的实现而非依赖 CUA driver，可改造后挂到任意 harness。"
tags: "[computer-use, ai-agent, pi, codex, desktop-automation, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/injaneity/pi-computer-use"
---

# pi-computer-use

把 **computer-use** 能力塞进 [pi](https://github.com/mariozechner/pi-coding-agent) 终端式 AI harness 的工具，支持 **macOS 和 Windows**——AI 看截图、决定点击哪里、模拟键鼠操作，**像人一样**直接驱动桌面应用。

## 它是什么

- 一个 **pi 扩展/Skill**，让 pi 这个终端 AI agent 拥有"看屏幕 + 操控 GUI"的能力；
- 不是用 CUA（Computer-Use API）官方 driver，而是**逆向自 codex 的实现**，所以**底层可控、可改造**；
- 理论上稍微改一下接口，**可以挂到任意 harness**（Claude Code、Aider、自家 agent 框架等）上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 桌面截屏 | 拿当前屏幕画面给模型看 |
| 鼠标 / 键盘模拟 | 点击、拖拽、输入、快捷键 |
| 多平台 | macOS + Windows 同步支持 |
| 与 pi 集成 | 作为 pi 的 Skill 直接调用，无需额外胶水 |
| 移植性 | 实现层与 CUA driver 解耦，逻辑可抽出来挂到其他 agent |

## 适合什么场景

- 桌面端**没有 API 只能 GUI 操作**的旧系统/企业软件自动化（订票、ERP、OA 等）；
- 想给现有终端 AI harness（不只是 pi）加一双"看屏幕的手"；
- 对官方 CUA driver 的云端依赖 / 延迟 / 成本不满意，想自己掌控实现。

## 实现要点（来自公开说明）

- 截屏 + 元素定位（OCR / 视觉） + 输入事件注入——三件套自实现；
- 通过 pi 的 Skill 机制挂入，对外暴露一组工具调用即可；
- 不强制依赖云端 LLM，本地模型 + 本地截屏也能闭环。

## 预览

![](https://pbs.twimg.com/media/HNEfvJQbgAAa4cS.jpg)

## 与同领域 Playbook 的关联

- 它是"**端到端 GUI 操控**"路线（无 DOM 中介、直接看图点图）的代表；
- 与 [多模态大模型驱动的 UI 自动化测试](playbook-multimodal-ui-test-automation.md)（基于 DOM + 截图的"测试代码生成"路线）形成对照——前者是**让 agent 直接动现成 GUI**，后者是**让 agent 产出可复用的测试脚本**。

## 相关概念

- [多模态 UI 自动化测试](playbook-multimodal-ui-test-automation.md) — 同一类"AI 看图操作 GUI"目标，但产出的是测试脚本而非人工操控
- [Claude Code](tool-claude-code.md) — 另一种 agent harness；该工具的"改造后挂到任意 harness"思路可参照
