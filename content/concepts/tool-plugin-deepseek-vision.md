---
type: "Tool"
title: "Plugin-Deepseek-Vision（DeepSeek 多图理解插件）"
description: "DeepSeek 文本模型读不了 OpenAI Responses 请求里的 input_image；本插件在 CLIProxyAPI 里用宿主已有的视觉模型先把多张图转成文字分析，再交给 DeepSeek 推理。"
tags: "[deepseek, vision, multi-modal, cli-proxy-api, plugin]"
timestamp: "2026-08-15T12:23:00Z"
resource: "https://github.com/Zesuy/Plugin-Deepseek-Vision"
---

# Plugin-Deepseek-Vision（DeepSeek 多图理解插件）

## 它是什么

`Zesuy/Plugin-Deepseek-Vision` 是一个针对 [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) 的插件，解决问题：

- **DeepSeek 文本模型本身不识图**——OpenAI Responses 请求里的 `input_image` 字段对它无效。
- 客户端发来「带图对话」时，插件**先用宿主已有的视觉模型**（如 GPT-4o / Claude / 任意视觉模型）**把多张图转成文字描述**，再把纯文本交给 DeepSeek 文本模型推理。
- 模型回答时**视觉信息已被压缩成文字**，DeepSeek 能正常接着推理。

> ![](https://pbs.twimg.com/media/HPph1jcaEAAYamt.jpg)

## 为什么用它 / 适合什么场景

- **DeepSeek + 视觉场景**：业务用 DeepSeek 文本模型，又需要分析截图 / 图片。
- **不放弃 DeepSeek 优势**：用文字转译保留视觉信息，仍由 DeepSeek 给出最终答案。
- **可插拔**：基于 CLIProxyAPI 扩展，不改客户端调用方式。

## 关键能力

| 能力 | 说明 |
|------|------|
| `input_image` 自动转文字 | 截获 OpenAI Responses 请求里的图片字段 |
| 多图处理 | 多张图分别转文字描述后拼接 |
| 视觉模型复用 | 用宿主已有的视觉模型，无需额外接入 |
| DeepSeek 推理 | 转译后的纯文本交给 DeepSeek 文本模型 |
| 兼容 CLIProxyAPI | 插件形态，不改代理主流程 |
| 透明切换 | 客户端无需感知「视觉模型已被代理过」 |

## 工作机制

```
客户端发 OpenAI Responses 请求（含 input_image）
                ↓
       CLIProxyAPI 拦截
                ↓
Plugin-Deepseek-Vision 接管
                ↓
用宿主视觉模型把图片转文字描述
                ↓
文本 + 转译结果发 DeepSeek 文本模型
                ↓
返回 DeepSeek 推理结果
```

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| 直接用 DeepSeek 多模态版 | 切模型 | 受限于 DeepSeek 多模态能力 |
| 接 GPT-4o 直接分析 | 切模型 | 失去 DeepSeek 文本成本/中文优势 |
| **Plugin-Deepseek-Vision** | **保留 DeepSeek + 视觉前置** | **视觉信息转文字后由 DeepSeek 继续** |

## 适用人群

- CLIProxyAPI 用户。
- 想在 DeepSeek 上跑多模态任务、又不想换模型的开发者。
- 关注 DeepSeek 文本成本 / 中文能力、希望保留它做主推理的团队。

## 参考链接

- [项目链接](https://github.com/Zesuy/Plugin-Deepseek-Vision)

## 相关概念

- [DeepSeek MCP WebSearch](tool-deepseek-mcp-websearch.md) — 基于 DeepSeek API 的 MCP 联网搜索
- [DeepSeek SSD](tool-deepseek-ssd.md) — 与 DeepSeek 相关的另一工具