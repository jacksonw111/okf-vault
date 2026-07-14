---
type: "Tool"
title: "TIMA — Tiny Interjection Model Alpha"
description: "Jiply 训练的小型模型,用于在打字聊天场景里实时判断助手应当「等待 / 回复 / 插话 / 继续」,把助手从「答得对」升级到「接得对」。"
resource: "https://github.com/Jiply/tiny-interjection-model-alpha"
tags: "[nlp, realtime, chat-agent, small-model, turn-taking, model]"
timestamp: "2026-07-14T03:51:00Z"
---

# TIMA — Tiny Interjection Model Alpha

[TIMA](https://github.com/Jiply/tiny-interjection-model-alpha) 是一个**小型模型**,专门解决打字聊天里**助手应当「等待 / 回复 / 插话 / 继续」**的实时判断问题。

## 解决问题

传统聊天助手只看「对方说了什么」决定回不回答。问题是:

- 对方发到一半就停了,助手接不上(过早回复)。
- 对方已经结束但助手没接话(漏掉信号)。
- 助手过早插话打断对方思路。

TIMA 把这件事拆成一个独立的小模型,**专做对话回合决策**。

## 四种动作

| 动作 | 含义 |
|------|------|
| 等待 | 对方还在输入,别动 |
| 回复 | 对方说完,该回了 |
| 插话 | 可以表示赞同 / 追问(对方已停) |
| 继续 | 鼓励对方继续(如「嗯,然后呢?」) |

## 关键能力

| 能力 | 说明 |
|------|------|
| 小型模型 | 不需 GPU,极快推断 |
| 实时性 | 毫秒级判断 |
| 独立模块 | 可与任意 LLM 主代理组合 |
| Open-source | MIT / Apache 风格,方便二次训练 |

## 适合什么场景

- AI 客服 / 实时对话产品希望**降低打断率**。
- 语音助手 / IM 插件的「自然接话」实验。
- 想给现有 agent 加一个回合决策层,而不是改主模型 prompt。

## 与同类资源的差别

| 资源 | 特征 | TIMA |
|------|------|------|
| eot-bench | LiveKit 话轮检测基准 | 数据 / 评测;TIMA 是模型实现 |
| MemGUI-Agent | 移动端 GUI Agent,ConAct 把上下文管理塞进模型输出 | 主 agent;TIMA 是单独的回合模块 |

## 参考链接

- [项目仓库](https://github.com/Jiply/tiny-interjection-model-alpha)

## 相关概念

- [eot-bench](./tool-eot-bench.md) — LiveKit 的首个公开话轮检测基准,可用于评估 TIMA 类模型
