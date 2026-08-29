---
type: Tool
title: "pi-clinepass（Pi 编码代理的 ClinePass 接入）"
description: "为 pi 编码智能体加上 ClinePass 接入：实现美元计价限额、实时成本跟踪与套餐额度使用情况上报。"
resource: "https://github.com/fifidayone/pi-clinepass"
tags: [pi, clinepass, coding-agent, cost-tracking, billing, subscription]
timestamp: "2026-08-29T21:30:00Z"
---

# pi-clinepass（Pi 编码代理的 ClinePass 接入）

## 它是什么

[fifidayone/pi-clinepass](https://github.com/fifidayone/pi-clinepass) 是给 [pi](./note-dg-ai-pi-agent-tutorial.md) 编码智能体加的 **ClinePass 接入**插件——让 pi 跑任务时遵循 ClinePass 的美元计价限额、实时跟踪成本、并把套餐额度使用情况上报回去。

解决的问题：pi 默认按调用计费时用户对**花了多少、还能用多少**没有直观视图，接 ClinePass 后把账单 / 限额 / 套餐三件事拉成一条线。

## 为什么用它 / 适合什么场景

- 用 pi 跑长任务怕被计费超出预算——给一个**硬限额**；
- 团队 / 公司报销场景：需要看到「本月在 pi 上的花销」；
- 多套餐用户：跨套餐合并计算用量；
- 自动化任务（CI / 批处理）：每次跑都心里有数。

## 关键能力

| 能力 | 说明 |
|------|------|
| 美元计价限额 | 任务运行前 / 运行中按美元成本判断要不要继续 |
| 实时成本跟踪 | 调用一次记一次，本地可见累计花销 |
| 套餐额度上报 | 把 pi 用量上报给 ClinePass 套餐系统 |
| 拦截超支 | 超过设定额度就停 |

## 相关概念

- [Pi Agent Tutorial](./note-dg-ai-pi-agent-tutorial.md) — Pi 编码代理的入门；pi-clinepass 是其「成本可控」配套
- [opencode-usage](./tool-opencode-usage.md) — opencode 的用量跟踪，pi-clinepass 是 pi 同类但更深一层（含限额 + 上报）

## 参考链接

- 项目链接：<https://github.com/fifidayone/pi-clinepass>
- 原始推文：<https://x.com/QingQ77/status/2093507928217231412>
- 媒体：<https://pbs.twimg.com/media/HQu0B_WaEAIvG4q.png>