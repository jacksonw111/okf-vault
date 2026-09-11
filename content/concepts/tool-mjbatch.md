---
type: "Tool"
title: "mjbatch（CPU 上并行数千 MuJoCo 仿真）"
description: "让开发者在 CPU 上并行运行数千个 MuJoCo 仿真：C++ 线程池释放 GIL，提供批量实时状态访问与逐仿真参数设置。"
resource: "https://github.com/kevinzakka/mjbatch"
tags: "[mujoco, rl, simulation, parallel, python, cpp]"
timestamp: "2026-09-11T22:05:00Z"
---

# mjbatch

## 它是什么

[kevinzakka/mjbatch](https://github.com/kevinzakka/mjbatch) 是**在 CPU 上并行跑数千个 MuJoCo 仿真**的工具：用 **C++ 线程池**释放 Python **GIL**，并提供**批量实时状态访问**与**逐仿真参数设置**——为强化学习训练提供高吞吐的并行 rollout 能力。

## 为什么用它 / 适合什么场景

- 做 RL 研究，想用一台 CPU 机器并行跑几千个环境，节省 GPU / 集群成本。
- 用 MuJoCo 但被 Python GIL 限制并行度。
- 想给 RL 训练做大批量 rollout 加速。

## 关键能力

| 能力 | 说明 |
|------|------|
| 并行仿真 | CPU 上跑数千 MuJoCo 环境 |
| C++ 线程池 | 释放 GIL |
| 批量状态访问 | 实时读全部环境状态 |
| 逐仿真参数 | 每个环境独立参数 |
| MuJoCo 原生 | 完整支持 MuJoCo API |
| Python 友好 | Python 接口调用 |

## 参考链接

- 项目仓库：<https://github.com/kevinzakka/mjbatch>

## 媒体

- ![](https://pbs.twimg.com/media/HR5e-cgbIAAQaqO.jpg)

## 相关概念

- [Microduck 复刻系列](./tool-microduck.md) — 强化学习双足机器人方向
- [swarmllm](./tool-swarmllm.md) — 另一类并行计算思路
- [toolrush](./tool-toolrush.md) — AI agent harness 运行时优化器
</content>
</invoke>