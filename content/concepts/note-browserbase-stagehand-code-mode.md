---
type: "Note"
title: "Browserbase 三代 Computer-Use 演进：从像素到 Code Mode"
description: "Browserbase 团队对浏览器 Agent 三代技术路线的复盘：纯视觉 CUA → 视觉+文本混合 → 代码模式终局；核心结论：做好 Agent 是 Harness 问题、不是模型研究问题。"
resource: "https://x.com/shao__meng/status/2097838012260585560"
tags: "[browser-agent, computer-use, stagehand, browserbase, langchain, note]"
timestamp: "2026-09-11T22:15:00Z"
---

# Browserbase 三代 Computer-Use 演进：从像素到 Code Mode

## 它是什么

[Browserbase](https://browserbase.com) 团队 `@kylejeong` / `@miguel_gonzf` 联合 LangChain 团队 `@sydneyrunkle` / `@huntlovell` 的完整复盘：**浏览器 Agent 的三代技术路线**，宣布**放弃「给模型预设工具」**，**全面转向「让模型直接写代码控制浏览器」**。

## 三代技术路线

| 代 | 代表 | 做法 | 问题 |
|----|------|------|------|
| **1. 纯视觉 CUA** | OpenAI Operator | 视觉模型识别屏幕像素，返回坐标点击 | 只在特定视口尺寸训练；窗口变就「Agent 基本失明」；截图看不到不可见组件 |
| **2. 视觉+文本混合** | Stagehand 早期 | 截图 + DOM / 无障碍树快照 | 基准测试有提升，但长任务迅速撑爆上下文窗口；精度达不到企业生产标准 |
| **3. 代码模式** | Stagehand v4 / Cloudflare | 模型直接写代码表达操作意图 | 团队认为**无根本缺陷**，成为终局方案 |

## 用 Sutton 的「bitter lesson」解释

> 每一代新模型出来，他们都发现之前精心设计的护栏式抽象反而成了瓶颈，于是不断**做减法、缩小工具表面积**。

## 三个核心工程洞见

### 1. 承认早期设计是错的

旧版 Stagehand 提供 Act / Extract / Observe 三个严格工具，出发点是「模型不可信，需要护栏」。团队直言：

> "we were so wrong"

**代码是模型最有效的意图表达方式**，模型甚至会写出设计者没想到的组合策略。**专用工具输给通用接口**。

### 2. 「Stagehand 不在模型权重里」

接入 MCP 后 Agent 反而稳定失败，原因很朴素：

> 所有前沿模型都在 **Playwright 语法**上做过后训练，没人见过 Stagehand。

试过教学 skill、强化 system prompt、加护栏——全部失败；后训练专用模型又违背用户「自带模型」的诉求。最终方案是**彻底顺从模型**：

> 让模型写 Playwright 代码，在发送到浏览器前**实时转译**为更快的 Stagehand 方法。

原则："**让模型做它擅长的事，然后让开**"——对「**模型能力分布决定接口设计**」的教科书式示范。

### 3. Demo 与生产的分界是安全边界

- 域名白名单
- 网络层防护
- 沙箱化 runtime + 策略治理

比喻：「**没有极好的刹车和防滚架，你不会把赛车开上公共道路**」。

技术上 Stagehand v4 做成 **Chrome 扩展**，runtime 直接跑在浏览器内，**run 工具天然不需要额外沙箱**；性能宣称：

- 比 Playwright **快 2 倍**
- **省 80% token**

MCP server 只保留三个工具：

| 工具 | 作用 |
|------|------|
| `run` | 执行代码 |
| `snapshot` | 剪枝后的 DOM + 无障碍树 |
| `screenshot` | 补充视觉上下文（覆盖 canvas、OS 层内容） |

## 生态卡位与行业判断

- **LangChain Deep Agents**（模型无关的通用 Harness，提供上下文自动卸载、子 Agent 委派、规划等编码 Agent 原语）合作：Browserbase 做浏览器 SDK，LangChain 做通用 harness。
- Cloudflare 的 `@threepointone` 与 `@KentonVarda` 是**代码模式思路的早期实践者**。

> **行业判断：做好 Agent 是 Harness 问题，不是模型研究问题；最好的 Agent 本质上都是换了外衣的 Coding Agent。**

## 参考链接

- 原始推文复盘：<https://x.com/shao__meng/status/2097838012260585560>

## 媒体

- ![](https://pbs.twimg.com/media/HR0EidyaAAARVBi.jpg)

## 相关概念

- [Browser Use Pi](./tool-browser-use-pi.md) — Browser-Use 团队轻量 Web Agent
- [Vercel Agent Browser](./tool-vercel-agent-browser.md) — Vercel Labs 模拟浏览器行为
- [tool-browser-use-pi](./tool-browser-use-pi.md) — Web Agent 另一类实现
- [CUA-Lite](./tool-cua-lite.md) — 电脑操作 Agent 全流程框架
</content>
</invoke>