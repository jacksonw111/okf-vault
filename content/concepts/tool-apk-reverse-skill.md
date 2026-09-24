---
type: "Tool"
title: "apk-reverse（安卓逆向 Skill）"
description: "把安卓逆向「解包 / 反编译 / 改 smali / 重签重打包 / Frida Hook / so & native 分析」的全流程沉淀为可交给 Claude Code、Codex 等 AI Agent 编排的 Skill，让 Agent 直接具备一套安卓逆向工作流。"
resource: "https://github.com/newliver666/apk-reverse"
tags: "[android, reverse-engineering, frida, smali, skill, agent, ai, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# apk-reverse（安卓逆向 Skill）

## 它是什么

[apk-reverse](https://github.com/newliver666/apk-reverse) 是基于实际逆向项目经验构建的 AI Agent Skill，把安卓逆向常用工具链（解包、反编译、改 smali、重签重打包、Frida Hook、so/native 分析）打包成 Claude Code / Codex 等 agent 可直接调用的工作流。

## 它覆盖的链路

| 阶段 | 内容 |
|------|------|
| 解包 | apk 反汇编 / 资源提取 |
| 反编译 | Java / Kotlin 层代码还原 |
| 改 smali | 在 smali 层面修改逻辑 |
| 重签重打包 | 签名校验 / 重打包 |
| Frida Hook | 运行时 hook Java 与 native 层 |
| so / native 分析 | native 库的逆向与调试 |

## 适用场景

- 用 Claude Code / Codex 做安卓逆向分析时，不想每次临时拼工具链
- 想给团队 / Agent 沉淀一套「开箱即用」的安卓逆向 SOP

## 原始链接
- 项目主页：<https://github.com/newliver666/apk-reverse>

## 相关概念