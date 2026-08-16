---
type: Tool
title: "dsh-agent-teams"
description: "DeepSeek Harness 多代理插件：让单个 DSH 会话化身「队长」，组建持久子代理团队，按依赖拆解目标并通过直接消息协调工作，无需独立工作流引擎"
resource: "https://github.com/NanmiCoder/dsh-agent-teams"
tags: [deepseek, harness, dsh, multi-agent, orchestration]
timestamp: 2026-08-16T16:00:00Z
---

# dsh-agent-teams

## 它是什么
`NanmiCoder/dsh-agent-teams` 是 **DeepSeek Harness (DSH)** 的一个多代理插件：在**一个 DSH 会话里**把它升格为「**队长**」，让它能**组建一组持久存在的子代理**、按依赖**拆解目标**、通过**直接消息协调** 各子代理的工作——整个过程**不需要额外的工作流引擎**（不依赖 Airflow / Temporal / LangGraph 等）。

## 为什么用它 / 适合什么场景
- 想在 DSH 里跑复杂项目（多文件、多模块），而不是单线程对话。
- 需要「一个总指挥 + 一组执行者」的拓扑，而不只是把任务塞进一个大 prompt。
- 不想为多代理单独搭一套工作流后端。
- 子代理需要**长期保活**：可以跨多轮迭代、互相回话。

## 关键能力
| 能力 | 说明 |
|------|------|
| 队长模式 | 单个 DSH 会话升格为「队长」，统筹子代理 |
| 持久子代理 | 子代理不是「一次性函数调用」，可以长期保活、积累上下文 |
| 依赖拆解 | 把目标按任务依赖图拆分（先 A 再 B、C 与 D 并行…） |
| 直接消息 | 子代理之间用直接消息协调，而不是只通过队长 |
| 无外部引擎 | 全在 DSH 内核里跑，不依赖 Airflow / Temporal / LangGraph |

## 媒体
- ![](https://pbs.twimg.com/media/HPvMqDdbYAAlcLG.jpg)

## 相关概念
- [项目链接](https://github.com/NanmiCoder/dsh-agent-teams)