---
type: "Tool"
title: "juggler（juggler-ai/juggler）"
description: "为想亲手掌控 LLM 对代码库做了什么的人, 提供一个可视化工作台式的 AI 编码 agent——可检视每次工具调用、用分支线程来回溯、直接编辑上下文。"
resource: "https://github.com/juggler-ai/juggler"
tags: "[coding-agent, visual-workspace, dev-tools, agent-ui]"
timestamp: "2026-07-17T15:33:00Z"
---

# juggler

[juggler](https://github.com/juggler-ai/juggler) 是一个**可视化工作台式的 AI 编码 agent**, 主打「**人对 LLM 在代码库上的每一步有完整掌控感**」。它的核心三件事:

1. **检视每次工具调用** — 工具名 / 输入 / 输出 / 读 / 写的文件全部可见
2. **分支线程回溯** — 任何一步可以展开「如果当时我给了不同上下文会怎样」的分支
3. **直接编辑上下文** — 不止看, 可在 UI 里直接改提示词 / 上下文片段再继续

## 它和「ChatGPT / Claude.ai」的差别

普通 AI 聊天界面把上下文当作**只读黑盒**:
- 看不到每一步细节
- 改不动上下文
- 无法快速对比分支走向

juggler 把这三件事显化为 UI:

| 维度 | 普通聊天 AI | juggler |
|------|------|------|
| 工具调用透明 | 仅结果 | 每步可见 |
| 上下文编辑 | 仅复制 | 直接改 |
| 分支回溯 | 不支持 | 一键开分支线程 |
| 适合场景 | 闲聊 / 单问单答 | **严肃的代码库工作** |

## 关键能力

| 能力 | 说明 |
|------|------|
| 每步工具调用可见 | 文件读写 / 命令执行 / 网络请求均可审计 |
| 分支线程 | 在任意节点开分支, 对比不同上下文的效果 |
| 上下文直接编辑 | UI 中编辑 prompt / 上下文片段 |
| 编码 agent 形态 | 与 Claude Code / Codex CLI 同样面向代码库 |

## 媒体

![](https://pbs.twimg.com/media/HNUJfm7awAARP9o.jpg)

## 参考链接

- [项目仓库](https://github.com/juggler-ai/juggler)

## 相关概念

- [Codex-X](./tool-codex-x.md) — Tauri 2 跨平台 Codex 桌面端管理器 (含 provider 切换 + 提示词注入), juggler 偏「对 agent 操作的视觉控制」
- [Aura-IDE](./tool-aura-ide.md) — 双智能体工作台 + 写文件前先 diff 让用户逐条审批, juggler 类似: 都是「让 agent 在用户眼皮底下干活」
- [herdr-reviewr](./tool-herdr-reviewr.md) — 终端 AI agent 的代码审查侧栏, juggler 是「在 GUI 里直接编辑上下文」的更激进版本
