---
type: "Tool"
title: "无状态自托管 TOTP 工具（zeropl/2FA）"
description: "无服务器、无数据库、无注册的 TOTP 两步验证码生成器，密钥通过 URL 片段在浏览器本地计算。"
resource: "https://github.com/zeropl/2FA"
tags: [security, totp, 2fa, self-host, web]
timestamp: "2026-06-23T15:30:00Z"
---

# 无状态自托管 TOTP 工具（zeropl/2FA）

## 它是什么

一款纯静态、无状态的自托管两步验证（TOTP）生成器。打开网页、扫码/手动录入密钥即可在浏览器本地算出 6 位验证码；整个过程不向服务器发送任何东西，关掉页面后密钥随 URL 片段一起丢弃，刷新即失忆。

## 为什么用它 / 适合什么场景

- **临时共享**：在群聊里给同事生成一个 5 分钟有效的验证码链接，过期就无效；
- **不想装 App**：移动端没装 Authenticator、桌面又不想留隐私痕迹时打开即用；
- **演示 / 教学**：前端调试 OAuth2 登录流程时随手生成一个 TOTP；
- **离线**：把页面本地存一份，离线状态也能算码（时钟本地走）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 无服务器 | 任何静态托管（Github Pages / S3 / Nginx）即可跑 |
| 无数据库 | 密钥不进任何持久化存储 |
| 无注册 | 没有账号、没有 token，直接访问 |
| URL 片段传密钥 | 密钥只在浏览器 hash（`#`）中可见，不会被服务器日志记录 |
| 标准 RFC 6238 | 与 Google Authenticator / 1Password / Authy 等主流 TOTP App 兼容 |

## 媒体 / 原始链接

![界面截图](https://pbs.twimg.com/media/HLZno8JaIAA7er1.jpg)

- 项目链接：<https://github.com/zeropl/2FA>

## 相关概念

- [SafeBucket](tool-safebucket.md) — 同属「预签名 / 客户端签名」自托管思路，省去服务器中转