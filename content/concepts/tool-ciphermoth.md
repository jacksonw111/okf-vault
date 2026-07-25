---
type: Tool
title: "CipherMoth"
description: "自托管密码管理器，采用 Argon2id 派生、Fernet 加密与 PostgreSQL 存储，并将解密密钥限制在浏览器会话内。"
resource: "https://github.com/mr-grj/ciphermoth"
tags: [password-manager, security, self-hosted]
timestamp: "2026-07-25T00:00:00Z"
---

# CipherMoth

自托管密码管理器，采用 Argon2id 派生、Fernet 加密与 PostgreSQL 存储，并将解密密钥限制在浏览器会话内。

## 适用场景

- 需要使用 Argon2id 做密钥派生、Fernet 加密数据的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 加密设计 | 使用 Argon2id 做密钥派生、Fernet 加密数据。 |
| 密钥边界 | 解密密钥仅保存在 sessionStorage，缩短持久暴露窗口。 |
| 密码库组织 | 支持标签、文件夹、TOTP 与自定义字段。 |

## 链接与媒体

- [项目链接](https://github.com/mr-grj/ciphermoth)
- [原始链接](https://x.com/QingQ77/status/2080876949615137153)

![](https://pbs.twimg.com/media/HN9rRppaEAAe28C.jpg)

## 相关概念

暂无需要强关联的现有概念。
