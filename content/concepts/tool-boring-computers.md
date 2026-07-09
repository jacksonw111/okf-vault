---
type: Tool
title: "Boring Computers（按需 Firecracker 微 VM 给 AI agent 用）"
description: "用 Firecracker 微 VM 给 AI agent 提供「一整台 Linux 电脑」的执行环境：毫秒级启动 / 硬件级隔离 / 用完销毁，可控平面开源 + MCP + SDK。"
resource: "https://github.com/michaelshimeles/boring-computers"
tags: "[microvm, firecracker, sandbox, ai-agent, linux, isolation]"
timestamp: "2026-07-09T20:50:00Z"
---

# Boring Computers（按需 Firecracker 微 VM 给 AI agent 用）

## 它是什么
`boring-computers` 是一个开源项目，让 AI agent 像登录一台完整 Linux 电脑一样工作——**每次按需启动一个独立的 Firecracker microVM**：自带内核、硬件级隔离（不同于容器共享内核）、启动时间是毫秒级，agent 可以在里面操控桌面、写代码、跑服务，最后交付一个 live URL。用完可自动销毁，也可选择保持运行以继续后台任务。

控制平面用 Go 写，自带 **MCP server** 与 **SDK**，便于 AI agent 直接接入。整套机制可自托管。

## 为什么用它 / 适合什么场景
- 想给 AI agent 一个**真正隔离**的执行环境，跑不可信代码、装任意系统包、改任意配置而不污染宿主。
- 想让 agent 交付一个**可点开看的 live URL**——演示 / 分享 / 长跑任务都可以。
- 适合：自动化运维、CI sandbox、长跑 dev server、agent 自主 demo。
- 对比容器隔离方案（gVisor / Docker sandbox / runC），microVM 在内核层就隔离了。

## 关键能力
| 能力 | 说明 |
|------|------|
| 按需 Firecracker microVM | 毫秒级冷启动，每次任务独立实例 |
| 硬件级隔离 | 自带内核，不与宿主机共享内核 |
| 控制平面（Go） | 启动 / 销毁 / 状态查看 / 路由规划 |
| MCP server | AI agent 通过标准 MCP 协议申请 VM |
| SDK | 多语言客户端可集成到现有 agent 框架 |
| Live URL | 每个任务产出可访问 URL，便于分享 |
| 自托管 | 无需外部 SaaS，完全本地运行 |

## 相关概念
- [forkd](tool-forkd.md) — microVM fork 化沙箱，100 个 100ms（也是 microVM sandbox 思路）
- [dd（jit-container）](tool-dd-jit-container.md) — JIT 编译在 macOS 上跑 Linux 容器
- [Flounder](tool-flounder.md) — 编码 agent 包装为端到端白帽安全审计系统，每步沙箱隔离
- [Strix](tool-strix.md) — 自主 AI 渗透测试 agent，使用沙箱隔离运行测试

## 参考链接
- 项目链接：<https://github.com/michaelshimeles/boring-computers>
