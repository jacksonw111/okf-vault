---
type: "Tool"
title: "bow-git-vault（Windows Git Electron GUI）"
description: "把 Windows 上的克隆仓库、看状态、暂存、提交、拉取、推送、切分支这些 Git 操作收进一个 Electron 桌面界面，不用再在文件夹和命令行之间来回切。"
tags: "[git, windows, electron, desktop, dev-tools]"
timestamp: "2026-08-15T14:17:00Z"
resource: "https://github.com/PotterService/bow-git-vault"
---

# bow-git-vault（Windows Git Electron GUI）

## 它是什么

`PotterService/bow-git-vault` 是一个 Electron 桌面应用，专门给 Windows 上的 Git 日常操作做图形界面。它把以下操作收进同一个窗口：

- 克隆仓库
- 看仓库状态
- 暂存 / 取消暂存
- 提交
- 拉取 / 推送
- 切换分支 / 创建分支
- 看 diff

用户不用在「文件夹资源管理器」+「Git Bash」+「VSCode」之间反复切。

> ![](https://pbs.twimg.com/media/HPqlFxiaEAIs63R.jpg)

## 为什么用它 / 适合什么场景

- **Windows 用户不爱敲 Git CLI**：习惯 GUI，命令记不住。
- **多仓库管理**：手上几个项目并行，想一个面板看完所有仓库状态。
- **新成员上手**：图形化降低 Git 学习成本。

## 关键能力

| 能力 | 说明 |
|------|------|
| 克隆仓库 | URL 粘贴 → 选择本地路径 → 克隆 |
| 状态查看 | 列出工作区变更（增 / 删 / 改） |
| 暂存 / 取消 | 单文件或批量 |
| 提交 | 带消息框，自动签名（可选） |
| 拉取 / 推送 | 一键 + 远程选择 |
| 分支管理 | 创建 / 切换 / 删除 / 合并（图形化） |
| diff 视图 | 内置文件 diff |
| 跨平台 | Electron 写成，理论也能跑 mac / Linux |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| GitHub Desktop | 图形化但绑 GitHub | 强 GitHub 集成 |
| Sourcetree | Atlassian 出品 | 功能全但重 |
| GitKraken | 商业 | 收费 |
| **bow-git-vault** | **轻量 Electron + 通用 Git** | **专注 Windows + 通用远程** |

## 适用人群

- Windows 上的 Git 用户。
- 习惯 GUI、不愿敲命令的非工程师协作者。
- 维护多仓库、希望统一面板的开发者。

## 参考链接

- [项目链接](https://github.com/PotterService/bow-git-vault)

## 相关概念

- [Conventional Commits](term-conventional-commits.md) — 规范化的 Git 提交消息约定，可与本工具搭配
- [codex-standard-devflow](playbook-codex-standard-devflow.md) — Codex 标准开发流