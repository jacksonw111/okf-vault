---
type: Tool
title: "mac-computer-use（Mac 桌面给大模型当操作员）"
description: "让大模型自己盯着 Mac 屏幕干活：列窗口、读控件、往里打字、点按钮、截屏对账，把没有开放 API 的桌面环节也塞进自动化流程。"
resource: "https://github.com/To3akaRin/mac-computer-use"
tags: [mac, computer-use, agent, automation, screen, desktop, llm]
timestamp: 2026-09-18T13:47:00Z"
---

# mac-computer-use（Mac 桌面给大模型当操作员）

## 它是什么

[To3akaRin/mac-computer-use](https://github.com/To3akaRin/mac-computer-use) 是一套把 **Mac 桌面**变成 **大模型可操作对象**的工具集。它暴露一组基础能力——列窗口、读控件、往里打字、点按钮、截屏对账——让 LLM 能在 macOS 上像人一样盯屏幕干活。

核心价值：**那些没有开放 API 的桌面应用 / 内嵌控件 / 系统设置面板，也能被纳入自动化。**

## 关键能力

| 能力 | 说明 |
|------|------|
| 窗口枚举 | 列出当前所有可见窗口及其层级 |
| 控件读取 | 读出按钮 / 输入框 / 文本的语义信息 |
| 键鼠操作 | 模拟输入文字、点击按钮 |
| 截屏对账 | 操作后截图与预期比对，决定下一步 |
| 无 API 兜底 | 把没有暴露 API 的桌面环节也拉进 agent 流程 |
| 自托管 | 项目本地运行，不依赖云服务 |

## 适合什么场景

- 想自动化一个 macOS 上的桌面应用，但该应用没有 API / SDK 的开发者。
- 想把 LLM agent 推到「看得见屏幕、动得了鼠标」层的 Mac 玩家 / 极客。
- 给不支持脚本的系统设置面板做 AI 辅助操作的人。

## 与相关概念的关系

- [Computer Use（计算机使用）](./term-computer-use.md) — mac-computer-use 是 Computer Use 在 macOS 平台的一个具体实现。
- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 一个面向浏览器、一个面向 macOS 桌面，是同一思路在不同平台的实现。

## 参考

- 项目链接：<https://github.com/To3akaRin/mac-computer-use>

![操作界面截图](https://pbs.twimg.com/media/HSdpSmzbwAAqZ87.jpg)
