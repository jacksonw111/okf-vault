---
type: Tool
title: "GamePhanes（GamePhanes/GamePhanes）"
description: "代码 Benchmark 只看测试过不过，游戏这类交互软件得真跑起来、接输入、改状态才算数——给游戏 Coding Agent 补上运行时验证"
resource: "https://github.com/GamePhanes/GamePhanes"
tags: "[game-dev, coding-agent, benchmark, runtime, verification, agent-eval]"
timestamp: "2026-08-22T10:12:00Z"
---

# GamePhanes

## 它是什么
[`GamePhanes/GamePhanes`](https://github.com/GamePhanes/GamePhanes) 是一套面向**游戏 Coding Agent**的运行时验证框架——传统代码 Benchmark 只看测试过不过，但游戏这种交互软件必须**真跑起来、接输入、改状态**才算数，GamePhanes 给游戏 Coding Agent 补上这段缺失的运行时验证环节。

## 为什么用它 / 适合什么场景
- 写了一个 Coding Agent 想让它生成可玩游戏，靠单元测试 / 编译通过根本判不出「能不能玩」。
- 想给游戏 AI 比赛 / 评测平台提供「自动跑游戏 + 评分」的基线。
- 想对比不同 Coding Agent 在「写游戏」这件事上的真实能力，而非纸上指标。

## 关键能力
| 能力 | 说明 |
|------|------|
| 运行时验证 | 真启动游戏进程、注入输入、观察状态变化 |
| 输入注入 | 模拟玩家操作（点击 / 键盘 / 手柄） |
| 状态观测 | 抓帧 / 读游戏日志 / 读内存状态做断言 |
| 评测打分 | 输出可比较的「能玩 / 不能玩 / 能玩到什么程度」指标 |
| 适配多 Agent | 同套验证框架可挂任何 Coding Agent 输出 |

## 媒体
- ![](https://pbs.twimg.com/media/HQT-c_jaYAAbwHx.jpg)

## 相关概念
- [EnterpriseClawBench](./tool-enterpriseclaw-bench.md) — 真实企业工作会话的编码 Agent 基准，思路同源但定位是企业编码
- [Strix](./tool-strix.md) — 自主 AI 渗透测试 agent，输出可直接复现的 PoC 而不是误报清单，验证思路相近
- [SkillSpec](./tool-skillspec.md) — 把 AI Agent 的 Skills 当成可遵守 / 可测试 / 可验证的契约
