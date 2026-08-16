---
type: Tool
title: "dsh-auto-continue"
description: "DeepSeek Harness 网页端会话被网络错误等意外打断时，插件自动替你敲一句「继续」发出去，不用人守着手动恢复"
resource: "https://github.com/HsiangNianian/dsh-auto-continue"
tags: [deepseek, harness, dsh, resilience, browser-plugin]
timestamp: 2026-08-16T16:00:00Z
---

# dsh-auto-continue

## 它是什么
`HsiangNianian/dsh-auto-continue` 是 **DeepSeek Harness (DSH)** 的一个**网页端插件**：当 DSH 会话因网络错误、断流、模型超时等**意外中断**时，插件会自动检测错误状态、替你**敲一句「继续」** 重发请求，把对话接力下去——**不需要人守在屏幕前手动恢复**。

## 为什么用它 / 适合什么场景
- 长对话跑几十分钟，临时网络抖动就被中断、上下文前功尽弃。
- 跑后台 / 跑自动化时无法时刻盯屏幕，需要自愈。
- 把 DSH 当「夜里跑任务的 agent」用，早上回来看结果而不是看一堆 error。
- 移动网络 / 4G 切 5G / WiFi 切换频繁的笔记本用户。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动检测中断 | 识别网络错误 / 模型超时 / 浏览器断流等异常状态 |
| 自动发「继续」 | 插件代替人工点 retry，恢复上下文继续生成 |
| 对话不丢 | 在原会话里续写，不开新会话、不复制上下文 |
| 守护式运行 | 适合长时间无人值守的任务 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvMTYIbAAEn4TS.jpg)

## 相关概念
- [项目链接](https://github.com/HsiangNianian/dsh-auto-continue)