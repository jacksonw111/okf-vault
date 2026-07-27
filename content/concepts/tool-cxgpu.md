---
type: "Tool"
title: "cxgpu（nickprotop/cxgpu）"
description: "终端 GPU 监控工具，同时支持 NVIDIA 和 AMD 显卡：概览页带仪表盘 + 实时折线图，多卡机器可看所有 GPU 总览大屏；进程页支持按 GPU 过滤、排序，并向目标进程发送 SIGTERM / SIGKILL。"
resource: "https://github.com/nickprotop/cxgpu"
tags: [gpu, monitoring, nvidia, amd, terminal, tui, process-management]
timestamp: "2026-07-27T20:30:00Z"
---

# cxgpu（nickprotop/cxgpu）

## 它是什么

`nickprotop/cxgpu` 是一个**终端 GPU 监控工具**，**同时支持 NVIDIA 与 AMD 显卡**。它把目前常见的「nvitop / nvtop」与「rocm-smi」的体验合二为一：

- 概览页：仪表盘 + 实时折线图；
- 多卡机器：看所有 GPU 的总览大屏；
- 进程页：按 GPU 过滤、排序，**对目标进程发 SIGTERM / SIGKILL**。

## 为什么用它 / 适合什么场景

- 机器**混插 NVIDIA + AMD**（如消费级 + 工作站），不想装两套监控；
- 喜欢 TUI 而非 GUI，远程 SSH 想直接 `vim`-style 操作；
- 需要在**终端一键 kill 占用 GPU 的进程**，而不是开 nvidia-smi / rocm-smi 找 PID；
- 想要**实时折线 + 多卡总览**，方便发现 GPU 抖动 / 显存泄漏。

## 关键能力

| 能力 | 说明 |
|------|------|
| NVIDIA + AMD 通吃 | 单工具覆盖两大 GPU 厂商 |
| 仪表盘视图 | 终端里看实时利用率 / 显存 / 温度 / 功耗 |
| 实时折线图 | 历史曲线辅助定位抖动 |
| 多卡总览 | 一屏看所有 GPU 整体负载 |
| 进程级筛选 | 按 GPU 过滤 / 排序当前进程 |
| 终端信号发送 | 对占用 GPU 的进程发 SIGTERM / SIGKILL |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOH7nDbaEAAM-2J.jpg)

- 项目链接：<https://github.com/nickprotop/cxgpu>
