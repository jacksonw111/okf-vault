---
type: "Term"
title: "decider-2b（端侧意图 / 风险判定小模型）"
description: "2B 参数量的端侧判定小模型，本地内存 / 显存占用约 3.8 GB——专做「意图识别 + 风险分级」类轻决策，给 Agent / 桌面助手当 System One 路由层用；典型如 jev-chat-jarvis-mac 用它判断微信 / QQ 消息意图与风险。"
tags: "[decider, system-one, small-model, intent-recognition, risk-classification, on-device, 2b]"
timestamp: "2026-09-26T21:50:00Z"
---

# decider-2b（端侧意图 / 风险判定小模型）

## 定义

**decider-2b** 是 **2B 参数** 的端侧判定小模型——专做「意图识别 + 风险分级」类轻决策，给 Agent / 桌面助手当 System One 路由层用。

- **占用**：约 **3.8 GB 内存 / 显存**
- **典型输入**：聊天消息、桌面弹窗内容、用户操作上下文
- **典型输出**：意图分类（问候 / 求助 / 推销 / …） + 风险等级（低 / 中 / 高）

## 要点

- **足够小**：2B 参数量，能在 M1 Pro / M2 Pro（≥ 12 GB 内存）上常驻。
- **System One 定位**：给 Agent 当快思考层，输出结构化判定结果。
- **延迟低**：本地推理，毫秒级响应，适合「弹窗 → 判定 → 候选回复」流水线。
- **不替代 LLM**：粗筛与路由交给它，复杂生成仍交回 LLM。

## 典型用例

[jev-chat-jarvis-mac](./tool-jev-chat-jarvis-mac.md) 用它：
1. 微信弹窗 → 截图 OCR → decider-2b 判定**意图 + 风险**
2. 输出**候选回复**，一键填入输入框
3. M1 Pro 上端到端延迟约 1.5 秒

## 相关概念

- [Jev](./term-jev.md) — System One 判定模型家族，decider-2b 是其「端侧小模型」定位
- [CLM-8B](./term-clm-8b.md) — 同样做 System One 决策但参数更大
- [jev-chat-jarvis-mac](./tool-jev-chat-jarvis-mac.md) — 使用 decider-2b 的桌面端工具