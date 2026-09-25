---
type: "Tool"
title: "jev-chat-jarvis-mac（Mac 版微信 / QQ 消息意图助手）"
description: "Mac 上微信或 QQ 弹出消息时，本机截图 OCR（QQ 走无障碍树），用本地 decider-2b 小模型判断对方真实意图与风险等级，给出候选回复一键填入输入框，全程只读不注入微信。"
resource: "https://github.com/jev-chat/jev-chat-jarvis-mac"
tags: "[macos, wechat, qq, ocr, intent-recognition, jev, accessibility, local-model, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# jev-chat-jarvis-mac（Mac 版微信 / QQ 消息意图助手）

## 它是什么

[jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac) 是 [jev-chat-jarvis](./tool-jev-chat-jarvis.md) 在 Mac 端的对应版本——桌面端变体，原理同样以「**只读 + 不注入宿主**」为底线：

- **微信**：弹窗出现时调用 Mac 本机截图 → OCR 出文字
- **QQ**：直接读取系统的**无障碍树**（免截图）
- 把抽取到的消息送进本地小模型 **`decider-2b`**，判断**对方真实意图**与**风险等级**
- 输出**候选回复**，可一键填到微信 / QQ 的输入框
- 整个过程**不读写微信 / QQ 进程**，发不发由用户自己点

## 为什么用它 / 适合什么场景

- Mac 上微信 / QQ 弹消息时，希望快速看到「对方真实在说什么 / 风险多大」，需要 AI 起草几种语气选择。
- 强调「**只读、不注入**」——避免 AI 越权代发聊天，所有动作必须由人点。
- 偏好**本地模型**而非云端 API，希望消息内容不出本机。
- 已有 M1 Pro / M2 Pro 等 Apple Silicon，且**内存 ≥ 12 GB**（`decider-2b` 占 3.8 GB，不到这个水位直接不加载）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 平台 | macOS（Apple Silicon 实测 M1 Pro） |
| 微信数据获取 | 本机截图 + OCR |
| QQ 数据获取 | 系统无障碍树（无需截屏） |
| 模型 | 本地 `decider-2b`（约 3.8 GB 显存 / 内存占用） |
| 输出 | 对方意图 + 风险等级 + 候选回复 |
| 触发 | 一键填入输入框（不自动发送） |
| 延迟 | M1 Pro 实测约 1.5 秒（截图 → 候选回复） |
| 隔离 | 不读写微信 / QQ 进程，只与系统无障碍 + OCR 交互 |

## 媒体

![](https://pbs.twimg.com/media/HTBKsibagAATugb.jpg)

## 相关概念

- [jev-chat-jarvis](./tool-jev-chat-jarvis.md) — 移动端版本（无障碍只读手机屏幕），同样不代发
- [decider-2b（TypeSafe 小模型）](./term-decider-2b.md) — 本项目用于意图 / 风险判定的本地小模型
