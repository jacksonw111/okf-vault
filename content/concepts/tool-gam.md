---
type: "Tool"
title: "GAM（GitHub 账号管理器）"
description: "TypeScript 写的命令行工具，专门用来在本地管理多个 GitHub 账号，通过 OAuth 设备流程认证，无需密码 / PAT / SSH 配置，账号切换无缝。"
tags: "[github, cli, oauth, typescript, devtools, account-manager]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/miguelbalvin-dev/gam"
---

# GAM（GitHub 账号管理器）

## 它是什么

[`GAM`](https://github.com/miguelbalvin-dev/gam) 是一个用 **TypeScript 写的 CLI 工具**，专门解决「同一个开发机要同时管理多个 GitHub 账号」的痛点：通过 **OAuth 设备流程（Device Flow）**认证，**完全不需要**手动管理密码、Personal Access Token 或 SSH key。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多账号管理 | 一台机器同时管理任意数量的 GitHub 账号 |
| OAuth 设备流程 | 通过浏览器一次性授权，CLI 轮询拿到 token |
| 无 PAT 配置 | 不需要手动 `gh auth login` 走 PAT 或 SSH |
| 无 SSH 配置 | 不依赖 SSH key 上传到 GitHub |
| TypeScript 实现 | 源码可读、可改、可打包发布 |
| 账号切换 | 一条命令切到目标账号，无需重启 shell |

## OAuth 设备流程的好处

- **零明文凭证**：本地不存密码 / PAT，token 由 GitHub 直接签发
- **零 SSH 折腾**：不用每个账号生成不同 SSH key 并配置 ssh-agent
- **可撤销**：在 GitHub 网页端撤销授权即可立即吊销本地 token
- **审计清晰**：每次授权都在 GitHub 设备列表里留痕

## 适用场景

- 自由职业者同时给客户 A、公司 B、自己项目 C 各用一个 GitHub 账号
- 安全团队成员需要定期切换身份做权限验证
- 经常需要在多账号间 `git push` 但不愿记 SSH 别名 / `gh auth switch` 的细节

## 参考链接

- [项目链接](https://github.com/miguelbalvin-dev/gam)

## 相关概念

- [Proxide](tool-proxide.md) — 任意 Agent 经 MCP / 浏览器桥接 ChatGPT Pro 等网页强模型，处理账号态的另一种思路