---
type: Tool
title: "Sprix SAGE Router（A2A 多代理决策路由器）"
description: "Sprix AI 出品的开源研究原型：任务在 A2A 网络里执行到一半时，SAGE 在一条效用函数里比完「继续独干 / 叫帮手 / 整体换人」三条路，交出一份带角色分配、通信拓扑和可读理由的决策。"
resource: "https://github.com/wang2122/sprix-sage-router"
tags: [agent, multi-agent, a2a, decision, routing, open-source]
timestamp: 2026-08-21T13:27:00Z
---

# Sprix SAGE Router（A2A 多代理决策路由器）

## 它是什么
Sprix SAGE Router 是 Sprix AI（挂在屿智同行名下）的开源研究原型：解决 A2A（agent-to-agent）网络里「一个任务跑到一半，下一步该怎么决策」的问题——该继续由当前 agent 独自推进，还是临时叫一个帮手，还是直接把整组团队换掉。SAGE 把三条路放进一条效用函数里比完，输出一份**带角色分配 + 通信拓扑 + 可读理由**的决策，而不是简单二选一。

## 为什么用它 / 适合什么场景
- 多代理 / 多智能体协作流程里卡在「下一步该怎么派单」的中心调度位置。
- 想把决策过程从「黑盒启发式」变成「可读理由 + 可追溯决策」，方便事后复盘与调优。
- 学术 / 研究场景：探索 A2A 网络里效用驱动调度的工程原型。

## 关键能力
| 能力 | 说明 |
|------|------|
| 三路效用比较 | 独干 / 协作 / 换人三条路同台比较 |
| 角色分配 | 给出当前任务的具体角色配比 |
| 通信拓扑 | 明确谁与谁通讯 |
| 可读理由 | 每条决策附人类可读解释 |
| 单文件 Python | Python 3.10+，零第三方依赖 |
| MIT 许可 | 可自由用于商业与研究 |

## 一句话总结
**「下一步继续独干还是换团队？」——SAGE 用效用函数比完三条路，附可读理由给你看。**

## 原始链接
- [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) — 原始仓库

## 相关概念
- [Cotal](./concepts/tool-cotal.md) — 多智能体开放协议框架，拓扑可配（对等 / 经理制 / 指挥链 / 混搭）
- [pi-hive](./concepts/tool-pi-hive.md) — Pi 的层次化多智能体团队协作工具