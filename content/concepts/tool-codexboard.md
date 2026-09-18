---
type: Tool
title: "CodexBoard（Codex 任务看板）"
description: "把项目任务看板接到 Apple Silicon Mac 上的 Codex，在网页或飞书里派任务、盯执行进度、处理审批；手机上还能随时继续 Mac 上的 Codex 对话。"
resource: "https://github.com/RocYan98/CodexBoard"
tags: [codex, task-board, apple-silicon, mac, feishu, lark, frp, remote]
timestamp: "2026-09-18T04:33:00Z"
---

# CodexBoard（Codex 任务看板）

## 它是什么

[RocYan98/CodexBoard](https://github.com/RocYan98/CodexBoard) 是一个**给 Mac 本机 Codex 加任务看板 + 远程入口**的中间件。装在 Apple Silicon Mac 上后，把项目任务看板接进本机 Codex，让用户在浏览器或飞书里就能：

- 派任务给 Mac 上的 Codex
- 盯执行进度、看结果
- 处理审批

手机端用配套的 Remote 应用，可以**新建或继续跑 Mac 上的 Codex 对话**——流式结果、附件图片、代码 diff 审查与审批都能在手机上处理。

## 关键能力

| 能力 | 说明 |
|------|------|
| 任务看板化 | 把 Codex 的工作组织为可视化任务列表 |
| 双入口 | HTTPS 公网 + Web 账号，或者接飞书自建应用，可同时开 |
| 看板共享 | 两个入口共用同一块看板 |
| 公网穿透 | 通过 frp 隧道做公网访问 |
| 手机 Remote | 移动端继续 Mac 上跑着的 Codex 会话 |
| 流式 / 附件 / diff | 移动端能看流式输出、图片附件、代码 diff、批审批 |

## 适合什么场景

- 长期让 Codex 跑在 Apple Silicon Mac 上的开发者，希望用任务看板而不是纯命令行驱动它。
- 想在飞书工作流里派 Codex 任务、合并到现有团队审批流的团队。
- 经常离开电脑、需要在手机上**继续** Mac 上 Codex 对话的人。

## 与相关概念的关系

- [Computer Use（计算机使用）](./term-computer-use.md) — CodexBoard 让 Codex 不再依赖「人在电脑前」的前提，是 Computer Use 时代的远程延伸形态。

## 参考

- 项目链接：<https://github.com/RocYan98/CodexBoard>

![看板界面](https://pbs.twimg.com/media/HSdmDdkagAAtYSX.jpg)
