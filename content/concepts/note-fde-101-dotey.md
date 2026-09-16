---
type: "Note"
title: "FDE 入门课（Anthropic 工程师 Kevin Bai 分享）"
description: "Anthropic Applied AI 工程师 Kevin Bai（前 Rippling FDE 创始成员、前 Palantir）做的 FDE 101 分享：FDE 解决的问题、与外包开发的差异、要不要做 FDE 的两个判断问题、2026 年 AI 带来的新变化、什么样的人适合做 FDE。"
tags: "[fde, career, sales, deployment, ai, palantir, anthropic]"
timestamp: "2026-09-16T16:17:00Z"
---

# FDE 入门课（Anthropic 工程师 Kevin Bai 分享）

## 它是什么

Anthropic **Applied AI 团队**的 Kevin Bai（前 **Rippling FDE 创始成员**、前 **Palantir**）做的一次 **FDE 101** 分享，把前线部署工程师（Forward Deployed Engineer, FDE）这个角色讲得很系统。

> 视频原始链接：<https://www.youtube.com/watch?v=KwhgfwOSToQ>
> 原帖原始链接：<https://x.com/dotey/status/2099982947394687156>

## 关键论点

### 一个数据点

上市 SaaS 公司里，按平均合同金额排：**Palantir 400 万美元**、ServiceNow 120 万、Workday 60 万，剩下的没有超过 50 万。Palantir 几千人做到了别人几万人做不到的客单价——**靠的就是 FDE 模式**。

### FDE 到底解决什么问题

- Palantir 的 Foundry 是高门槛应用构建平台，但买家是石油 / 消费品行业的非技术高管。
- 客户买的**既不是软件也不是咨询，而是「结果」**——货架上多多少商品、产线效率提升多少。
- FDE 是把工程师派到客户那里，深入业务场景，在平台上把东西建出来。

### FDE 和外包开发的区别

> 如果每次都从零给客户写定制代码，你做的不是 FDE，是外包开发。

- FDE 成立的前提是**有一个可复用平台**，工程师在平台已有能力上组装和定制。
- 没有共享基础组件，维护成本会吞掉所有利润。

### 什么时候需要 FDE

两个问题就能判断：

1. **你是不是必须把复杂技术卖给非技术买家？** 客户是工程师（如 GitHub、Datadog）或产品开箱即用（如 Slack、Jira），都不需要 FDE。
2. **你有没有可复用平台？** 愿不愿意投入去建？没有共享基础组件，FDE 不可持续。

### 2026 年的新变化

- AI 让构建软件极其容易，几乎所有平台都在走向 Agent 化、高度可定制。
- 客户越来越搞不清产品能做什么——**FDE 从 Palantir 独有的小众玩法，变成更多软件公司需要认真考虑的事**。

### 什么样的人适合做 FDE

> FDE 就是一个你**信任到可以让他直接面对客户**的软件工程师。

技术能力是基本盘，但还得能代表公司去跟客户打交道。

## 与「FDE 完整指南」的差异

- [FDE 完整指南（范冰）](./note-fde-guidance-book.md) — 系统性电子书，覆盖三部分 / 150 个案例
- 本条笔记 — 一次公开分享，重点在「2026 年 AI 化后 FDE 是否还有价值」的视角

## 相关概念

- [FDE 完整指南（范冰）](./note-fde-guidance-book.md) — 同主题系统化资料
- [Harness Engineering](./term-harness-engineering.md) — 与 FDE 的「平台 + 定制化」思路同源