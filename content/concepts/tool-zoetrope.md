---
type: Tool
title: "Zoetrope（furkankly/zoetrope）"
description: "把 Claude Code 会话实时画成一张流程图，在终端或浏览器里观看主 agent、子 agent 与工具调用的运行过程"
resource: "https://github.com/furkankly/zoetrope"
tags: [claude-code, visualization, observability, sub-agent, terminal-ui]
timestamp: "2026-08-22T09:11:00Z"
---

# Zoetrope

## 它是什么
[`furkankly/zoetrope`](https://github.com/furkankly/zoetrope) 把 Claude Code 的会话**实时**渲染成一张节点-边流程图：在终端或浏览器里同时看主 agent、子 agent 与每一次工具调用的运行顺序、父子关系与并发分支，让原本只能翻 transcript 文本的会话变成一张「一眼能看明白调用结构」的图。

## 为什么用它 / 适合什么场景
- 跑长任务时，主 / 子 agent 套娃越深越难定位「是哪一步走了歪路」，可视化能直接看出来。
- 想给团队 / 同事演示「Claude Code 是怎么一步步解决问题」时，一张流程图胜过千行日志。
- 想给 Agent Harness / Orchestration 类项目做调试或 QA，需要可视化工具调用轨迹。

## 关键能力
| 能力 | 说明 |
|------|------|
| 实时绘制 | 会话进行中持续更新节点与边，不是事后回放 |
| 多视角 | 主 agent / 子 agent / 工具调用 三类节点同图共存 |
| 双前端 | 既能在终端跑（TUI），也能起一个浏览器视图 |
| 父子关系 | 自动识别 sub-agent 的派生与汇合 |
| Claude Code 适配 | 监听 Claude Code 的事件流而非通用模型 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HQT-ZtEbQAAxDHB.mp4>

## 相关概念
- [kcap-cli](./tool-kcap-cli.md) — 同样给 AI 编码助手做可观测性 CLI，但走指标 / 仪表盘路线
- [AgentStalker](./tool-agent-stalker.md) — 把 LLM Agent 当系统审计（污点图 / 攻击链），思路比 Zoetrope 更「安全取证」
