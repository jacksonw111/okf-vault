---
type: "Tool"
title: "FableCut（ronak-create/FableCut）"
description: "浏览器内运行的视频编辑器,时间线是一份 JSON,让 Claude 这类 AI 代理通过 MCP 或 REST 直接剪视频,画面实时跟着变。"
resource: "https://github.com/ronak-create/FableCut"
tags: "[video-editing, ai-agent, mcp, json, browser, rest]"
timestamp: "2026-07-15T13:26:00Z"
---

# FableCut

[FableCut](https://github.com/ronak-create/FableCut) 把视频剪辑**搬进浏览器**,核心数据结构是一份 **JSON 时间线**,让 Claude 这类 AI 代理通过 **MCP 或 REST** 直接剪——画面实时跟着变。

## 它解决了什么

传统剪辑软件(NLE)时间线是私有的 .prproj / .fcpxml / 内部 OMML。Agent 不会用鼠标拖拽轨道、无法程序化精确控制,只能输出一份脚本请人跑。FableCut 把时间线**外化**成 JSON + HTTP/MCP,剪视频像调一个 API,Agent 拿到任务后改 JSON 即可。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器内运行 | 基于 Web 栈,无需下载安装客户端 |
| JSON 时间线 | 数据结构可读、可 diff、可程序化改写 |
| MCP / REST 双入口 | 既能被 Claude 通过 MCP 调,也能被 curl 走 REST |
| 实时预览 | Agent 改 JSON 画面同步更新 |
| 适合 agent pipeline | 多模态模型产出剪辑指令脚本可直接喂 |

## 媒体

![](https://pbs.twimg.com/media/HNJ5NICacAAkrNB.jpg)

## 参考链接

- [项目仓库](https://github.com/ronak-create/FableCut)

## 相关概念

- [Claude Real Video](./tool-claude-real-video.md) — 同样涉及「Agent 介入视频生产」的素材样本,可对比参考
