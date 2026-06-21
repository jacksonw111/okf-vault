---
type: "Tool"
title: "agentcn（shadcn 的 AI Agent UI 仓库）"
description: "由 shadcnlabs 发布、构建在 Vercel Eve 与 flueai 之上的开源 AI Agent UI 组件集合，零配置一行命令安装，与 shadcn/ui copy-paste 兼容，并预置 10+ 可投产的 Agent 配方。"
resource: "https://agentcn.dev"
tags: "[agent, ui, shadcn, eve, registry]"
timestamp: "2026-06-21T00:30:00Z"
---

# agentcn（shadcn 的 AI Agent UI 仓库）

## 它是什么

[agentcn](https://agentcn.dev) 是 `@shadcnlabs` 在 2026-06 推出的开源项目，把「AI Agent 需要的 UI 积木」做成了 shadcn/ui 风格的 registry：一个 Agent = 一组可复制粘贴的组件块，零配置、一行命令安装，10+ 可投产的 Agent 配方全部免费开源。

底层基于 **Vercel Eve**（filesystem convention 风格的 Agent 框架）与 **flueai**。

## 关键卖点

- **零配置、一行命令安装** —— `npx agentcn add ...` 即可拉取组件。
- **shadcn/ui 兼容** —— 复用 shadcn/ui 习惯：「复制粘贴进项目 = 拥有它」，不锁版本、不绑 npm 依赖。
- **10+ 可投产 Agent 配方** —— 研究助手、对话机器人、Agent 监控面板等开箱即用模板。
- **完全可定制** —— 组件代码直接落到项目源码里，改起来没有 vendor 黑盒。
- **100% 开源** —— MIT 协议，没有「免费增值」陷阱。

## 演示

- 视频：<https://video.twimg.com/amplify_video/2068381899249397760/vid/avc1/1920x1080/FrZUE5KycTtpZisY.mp4?tag=28>

## 与 OKF 知识库的关系

> 它复用 shadcn/ui 的「复制即拥有」哲学，与 OKF 的「一份 Markdown = 一个概念、放进目录就能用」思路同源 —— 都是反 SaaS 锁定、反黑盒基础设施。

## 相关概念

- [shadcn/improve](tool-shadcn-improve.md) — 同一作者社群作品，用最强模型审计代码
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — agentcn 的底层 Agent 运行时
- [Agent Skills（代理技能包）](term-agent-skills.md) — 概念元定义