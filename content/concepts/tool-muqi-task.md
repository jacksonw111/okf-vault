---
type: Tool
title: "Muqi Task (LinuxForYQH/muqi-task)"
description: "把 AI 的工作拆成 Task 主线，会话挂在任务底下，多任务并行时不用在聊天列表里翻谁对应谁"
resource: "https://github.com/LinuxForYQH/muqi-task"
tags: [task, chat, ai-agent, knowledge-work, organization]
timestamp: 2026-08-20T11:15:00Z
---

# Muqi Task (LinuxForYQH/muqi-task)

## 它是什么
[`LinuxForYQH/muqi-task`](https://github.com/LinuxForYQH/muqi-task) 是一种**任务优先**（Task-first）的 AI 协作组织方式：把"AI 该干的活"先抽象成**任务（Task）**作为主线，**会话（chat）挂在任务底下**。同时推进多个需求时，从任务维度进入就能顺着点回对应聊天，不再陷入"对话框越堆越乱、谁对谁"的混乱。

## 为什么用它 / 适合什么场景
- 同时跟 AI 跑 3 个以上并行需求，聊天列表已经分不清谁在改什么。
- 想让"需求状态"先于"对话记录"，按 Task 而非按时间浏览历史。
- 需要把 AI 协作的工作流与人类任务面板对齐（敏捷 / OKR / 看板都更容易嵌入）。

## 关键能力
| 能力 | 说明 |
|------|------|
| Task 主线 | 一个 Task = 一个需求主线 |
| 会话挂载 | 一个 Task 下可挂多个 chat / 多段对话 |
| 任务 → 会话导航 | 点 Task 直接进入对应会话，不用在列表里翻 |
| 并行可达 | 多 Task 同时推进不互相污染上下文 |

## 媒体
- ![Muqi Task 界面](https://pbs.twimg.com/media/HQD2UleagAAzgTW.jpg)

## 相关概念
- [项目仓库](https://github.com/LinuxForYQH/muqi-task) — 仓库主页
- [orca-ticket-orchestration](./playbook-orca-ticket-orchestration.md) — 关于把 ticket 作为 AI 协作主线的另一套思路
