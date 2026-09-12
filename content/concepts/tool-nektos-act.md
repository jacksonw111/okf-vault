---
type: "Tool"
title: "nektos/act（本地跑 GitHub Actions）"
description: "71.4k star 的本地跑 GitHub Actions 工具：改完 workflow 本地直接测，几秒出结果；环境变量 / 文件系统与 GitHub 对齐，本地跑通基本等于线上跑通。"
resource: "https://github.com/nektos/act"
tags: "[github-actions, ci, local-dev, devops, docker]"
timestamp: "2026-09-12T22:30:00Z"
---

# nektos/act

## 它是什么

[nektos/act](https://github.com/nektos/act) 是 GitHub 上 **71.4k star** 的**本地跑 GitHub Actions 工具**：改完 workflow 直接本地测，几秒出结果，不用每次 commit push 等 CI。

## 核心特性

| 特性 | 说明 |
|------|------|
| 本地跑 | 改完直接本地测 |
| 秒级反馈 | 不用等 CI 队列 |
| 环境对齐 | 与 GitHub 同环境变量 / 文件系统 |
| 双用 | 当本地任务 runner 也行 |
| 替代 Makefile | `.github/workflows/` 两处用 |

## 为什么用它 / 适合什么场景
- 频繁调 workflow 不愿每次 push 等 CI。
- 本地写 / 测 CI 配置提速。
- 想用统一格式管理本地任务与 CI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地执行 | 跑 .github/workflows/ |
| 环境对齐 | 与 GitHub 一致 |
| 快速反馈 | 秒级 |
| Docker 镜像 | 复用 GitHub 同镜像 |
| 双用 | 本地任务 + CI |
| 71k+ star | 久经考验 |

## 参考链接

- 项目仓库：<https://github.com/nektos/act>

## 媒体

- ![](https://pbs.twimg.com/media/HR-YAuha0AA5rkU.jpg)

## 相关概念
