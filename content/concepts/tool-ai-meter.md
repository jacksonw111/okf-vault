---
type: "Tool"
title: "ai-meter"
description: "macOS 菜单栏应用, 通过 ccusage 读取本地用量数据, 在菜单栏里实时显示各编码 agent 的剩余预算、用量周期和重置日期。"
resource: "https://github.com/lizill/ai-meter"
tags: "[macos, menubar, billing-monitor, agent-tools, usage-tracker]"
timestamp: "2026-07-17T03:04:00Z"
---

# ai-meter

[ai-meter](https://github.com/lizill/ai-meter) 是一个 macOS 菜单栏小程序, 通过 **ccusage** 读取本地编码 Agent (Claude / Codex / Cursor / Kimi 等) 的用量数据, 把**剩余预算 / 当前用量周期 / 下次重置日期**三类信息常驻右上角菜单栏里。

## 它解决了什么

订阅多个编码 Agent 后, 用户普遍有三个疑问:

1. 这个月还剩多少钱没烧
2. 现在是哪个计费周期
3. 哪天重置额度

每家平台都得登录 Web 控制台看; **ai-meter 直接把这数据接进系统菜单栏**, 一眼可读, 点一下展开看历史曲线。

## 关键能力

| 能力 | 说明 |
|------|------|
| 菜单栏常驻 | 顶栏数字一瞥即可知剩余额度 |
| ccusage 后端 | 复用本地 ccusage 数据, 不直连各服务商 |
| 多 Agent 切换 | 下拉切换目标 Agent, 显示对应预算 |
| 用量周期显示 | 周期起止 + 下次重置日, 一并可见 |
| 历史曲线 | 展开面板查看近期用量趋势 |

## 媒体

![](https://pbs.twimg.com/media/HNUHY4KaoAADNim.jpg)

## 参考链接

- [项目仓库](https://github.com/lizill/ai-meter)

## 相关概念

- [TokenScope](./tool-tokenscope.md) — Claude CLI token 用量 / 费用估算菜单栏工具, 思路完全同类
- [frugon](./tool-frugon.md) — 给 LLM 调用日志算账的本地分析器, ai-meter 看「订阅余额」, frugon 看「按 token 计费的累计成本」,互补
- [Claude Code](./tool-claude-code.md) — ai-meter 的典型监控对象之一
