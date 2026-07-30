---
type: Tool
title: "hark（任意 webhook → 带来源标识的 iPhone 推送）"
description: "把任意 webhook 转成带来源标识的 iPhone 推送通知，无需自己搭推送服务。"
resource: "https://github.com/R44VC0RP/hark"
tags: [webhook, push-notification, ios, serverless, automation]
timestamp: "2026-07-30T08:45:00.000Z"
---

# hark

## 它是什么

**Webhook → iPhone 推送的轻量桥**——很多 SaaS / 脚本 / AI agent 想推通知到手机，但搭 APNs 要证书、要后端、运营成本高。

hark 把这件事压缩到一个轻量服务：

- 接收任意 webhook（HTTP POST）
- 转成 iPhone 推送通知
- 自动加来源标识（哪个 hook 来的）
- 不用自己搞 APNs 证书 / 后端服务

![效果视频](https://video.twimg.com/amplify_video/2082311429273862144/vid/avc1/1280x720/Q_RJBrIdhwRHpMvO.mp4?tag=29)

## 关键能力

| 能力 | 说明 |
|------|------|
| 任意 webhook 入 | HTTP POST 即可 |
| iPhone 推送 | APNs 转发 |
| 来源标识 | 每个 hook 一个标识 |
| 无需自建推送 | 跳过 APNs 证书 |
| 自托管 | 数据私有 |

## 适合谁

- 想让 CI / 脚本 / AI agent 推手机通知的开发者
- 想自托管 push 通道的隐私派
- 不想买 SaaS push relay 服务的极简派

## 原始链接

- [项目仓库](https://github.com/R44VC0RP/hark)
- [推文剪藏](https://x.com/QingQ77/status/2082749286647812539)

## 相关概念

- [shuangzi-xubei（双子续杯）](./tool-shuangzi-xubei.md) — iPhone 桌面小组件，锁屏看 Claude Code / Codex 额度
- [Hermex](./tool-hermex.md) — iOS 应用，远程操控自托管 Hermes AI 代理
- [Squawk](./tool-squawk.md) — macOS 智能通知代理，给 Claude Code 用