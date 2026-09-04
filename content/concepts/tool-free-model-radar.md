---
type: Tool
title: "free-model-radar（免费模型可用性与速度定时巡检）"
description: "定时把一批免费大模型跑一遍，测出谁当前可用、谁最快，直接给出当下最优选择；应对免费模型数量多、下线换代频繁的问题。"
resource: "https://github.com/a1667834841/free-model-radar"
tags: [llm, benchmark, monitoring, free-tier, model-selection]
timestamp: 2026-09-04T12:00:00Z
---

# free-model-radar（免费模型可用性与速度定时巡检）

## 它是什么

免费大模型多、下线和换代又快，「今天还能用的那个」明天可能就不行了。free-model-radar 定时把候选模型挨个跑一遍，测**可用性**和**响应速度**，直接输出当前最优的那个。

![](https://pbs.twimg.com/media/HRRWHl2asAA7LxY.jpg)

## 为什么用它 / 适合什么场景

- 手上有一堆免费额度 / 免费接口，不想每次手工试哪个还活着。
- 给自己的应用挑默认模型时，需要一个持续更新的可用性快照而非一次性测试。

## 关键能力

| 能力 | 说明 |
|------|------|
| 定时巡检 | 周期性对一批免费模型发起真实调用 |
| 可用性判定 | 标出当前能用 / 不能用 |
| 速度排名 | 比较响应速度，给出最快的选择 |

## 参考链接

- 项目链接：<https://github.com/a1667834841/free-model-radar>
- 原始链接：<https://x.com/QingQ77/status/2095759514356085194>

## 相关概念

- 暂无强关联概念。
