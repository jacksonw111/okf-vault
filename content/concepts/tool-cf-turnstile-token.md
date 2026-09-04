---
type: Tool
title: "cf-turnstile-token（Turnstile 验证 token 获取器）"
description: "在脚本与 CI 环境里通过调用 Peak 的付费 API 取回 Cloudflare Turnstile 验证 token，省掉为每个 token 单独拉起一个浏览器实例的开销。"
resource: "https://github.com/kowalski76057/cf-turnstile-token"
tags: [cloudflare, turnstile, ci, automation, api]
timestamp: 2026-09-04T12:00:00Z
---

# cf-turnstile-token（Turnstile 验证 token 获取器）

## 它是什么

一个小工具：脚本或 CI 流水线里需要一个 Cloudflare Turnstile 的验证 token 时，它调用 Peak 的付费 API 直接把 token 取回来，而不是在流水线里为每个 token 现拉一个 headless 浏览器跑一遍前端挑战。

## 为什么用它 / 适合什么场景

- 对**自己拥有或已获授权的站点**做端到端测试 / 巡检时，测试机器人被自家 Turnstile 拦下。
- CI 环境里每次起浏览器实例的时间与内存开销明显，希望用一次 API 调用替代。

> ⚠️ 使用前提：只对自己有权访问的站点使用；绕过第三方站点的机器人防护通常违反其服务条款。

## 关键能力

| 能力 | 说明 |
|------|------|
| 取 token | 通过 Peak 付费 API 返回可用的 Turnstile 验证 token |
| 免浏览器 | 不需要在脚本 / CI 里维护浏览器实例 |
| 适用环境 | 脚本、CI 流水线等无图形界面环境 |

## 参考链接

- 项目链接：<https://github.com/kowalski76057/cf-turnstile-token>
- 原始链接：<https://x.com/QingQ77/status/2095693076480111084>

## 相关概念

- 暂无强关联概念。
