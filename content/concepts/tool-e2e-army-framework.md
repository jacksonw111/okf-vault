---
type: Tool
title: "e2e（tester.army 出品的 Agent 化端到端测试框架）"
description: "tester.army 出品的「agentic testing framework」：一行 `npx e2e init` 把可组合的确定性 API 与 Agent API 混在一起写端到端测试，支持 Web / 移动端，本地与 CI 都能跑，框架中立、可自带 Agent。"
resource: "https://tester.army/e2e"
tags: [e2e, testing, agentic-testing, web-testing, mobile-testing, ci]
timestamp: 2026-10-01T16:29:04Z
---

# e2e

## 它是什么

**e2e** 是 [tester.army](https://tester.army) 发布的「**agentic testing framework for any app**」——把**确定性 API**（assertion / 模拟 / 流程编排）和 **Agent API**（让模型在测试里自主决策）混合在同一套用例里写端到端测试。

定位非常明确：

- **完全开源**
- **混合确定性 + Agentic**：稳定性与灵活度按场景自由搭配
- **跨端**：Web / 移动端 / 其他
- **自带 Agent 与基础设施**：不绑定某个 Agent 或云
- **本地与 CI 都能跑**

一行 `npx e2e init` 即可在任意仓库内初始化。

## 为什么用它 / 适合什么场景

- 现有 e2e 测试（Cypess / Playwright / Detox）写得太死，遇到产品改动大面积失效。
- 想在测试里让模型识别 UI 变化、做模糊匹配，但又怕全 Agent 不可控。
- 团队已经引入 Claude Code / Codex / 其他 Agent，希望测试本身能调度它们。
- CI 需要稳定，但本地开发又想要更高的灵活度。

## 关键能力

| 能力 | 说明 |
|------|------|
| 安装 | `npx e2e init` 一行起步 |
| API 风格 | 混合 deterministic + agentic，可分阶段调用 |
| 平台 | Web / Mobile / 其他 |
| 接入模型 | 自带 Agent + 基础设施（BYO） |
| 运行环境 | 本地 + CI |
| 许可 | 完全开源 |

## 参考链接

- 项目入口：<https://tester.army/e2e>

## 媒体

- ![](https://pbs.twimg.com/media/HTjbJPEWQAEBJmV.jpg)

## 相关概念

- [Playwright](https://playwright.dev/) — 同类 Web 端到端测试基座（外部链接）
- [Vitest](./tool-cove-stack.md) — 同为测试工具链，但偏单元 / 集成层
