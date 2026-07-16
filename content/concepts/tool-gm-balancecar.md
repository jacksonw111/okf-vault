---
type: "Tool"
title: "GM_BalanceCar（lijinshang/GM_BalanceCar）"
description: "基于 STM32F4 的开源智能两轮平衡车项目,从硬件(双层 PCB / 电机驱动)到串级 PID 控制算法的完整方案,免调参、低成本、极易复刻。"
resource: "https://github.com/lijinshang/GM_BalanceCar"
tags: "[stm32, balance-robot, embedded, pid, hardware, open-source-hardware]"
timestamp: "2026-07-16T11:28:00Z"
---

# GM_BalanceCar

[GM_BalanceCar](https://github.com/lijinshang/GM_BalanceCar) 是一套**基于 STM32F4 的开源智能两轮平衡车项目**——从双层 PCB、电机驱动、IMU 选型到串级 PID 控制算法全部开源,免调参、低成本、极易复刻。

## 它解决了什么

两轮平衡车是嵌入式控制领域的经典练手项目,但传统教程或缺硬件细节、或缺 PID 参数整定过程,复刻者经常要反复试错。本项目把从 PCB 制板到控制算法的整套链路打包,学习者按 BOM 打板焊接即可跑通。

## 关键能力

| 能力 | 说明 |
|------|------|
| STM32F4 主控 | 基于常见 ARM Cortex-M4 单片机 |
| 双层 PCB | 公开电路图,可直接嘉立创 / OSH Park 打样 |
| 电机驱动 | 含完整电机驱动电路,适配常见的减速直流电机 |
| 串级 PID | 角度环 + 速度环双闭环控制 |
| 免调参 | 公开默认参数,新手不用纠结 PID 整定 |
| 低成本 | 全 BOM 控制在爱好者可承受价位 |

## 媒体

![](https://pbs.twimg.com/media/HNQ-82KaoAEhyKi.jpg)

## 参考链接

- [项目仓库](https://github.com/lijinshang/GM_BalanceCar)

## 相关概念

- [Pocket Lab Power Supply](./tool-pocket-lab-power-supply.md) — 同为嵌入式/电子爱好者领域工具,与本工具并列参考(给口袋实验室供电)
- [Marine Acoustic Monitor](./tool-marine-acoustic-monitor.md) — 同样基于 STM32 类的边缘计算设备方向,与本工具并列参考
