---
type: "Tool"
title: "WechatOnCloud（云微）"
description: "Gloridust 开源的「云端微信 / 多账号管理」项目：通过 chromium 容器化运行多个独立 web 微信、X、Telegram、Instagram、小红书等账号；利用社媒 Web 通知打通 PWA 推送，实现跨端一致体验。"
tags: "[pwa, cloud, multi-account, chromium, wechat, social-media]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/Gloridust/WechatOnCloud"
---

# WechatOnCloud（云微）

## 它是什么

[`WechatOnCloud`](https://github.com/Gloridust/WechatOnCloud)（项目作者自称为「**云微**」）是 @gloridust 开源的项目：**把 Web 版微信 / X / Telegram / Instagram / 小红书等「支持浏览器登录」的社交媒体，装进一个 chromium 容器里**，让你在云端同时跑多个账号，再通过 PWA 通知机制让手机 / 桌面端都能收到推送。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多账号多开 | 每个社媒账号一个独立 chromium 容器，会话隔离 |
| 支持社媒 | 微信网页版、X、Telegram Web、Instagram、小红书 等（凡有 Web 版即可加） |
| 跨端 PWA 通知 | 利用社媒的 Web 通知，通过 PWA 推到手机 / 桌面，体验接近原生 App |
| 云端常驻 | 在 VPS / NAS 上 24h 运行，手机端不再受「多端登录踢人」限制 |
| 截图 | 截图即存证，适合客服 / 运营场景 |

## 适合谁

- **多账号运营** —— 跨境电商 / 自媒体矩阵 / 客服团队。
- **个人多账号** —— 工作号 + 生活号分开。
- **被「手机端才能扫码」束缚** —— 在云端登录一次后，所有设备走 PWA。

## 风险 / 注意

- **违反部分平台 ToS** —— 大部分社媒明确禁止多账号 + 自动化；账号封禁风险自担。
- **浏览器指纹** —— chromium 容器化后指纹仍可能被平台识别为同一设备，建议配合代理池。
- **资源占用** —— 每个账号一个 chromium 容器，10 个账号 ≈ 10 × 300MB 内存。

## 相关概念

- [Cabinet](./tool-cabinet.md) — 同样强调「本地 / 云端常驻 + 多源聚合」
