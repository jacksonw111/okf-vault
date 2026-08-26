---
type: "Tool"
title: "doop（开源对标 Paper.design 的 HTML 协作画布）"
description: "kgoedecke 出品的 TypeScript + AGPL-3.0 开源协作画布，对标 Paper.design：Canvas + Frame 组成画布，Frame 内跑沙箱 iframe 渲染真实 HTML，光标 / presence / 评论 / 活动日志走 WebSocket 同步。"
tags: "[design, collaboration, canvas, frame, websocket, paper, opensource]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/kgoedecke/doop"
---

# doop（开源对标 Paper.design 的 HTML 协作画布）

## 它是什么

[`doop`](https://github.com/kgoedecke/doop) 是 kgoedecke 出品的 **TypeScript + AGPL-3.0** 开源协作画布，「**对标 Paper.design**」：

- 画布由 **Canvas + Frame** 组成
- Frame 内是**沙箱 iframe 渲染的真实 HTML**——不是图片 / 截图，可以交互
- 协作者的 **光标 / presence / 评论 / 活动日志** 走同一条 **WebSocket** 同步
- 适合做产品 / 营销 / 落地页的多人设计协作

## 为什么用它 / 适合什么场景

- 想要 Paper.design 的能力，但希望自托管 / 数据自主
- 把多个 Frame 排版成 marketing landing / 调研 / 设计参考时仍要 HTML 真实响应
- 不希望依赖 SaaS 商业产品的帐号 / 收费档

## 关键能力

| 能力 | 说明 |
|------|------|
| Canvas + Frame 模型 | 把每张「画」视为 Frame 拼贴 |
| HTML 真渲染 | Frame 内是 iframe 而非位图 |
| 多人协作 | 光标 / presence / 评论 / 活动日志 |
| WebSocket 同步 | 一条通道统揽实时状态 |
| AGPL-3.0 | 强 copyleft，自托管友好 |

## 媒体

![](https://pbs.twimg.com/media/HQiOZKhbwAAwmi4.jpg)

## 参考链接

- [项目链接](https://github.com/kgoedecke/doop)
