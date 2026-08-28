---
type: Tool
title: "remotifyd（Dify 团队开源的远程设备管理守护进程）"
description: "langgenius/remotifyd：Dify 团队专为 AI Agent 设计的远程设备管理守护进程，让 agent 能安全地操作远程设备。"
resource: "https://github.com/langgenius/remotifyd"
tags: [dify, agent, remote-device, daemon, device-management]
timestamp: "2026-08-27T11:29:00Z"
---

# remotifyd

## 它是什么
[langgenius/remotifyd](https://github.com/langgenius/remotifyd) 是 **Dify 团队开源的远程设备管理守护进程**——专为 **AI Agent** 设计，让 agent 能**安全地操作远程设备**。

定位类似"agent-side 的 SSH + 设备守护层"：agent 不会直接去连远端机器，而是通过 remotifyd 这个守护进程做权限控制、命令校验、设备识别。

## 为什么用它 / 适合什么场景
- 想让 Dify / 自建 agent 能操作远程机器，但又不放心直接把 SSH 凭证交给 agent；
- 想给"agent × 多台设备"场景做集中的权限 / 审计层；
- 关心 agent 远程操作的可控性与可追溯性。

## 关键能力
| 能力 | 说明 |
|------|------|
| 守护进程 | 在目标设备上常驻 |
| 远程控制 | agent 通过它操作设备 |
| 权限控制 | 命令 / 路径白名单 |
| 设备识别 | 标记 / 管理多台设备 |
| 出品方 | Dify 团队（langgenius） |
| 开源 | 仓库开源 |

## 相关概念
- [sim-use](tool-sim-use.md) — 移动端 GUI agent（CLI 形态）；remotifyd 是桌面 / 服务器侧的 agent 设备守护层
- [Strado](tool-strado.md) — 多 AI 编码代理工作台；remotifyd 是 agent × 远程设备的能力通道——一个管代码改动，一个管设备操控

## 参考链接
- 项目链接：<https://github.com/langgenius/remotifyd>
