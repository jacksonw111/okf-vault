---
type: "Note"
title: "本地 LLM 硬件搭建实操指南（local-llm 仓库）"
description: "jamesob/local-llm 给出的两档预算本地 LLM 主机方案——2k 跑 Qwen3-27B、40k 跑 GLM-5.2-594B 级模型，核心思路是把钱花在 VRAM 上、用 PCIe Gen4 交换芯片让多卡直接通信，Docker 化 + 沙盒 VM 保护宿主。"
tags: "[llm, hardware, gpu, vram, self-hosted, local-ai]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/jamesob/local-llm"
---

# 本地 LLM 硬件搭建实操指南（local-llm 仓库）

## 是什么

[`local-llm`](https://github.com/jamesob/local-llm) 是一份**在本地硬件上跑 SOTA 大语言模型的实操指南**，作者给出了两档预算配置，全程用二手 EPYC 7313P + DDR4 把预算省下来全堆到 GPU 与互联带宽上。

![local-llm 机箱图](https://pbs.twimg.com/media/HMXTfhXakAAqTa3.jpg)

## 两档预算配置

| 预算 | GPU 方案 | 显存 | 目标模型 |
|------|----------|------|----------|
| **~$2k** | 双 RTX 3090 | 48 GB | Qwen3-27B 级 |
| **~$40k** | 四路 RTX PRO 6000 | 384 GB | GLM-5.2-594B 级（接近 Opus 水平） |

## 核心思路

- **预算花在 VRAM，不花在新平台**：宿主机的 EPYC 7313P + DDR4 内存从 eBay 淘二手
- **多卡直连替代 NVLink**：使用 c-payne 的 **PCIe Gen4 交换芯片**，让四张显卡之间可以直接通信
  - 实测双向带宽 50.4 GB/s
  - 延迟 < 0.5 µs
  - 达到 Gen4 线速
- **事无巨细记录**：BIOS 里 `bifurcation` 与 `ASPM` 设置、内核参数加 `iommu=off`、110V 电路限制每张卡 350W、SAS 线缆选型雷区

## 运行架构

- **Docker 化方案**：每个模型一个独立容器
- 通过 [opencode](https://github.com/opencode-ai/opencode) 暴露 API
- 最后搭**沙盒 VM**，让 agent 在里面干活，不会搞乱宿主系统

## 关键要点

| 要点 | 说明 |
|------|------|
| VRAM > 新平台 | 把预算尽可能多地花在显存上，而不是追逐最新 CPU / 主板 |
| PCIe 交换芯片 | 用 c-payne 的交换芯片让多卡直接通信，绕开 CPU 瓶颈 |
| Docker 容器隔离 | 每个模型独立容器，模型库/配置互不污染 |
| 沙盒 VM 保护 | 让 agent 在隔离 VM 里跑，宿主系统不被打乱 |
| 二手 EPYC | 性价比之选，把预算留给 GPU |

## 适用人群

- 想摆脱商业 API 限制、需要本地 SOTA 模型做推理或微调
- 个人 / 小团队预算在 2k ~ 40k 美元之间
- 能容忍「自己攒机 + 调 BIOS + 调内核参数」的折腾成本

## 参考链接

- [项目链接](https://github.com/jamesob/local-llm)

## 相关概念

- [Qwen-AgentWorld](tool-qwen-agentworld.md) — 通义千问原生世界模型，可在本地 LLM 主机上做智能体交互训练
- [Ornith-1](tool-ornith-1.md) — 9B/35B/397B 三规格开源编程智能体模型，适合本地推理