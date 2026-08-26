---
type: "Tool"
title: "qiling-soulmate（多 Agent CLI 本地工作台）"
description: "Soulmate-Halo 独立开发的本地优先桌面应用：把你常用的几个 Agent CLI 收进同一工作台统一调度，某条通道挂了别的照常跑；强模型拆任务 / 定方向 / 做终审，便宜模型跑读文件 / 查资料 / 重复活；中间靠「器灵压缩」规则压主模型上下文。"
tags: "[agent, cli, local-first, router, multi-agent, desktop, cost-splitting]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/Soulmate-Halo/qiling-soulmate"
---

# qiling-soulmate（多 Agent CLI 本地工作台）

## 它是什么

[`qiling-soulmate`](https://github.com/Soulmate-Halo/qiling-soulmate) 是 **Soulmate-Halo** 个人独立开发的 **本地优先桌面应用**——把多套 **Agent CLI 收进同一工作台统一调度**：

- **核心场景**：你常用 Codex / Claude Code / Gemini CLI / OpenCode 等多个 Agent CLI 时，往往需要「哪个适合干啥就用哪个」
- **容错**：某条通道挂了，别的照常跑（不因为一个服务商宕机全停）
- **按任务强弱分配模型**：
  - **强模型**（多花 token）→ **拆任务 / 定方向 / 做终审**
  - **便宜模型**（少花 token）→ **读文件 / 查资料 / 跑重复活儿**
- **「器灵压缩」规则**：中间靠一套压缩机制，**压住主模型的上下文**不爆

## 为什么用它 / 适合什么场景

- 个人开发者想用**多 Agent CLI 调度**，但不想逐个开终端
- 对某通道服务中断零容忍（云上 API 偶尔抽风）
- 想**按任务复杂度自动分级**用模型，**控制总成本**
- 想省掉主模型上下文膨胀的问题

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Agent CLI 统一调度 | 一个 UI 操作多套 CLI |
| 通道容错 | 单点失败不影响其他 |
| 模型分工 | 强 / 弱模型按任务分配 |
| 上下文压缩 | 「器灵压缩」规则 |
| 本地优先 | 不上传任务数据 |
| 独立开发者维护 | 单兵长期跟进 |

## 媒体

![](https://pbs.twimg.com/media/HQibtA_b0AADnui.jpg)

## 参考链接

- [项目链接](https://github.com/Soulmate-Halo/qiling-soulmate)

## 相关概念

- [Minke](./tool-minke.md) — 把 DSH 装进本地优先桌面工作台
- [harness-router](./tool-harness-router.md) — OpenAI Responses API 兼容的统一网关
- [Comet](./tool-comet-zeronsh.md) — 把多套编码 agent 收拢到本机控制，会话存本机
- [OPCNexus](./tool-opc-nexus.md) — 单人公司 / 独立开发者的本地优先 Agent 管理器
