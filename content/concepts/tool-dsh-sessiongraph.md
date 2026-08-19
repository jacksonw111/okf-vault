---
type: Tool
title: "DSH-SessionGraph（lwklbb/DSH-SessionGraph）"
description: "把充满调试 / 报错 / 反复修改的长聊天会话压缩成可编辑、可复制的结构化导图与大纲，DeepSeek Harness 的会话可视化插件"
resource: "https://github.com/lwklbb/DSH-SessionGraph"
tags: "[deepseek-harness, dsh, session-graph, visualization, summary]"
timestamp: "2026-08-19T16:00:00Z"
---

# DSH-SessionGraph（lwklbb/DSH-SessionGraph）

## 它是什么
[`lwklbb/DSH-SessionGraph`](https://github.com/lwklbb/DSH-SessionGraph) 是 DeepSeek Harness 的插件：把一次长达几千轮的「调试 → 报错 → 修复 → 再调试」聊天会话，压缩成一份**结构化导图 / 大纲**，可编辑、可复制，让与会话无关的人也能 30 秒看懂脉络。

## 为什么用它 / 适合什么场景
- 团队有人用 dsh 跑长任务，会话长度爆炸，第二天接手的人看不懂上下文。
- 写技术文章 / 案例分享，需要把一场调试会话提炼成图。
- 想把会话归档作为可检索的知识资产，而不是单纯的滚动文本。

## 关键能力
| 能力 | 说明 |
|------|------|
| 长会话压缩 | 把几千轮滚动文本压成结构化导图 |
| 节点可编辑 | 生成的导图 / 大纲可手工微调 |
| 可复制 | 节点内容支持复制粘贴进 Markdown / Notion / 文档 |
| DSH 原生 | 作为 dsh 插件挂载，不另起一个应用 |

## 媒体
- ![DSH-SessionGraph 截图](https://pbs.twimg.com/media/HP-pse5b0AAANxk.jpg)

## 相关概念
- [项目仓库](https://github.com/lwklbb/DSH-SessionGraph) — 仓库主页
- [codex-trajectory](./tool-codex-trajectory.md) — 同样做「长会话结构化」，但只读不改原日志
- [dsh-visualize](./tool-dsh-visualize.md) — dsh 把单次模型输出渲染为可视化卡片（粒度不同）