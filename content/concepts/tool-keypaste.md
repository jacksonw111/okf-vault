---
type: "Tool"
title: "keypaste（本地 KDBX 密钥管理 + Agent 审批）"
description: "notinferred 出品的开源密码 / 密钥管理器：用 KeePass KDBX 4 格式存一个本地文件，不联网、不注册账号，KeePassXC 可直接打开；AI Agent 取每个字段都要经人工审批，避免直接拿走 .env。"
resource: "https://github.com/notinferred/keypaste"
tags: "[password-manager, kdbx, keepass, ai-agent, approval-gate, security]"
timestamp: "2026-10-04T13:00:00Z"
---

# keypaste

## 它是什么

[keypaste](https://github.com/notinferred/keypaste) 是 **notinferred** 出品的开源**密码与密钥管理器**——用 KeePass 的 KDBX 4 格式存一个本地文件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 存储格式 | KeePass KDBX 4 |
| 离线 | 不联网、不注册账号 |
| 互操作性 | KeePassXC 可直接打开 / 编辑同一文件 |
| 跨平台验证 | CI 在 Linux / macOS / Windows 上双向验证与 `keepassxc-cli` 的读写兼容性 |
| Agent 审批 | AI Agent 取每个字段都要经人工审批 |

## 与传统做法的对比

| 场景 | 传统做法 | keypaste |
|------|---------|---------|
| Agent 读密钥 | 直接读 `.env` | 必须经过人工审批 |
| 密钥存储 | 散落在 .env / config / secret manager | 收进统一 KDBX 保险库 |
| 跨工具兼容 | 各家密码管理器互不兼容 | 与 KeePassXC 直接互通 |
| 联网风险 | 在线密码管理器有外泄面 | 完全本地，零联网 |

## 适合场景

- AI Agent 频繁需要访问项目密钥 / API Key 的开发场景
- 想用开源 / 本地工具替代 1Password / Bitwarden 类服务
- 团队需要「Agent 不能自助拿走密钥」的强治理

## 参考链接

- 项目链接：<https://github.com/notinferred/keypaste>

## 相关概念

- [ThinkWatch-Lite](./tool-thinkwatch-lite.md) — 同样从「Agent 不能自助外发凭据」出发的本地网关