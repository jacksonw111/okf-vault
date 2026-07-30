---
type: Tool
title: "Local-Hermes-Portable（llama.cpp + Hermes Agent 便携包）"
description: "把 llama.cpp 和 Nous Research Hermes Agent 打包成跨平台（Windows/macOS/Linux）便携包，本地跑大模型和 agent 不需要手动装 Python、CUDA、下载模型，双击脚本就能跑。"
resource: "https://github.com/techjarves/Local-Hermes-Portable"
tags: [llama.cpp, hermes, local-llm, agent, portable, offline]
timestamp: "2026-07-30T09:45:00.000Z"
---

# Local-Hermes-Portable

## 它是什么

**llama.cpp + Hermes Agent 的「双击即跑」便携包**——本地跑大模型最大的门槛是装环境：

- Python 版本
- CUDA / Metal / Vulkan 驱动
- 模型权重下载 / 校验
- Hermes Agent 与 llama.cpp 的版本对齐

Local-Hermes-Portable 把这些全部打包好：

- 跨平台（Windows / macOS / Linux）
- 便携（不污染系统，U 盘也能跑）
- 离线（模型随包 / 一次下载）
- 双击即跑（脚本入口）

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | Win / macOS / Linux |
| 便携 | 不写注册表 / dotfiles |
| 自动配置 | Python / CUDA / 驱动不操心 |
| 内置 Hermes Agent | Nous Research 出品 |
| llama.cpp 内置 | 量化推理引擎 |
| 双击启动 | 一键跑 |

## 适合谁

- 想本地跑 LLM Agent 但被环境配置劝退的人
- 想在 U 盘 / 内网环境离线跑 AI 的用户
- 做本地 AI 演示 / 教学 / 比赛的极简部署
- 不想折腾 Python 虚拟环境的人

## 原始链接

- [项目仓库](https://github.com/techjarves/Local-Hermes-Portable)
- [推文剪藏](https://x.com/QingQ77/status/2082764386217959624)

## 相关概念

- [Local LLM Hardware Guide](./note-local-llm-hardware-guide.md) — 本地 LLM 硬件选购与配置
- [hermes-desktop](./tool-hermes-desktop.md) — Hermes Agent 的原生桌面 GUI 客户端
- [Nyx Local AI](./tool-nyx-local-ai.md) — VS Code / Cursor 本地 AI 编码插件