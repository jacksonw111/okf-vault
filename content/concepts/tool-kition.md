---
type: Tool
title: "Kition（KitionAI/kition）"
description: "桌面工作区：写文档 / 管表格 / 跑智能体 / 浏览器查资料 / 搭工作流五合一；智能体直接改工作区里的真实文件，改动逐条可见、逐条可驳回"
resource: "https://github.com/KitionAI/kition"
tags: "[desktop-app, workspace, agent, electron, react, workflow]"
timestamp: "2026-08-22T01:29:00Z"
---

# Kition

## 它是什么
[`KitionAI/kition`](https://github.com/KitionAI/kition) 是一个 Electron + React + TypeScript 写的桌面工作区应用，把「写文档 / 管表格 / 跑智能体 / 浏览器查资料 / 搭工作流」**统一塞进同一个工作区**。智能体直接修改工作区里的真实文件，每次改动逐条可见、逐条可驳回，仓库里开源的只有客户端部分。

## 为什么用它 / 适合什么场景
- 想要一个本地优先的「一站式生产力桌面」，不必在 Word + Excel + ChatGPT + Notion + Zapier 之间来回切。
- 想让 Agent 真的动手改文件，但又怕它乱动——Kition 给每条改动单独的「接受 / 驳回」按钮。
- 想要「搭工作流」的低代码能力，但不想上 n8n 这种又重又要云的方案。

## 关键能力
| 能力 | 说明 |
|------|------|
| 五合一 | 文档 / 表格 / 智能体 / 浏览器 / 工作流统一入口 |
| 真实文件 | Agent 操作磁盘上的真实文档，不是聊天气泡 |
| 逐条审批 | 每次 Agent 改动独立可接受 / 可驳回 |
| 工作流搭建 | 内置低代码工作流编辑器 |
| Electron 桌面 | 本地运行，不依赖云服务 |

## 媒体
- ![](https://pbs.twimg.com/media/HQNmRkAboAAcN9Q.jpg)

## 相关概念
- [Notion AI / 国产同类](./tool-open-knowledge.md) — WYSIWYG Markdown 编辑器 + LLM 知识库，云优先路线相反
- [Worf](./tool-worf.md) — MIT 本地优先桌面应用，看板 / 笔记 / OKR / AI 聊天 / Sprint / 终端六合一，AI 可接 OpenAI 兼容端点
- [Lemma](./tool-lemma-platform.md) — 开源人 + AI agent 共享工作空间，统一表格 / 文件 / 工作流 / 权限 / 审批
