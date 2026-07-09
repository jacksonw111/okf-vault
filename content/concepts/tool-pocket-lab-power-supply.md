---
type: Tool
title: "Pocket Lab Power Supply（口袋型便携实验室电源）"
description: "基于 4S 锂电池组、口袋大小、支持 USB-C/PD 充电的便携实验室电源：可调输出电压与电流限制，配 8 字符 5x7 LED 点阵屏显示状态，面向无市电的现场电子实验。"
resource: "https://github.com/BenMakesEverything/Pocket-Lab-Power-Supply"
tags: "[electronics, hardware, lab, diy, power-supply, portable, 4s-lipo]"
timestamp: "2026-07-09T20:50:00Z"
---

# Pocket Lab Power Supply（口袋型便携实验室电源）

## 它是什么
`BenMakesEverything/Pocket-Lab-Power-Supply` 是一个开源**便携式实验室电源方案**：

- **电池**：4S 锂离子电池组供电
- **充电**：USB-C / PD 输入
- **输出**：可调电压 + 限流
- **显示**：8 字符 × 5×7 LED 点阵屏，显示电压 / 电流 / 状态

整套设备定位"无市电的现场电子实验"——出差、户外、维修、教学课上演示都合适。

## 为什么用它 / 适合什么场景
- **出差 / 户外 / 现场调试**电子设备：不用找插座即可有稳定直流输出。
- **教具**：体积小，5×7 LED 屏直接可见状态，比台式电源更适合课堂。
- **应急维修**：家里停电 / 实验室关闭时给待修电路供测试电。
- 对比台式 Bench PSU：体积砍到口袋级，电流上限低，但真正便携。

## 关键能力
| 能力 | 说明 |
|------|------|
| 4S 锂电供电 | 自带能量，无市电依赖 |
| USB-C / PD 充电 | 用主流笔记本 / 手机充电头即可补能 |
| 可调输出电压 | 适配常见 3.3V / 5V / 12V 等目标 |
| 可调限流 | 防止测试设备过流 |
| 5×7 LED 点阵屏 | 显示电压、电流、模式、错误码 |

## 媒体参考

设备照片：
- ![](https://pbs.twimg.com/media/HMr4ihIbMAAkkVo.jpg)

## 相关概念
- [Seahi-Serial](tool-seahi-serial.md) — VS Code 风格的桌面多串口调试工具
- [clearCore](tool-clearcore.md) — C++20 写的 MIPS CPU 模拟器（教具方向互补）
- [Hardware-related index] — 本条目暂未指向其它 hardware 类别条目

## 参考链接
- 项目链接：<https://github.com/BenMakesEverything/Pocket-Lab-Power-Supply>
