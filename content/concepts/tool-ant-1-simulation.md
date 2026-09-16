---
type: "Tool"
title: "ant-1（仿真蚂蚁 + 合成神经控制器）"
description: "把仿真蚂蚁身体接到 32 单元合成神经控制器上，做成可观察、可干预、可按种子复现的闭环实验台。"
resource: "https://github.com/ashleyotooligan/ant-1"
tags: "[computational-neuroscience, simulation, neural-controller, agent, reproducible]"
timestamp: "2026-09-16T16:05:00Z"
---

# ant-1（仿真蚂蚁 + 合成神经控制器）

## 它是什么

[ashleyotooligan/ant-1](https://github.com/ashleyotooligan/ant-1) 是一个**闭环神经控制实验台**：把**仿真蚂蚁身体**接到一个 **32 单元合成神经控制器**上，整体可观察、可干预、可按种子复现。让研究 / 学习 / 演示场景下「神经活动 ↔ 行为」的关系不再依赖一次性跑分。

## 为什么用它 / 适合什么场景

- 想做「小脑/无脑回路如何驱动身体」一类的入门研究，没有真硬件成本。
- 教学场景下向学生展示神经-身体耦合如何涌现出行为。
- 实验要可复现：相同种子 → 相同轨迹，方便消融对照。
- 想把控制器参数当「可旋钮」暴露出来，观察行为变化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 仿真蚂蚁身体 | 物理仿真层负责身体动力学 |
| 32 单元合成神经控制器 | 小型神经网络结构，便于可视化和分析 |
| 可观察 | 神经活动与身体姿态同步呈现 |
| 可干预 | 控制器参数 / 神经元权重可在线调节 |
| 种子复现 | 每次运行固定随机种子，实验可重放 |
| 闭环 | 身体反馈回流到控制器，没有开环偏差 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTtlo9aUAA825u.jpg)

## 相关概念

- [Computational Neuroscience（计算神经科学）](./term-comp-neuro.md) — ant-1 是面向「小网络 + 真实身体」的实验范式
- [fly-wirehead](./tool-fly-wirehead.md) — 类似思路但聚焦果蝇全脑连接组