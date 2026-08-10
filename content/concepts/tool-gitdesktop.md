---
type: "Tool"
title: "GitDesktop"
description: "theBGuy 维护的开源桌面 Git 客户端：Tauri 2 + React 19 跨 Win/macOS/Linux，GitHub 操作走 gh CLI（不申请 OAuth / 不存令牌），GitHub Enterprise 走已登录 gh 直连，把 PR 生命周期（评审 / 评论 / 指派 / 审批 / 合并 / 解决冲突）+ Actions / Issues / Dependabot 全部搬进应用。"
resource: "https://github.com/theBGuy/GitDesktop"
tags: [git, github, desktop, tauri, react, pr, cli]
timestamp: "2026-08-10T06:30:00Z"
---

# GitDesktop

## 它是什么

[GitDesktop](https://github.com/theBGuy/GitDesktop) 是 theBGuy 维护的一款**开源桌面 Git 客户端**：底层壳是 Tauri 2 + React 19，覆盖 Windows / macOS / Linux；面向 GitHub / GitLab / Bitbucket 三平台。它有两个非常鲜明的设计取舍：

- **GitHub 操作全部走 `gh` CLI**，应用本身**不申请 OAuth 权限也不存令牌**——能做的事就是「当前已登录 gh 那一套会话能做的事」。
- **底层 git 操作全部走系统 git**，所以登录过 gh 的 GitHub Enterprise 服务器也能直接用。

UI 沿用 GitHub Desktop 那种好上手的交互，**完整的 PR 生命周期被搬进应用**——评审、评论、指派、审批、合并、解决冲突都不用开浏览器；另外还内置 Actions 面板、Issues / Discussions、Dependabot 等安全告警、仓库浏览与克隆。

## 为什么用它 / 适合什么场景

- 不想让 Git 客户端再开 OAuth / 走一套自带账号系统；信任并复用系统里已有的 `gh` 登录就够了。
- 在企业里混用 GitHub Enterprise，希望客户端不需要重新认证。
- 想用一套桌面工具覆盖 PR 评审 + Actions 监控 + 仓库浏览，不想在浏览器与终端间来回切。

## 关键能力

| 能力 | 说明 |
|------|------|
| Tauri 2 + React 19 | 跨平台原生壳 + 现代前端 |
| 走 `gh` CLI | 不申请 OAuth / 不存令牌 |
| 走系统 git | GHE 直连，免重认证 |
| PR 全生命周期 | 评审 / 评论 / 指派 / 审批 / 合并 / 解决冲突 |
| Actions 面板 | 不开浏览器看工作流运行状态 |
| Issues / Discussions | 浏览 / 跳转常用操作 |
| Dependabot 告警 | 安全告警面板内可见 |
| 仓库浏览克隆 | 仓库管理内嵌 |

## 媒体

![](https://pbs.twimg.com/media/HPQBEVsbAAAL0nf.jpg)
![](https://pbs.twimg.com/media/HPQBFIgaYAAKgyJ.jpg)

## 参考链接

- [项目仓库](https://github.com/theBGuy/GitDesktop)
- [原始链接](https://x.com/QingQ77/status/2086701581391564998)
