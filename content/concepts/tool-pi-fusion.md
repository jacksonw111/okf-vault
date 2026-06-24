---
type: "Tool"
title: "pi-fusion（leblancfg/pi-fusion）"
description: "Pi 的多模型并行扇出扩展：每次提问前先派数个工作模型同时思考，再把答案汇总成一条；终端实时分屏显示，Esc 退回普通模式。"
resource: "https://github.com/leblancfg/pi-fusion"
tags: [pi, multi-model, fan-out, extension, orchestration]
timestamp: "2026-06-23T15:30:00Z"
---

# pi-fusion（leblancfg/pi-fusion）

## 它是什么

Pi 编码代理的一个扩展，给「单模型思考」叠加了「并行扇出 + 汇总」层。每次提问前，先派多个工作模型并行思考，再把答案合并成一条完整回复。运行期间终端实时分屏显示每个工作模型的输出，按 Esc 即可取消并退回普通模式。

## 为什么用它 / 适合什么场景

- **省 token / 提质量**：研究显示部分编码任务用多模型并行比单用最强模型更快、更便宜；
- **观察模型差异**：分屏可视化让用户直接对比不同模型在同一 prompt 下的输出；
- **项目上下文预热**：自带的「发现代理」可提前加载项目上下文，提示词也会自动改写；
- **会话可恢复**：预设可保存，会话可存档回放。

## 关键能力

| 能力 | 说明 |
|------|------|
| 并行扇出 | 多工作模型同时思考 |
| 答案汇总 | 把多个回答合并为一条 |
| 分屏显示 | 终端 TUI 实时看到每个模型在干嘛 |
| 发现代理 | 提前加载项目上下文 |
| 提示词改写 | 自动重写以适配多模型 |
| 会话存档 | 可保存 / 恢复整套对话 |
| 可取消 | Esc 即退回普通 Pi 模式 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/leblancfg/pi-fusion>

## 相关概念

- [pi-task](tool-pi-task-delegation.md) — 同属 Pi 生态扩展（pi-task 偏子任务委派，pi-fusion 偏多模型汇总）
- [Pi Web Agent](tool-pi-web-agent.md) — 同样为 Pi 加能力（联网工具）
- [Brigade](tool-brigade.md) — 同样是「多 AI 协同工作」的方案（Brigade 走多 Agent，pi-fusion 走多模型）