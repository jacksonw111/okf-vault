---
type: "Tool"
title: "Vercel Labs `run`（QuickJS 沙箱执行 npm 包）"
description: "Vercel Labs 出品的 npm 包：在 worker 线程里跑全新 QuickJS 上下文，无 Node.js 环境、文件系统、模块或网络权限；来宾代码只能调用宿主注入的函数。"
resource: "https://github.com/vercel-labs/run"
tags: [sandbox, security, quickjs, vercel, npm, isolation]
timestamp: "2026-08-31T16:00:00Z"
---

# Vercel Labs `run`

## 它是什么

[`@vercel-labs/run`](https://github.com/vercel-labs/run) 是 Vercel Labs 出的 **JavaScript 安全沙箱执行包**。每次执行都在 **worker 线程里启动一个全新的 [QuickJS](https://bellard.org/quickjs/) 上下文**——里面**没有** Node.js 环境、文件系统、模块系统或网络访问能力。来宾代码只能调用宿主显式注入的函数。

兼容性：Node.js 22.13+ 和 [Bun](https://bun.sh/) 都能跑。

## 为什么用它 / 适合什么场景

- **让用户上传的 JS 代码在你服务里跑**：评论插件、低代码平台、AI 生成的脚本评估；
- **AI 工具执行不可信代码**：Agent / Code Interpreter 场景；
- **能力注入式 API**：你给宿主的能力 = 来宾的能力上限；
- **Worker 线程隔离**：主进程与沙箱在 OS 层面就分开。

## 关键能力

| 能力 | 说明 |
|------|------|
| QuickJS 沙箱 | 无 Node API / 无 fs / 无 net |
| Worker 线程隔离 | 主进程与沙箱 OS 层分开 |
| 能力注入 | 宿主显式传给来宾可调用的函数 |
| 双运行时 | Node.js 22.13+ / Bun |
| 来自 Vercel Labs | 与 Next.js / AI SDK 同生态 |

## 相关概念

- [OpenTag](tool-opentag.md) — 自托管 Slack AI 代理，关键操作前需审批

## 参考链接

- 项目链接：<https://github.com/vercel-labs/run>