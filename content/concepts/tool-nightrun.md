---
type: "Tool"
title: "NIGHTRUN"
description: "Rust 写的 UEFI 常驻 LLM 运行时：把量化模型直接读进内存、帧缓冲上画界面，底下不跑操作系统 / 内核 / 网络栈，x86_64 从 USB 启动、树莓派 5 从 SD 卡启动，开机即变成 LLM 聊天终端。"
resource: "https://github.com/hardrave/NIGHTRUN"
tags: ["rust", "uefi", "llm", "local-llm", "embedded", "raspberry-pi", "firmware", "bare-metal"]
timestamp: "2026-08-12T07:19:00Z"
---

# NIGHTRUN

[NIGHTRUN](https://github.com/hardrave/NIGHTRUN) 是一个 **Rust 写的 UEFI 常驻 LLM 运行时**：机器开机就变成 LLM 聊天终端，UEFI 固件把量化模型读进内存、帧缓冲上画 UI，底下**不跑操作系统、不跑内核、不跑网络栈**。

## 它是什么

一个 bare-metal LLM 启动器。x86_64 机器从 USB 启动、树莓派 5 从 SD 卡启动，一开机就直接进入 LLM 聊天界面。整台机器"只剩下 LLM"。

## 为什么用它 / 适合什么场景

- **极简启动介质**：一台机器 + 一个 U 盘 / SD 卡就能用 LLM。
- **无 OS 攻击面**：没有操作系统、没有内核、没有网络栈，攻击面极小。
- **裸金属性能**：直接驱动硬件，免去 OS 开销。
- **冷启动快**：开机即聊天，绕过 OS 启动链。
- **隐私优先**：数据完全留在本机，不存在任何系统服务层。

## 关键能力

| 能力 | 说明 |
|------|------|
| UEFI 启动 | x86_64 直接从 USB 引导 |
| 树莓派 5 | SD 卡启动，兼容性强 |
| 量化模型 | 把压缩后的 LLM 加载进内存 |
| 帧缓冲 UI | 自行绘制界面，不依赖 OS |
| 无 OS / 无内核 | bare-metal 运行 |
| 无网络栈 | 离线运行 |
| Rust 实现 | 安全 + 性能 + 适合底层开发 |

## 媒体

![](https://pbs.twimg.com/media/HPaEMxSa4AAT_u5.png)

## 参考链接

- [项目仓库](https://github.com/hardrave/NIGHTRUN)

## 相关概念

- [Ollama](./tool-ollama.md) — 本地 LLM 一键启动器，依赖 OS；NIGHTRUN 是其 bare-metal 极端版
- [PicoLM](./tool-picolm.md) — 极简 LLM 推理引擎，单文件 ~80KB，同样面向极简本地推理