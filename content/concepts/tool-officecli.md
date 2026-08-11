---
type: "Tool"
title: "OfficeCLI（iOfficeAI/OfficeCLI）"
description: "把 Word / Excel / PowerPoint 的创建、读取、编辑压成一行命令,AI 智能体无需启动 Office 软件即可操作整套 Office 文档,Linux / macOS / Windows 三平台通用。"
resource: "https://github.com/iOfficeAI/OfficeCLI"
tags: "[office, cli, automation, ai-agent, docx, xlsx, pptx, cross-platform]"
timestamp: "2026-08-11T16:00:00Z"
---

# OfficeCLI

[OfficeCLI](https://github.com/iOfficeAI/OfficeCLI) 把 Word / Excel / PowerPoint 的**创建、读取、编辑压成一行命令**,AI 智能体不必再起 Office 软件或模拟点击,直接通过 CLI 操作整套 Office 文档。Linux / macOS / Windows 三平台通用。

项目链接：<https://github.com/iOfficeAI/OfficeCLI>

## 它是什么

Office 文档自动化 CLI:把 Office Open XML 格式(docx / xlsx / pptx)的解析与生成包成子命令,既能生成空白模板填数据,也能读现有文档做结构化抽取与改写。

## 为什么用它 / 适合什么场景

- **AI agent 流水线**:不需要 LibreOffice / Office GUI,Agent 直接调 CLI 改文档。
- **跨平台一致性**:同一套命令 Linux / macOS / Windows 行为一致。
- **批处理场景**:批量生成合同 / 报表 / 演示稿 / 抽取内容做摘要。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三件套覆盖 | Word / Excel / PowerPoint 的读 / 写 / 编辑 |
| 单命令 | 一行命令完成原本要打开 GUI 的事 |
| AI agent 友好 | 不依赖 Office 软件或模拟点击 |
| 跨平台 | Linux / macOS / Windows 同一套命令 |
| 结构化抽取 | 把现有文档解析成可程序化处理的数据 |
| 模板生成 | 支持模板填充,批量产出 |

## 参考链接

- [项目仓库](https://github.com/iOfficeAI/OfficeCLI)

## 相关概念

- [12-Factor Agents](./tool-12-factor-agents.md) — 把 agent 当工程产物设计的原则集,OfficeCLI 是"agent 调用外部工具"原则的具体落地