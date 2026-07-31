---
type: "Tool"
title: "Eve Directory（nolly-studio/eve-directory）"
description: "Eve 智能体（agent）的开放注册中心——通过 shadcn CLI 把智能体装进项目，匿名可浏览仓库，GitHub 登录即可贡献，可用 Composer 一次打包多个。"
resource: "https://github.com/nolly-studio/eve-directory"
tags: "[eve, agent-registry, shadcn-cli, open-source, agent-marketplace]"
timestamp: "2026-07-31T20:30:00Z"
---

# Eve Directory

[Eve Directory](https://github.com/nolly-studio/eve-directory) 是 **Eve 智能体（agent）的开放注册中心**——一个让社区共同发现、安装和贡献 Eve agent 的目录站。安装走 `shadcn` CLI，浏览无需登录，贡献靠 GitHub 登录，多包组合用 Composer。

## 它是什么

类似 shadcn/ui 的 add 流程，但服务对象从「UI 组件」换成了「agent」：

- **发现**：匿名浏览即可看每个 agent 的文件内容
- **安装**：用 shadcn CLI 把 agent 拉到自己项目里
- **贡献**：GitHub 登录后提交自己的 agent
- **组合**：用 Composer 一次打包多个 agent

## 为什么用它 / 适合什么场景

- 想找现成的 Eve agent 而不是从零写
- 想把自己写的 agent 发布给社区且享受「复制即用」体验
- 想一次性组合 / 部署多个 agent

## 关键能力

| 能力 | 说明 |
|------|------|
| 匿名浏览 | 不登录可看完整 agent 文件源码 |
| shadcn CLI 安装 | 与 shadcn/ui 同一命令行体验，`npx shadcn add <agent>` |
| GitHub 登录贡献 | OAuth 提交流程无需额外账号体系 |
| Composer | 一个命令打包多个 agent 一起装 |
| 目录索引 | 集中展示所有可用 agent 及元信息 |

## 相关概念

- [agentcn（shadcn 的 AI Agent UI 仓库）](./tool-agentcn.md) — 同样走 shadcn CLI，但服务 UI 组件而不是 Eve agent
- [Vercel Eve 框架](./tool-vercel-eve-framework.md) — Eve Directory 注册的「Eve agent」的运行时框架
- [shadcn/improve](./tool-shadcn-improve.md) — 用最强模型审计代码，CLI 体验同源
- [agentcn registry 范式](./tool-agentcn.md) — 对「registry + 一行命令」的范式示范，Eve Directory 把同范式带到 agent 域
