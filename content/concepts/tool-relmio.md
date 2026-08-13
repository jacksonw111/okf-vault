---
type: Tool
title: "relmio"
description: "OpenAI 兼容 API 边车——在自托管 n8n 旁侧运行，复用用户自己的 ChatGPT / Codex 登录态访问模型，n8n 端只需填占位 key + 本地 URL，免另购 OpenAI Platform API 额度。"
resource: "https://github.com/Demonbane18/relmio"
tags: "[openai, n8n, sidecar, api-compat, self-hosted, open-source]"
timestamp: "2026-08-13T19:53:00Z"
---

# relmio

## 它是什么
一个**OpenAI 兼容 API 边车**（sidecar），专门为**自托管 n8n** 用户设计：

- 部署在自托管 n8n **旁边**
- **复用**用户自己的 **ChatGPT / Codex 登录态**（订阅账户）访问模型
- 对外暴露 **OpenAI 兼容 API**（n8n 的 OpenAI 节点可直接对接）
- n8n 配置里只需要填**占位 key + 本地 URL**——不需要另买 OpenAI Platform 的 API 额度

本质上是把「**已有 ChatGPT 订阅**」转成「**可被任意 OpenAI 兼容客户端调用的本地端点**」。

## 为什么用它 / 适合什么场景
- 自托管 n8n 用户，希望 n8n 能调用 LLM，但不想为 OpenAI Platform API 单买额度。
- 已有 ChatGPT Plus / Pro 订阅，想让订阅「溢出」到自动化工作流。
- 想把 n8n 的 OpenAI 节点无侵入地接进来（兼容 API）。
- 数据 / 凭据**本地化**（订阅登录态在本地边车里跑）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | 边车进程（sidecar） |
| 配套 | 自托管 n8n |
| 认证复用 | 用户自己的 ChatGPT / Codex 登录态 |
| 协议 | OpenAI 兼容 API |
| n8n 端 | 填占位 key + 本地 URL 即可 |
| 节省 | OpenAI Platform API 额度 |

## 相关概念
- （暂无强相关概念——独立的 n8n 配套工具）

## 媒体
- 工具截图：<https://pbs.twimg.com/media/HPkVeSFaIAAMR7y.jpg>

## 项目链接
- 项目主页：<https://github.com/Demonbane18/relmio>