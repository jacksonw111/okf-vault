---
type: "Tool"
title: "jev-webmcp-extension"
description: "浏览器扩展——用户输入一句自然语言，Jev 从当前页面已注册的 WebMCP 工具中挑出该调用哪个、参数怎么填，不需要站点专属配置。"
resource: "https://github.com/sdras/jev-webmcp-extension"
tags: "[browser-extension, webmcp, mcp, jev, intent-routing, open-source]"
timestamp: "2026-09-23T22:35:00Z"
---

# jev-webmcp-extension

## 它是什么

[jev-webmcp-extension](https://github.com/sdras/jev-webmcp-extension) 是一个**浏览器扩展**，把 Jev 决策模型用作 WebMCP 工具的「路由器」：

> 让用户在浏览器里打一句自然语言，由 Jev 从当前页面已注册的 WebMCP 工具中挑出该调用哪个、参数怎么填，不需要站点专属配置。

## 为什么用它 / 适合什么场景

- 想用自然语言驱动当前页面已注册的 WebMCP 工具——不必为每个站点写专属映射。
- 想验证「**通用意图路由**」是否真能跨站点泛化。
- 浏览器 MCP 客户端的用户，想要「一句话完成跨工具组合操作」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 意图路由 | 自然语言 → 工具选择 + 参数提取 |
| 数据源 | 当前页面已注册的 WebMCP 工具 |
| 配置 | 无需站点专属映射 |
| 部署 | 浏览器扩展 |

## 与传统浏览器自动化的差异

| 维度 | jev-webmcp-extension | Selenium / Playwright |
|------|----------------------|------------------------|
| 目标 | 语义化意图 → 工具调用 | 选择器脚本 |
| 站点适配 | 自动（依赖 WebMCP 工具注册） | 每站点一套脚本 |
| 输入 | 自然语言 | 编程语言 |

## 项目链接
- 项目主页：<https://github.com/sdras/jev-webmcp-extension>

## 媒体
![jev-webmcp-extension 截图](https://pbs.twimg.com/media/HSyiVzNbAAAY_Xr.jpg)
