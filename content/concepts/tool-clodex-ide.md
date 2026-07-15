---
type: "Tool"
title: "Clodex IDE（mereyabdenbekuly-ctrl/clodex-ide）"
description: "本地优先、零信任的 agentic IDE,Electron + TypeScript 写成,把 AI 任务 / 代码 / 终端 / 浏览器 / Git / 模型 / 受控执行统一进一个工作区,用显式策略和隔离运行时管模型动作。"
resource: "https://github.com/mereyabdenbekuly-ctrl/clodex-ide"
tags: "[ide, agent, electron, typescript, zero-trust, local-first, sandbox]"
timestamp: "2026-07-15T05:30:00Z"
---

# Clodex IDE

[Clodex](https://github.com/mereyabdenbekuly-ctrl/clodex-ide) 是一个**本地优先、零信任的 agentic 版 IDE**。用 Electron + TypeScript 写成,把 AI 任务、代码、终端、浏览器、Git、模型和受控执行**全塞进一个工作区**,再用**显式策略 + 隔离运行时**管住模型的动作。

## 它解决了什么

很多 AI IDE「助手太自由」——agent 拿到 shell 之后能改哪改哪。Clodex 把模型所有动作过一遍策略层,再丢进隔离运行时,**和 IDE 本体解耦**,避免模型直接动到工作目录外的资源。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工作区统一收口 | AI 任务 / 代码 / 终端 / 浏览器 / Git / 模型都在一个 app |
| 显式策略 | 模型能不能动什么由策略层控制,不靠 prompt 自觉 |
| 隔离运行时 | agent 的 shell / file ops 在沙箱里执行 |
| 本地优先 | 数据不出本机,模型可接本地/远端 |

## 媒体

![](https://pbs.twimg.com/media/HNJsdW_aQAAkxp2.jpg)

## 参考链接

- [项目仓库](https://github.com/mereyabdenbekuly-ctrl/clodex-ide)

## 相关概念

- [Claude Code（终端原生 AI 编码 agent）](./tool-claude-code.md) — 同样「agent 接管 IDE/终端」思路,本工具侧重 GUI 与零信任策略
- [BuilderIO / agent-native](./tool-builder-io-agent-native.md) — 另一类 agent-ready 前端仓库模板,可参考其结构
