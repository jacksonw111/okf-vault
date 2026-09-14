---
type: "Term"
title: "Sandbox（沙箱）"
description: "把代码 / agent 限制在一个与宿主隔离的运行环境里：文件系统、网络、进程派生都受控。agent / 不可信代码 / 第三方工具的标准安全做法。"
tags: "[sandbox, isolation, security, container, agent]"
timestamp: "2026-09-14T22:30:00Z"
---

# Sandbox（沙箱）

## 它是什么

**Sandbox（沙箱）** 是一种**隔离执行环境**：把代码 / agent / 不可信程序的运行范围限制在与宿主**文件系统 / 网络 / 进程**全部隔离的容器里。即便内部程序崩溃、被攻击、写出恶意行为，破坏面也只限于沙箱内部。

沙箱是现代 AI agent 体系里的**基础设施**：当 agent 能执行 shell / 写文件 / 装包 / 调网络时，必须把它关在沙箱里，否则它在生产里几乎一定会出事。

## 分类

| 形态 | 隔离强度 | 典型场景 |
|------|----------|----------|
| 进程级沙箱 | 低 | Python venv / Node sandbox |
| OS 级容器 | 中 | Docker / Podman / Apple Container |
| VM 级沙箱 | 高 | Firecracker / gVisor / Kata Containers |
| 微虚拟机 + 远程 | 极高 | Cloudflare Workers / Anthropic 沙箱 |
| WASM 沙箱 | 高（受限语言） | Fastly Compute / Wasmtime |
| 硬件级 | 最高 | Apple Private Cloud Compute / TEE |

## 关键能力

- **文件系统隔离**：读写路径白名单
- **网络隔离**：可访问域名 / 端口白名单
- **进程隔离**：派生进程 / fork 限制
- **资源配额**：CPU / 内存 / 磁盘 / 时间上限
- **重置 / 复现**：每次启动都从干净镜像起
- **审计**：所有写动作记录到日志

## Agent 沙箱现状

主流 AI agent（Claude Code / Codex / Pi / Cursor）都默认把 agent 跑在沙箱里。开发者视角下常见的沙箱配置：

- **Claude Code**：默认 Bash 走沙箱，可写白名单
- **Codex**：本地 sandbox shell，云端跑在容器
- **Pi Coding Agent** + **pi-env**：可叠加第三方沙箱
- **Devin / Cursor Background**：云端 VM 沙箱

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — 自托管常需要自己跑沙箱
- [Harness Engineering](./term-harness-engineering.md) — 沙箱是 harness 设计的核心组件
- [Cloud Coding Agent](./term-cloud-coding-agent.md) — 云端 agent 几乎都跑在沙箱里
- [mobai-dev](./tool-mobai-dev-ios-from-linux.md) — iOS 沙箱在 Linux 云的实现

## 参考链接

- Anthropic 沙箱介绍：<https://docs.anthropic.com/en/docs/agents-and-tools/computer-use>
