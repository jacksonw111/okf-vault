---
type: Tool
title: "clearCore"
description: "C++20 写的透明、教学型 MIPS CPU 模拟器，终端 TUI + Qt6 桌面两套前端，单周期和 5 级流水线两模型同一接口可运行时切换，实时可视化管道状态。"
resource: "https://github.com/khenderson20/clearCore"
tags: "[mips, cpu-simulator, education, cplusplus, qt6, tui, computer-architecture]"
timestamp: "2026-07-02T11:40:00Z"
---

# clearCore

## 它是什么
C++20 写的 MIPS 处理器模拟器，**透明 + 教学导向**。提供终端 TUI 和 Qt6 桌面两套前端，单周期和 5 级流水线两种模型共用同一接口，可运行时切换。实时可视化管道状态帮助学习计算机体系结构。

## 为什么用它 / 适合什么场景
- 学计算机体系结构时，想直观看到 5 级流水线的 IF / ID / EX / MEM / WB 各阶段寄存器、转发、冒险。
- 想对比「单周期」与「5 级流水线」两种实现方式的吞吐差异。
- 想要一份既能在终端跑、也能在桌面跑的可视化模拟器。
- 教学场景：让学生在课堂或实验里观察数据冒险、控制冒险如何发生。

## 关键能力
| 能力 | 说明 |
|------|------|
| 语言 | C++20 |
| 前端 | 终端 TUI + Qt6 桌面 GUI 两套 |
| CPU 模型 | 单周期 + 5 级流水线 |
| 接口统一 | 同一接口可运行时切换模型 |
| 可视化 | 实时展示管道各阶段状态、寄存器、转发/冒险 |
| 形态 | 教学型开源项目 |

## 相关概念
- [Haskell 反应式交互式笔记本](tool-haskell-reactive-notebook.md) — 同为「教学型反应式编程工具」
- [Study Dost AI](tool-study-dost-ai.md) — STEM 学习助手；clearCore 是体系结构专项工具
- [CS-Fundamentals](tool-cs-fundamentals.md) — 校招 CS 基础仓库；clearCore 是体系结构章节的实操补充

## 项目链接
- 项目主页：<https://github.com/khenderson20/clearCore>

## 媒体
![](https://pbs.twimg.com/media/HMJUn9obsAAWG8s.jpg)