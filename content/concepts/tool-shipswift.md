---
type: "Tool"
title: "ShipSwift（signerlabs/ShipSwift）"
description: "AI 原生的 SwiftUI 组件库 + 全栈 recipe：通过 MCP 把「生产级 SwiftUI 组件（动画 / 图表 / UI / 认证 / 相机 / 聊天 / 订阅墙）」即时喂给 LLM，让 Claude Code、Gemini CLI、Cursor 直接生成真实可编译的 iOS 应用代码。"
tags: "[ai, mcp, swift, swiftui, ios, agent-skills, code-generation]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/signerlabs/ShipSwift"
---

# ShipSwift（signerlabs/ShipSwift）

> 来源：[@QingQ77 on X 2026-06-17](https://x.com/QingQ77/status/2058463261885157435)

## 它是什么

[ShipSwift](https://github.com/signerlabs/ShipSwift) 是 **AI 原生的 SwiftUI 组件库 + 全栈 recipe**——把生产级 SwiftUI 代码（动画、图表、UI 组件、认证、相机、聊天、订阅墙等模块）**通过 MCP（Model Context Protocol）和 Skills 暴露给 LLM**，让 AI 编码 agent 在写 iOS app 时能拿到**完整源码、实现步骤、踩坑经验**，而不是从零猜 API。

## 解决的痛点

LLM 写 SwiftUI 的常见问题：

- **API 记不全**——SwiftUI 每年一大改，模型知识截止后容易用过时写法。
- **缺生产细节**——能写出 `List`，但写不出真正的「带渐变 hero + 错位入场 + 列表 stagger」的成熟页面。
- **缺全栈思维**——SwiftUI 只是 UI，认证 / 相机 / 订阅都要拼后端，纯前端模型拼不全。

ShipSwift 把「**正确、可编译、可抄**」的 SwiftUI + 配套后端合模板做出来，给 LLM 当外挂知识库。

## 关键能力

| 模块 | 内容 |
|------|------|
| 动画 | 渐变 / 错位入场 / 手势过渡 / 弹簧 |
| 图表 | 折线 / 柱状 / 饼图 / 实时刷新 |
| UI 组件 | 列表 / 表单 / 设置页 / Tab / Navigation |
| 认证 | Apple / Google / Email Magic Link |
| 相机 | AVFoundation 封装 / 拍照 / 扫码 |
| 聊天 | 实时消息 / 表情 / 已读 |
| 订阅墙 | StoreKit 2 / 恢复购买 / 试用期 |

## 接入方式

| 工具 | 怎么用 |
|------|--------|
| Claude Code | 通过 MCP server 接入，agent 自动按需加载组件 |
| Gemini CLI | 同上 |
| Cursor | 同上 |
| 直接复制 | 三个开源 Demo App + 组件源码直接抄进 Xcode |

## 授权模式

- **iOS 客户端代码：MIT**——可自由用、可商用。
- **Pro 版**——加后端实现（认证 / 支付 / 推送）+ 合规模板（隐私 / IAP 合规）。

## 三个开源 Demo App

照着抄就能跑——具体项目以仓库 README 为准。

## 与本知识库其他概念的关系

- [Agent Skills 是什么](term-agent-skills.md) — ShipSwift 是「领域专用 skill」的代表，把 iOS SwiftUI 这个垂直领域做成可分发的能力包。
- [Claude Code](tool-claude-code.md) — Claude Code 是 ShipSwift 首批支持的目标 agent 之一。
- [mattpocock/skills](tool-mattpocock-skills.md) — 同一波「skill 仓库」生态；区别是 mattpocock 偏通用 SOP，ShipSwift 偏垂直领域代码库。

## 相关概念

- [Agent Skills 是什么](term-agent-skills.md) — ShipSwift 是「领域专用 skill」的典型实现
- [Claude Code](tool-claude-code.md) — ShipSwift 通过 MCP 首批接入的目标 agent
- [mattpocock/skills](tool-mattpocock-skills.md) — 同一波 skill 生态；通用 SOP vs 垂直代码库的互补
