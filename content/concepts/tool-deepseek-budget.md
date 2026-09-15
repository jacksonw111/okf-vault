---
type: "Tool"
title: "DeepSeekBudget（DeepSeek API 价格指示器）"
description: "FAAATQ/DeepSeekBudget：在菜单栏驻一个 DeepSeek API 价格指示器，实时显示当前处于高峰还是低谷计费、距离下次切换还有多久，帮用户挑便宜时段调用 API 省钱。"
resource: "https://github.com/FAAATQ/DeepSeekBudget"
tags: "[deepseek, api-pricing, menubar, cost-saving, desktop]"
timestamp: "2026-09-15T11:25:00Z"
---

# DeepSeekBudget（DeepSeek API 价格指示器）

## 它是什么

[DeepSeekBudget](https://github.com/FAAATQ/DeepSeekBudget) 是一个**菜单栏常驻小程序**：把 DeepSeek API 的「**高峰 / 低谷**」计费时段实时显在屏幕上，并倒计时距离下次时段切换还有多久。对于经常调用 DeepSeek API 的用户，它帮你**挑便宜时段发请求**。

## 为什么用它

- DeepSeek 现行 API 按**时段差异化定价**，谷时单价可远低于峰时。
- 多数用户没意识去记时段表——DeepSeekBudget 把这件事**做到菜单栏常驻**，看一眼就能决策。
- 比手算 cron 触发要直观得多。

## 关键能力

| 能力 | 说明 |
|------|------|
| 菜单栏常驻 | macOS 菜单栏始终可见 |
| 时段识别 | 实时显示当前处于高峰 / 低谷 |
| 倒计时 | 显示距离下次时段切换还有多久 |
| 价格预估 | 根据时段给出当前单价档位 |
| 省钱提醒 | 把「**等到低谷再调**」变成肌肉记忆 |

## 适合谁

- 把 DeepSeek API 当主力 LLM 提供方的开发者 / 团队
- 重度调用、想把账单压下去的独立开发者
- 想做成本可视化但不想自建监控的极简党

## 媒体

![](https://pbs.twimg.com/media/HSOzm1BacAA1P4Y.jpg)

## 项目链接

- 仓库：<https://github.com/FAAATQ/DeepSeekBudget>