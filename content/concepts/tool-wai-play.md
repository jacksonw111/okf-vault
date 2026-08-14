---
type: "Tool"
title: "wai-play"
description: "waiterve 开源的 AI 网页游戏自动试玩工具：让 AI 在真实浏览器里自动游玩网页游戏，输出可复现的问题证据与具体修改建议，省去创作者手动反复测试。"
resource: "https://github.com/waiterve/wai-play"
tags: ["agent", "game-testing", "browser", "automation", "open-source", "ai-tester"]
timestamp: "2026-08-14T19:50:00Z"
---

# wai-play

## 它是什么
wai-play 是给网页游戏开发者的「AI 自动测试员」：驱动一个真实浏览器，自动玩自己的网页游戏，每局记录出现的卡顿 / bug / UX 问题，并附可复现的证据（截图、操作序列、控制台日志）和具体的修复建议。

## 为什么用它 / 适合什么场景
- 网页游戏上线前需要大量手动回归测试，AI 可代为反复跑。
- 适合 Indie 团队 / 个人开发者，把「QA」精力交给 AI。
- 提交游戏到平台或集成到 CI，做「每一版自动跑一遍」。

## 关键能力
| 能力 | 说明 |
|------|------|
| 测试环境 | 真实浏览器（驱动层自动化） |
| 输出 | 问题清单 + 可复现证据 + 修复建议 |
| 角色 | AI 替开发者试玩 + 复现 + 反馈 |
| 适用 | 网页游戏（HTML5 / WebGL / Canvas） |
| 形态 | 开源工具 |

## 媒体

效果截图：![效果截图](https://pbs.twimg.com/media/HPklU27aMAAkANe.jpg)

## 相关概念
- [Pi-Computer-Use](./tool-pi-computer-use.md) — Pi 框架里的真实电脑控制能力，wai-play 是其「网页游戏场景」专门化
- [Multimodal UI Test Automation](./playbook-multimodal-ui-test-automation.md) — 多模态 UI 测试自动化的方法论，wai-play 是其「游戏场景」实例
- [OpenChatCut](./tool-openchatcut.md) — 让 Agent 直接读、剪、导出可继续编辑的真实视频项目，wai-play 与之同属「Agent 替代创作流程」思路
