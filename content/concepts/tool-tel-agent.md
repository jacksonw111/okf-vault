---
type: Tool
title: "Tel-Agent"
description: "开源电话网关，来电按规则分流（转人工 / 挂掉 / 交给 AI），AI 可转接、留言、查日历、调外部接口；通话全程录音 + 文字记录可查。"
resource: "https://github.com/Dpro-at/Tel-Agent"
tags: "[telephony, voice, ai-agent, ivr, sip]"
timestamp: "2026-09-07T13:07:00Z"
---

# Tel-Agent

## 它是什么
一个开源的电话网关（Telephony Gateway）。当有电话打进来时按预设规则分流：转接人工、直接挂断，或者交给 AI Agent 直接跟对方聊。AI 侧可执行转接、留言、查日历、调用外部接口等动作，所有通话自动录音 + 文字转写，便于事后回看。

## 工作流
1. 来电接入 → 规则匹配
2. 三选一：转人工 / 挂断 / AI Agent 应答
3. AI Agent 应答路径：可主动转接、留言、调 API、查日程
4. 通话全程：录音 + 转写并存档
5. 其它聊天渠道可在同一面板回复（统一收件箱）

## 关键能力
| 能力 | 说明 |
|------|------|
| 规则分流 | 来电按规则三选一处理 |
| AI 应答 | LLM Agent 实时跟对方对话 |
| 可执行动作 | 转接 / 留言 / 查日历 / 调外部 API |
| 通话记录 | 录音 + 文字，全可检索 |
| 渠道统一 | 电话 + 其它聊天同面板回 |

## 适用场景
- 个人 / 小团队：不想接推销电话、不漏重要电话
- 客服：下班后 AI 顶班、记录诉求
- 创业者：用一个号码接所有客户咨询 + 自己的 IM

## 参考
- 项目链接：<https://github.com/Dpro-at/Tel-Agent>

## 相关概念
- [OpenMac](tool-openmac.md) — 把 macOS Vision/Translation 等系统能力暴露成 API，与 Tel-Agent 在"系统能力 API 化"思路上一致