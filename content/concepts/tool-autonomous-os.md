---
type: "Tool"
title: "Autonomous OS（机器人开源操作系统）"
description: "把机器人\"活过来\"的开源操作系统：以前机器人全靠遥控器、只会跑写好的脚本，装上它之后机器人能自己看、自己听、自己想下一步干什么；硬件随便配，系统免费装。"
resource: "https://github.com/autonomous-ai/autonomous-os"
tags: "[robot, os, agent, hermes, claude-code, skill-store]"
timestamp: "2026-09-11T22:10:00Z"
---

# Autonomous OS

## 它是什么

[autonomous-ai/autonomous-os](https://github.com/autonomous-ai/autonomous-os) 是一个让机器人**「活过来」**的开源操作系统——把机器人比喻为「机器人界的 Android」：

> 以前机器人全靠遥控器、只会跑写好的脚本，装上它之后，机器人能自己看、自己听、自己想下一步干什么。

## 核心架构

| 模块 | 角色 |
|------|------|
| **推理引擎** | Hermes、Claude Code 等可接入 |
| **感知** | 看 / 听 |
| **决策** | 想下一步干什么 |
| **技能包（Skill Store）** | 看家护院、人脸识别、跟随、读表情、控制灯光、处理 Gmail / GitHub / Mac 操作 |
| **学习循环** | 用着用着能自己写新技能、记住用户喜好 |
| **硬件抽象** | 只要能写四个 Markdown 文件（ROBOT.md / SOUL.md / SAFETY.md / SKILL.md）就能接入 |
| **模块化** | 引擎 / 模型 / 语音 / 技能 / 开发板全部可替换 |

## 四个 Markdown 文件

| 文件 | 作用 |
|------|------|
| ROBOT.md | 硬件抽象 |
| SOUL.md | 人格 / 性格 |
| SAFETY.md | 安全边界 |
| SKILL.md | 技能列表 |

## 为什么用它 / 适合什么场景

- 想给硬件创客 / 机器人厂商做定制化部署。
- 想给实体店主配前台机器人（迎宾 / 导购 / 巡逻）。
- 想做\"机器人 + AI\"方向的内容 / 教程流量变现。
- 想给 DIY 设备装系统改人格 / 让两台设备互相聊天。

## 关键能力

| 能力 | 说明 |
|------|------|
| 推理引擎可选 | Hermes / Claude Code 等 |
| Skill Store | 一键装技能包 |
| 学习循环 | 自我进化 |
| 硬件无关 | 任何硬件四文件接入 |
| 开源可商用 | 完全可自定义 |
| 模块化 | 替换任何一层不影响其他层 |

## 参考链接

- 项目仓库：<https://github.com/autonomous-ai/autonomous-os>

## 相关概念

- [Microduck 复刻系列](./tool-microduck.md) — 强化学习双足机器人方向
- [Microduck 装机教程](./tool-microduck-build-tutorial.md) — 从买件到跑起来的全流程
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) — 同为 agent 框架
</content>
</invoke>