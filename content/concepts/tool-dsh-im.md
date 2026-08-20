---
type: Tool
title: "dsh-im (xmanrui/dsh-im)"
description: "把 9 个 IM 平台（飞书/微信/钉钉/企微/QQ/Slack/Telegram/Discord/WhatsApp）的机器人统一接入 DeepSeek Harness"
resource: "https://github.com/xmanrui/dsh-im"
tags: [deepseek-harness, dsh, im, bot, feishu, slack, telegram, discord]
timestamp: 2026-08-20T14:01:00Z
---

# dsh-im (xmanrui/dsh-im)

## 它是什么
[`xmanrui/dsh-im`](https://github.com/xmanrui/dsh-im) 是一个把 **9 个 IM 平台**的官方/自定义机器人**统一**接入 **DeepSeek Harness (DSH)** 的桥接层：飞书、微信、钉钉、企业微信、QQ、Slack、Telegram、Discord、WhatsApp 都通过同一个适配层对接 dsh 后端，无需为每个平台单独写一个 agent 后台。

## 为什么用它 / 适合什么场景
- 团队成员散落在多个 IM（飞书 + 微信 + Slack），希望同一个 DSH agent 都能响应。
- 想在客户已有的企业微信 / 飞书 / 钉钉里嵌入一个 AI 助理，又不想为每个平台都搭一套后端。
- 已有 DSH 业务逻辑，只差"怎么把消息送进来"的适配器。

## 关键能力
| 能力 | 说明 |
|------|------|
| 9 平台统一适配 | 飞书 / 微信 / 钉钉 / 企微 / QQ / Slack / Telegram / Discord / WhatsApp |
| DSH 后端共享 | 所有平台的会话最终汇入同一个 DSH 后端 |
| 机器人接入 | 每个平台用各自官方机器人协议 |
| 一处实现，到处跑 | 加一个 IM 平台只需写一个新适配，不必复制 DSH 业务 |

## 媒体
- ![dsh-im 截图](https://pbs.twimg.com/media/HQEDrifbIAA4GQN.jpg)

## 相关概念
- [项目仓库](https://github.com/xmanrui/dsh-im) — 仓库主页
- [dsh-crew](./tool-dsh-crew.md) — DSH agent 作为子代理接入 Claude Code / Codex；本工具把 IM 当作入口
- [dsh-agent-teams](./tool-dsh-agent-teams.md) — 同一 DSH 生态的多代理插件
