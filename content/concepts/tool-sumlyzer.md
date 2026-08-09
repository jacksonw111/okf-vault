---
type: "Tool"
title: "sumlyzer"
description: "ErwanRaulo 写的 npm workspace 测试增强工具：在原生 npm test 之上补聚合摘要、fail-fast、并发执行、JUnit 报告输出，让 monorepo CI 一次跑完所有 workspace 测试并给出一致可读的结果。"
resource: "https://github.com/ErwanRaulo/sumlyzer"
tags: [npm, workspace, monorepo, test-runner, junit, ci]
timestamp: "2026-08-09T19:35:00Z"
---

# sumlyzer

## 它是什么

[sumlyzer](https://github.com/ErwanRaulo/sumlyzer) 是 npm workspace 的测试增强 CLI：原生 `npm test` 在 monorepo 里跑 N 个 workspace 时**没有聚合摘要、不能 fail-fast、并发执行也不可控**，CI 体验差。sumlyzer 把这些补全——一次跑完所有 workspace 测试，**聚合摘要 / fail-fast / 并发执行 / JUnit 报告**一次给齐。

## 为什么用它 / 适合什么场景

- 维护 monorepo，CI 上 `npm test` 输出散在几十个 workspace 里，找失败项费眼。
- 想让 CI 在第一个 workspace 失败时就停，节省调试时间。
- 想把 monorepo 测试结果上传到 GitLab / Jenkins / SonarQube / Codecov 等支持 JUnit 的系统。
- 想控制并发度，避免 monorepo 测试同时启动把 CI runner 跑爆。

## 关键能力

| 能力 | 说明 |
|------|------|
| 聚合摘要 | 一次跑完所有 workspace 后给一份统一报告 |
| fail-fast | 任一 workspace 测试失败立刻停，节省 CI 时间 |
| 并发执行 | 控制并发度，避免资源争抢 |
| JUnit 报告 | 输出标准 JUnit XML，对接 CI 系统 |
| 兼容 npm | 基于 `npm test`，不动 package.json 现有脚本 |

## 媒体

![](https://pbs.twimg.com/media/HPMTukLakAAgOCs.jpg)

## 相关概念

（暂无直接相关概念）