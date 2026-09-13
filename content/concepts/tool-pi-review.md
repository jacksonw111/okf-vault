---
type: "Tool"
title: "Pi Review（earendil-works 的 Pi 官方 review 插件）"
description: "earendil-works（Pi 作者）出品的 Pi review 插件，通过 `pi install git:...` 一行命令安装，给 Pi 加装代码 review 能力。"
resource: "https://github.com/earendil-works/pi-review"
tags: "[pi, review, earendil, plugin, coding-agent]"
timestamp: "2026-09-12T22:19:00Z"
---

# Pi Review（earendil-works 的 Pi 官方 review 插件）

## 它是什么

[earendil-works/pi-review](https://github.com/earendil-works/pi-review) 是 Pi 作者所在团队 **earendil-works** 出品的 **Pi 官方 review 插件**。一行命令装进 Pi：

```
pi install git:https://github.com/earendil-works/pi-review
```

## 为什么用它 / 适合什么场景

- 已经在用 Pi 写代码，**想让 AI 也帮我做 code review**。
- 想用**作者自己写的 review 规则**而不是社区第三方。
- 想保持 Pi 生态一致——插件就在 Pi 自己的 install 体系里。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一行安装 | 通过 `pi install git:...` |
| 作者出品 | earendil-works（Pi 作者所在团队） |
| 与 Pi 深度集成 | 走 Pi 的插件体系，不是外挂工具 |
| 代码 review 能力 | 给 Pi 加装 review 步骤 |

## 项目链接

- 仓库：<https://github.com/earendil-works/pi-review>

## 相关概念

- [Pi Coding Agent](./tool-pi-coding-agent.md) — Pi Review 的宿主
- [open-code-review（阿里 AI 代码审查）](./tool-open-code-review.md) — 同类定位但跨 agent 的 review harness