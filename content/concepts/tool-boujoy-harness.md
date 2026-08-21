---
type: Tool
title: "Boujoy Harness（DeepSeek Harness 产品化包装）"
description: "面向把 DeepSeek Harness 当引擎、但缺工作区和桌面体验的用法：把任务、对话、知识库、运行信号包进产品界面，让 Agent 能读写本地 Markdown Vault，把长对话跑稳。"
resource: "https://github.com/asen-goat-mine/boujoy-harness"
tags: [agent, deepseek-harness, dsh, workspace, knowledge-base, markdown]
timestamp: 2026-08-21T04:16:00Z
---

# Boujoy Harness（DeepSeek Harness 产品化包装）

## 它是什么
Boujoy Harness 是一个把「DeepSeek Harness 当底层引擎」重新包裹一层产品界面与工作区逻辑的桌面应用。它把原本只暴露命令行 / 裸 HTTP 的 dsh 体验，补上任务面板、对话面板、知识库面板、运行信号可视化，让 Agent 在跑长对话时能稳定读写本地 Markdown Vault。

## 为什么用它 / 适合什么场景
- 想用 dsh 但觉得「裸命令行太原始、自己搭 GUI 太麻烦」的团队 / 个人。
- 长对话需要稳定的「任务上下文 + 文档上下文」双向锚点，避免几十轮后模型丢失最初目标。
- 想把本地 Markdown Vault 当知识源，让 agent 在做工程任务时主动读写而不只是检索。

## 关键能力
| 能力 | 说明 |
|------|------|
| 产品化工作台 | 任务 / 对话 / 知识库 / 运行信号四个面板并列 |
| dsh 后端 | 引擎沿用 DeepSeek Harness，模型与插件生态与上游一致 |
| 本地 Markdown Vault | Agent 可读写，与笔记库双向锚定 |
| 长会话稳定 | 把上下文按「任务 / 文档 / 对话」切片，避免线性膨胀后丢目标 |
| 桌面级体验 | 不用每次都打开 Web UI，直接在本机应用里跑 |

## 一句话总结
**给 dsh 套一层产品工作台外壳：任务 + 知识库 + 对话分得开，长对话跑得稳。**

## 原始链接
- [asen-goat-mine/boujoy-harness](https://github.com/asen-goat-mine/boujoy-harness) — 原始仓库

## 相关概念
- [DeepSeek Harness 桌面壳](./concepts/tool-deepseek-harness-desktop.md) — dsh Web UI 的桌面外壳同类项目
- [DeepSeek Harness](./concepts/note-deepseek-harness-handbook.md) — 中文手册