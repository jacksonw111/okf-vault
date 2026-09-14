---
type: "Tool"
title: "Artemis（Google 真机 Android 自动化）"
description: "Google 团队开源的真机 Android 自动化工具：让 AI 助手与测试套件像人一样直接操作真机。看屏幕抓画面、划屏点按打字切 App 全自动跑，无需 Root；在 AndroidWorld 上 100+ 复合任务完成率超 99%。"
resource: "https://github.com/google/artemis"
tags: "[android, automation, testing, google, ai-agent, mobile, mcp]"
timestamp: "2026-09-13T08:58:00Z"
---

# Artemis（Google 真机 Android 自动化）

## 它是什么

[google/artemis](https://github.com/google/artemis) 是 **Google 团队开源**的真机自动化工具：**让 AI 助手 + 测试套件像人一样直接操作 Android 真机**。插上数据线开 USB 调试，AI 直接看屏幕抓画面，划屏、点按、打字、切 App 全自动跑——**不用 Root**。

## 为什么用它 / 适合什么场景

- 测 App 想拿真机反复点，不想写一堆脚本。
- 跨软件搬数据需要手动来回切，想让 AI 自动化。
- 写完代码想让 AI 在真机直接验证。
- 现有自动化脚本遇到自绘界面 / 延迟弹窗 / 动画卡顿就歇菜，需要抗干扰能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 真机全自动 | 插数据线 + USB 调试即可 |
| 屏幕抓画面 | AI 直接读屏 |
| 划屏 / 点按 / 打字 / 切 App | 全套人类操作 |
| 无需 Root | 普通手机即可 |
| AndroidWorld 评测 | 20+ App / 100+ 复合任务完成率 99%+ |
| Flash / Pro 双模式 | 简单任务 3-5 秒响应；复杂流程自动拆步 + 重试 + 留测试记录 |
| 原生 MCP 支持 | Claude Code / Cursor / Windsurf 一键接入 |
| 写完直接测 | 编辑器说句话就能打包 → 安装 → 跑测试 → 截图 |
| 网页投屏 | 浏览器看手机高清低延迟投屏，左侧输入任务，右侧显示思考过程与操作轨迹 |
| Apache-2.0 完全开源 | 无广告无付费 |

## 集成模式

| 模式 | 适用 |
|------|------|
| Flash | 简单任务（点开 / 输入），3-5 秒响应 |
| Pro | 复杂流程（跨 App / 多步 / 重试），自动拆步骤 + 测试记录 |

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HSEPbXhbYAAJGtx.mp4>

## 注意事项

- 银行、支付类 App 风控严，可能触发验证码。
- 微信自动发消息暂不支持。

## 项目链接

- 仓库：<https://github.com/google/artemis>

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — Artemis 原生支持 MCP，与 Claude Code / Cursor / Windsurf 一键对接
- [Computer Use](./term-computer-use.md) — Artemis 是「Android 真机版 Computer Use」类实现