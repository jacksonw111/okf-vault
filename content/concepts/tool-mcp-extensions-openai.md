---
type: "Tool"
title: "OpenAI MCP Extensions（ChatGPT 专有的 MCP 入口与 UI 能力）"
description: "OpenAI 官方推出的 MCP 扩展协议层：在 MCP 之上加 ChatGPT 专有的入口（apps / connectors / UI widgets）和界面渲染能力，让第三方插件用起来像 ChatGPT 自带功能。"
resource: "https://github.com/openai/mcp-extensions"
tags: "[openai, mcp, chatgpt, plugins, ui-widget, connectors, agent]"
timestamp: "2026-10-02T02:50:00Z"
---

# OpenAI MCP Extensions（ChatGPT 专有的 MCP 入口与 UI 能力）

## 它是什么

[OpenAI MCP Extensions](https://github.com/openai/mcp-extensions) 是 OpenAI 官方在 **MCP 基础协议之上**加的「ChatGPT 专有扩展层」：

- 入口扩展：让 MCP server 能注册为 ChatGPT 内的 **App / Connector**，出现在侧栏里
- UI 扩展：让 MCP 工具调用能渲染出 ChatGPT 风格的**内嵌组件**（卡片、表单、按钮、列表）
- 元数据扩展：把 MCP 工具的展示名称、图标、分类也写进协议

## 为什么用它 / 适合什么场景

| 场景 | MCP Extensions 的好处 |
|------|---------------------|
| 让自家 MCP server 进入 ChatGPT 侧栏 | 走 Apps SDK 接入，用户免配置即可用 |
| 让工具调用有可点击 UI 而非纯文本 | 提升交互效率（订餐、订票、查订单不需要复制粘贴） |
| 跟 ChatGPT 自带功能做深度整合 | 比如把 connector 接入日程 / 邮件 / 文件 |
| 给 MCP server 加品牌资产 | 自定义图标 / 名称 / 分类 |

## 与「裸 MCP」的区别

| 维度 | 裸 MCP | MCP + Extensions |
|------|--------|-----------------|
| 协议规范 | Anthropic 开源，跨厂商 | OpenAI 在 MCP 上做的扩展 |
| 入口 | 需要客户端集成 | 直接作为 ChatGPT 内的 App 出现 |
| 输出 | 通常是文本 / JSON | 可渲染富 UI（卡片、表单、按钮） |
| 适用 | Claude Desktop / Cursor / 自家客户端 | ChatGPT 内 |
| 互通 | 标准 MCP 可被任何客户端消费 | ChatGPT 专有部分不可被其他客户端消费 |

## 关键能力

| 能力 | 说明 |
|------|------|
| Apps 注册 | 把 MCP server 注册为 ChatGPT 内的 App |
| Connectors 注册 | 把外部 API / 服务接入 ChatGPT |
| UI Widget | 工具调用可渲染富组件 |
| Manifest | 描述 App 的元数据（图标 / 名称 / 分类） |
| 鉴权 | ChatGPT 统一身份与权限 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105851764734128451>
- 项目链接：<https://github.com/openai/mcp-extensions>

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — 底层协议，Extensions 是其上扩展
- [Agent Skills](./term-agent-skills.md) — 另一种「给 LLM 配外部能力」的范式
- [ChatGPT Apps SDK](#) — 本仓库目前未收录
