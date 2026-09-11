---
type: "Tool"
title: "CUA-Lite（轻量电脑操作 Agent 全流程框架）"
description: "电脑操作智能体全流程框架：10 多种模型接进来就能在桌面 / 浏览器 / 手机三端直接开跑；沙箱不用虚拟机，自带 3 万多个可验证任务，SFT 数据统一成 LiteSample 一种格式。"
resource: "https://github.com/cua-lite/cua-lite"
tags: "[ai-agent, computer-use, dataset, sandbox, agent-framework]"
timestamp: "2026-09-11T22:00:00Z"
---

# CUA-Lite

## 它是什么

[cua-lite/cua-lite](https://github.com/cua-lite/cua-lite) 是一个**轻量级 Computer-Use Agent（CUA）全流程框架**：把「训练数据 + 沙箱 + 多模型接入」三件事打包到一起，开发者只需接 10 多种现成模型，就能让 Agent 在桌面 / 浏览器 / 手机三端直接跑。

## 核心特点

| 维度 | 做法 |
|------|------|
| 沙箱 | **不用虚拟机**，启动轻、占用小 |
| 训练任务 | 自带 3 万多个可验证任务 |
| 数据格式 | 统一为 LiteSample 一种格式，多模型共用 |
| 模型接入 | 10 多种主流 LLM 接进来即可 |
| 运行端 | 桌面 / 浏览器 / 手机三端 |

## 为什么用它 / 适合什么场景

- 想做电脑操作 Agent（点屏幕 / 操作 UI / 填表）但不想自己搭沙箱。
- 想用统一格式微调 / 评测多个 CUA 模型，少写胶水。
- 想研究「**无 VM 沙箱**」在 CUA 训练中的可行性与边界。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模型即插即用 | 10+ LLM 适配器 |
| 三端一致 | 桌面 / Web / Mobile 同套 API |
| 3 万+ 任务 | 内置可验证任务集 |
| LiteSample | 训练数据统一格式 |
| 轻量沙箱 | 无 VM 启动 |

## 参考链接

- 项目仓库：<https://github.com/cua-lite/cua-lite>

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HRvm_dCbIAAjMK4.mp4>

## 相关概念

- [Browser Use Pi](./tool-browser-use-pi.md) — Browser-Use 团队的轻量 TypeScript Web Agent
- [Vercel Agent Browser](./tool-vercel-agent-browser.md) — 让 AI agent 模拟浏览器行为
- [Stagehand / Browserbase](./tool-browserbase-stagehand.md) — 三代 computer-use 演进的代码模式终局
</content>
</invoke>