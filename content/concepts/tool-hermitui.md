---
type: Tool
title: "HermitUI"
description: "把隐私放在第一位的本地 AI 聊天界面：整个应用就一个 HTML 文件，接任意 OpenAI 兼容的本地或云端接口，默认一点聊天记录都不存。"
tags: "[privacy, local-ai, chat-ui, single-html, openai-compatible, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/moooff/HermitUI"
---

# HermitUI

把**隐私放在第一位**的**本地 AI 聊天界面**——整个应用**就一个 HTML 文件**，接任意 **OpenAI 兼容的本地或云端接口**，**默认一点聊天记录都不存**。

## 它是什么

- 一个**单文件 HTML** 的 AI 聊天 UI，浏览器双击即可打开使用；
- 后端接口**完全 OpenAI 兼容**——可以接本地 Ollama / LM Studio / vLLM，也可以接云端 OpenAI / DeepSeek / 任意网关；
- **默认零持久化**：刷新即清空，不写本地、不上云、不埋点；
- 隐私敏感场景下的"**零足迹聊天**"工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单 HTML 文件 | 无构建、无依赖，双击就能用；可本地保存一份随身携带 |
| OpenAI 兼容 | 兼容任意 `/v1/chat/completions` 接口 |
| 本地 / 云端随意切 | 自填 Base URL 即可接 Ollama / LM Studio / DeepSeek / OpenAI 等 |
| 默认不存记录 | 刷新即清空，无 localStorage / IndexedDB 持久化 |
| 隐私优先 | 无埋点、无遥测、无第三方脚本 |

## 为什么用它 / 适合什么场景

- 在**公用电脑 / 借来的设备 / 网吧**上临时和 AI 聊几句，不想留痕；
- **临时问题**（代码报错、随手翻译、敏感对话）不想污染自己常用的 ChatGPT 历史；
- 想**自己控制聊天留存策略**——默认不存，需要时自己手动复制；
- 教学 / 演示场景：让学生 / 同事**直接打开 HTML 就能体验**，免装客户端；
- 想给不熟悉技术的人一个**"零安装 AI 客户端"**，又不想暴露给他 ChatGPT 账号。

## 设计哲学

1. **文件即应用**——单个 HTML，无安装；
2. **接口即配置**——接谁、存不存，都由你填的 URL 决定；
3. **默认不存 = 默认安全**——把"不留痕"做成开箱即用，而不是要靠配置去达成；
4. **不留即隐私**——只要不存，就没有泄漏的可能。

## 预览

![](https://pbs.twimg.com/media/HNAtqqtbkAAiMlk.jpg)

## 相关概念

- [ackem](tool-ackem.md) — 同样是"本地优先 + 可换端点"的桌面 AI 伙伴
- [OpenMac](tool-openmac.md) — 把 macOS 系统能力以 HTTP API 暴露，与本工具"接口即配置"思路类似