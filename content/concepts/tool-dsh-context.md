---
type: Tool
title: "dsh-context (bowenliang123/dsh-context)"
description: "DeepSeek Harness 的上下文窗口可视化插件，把黑盒的 token 用量与压缩过程拆开，搞清 token 花在哪、怎么被压缩的"
resource: "https://github.com/bowenliang123/dsh-context"
tags: [deepseek-harness, dsh, context, token, visualization, debugging]
timestamp: 2026-08-20T15:01:00Z
---

# dsh-context (bowenliang123/dsh-context)

## 它是什么
[`bowenliang123/dsh-context`](https://github.com/bowenliang123/dsh-context) 是 **DeepSeek Harness (DSH)** 的一个上下文窗口可视化插件。DSH 的 agent 上下文窗口本身是个"黑盒"——几万 token 看不到结构。这个插件把它**拆开**呈现：每段 token 的来源、内容占比、压缩时间点与压缩策略，一目了然。

## 为什么用它 / 适合什么场景
- 调试 agent 行为时怀疑"上下文被压坏了 / 漏了关键信息"，但肉眼看不到压缩过程。
- 优化 prompt / 系统消息的 token 占用，需要看到数据再裁剪。
- 做 agent benchmark / 复现实验，想精确控制"哪一段上下文在哪一轮被丢"。

## 关键能力
| 能力 | 说明 |
|------|------|
| Token 分布 | 把上下文按来源 / 类型拆开，标出占比 |
| 压缩追溯 | 看到什么时候触发了压缩、压缩前 → 后差异 |
| 段落级定位 | 点一段就跳回原始消息位置 |
| DSH 原生集成 | 作为 dsh 插件，不另起服务 |

## 媒体
- ![dsh-context 截图](https://pbs.twimg.com/media/HQEDx-PboAAXJXG.jpg)

## 相关概念
- [项目仓库](https://github.com/bowenliang123/dsh-context) — 仓库主页
- [dsh-sessiongraph](./tool-dsh-sessiongraph.md) — 同样做"对话过程可视化"，但偏结构化导图；本工具偏 token 维度
- [dsh-visualize](./tool-dsh-visualize.md) — dsh 把单次模型输出可视化的另一个插件
- [dsh-usage-stats](./tool-dsh-usage-stats.md) — 多供应商账户余额与 token 用量监测
