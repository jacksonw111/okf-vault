---
type: "Tool"
title: "SoL-Pi（NVIDIA 给 Pi 编码代理的省 token 开源扩展）"
description: "NVIDIA Labs 开源、给 Pi 编码代理用的省 token 扩展：四个默认全关、按需开关的能力——验证命令联动、句柄化大文本、日志摘要 + 原文回查、计划压缩。"
resource: "https://github.com/NVlabs/SoL-Pi"
tags: "[pi, nvidia, token-saving, agent-extension, coding-agent]"
timestamp: "2026-09-13T10:25:00Z"
---

# SoL-Pi（NVIDIA 给 Pi 编码代理的省 token 开源扩展）

## 它是什么

[NVlabs/SoL-Pi](https://github.com/NVlabs/SoL-Pi) 是 **NVIDIA Labs** 出品的 **Pi 编码代理扩展**。它不改 Pi 本体，而是在 Pi 之外加四个**默认全关、按配置文件启用**的省 token 招数。每一招都把上下文里最贵的部分抽走，但保留可回查的接口。

## 四招省 token 设计

| 招数 | 解决什么 | 关键思路 |
|------|----------|----------|
| 验证命令联动 | 编辑完再来回跑测试浪费 token | 编辑完自动跑验证命令，少一轮往返 |
| 大文本句柄化 | 读过的大段结果反复重传 | 看过的大文本结果存成句柄，下次按页取 |
| 日志摘要 + 原文可查 | 长日志占满上下文 | 压成摘要，但原文保留随时可查 |
| 计划步骤压缩 | 计划越写越长 | 完成后及时把计划步骤压成上下文摘要 |

四招**默认全关**，想用哪个自己改配置文件开。**不动 Pi 本体**——属于旁挂式扩展。

## 新手建议

> 前两个（验证联动 + 句柄化大文本）是**纯本地**的，不花额外模型钱，新手建议先开这两招；后两个涉及摘要会触发额外模型调用，再视需要打开。

## 关键能力

| 能力 | 说明 |
|------|------|
| 编辑 → 验证联动 | 一次会话内少跑一趟 |
| 大文本句柄 | 按页访问避免整段重传 |
| 日志摘要 | 长日志压成可读摘要 |
| 原文可查 | 摘要背后保留原文，按需回查 |
| 计划压缩 | 完成后清理历史步骤 |
| 配置即开关 | 默认全关，按需开 |
| 不改 Pi 本体 | 旁挂式扩展 |

## 项目链接

- 仓库：<https://github.com/NVlabs/SoL-Pi>

## 相关概念

- [Pi Coding Agent](./tool-pi-coding-agent.md) — SoL-Pi 的宿主
- [DeepSeek Harness 生态（dsh-*）](./tool-deepseek-harness-rs.md) — 同类「在编码代理之外省 token / 省步骤」的扩展思路
- [上下文工程](./term-context-engineering.md) — 四招的本质都是压缩 / 句柄化的上下文工程技法