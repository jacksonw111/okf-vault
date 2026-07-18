---
type: "Tool"
title: "MOMO CODE（momozi1996/momo-code）"
description: "搭在 opencode 之上的开源编程代理，核心卖点是「双速自我进化」：秒级 /evolve 走 KEP 协议，把成功招数压成战术卡，再用 Thompson 采样注入提示；小时级 /fine-tune 用 MCGS 加 LoRA 改模型权重，配 Ratchet 门控防回退。"
tags: "[agent, opencode, self-evolution, lora, fine-tune, kex, mcgs, ratchet, thompson-sampling]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/momozi1996/momo-code"
---

# MOMO CODE（momozi1996/momo-code）

## 它是什么

[`MOMO CODE`](https://github.com/momozi1996/momo-code) 是 momozi1996 开源的**自我进化编程代理**，搭在 [opencode](https://github.com/opencode) 之上。

它的核心创新是把「自我进化」拆成**两个速度档位**：

| 速度档 | 触发命令 | 机制 | 作用 |
|--------|----------|------|------|
| **秒级** | `/evolve` | KEP 协议 + Thompson 采样 | 把刚跑成功的「招数」压成**战术卡**，注入后续提示 |
| **小时级** | `/fine-tune` | MCGS + LoRA + Ratchet 门控 | 用蒙特卡洛树搜索找更好的训练数据，LoRA 微调权重，**单向门控防回退** |

## 关键概念速览

| 概念 | 含义 |
|------|------|
| KEP 协议 | 把 Agent 成功操作序列提炼成「可复用战术卡」的协议 |
| Thompson 采样 | 用 bandit 算法挑出当前最有希望的战术卡注入提示 |
| MCGS | Monte Carlo Graph Search，蒙特卡洛图搜索——用试错找高质量训练数据 |
| LoRA | Low-Rank Adaptation，轻量微调技术，不动基座权重 |
| Ratchet 门控 | 单向棘轮机制——只允许效果正向变化，不允许回退 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 秒级战术进化 | 跑成功的招数立刻能复用到下一次 |
| 小时级权重进化 | 长期记忆沉淀到 LoRA 权重 |
| 防回退 | Ratchet 门控确保新权重不会比旧权重更差 |
| 开放基座 | 搭在 opencode 之上，可继承其多 Provider / 多语言支持 |

## 适合什么场景

- 想让编程 Agent **越用越顺手**而不是「每次都从头学」；
- 内部团队有大量「项目专属套路」，希望 Agent 自动把它们沉淀成可复用知识；
- 对 Agent 自我修改有强戒心，但愿意接受「带 Ratchet 护栏的有限度自我微调」。

## 参考链接

- [原始链接](https://github.com/momozi1996/momo-code)

## 相关概念

- [antidoom](tool-antidoom.md) — 同样用 LoRA 做「行为层小补丁」；antidoom 压 doom-loop，MOMO CODE 沉淀成功套路
- [optim-agent](tool-optim-agent.md) — 同样基于编程 Agent 的「持续变好」思路；optim-agent 走「外部寻优」、MOMO CODE 走「自我微调」
- [matterloop](tool-matterloop.md) — matterloop 给 Agent 流程装「护栏」，MOMO CODE 给 Agent 装「进化能力」，两者正交