---
type: "Tool"
title: "auto-reply（DreDabe/auto-reply）"
description: "基于 SightFlow(Apache-2.0)改出来的桌面端自动回复工具:用视觉语言模型直接读聊天窗口截图(微信 / 钉钉等),判情绪 + 攒本地经验,不接聊天软件 API。"
resource: "https://github.com/DreDabe/auto-reply"
tags: "[auto-reply, vlm, chat, desktop, wechat, dingtalk, agent, vision]"
timestamp: "2026-07-14T10:30:00Z"
---

# auto-reply

[auto-reply](https://github.com/DreDabe/auto-reply) 是基于 **SightFlow** 改出来的桌面端**自动回复工具**:用**视觉语言模型**(VLM)直接读聊天窗口截图,识别消息、判断情绪、生成回复,同时把每次对话攒成本地经验。

## 工作原理

```
聊天窗口截图 ──▶ 截图裁剪 + 文字提取(VLM)
              │
              ├─▶ 情绪判别
              ├─▶ 消息语义理解
              └─▶ 历史经验检索(RAG)
                          │
                          ▼
                  生成回复草稿
```

## 关键能力

| 能力 | 说明 |
|------|------|
| 截图即数据 | 不接任何聊天软件 API,只读窗口截图 |
| 情绪识别 | 对方是新消息时顺手判情绪 |
| 本地经验 | 每次对话攒到本地,后续可检索复用 |
| 多聊天工具 | 理论上任何聊天窗口(微信 / 钉钉 / Slack)都适用 |
| 桌面端运行 | 本地推理,数据不出端 |

## 适合什么场景

- 想**自动化回复**又不愿把账号数据交给第三方聊天 API 的用户。
- 在多个聊天软件间切换,**统一回复助理**。
- 对延迟 / 隐私敏感,要求**本地优先**自动回复的个人 / 副业。

## 与同类资源的差别

| 资源 | 特征 | auto-reply |
|------|------|-----------|
| SimpleX Chat | 去中心化聊天工具本身 | 聊工具 vs 聊**助手** |
| Hermes / Hermes Extension | 给 agent 配浏览器侧栏 | 浏览器场景;本工具桌面聊天窗口 |
| MemGUI-Agent | 移动端 GUI agent(快手) | 移动端;本工具桌面端 |

## 参考链接

- [项目仓库](https://github.com/DreDabe/auto-reply)

## 相关概念

- [MemGUI-Agent](./tool-memgui-agent.md) — 同样基于视觉的 GUI Agent,移动端版
- [page-agent](./tool-page-agent.md) — 浏览器 GUI Agent,本工具是其桌面聊天窗口的对应物
