---
type: Tool
title: "dsh-mobile（DeepSeek Harness 手机远控）"
description: "用手机在局域网或公网通道里接着用电脑上的 DeepSeek Harness：DSH Mobile 是一套 DeepSeek Harness 插件加 Android App，手机走局域网或 Tailscale Funnel / cpolar / 自建 FRP 远程通道，连回电脑端正在跑的 DSH，接着用同一份会话、工作区和工具。"
resource: "https://github.com/saya-ch/dsh-mobile"
tags: [deepseek-harness, android, remote, tailscale, frp, mobile]
timestamp: "2026-09-03T00:00:00Z"
---

# dsh-mobile（DeepSeek Harness 手机远控）

## 它是什么

[dsh-mobile](https://github.com/saya-ch/dsh-mobile) 让你**用手机接着用电脑上的 DeepSeek Harness**——DSH Mobile 是一套 DeepSeek Harness 插件 + Android App：

- 手机走局域网，或经 Tailscale Funnel / cpolar / 自建 FRP 等远程通道连回电脑端正在跑的 DSH；
- 会话、工作区、工具保持同一份，无需在手机上重新配置；
- 全程不动 DSH 源码（只是用插件扩展）。

## 为什么用它 / 适合什么场景

- DSH 在电脑上跑，但想躺在沙发上用手机继续问问题 / 看输出；
- 出差时希望从公网连回家里 / 公司电脑上一直开着的 DSH 会话；
- 想保持会话上下文延续，不想换设备就丢历史；
- 不愿自己 hack 源码——希望以插件形式接入。

## 关键能力

| 能力 | 说明 |
|------|------|
| DSH 插件 + Android App | 客户端双形态 |
| 局域网 + 公网通道 | Tailscale Funnel / cpolar / 自建 FRP |
| 同会话续用 | 工作区 / 工具保持同一份 |
| 不动源码 | 走插件扩展路线 |
| 会话延续 | 切设备不丢历史 |

## 参考链接

- 项目链接：<https://github.com/saya-ch/dsh-mobile>
- 原始推文：<https://x.com/QingQ77/status/2095505592068473228>
- 媒体：<https://pbs.twimg.com/media/HRL2LzhbcAAKhWZ.jpg>

## 相关概念

- [deepseek-harness](./tool-deepseek-harness-core.md) — DeepSeek 官方可插拔智能体框架
- [happier](./tool-happier.md) — 开源端到端加密跨设备 AI 编码客户端
- [Cxx WeChat](./tool-cxx-wechat.md) — 用微信当遥控器接管 Codex / Claude Code
