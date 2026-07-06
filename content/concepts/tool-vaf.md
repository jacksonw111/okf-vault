---
type: "Tool"
title: "VAF（自主智能体框架，三种运行模式）"
description: "Python 写的自主智能体框架，本地或云端 LLM 都支持，桌面/服务端/终端三种跑法；内置 100+ 工具与编程/搜索/研究三个子智能体，pgvector + Redis 持久化记忆，Git 快照回退代码改动。"
tags: "[agent, framework, python, gguf, openai, anthropic, pgvector, redis]"
timestamp: "2026-07-06T04:33:00.000Z"
resource: "https://github.com/Veyllo-Labs/VAF"
---

# VAF（自主智能体框架，三种运行模式）

## 它是什么

[`VAF`](https://github.com/Veyllo-Labs/VAF)（Veyllo Agent Framework）是 Python 写的**自主智能体框架**，主张「一个框架，三种跑法」。本地 GGUF 模型与 OpenAI / Anthropic 等云 API 一视同仁，都可作为后端。

## 三种运行模式

| 模式 | 形态 |
|------|------|
| 桌面模式 | 系统托盘常驻 + 浏览器网页界面 |
| 服务端模式 | systemd 开机自启，跑在服务器 / NAS 上，可配 HTTPS |
| 终端模式 | TUI 聊天界面或单次 prompt 命令 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多种 LLM 后端 | 本地 GGUF（llama.cpp 系）/ OpenAI / Anthropic |
| 内置 100+ 工具 | 编程 / 搜索 / 研究三大子智能体共享工具池 |
| 持久化记忆 | pgvector（向量检索）+ Redis（KV / 会话状态） |
| 代码回退 | 每次代码改动生成 Git 快照，可一键回滚 |
| 三入口 | 桌面托盘 / systemd / TUI |

![VAF 架构示意](https://pbs.twimg.com/media/HMdgKh6aoAAu8Wb.jpg)

## 适用场景

- 想在 NAS / 服务器上 7×24 跑一个本地智能体
- 需要本地 GGUF 模型跑数据敏感的自动化任务
- 想在桌面、服务器、终端三种形态间切换同一份配置

## 参考链接

- [项目链接](https://github.com/Veyllo-Labs/VAF)

## 相关概念

- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架
- [agent-sphere](tool-agent-sphere.md) — Spring Boot 3.4 AI Agent 编排平台
- [Evano Studio](tool-evano-studio.md) — 本地优先桌面多 Agent 团队 + Ollama