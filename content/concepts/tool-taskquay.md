---
type: Tool
title: "TaskQuay"
description: "DevSpace 二开而来的自托管工具：给 ChatGPT 网页对话开一条直达本地工作区的通道，主控 agent 自己看文件、搜代码、写操作一次只放一个过、读操作放两个，并按资源排队等。"
resource: "https://github.com/wrfgup/taskquay"
tags: [agent, chatgpt, local-workspace, devspace, coding-agent]
timestamp: "2026-09-08T00:00:00Z"
---

# TaskQuay

## 它是什么
从 [DevSpace](https://github.com/) 二开的**自托管工具**：跑在自己电脑上，给 ChatGPT 网页对话开一条直达本地工作区的通道——主控 agent 自行先看文件、搜代码，确认确实要改才调用 Codex 写代码，**写操作一次只放一个过、读操作一次放两个**，编译和设备调用则按资源排队等，避免 agent 把本地环境搞炸。

## 为什么用它 / 适合什么场景
- 想让 ChatGPT 直接帮自己改本地项目代码，但又不希望它失控乱动文件。
- 想在多个 agent（主控 + Codex + 编译/调试）之间对资源访问做串行/排队约束。
- 不信任云端 IDE 代理的写权限，希望所有写操作都过自己电脑的一道闸。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地中继 | ChatGPT 网页对话 ↔ 本地工作区，零数据出域 |
| 主控先看再写 | agent 自检文件/搜索后才决定是否调 Codex |
| 写串行/读并发 | 写一次一个、读一次两个，规避 race |
| 资源排队 | 编译、设备调用按机器资源排队 |
| 自托管 | 二开自 DevSpace，可控可改 |

## 参考
- 原始链接：<https://github.com/wrfgup/taskquay>

## 媒体
- ![](https://pbs.twimg.com/media/HRqILNeaUAIhoYN.jpg)

## 相关概念
- [DevSpace](https://github.com/) — 上游项目
- [Codex](https://openai.com/index/codex/) — 写代码的下游 agent
