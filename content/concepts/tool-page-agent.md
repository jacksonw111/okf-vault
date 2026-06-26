---
type: Tool
title: "page-agent（阿里巴巴浏览器端 GUI Agent 库）"
description: "阿里巴巴开源的浏览器端 GUI Agent 库，纯 TypeScript 编写，引入一段脚本即可让任何网页用自然语言操控：文本操作 DOM、无需截图或多模态、可接自有 LLM，支持 npm / CDN / Chrome 扩展 / MCP Server 四种用法。"
resource: "https://github.com/alibaba/page-agent"
tags: [gui-agent, browser-agent, typescript, alibaba, dom, mcp]
timestamp: 2026-06-26T16:50:00Z
---

# page-agent

## 它是什么

page-agent 是**阿里巴巴开源的浏览器端 GUI Agent 库**，核心理念是"通过几行 JavaScript 让任何网页拥有自然语言操控能力，无需浏览器扩展或后端改造"。

实现：纯 TypeScript，**通过文本操作 DOM**（不走截图 / 多模态路线）。

四种用法：

| 形态 | 适用场景 |
|------|---------|
| npm 包 | 集成进自家前端项目 |
| CDN 引入 | 临时调试 / 演示 |
| Chrome 扩展 | 跨标签页操作 |
| MCP Server | 让外部 Agent 通过 MCP 控制浏览器 |

## 它与传统方案的差异

| 维度 | 截图 + 多模态 | page-agent |
|------|--------------|-----------|
| 感知方式 | 视觉（截图 + VLM） | DOM 文本 |
| 成本 | 高（每步都要 VLM 推理） | 低（纯文本解析） |
| 速度 | 慢 | 快 |
| 精确度 | 像素级 | 选择器级 |
| 跨站兼容 | 视觉模型泛化 | 依赖 DOM 结构稳定 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 一行脚本接入 | 任何网页秒变 AI 可控 |
| 纯文本操作 DOM | 不走多模态，token 成本低 |
| 自有 LLM 接入 | 不绑定阿里模型 |
| 多入口 | npm / CDN / 扩展 / MCP 四种 |
| 跨标签页 | Chrome 扩展形态支持 |
| MCP 兼容 | 外部 Agent 通过 MCP 控制 |

## 典型场景

- SaaS 嵌入 AI 助手（"帮我把这个表格按金额排序"）
- 智能填表（"把这一列的地址转拼音"）
- 无障碍访问（"帮我点这个按钮"）

## 原始链接

- [项目仓库](https://github.com/alibaba/page-agent)
- [原始推文剪藏](https://x.com/QingQ77/status/2070532789351674036)

## 相关概念

- [Obscura（Rust 无头浏览器）](./tool-obscura-headless-browser.md) — 同样是"Agent 控浏览器"思路，但 Obscura 走无头浏览器 + 反检测
- [Proxide](./tool-proxide.md) — 同样"Agent 接外部环境"，但 Proxide 是"接 ChatGPT Pro 网页"而非"接任意网页"
- [MemGUI-Agent](./tool-memgui-agent.md) — 同为 GUI Agent，但 MemGUI-Agent 聚焦"移动端长任务上下文管理"
