---
type: Tool
title: "clearai-dsh"
description: "DeepSeek Harness 里的研究过程加装一道「证据链 + 独立评审」机制——每条结论由证据链支撑，且必须经过独立评审，而不是模型自己宣布完成。"
resource: "https://github.com/Clearailhc/clearai-dsh"
tags: "[deepseek-harness, research, ontology, ai-agent, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# clearai-dsh

## 它是什么
一个**给 DeepSeek Harness 研究流程补的「完工护栏」**：

> 让 DeepSeek Harness 里的研究过程产出可检索的领域本体；每条结论由证据链和独立评审支撑——而不是模型自己宣布完成。

七段循环、结论带边界和证据链、矛盾自动摆出来——这套账本确实能管住 agent 随口宣布完工的毛病。

## 为什么用它 / 适合什么场景
- DeepSeek Harness 做研究时，常常「模型自报完成」而实际缺证据 / 漏矛盾。
- 希望每条结论都能查到证据链，便于复核与审计。
- 想要在多轮研究循环里把矛盾显式摆出来，避免掩盖。
- 想把研究产出沉淀成可检索的领域本体。

## 关键能力
| 能力 | 说明 |
|------|------|
| 流程 | 七段研究循环 |
| 结论属性 | 带边界 + 带证据链 |
| 评审 | 独立评审（不靠模型自评） |
| 矛盾处理 | 自动摆出来 |
| 产出 | 可检索的领域本体 |
| 价值 | 治「agent 随口宣布完工」的毛病 |

## 相关概念
- [DeepSeek Harness Handbook](note-deepseek-harness-handbook.md) — DeepSeek Harness 的方法论基础
- [jingyun-dsh](tool-jingyun-dsh.md) — 同样面向 DeepSeek Harness 的扩展（商业闭环方向）

## 项目链接
- 项目主页：<https://github.com/Clearailhc/clearai-dsh>

## 媒体
- 截图：<https://pbs.twimg.com/media/HSyKuSGaUAAR4m-.jpg>
