---
type: Tool
title: "uavsim（四旋翼飞控本地仿真）"
description: "在本地跑四旋翼飞控仿真，调 LQR / PID / NDI 三种控制律，比效果、测散布、看回放，不用真机。"
resource: "https://github.com/trey-copeland/uavsim"
tags: [quadrotor, control-theory, lqr, pid, ndi, simulation]
timestamp: "2026-07-28T11:24:00.000Z"
---

# uavsim

## 它是什么

**本地四旋翼飞控仿真平台**——在 PC 上调三种经典控制律：

- **LQR**（线性二次型调节器）
- **PID**（比例-积分-微分）
- **NDI**（非线性动态逆）

能做的事：

- 比效果：哪个控制器在这个模型下更好
- 测散布：蒙特卡洛跑多次，看稳定性分布
- 看回放：轨迹可视化，重放

![截图示例](https://pbs.twimg.com/media/HOSM-8CaAAE5UBU.jpg)

## 与真机调试的差异

| 维度 | 真机 | uavsim |
|------|------|--------|
| 成本 | 摔一架上千 | 零成本 |
| 安全 | 物理风险 | 零风险 |
| 速度 | 飞行才能试 | 几秒跑一次 |
| 散布统计 | 难 | 跑 1000 次 |
| 控制器对比 | 慢 | 快 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 三种控制律 | LQR / PID / NDI |
| 本地运行 | 无需云端 |
| 散布统计 | 蒙特卡洛友好 |
| 轨迹回放 | 可视化 |
| 控制理论学习 | 教学 / 论文友好 |

## 原始链接

- [项目仓库](https://github.com/trey-copeland/uavsim)
- [推文剪藏](https://x.com/QingQ77/status/2082064524707037248)

## 相关概念

- [ClearCore（MIPS CPU 模拟器）](./tool-clearcore.md) — 同类本地仿真思路（CPU 角度）
- [GM BalanceCar（STM32 智能两轮平衡车）](./tool-gm-balancecar.md) — 控制理论硬件落地参考
- [ESPHome Guition 语音助手旋钮屏](./tool-esphome-guition-va.md) — 嵌入式控制 + 物联网
- [Strix（自主 AI 渗透测试 agent）](./tool-strix.md) — 不同领域（安全）的本地仿真 agent