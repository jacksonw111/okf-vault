---
type: "Tool"
title: "Ars Umbris"
description: "能自己改的 IDE：把分散的 Markdown / YAML 知识库变成带类型校验的跨仓库图谱，让人与 Agent 用同一套原语一起搭建工具、视图与界面；字段写错、引用挂空直接报诊断，Agent 拿到就能修。"
resource: "https://github.com/arsumbris/arsumbris"
tags: "[knowledge-base, markdown, yaml, type-check, graph, agent-native, ide]"
timestamp: "2026-09-16T16:06:00Z"
---

# Ars Umbris

## 它是什么

[arsumbris/arsumbris](https://github.com/arsumbris/arsumbris) 是一个**能自己改的 IDE**，面向**带类型的知识**做管理。当前是 early alpha，仅支持 macOS。笔记、类型、技能、工具、界面全部塞进可互相依赖的仓库，引擎扫一遍合成一张**实时图谱**，**字段写错、引用挂空直接报诊断**，Agent 拿到诊断就能改。

## 为什么用它 / 适合什么场景

- 已有零散 Markdown / YAML 知识库，想把它升级为可校验的图谱。
- 想让人与 Agent 共享同一套原语：笔记、类型、技能、视图都是一等公民。
- 项目跨多仓库时，希望类型系统替 Agent 把跨仓引用「先校验再改」。
- 希望 Agent 的修改有可视化反馈：哪些字段挂了、哪些引用空了。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨仓库图谱 | 引擎扫描所有依赖仓库合成实时图谱 |
| 类型校验 | Markdown / YAML 字段对不上即报错 |
| Agent 协同 | 报错即指令，Agent 可直接按诊断修 |
| 可视化视图 | 笔记、技能、工具、界面同源渲染 |
| macOS early alpha | 当前仅 macOS 可跑，社区在快速迭代 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTZt4tacAAMZ30.jpg)

## 相关概念

- [OKF 是什么](./term-okf.md) — Ars Umbris 是「带类型校验 + Agent 协同」路线的 Markdown 知识库，与 OKF 同源思路
- [Understand-Anything](./tool-understand-anything.md) — 把代码库变知识图谱；Ars Umbris 把 Markdown 知识库变带类型图谱