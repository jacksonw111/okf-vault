---
type: "Term"
title: "Computer Use（计算机使用）"
description: "让 AI 像人一样直接操作桌面 / 浏览器 / 手机：读屏幕 → 决策 → 模拟键鼠点击执行。Anthropic 2024 年在 Claude 3.5 Sonnet 上首次正式开放该能力。"
resource: "https://docs.anthropic.com/en/docs/agents-and-tools/computer-use"
tags: "[computer-use, anthropic, agent, ui-automation, vision]"
timestamp: "2026-09-14T22:30:00Z"
---

# Computer Use（计算机使用）

## 它是什么

**Computer Use** 是让 AI **像人一样直接操作图形界面**的能力：读取屏幕像素 / UI 元素、决策下一步动作、模拟键鼠点击 / 输入 / 滑动执行。从浏览器到桌面应用、再到手机屏幕，agent 不再依赖 API，而是直接「看屏幕 + 操作界面」。

Anthropic 在 **2024-10** 发布的 **Claude 3.5 Sonnet (new)** 上首次正式开放该能力，配套发布 **Computer Use API**；之后 OpenAI、Google 等陆续推出类似能力（Operator、Project Mariner、Astra 等）。

## 工作循环

1. **观察** — 截图 / 读屏（accessibility tree）
2. **思考** — LLM 决定下一步动作
3. **执行** — 模拟鼠标 / 键盘 / 触摸
4. **再观察** — 截图确认结果，回到 1

## 适用 / 不适用

| 适用 | 不适用 |
|------|--------|
| 没有 API 的老旧桌面应用 | 有完善 API 的服务（直接调 API 更稳） |
| 跨软件搬数据需要切窗口 | 高频重复任务（DOM 结构稳定的场景用 Playwright 更省） |
| 真机自动化测试 | 银行 / 支付类风控敏感场景 |
| UI 自绘 / 延迟弹窗抗干扰测试 | 需要亚秒级响应的实时任务 |

## 实例项目

- **Anthropic Computer Use** — Claude 桌面版「我能操作你的电脑」
- **OpenAI Operator** — 浏览器内自动化
- **Google Artemis** — Android 真机版 Computer Use
- **Browser Use** — Playwright + LLM 的浏览器自动化
- **CUA** — Computer Use Agent 评测基准

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — Computer Use 之外的另一套 agent ↔ 工具接入标准
- [Artemis（Google 真机 Android 自动化）](./tool-artemis-google-android-automation.md) — Android 真机版 Computer Use 实现

## 参考链接

- Anthropic 官方文档：<https://docs.anthropic.com/en/docs/agents-and-tools/computer-use>
