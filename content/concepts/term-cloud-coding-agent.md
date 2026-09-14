---
type: "Term"
title: "Cloud Coding Agent（云端编码代理）"
description: "跑在云端 / 远程沙箱里的 AI 编码 agent：本地不占资源、统一环境、可并行多个任务、支持任意语言栈与平台（含 iOS / Android 等传统本地受限场景）。"
tags: "[cloud-agent, coding-agent, sandbox, ci, remote-dev]"
timestamp: "2026-09-14T22:30:00Z"
---

# Cloud Coding Agent（云端编码代理）

## 它是什么

**Cloud Coding Agent** 是一种部署形态：AI 编码 agent 跑在**云端 / 远程沙箱**里，本地只是一个客户端（终端 / IDE / 浏览器）。区别于传统本地 CLI / IDE 插件形式的 coding agent，云端 agent 把「代码编辑 + LLM 调用 + 工具执行 + 环境依赖」整体放到云上。

## 为什么选云端

| 收益 | 说明 |
|------|------|
| 环境统一 | 团队所有 agent 跑同一份容器，行为可复现 |
| 资源充足 | 大仓库 / 长任务不会卡本地笔记本 |
| 多任务并行 | 一个项目起 N 个 agent 同时干不同分支 |
| 平台无门槛 | Linux 沙箱里跑 iOS / Android / 嵌入式等本地受限工程 |
| 永不关机 | 长期任务（CI / 训练）持续跑 |
| 本地零负担 | 浏览器 / 平板都能用 |

## 典型形态

| 形态 | 例子 |
|------|------|
| 浏览器 IDE + 云端执行 | StackBlitz / GitHub Codespaces / Replit |
| CLI 本地 + 云端算力 | Claude Code + 远程容器 / Aider Cloud |
| 全云 agent 平台 | Devin / Codex Cloud / Cursor Background |
| 垂直沙箱 | mobai-dev（iOS） / Claude Code 沙箱 |

## 关键挑战

- **延迟**：每步操作都要跨网络
- **成本**：云算力 / 数据传出 / 存储都按量计费
- **代码安全**：把公司代码交给云端 sandbox 需要合规
- **断网兜底**：本地要能离线继续读代码、写注释

## 相关概念

- [Sandbox / 沙箱](./term-sandbox.md) — 云端 agent 的执行环境
- [mobai-dev（云端 coding agent 跑 iOS 开发）](./tool-mobai-dev-ios-from-linux.md) — Cloud coding agent 在 iOS 域的扩展
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 本地 agent 也能扩展到云端
