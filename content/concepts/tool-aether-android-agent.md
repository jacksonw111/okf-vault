---
type: Tool
title: "Aether（Android 本地 AI Agent）"
description: "Android 上的本地通用 AI Agent：界面不输 ChatGPT，内置 Alpine VM 跑 Shell 命令，支持 Shizuku / Termux 控制手机本体。"
resource: "https://github.com/Zhou-Shilin/Aether"
tags: [android, ai-agent, local-first, alpine-vm, shizuku, termux]
timestamp: "2026-07-21T11:51:00Z"
---

# Aether（Android 本地 AI Agent）

## 它是什么
[Aether](https://github.com/Zhou-Shilin/Aether) 是一款 **Android 本地通用 AI Agent**：手机上想用 Agent 又怕云端隐私、功能弱的不够用、界面看得过去的又少。Aether 直接在 Android 端提供类 ChatGPT 体验，并 **内置 Alpine VM 跑 Shell 命令**，配合 Shizuku / Termux 进一步控制手机本体。

## 为什么用它 / 适合什么场景
- 在 Android 上想要一个能跑命令 / 调本地能力的 AI Agent，而不是只能聊天的客户端。
- 担心数据上传云端，希望 Agent 的推理 / 工具调用都在本机完成。
- 想把 Shizuku / Termux 这套 Android 「root 之外的高级控制」接进 Agent 自动化。

## 关键能力
| 能力 | 说明 |
|------|------|
| Android 原生界面 | 体验贴近主流聊天式 AI |
| Alpine VM | 内置 Alpine Linux 虚拟机，可跑 Shell |
| Shizuku / Termux 联动 | 借用系统级权限控制手机硬件 / 应用 |
| 本地优先 | Agent 能力尽量在端侧完成 |
| 通用 Agent | 适配多种本地 / 远端模型 |

## 相关概念
- [HermitUI](tool-hermitui.md) — 把隐私放在第一位的本地 AI 聊天界面（同类「本地优先」范式）
- [Nyx Local AI](tool-nyx-local-ai.md) — VS Code / Cursor 本地 AI 编码插件（桌面端对照）

## 参考链接
- 项目链接: <https://github.com/Zhou-Shilin/Aether>
- 预览截图: ![Aether 截图](https://pbs.twimg.com/media/HNmTvOmbsAAAFcB.jpg)
