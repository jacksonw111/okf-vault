---
type: "Tool"
title: "paperless-brain（Vailsen/paperless-brain）"
description: "给 Paperless-ngx 加上一层 AI 大脑：原本只能分类检索文档，现在可以直接跟存档对话——问问题、提取截止日期、写信、做研究。"
resource: "https://github.com/Vailsen/paperless-brain"
tags: "[paperless-ngx, document-archive, ai-rag, qa, email-assist, retrieval]"
timestamp: "2026-07-31T20:30:00Z"
---

# paperless-brain（Vailsen/paperless-brain）

[paperless-brain](https://github.com/Vailsen/paperless-brain) 给 **Paperless-ngx**（流行的自托管文档归档工具）**加一层 AI 大脑**：原本只能「分类 + 检索」文档，现在可以**直接跟存档对话**——问问题、提取截止日期、起草邮件、做研究。

## 它是什么

- 在 Paperless-ngx 之上接 AI 后端
- 让归档的纸质 / PDF 文档变成可对话的知识库
- 支持 RAG 风格问答与任务型操作（提截止日期、写信）

## 为什么用它 / 适合什么场景

| 痛点 | paperless-brain 怎么解 |
|------|-----------------------|
| 自托管 PDF 归档里信息查找慢 | 直接对存档问问题 |
| 截止日期 / 关键条款要逐个文档翻 | AI 自动提取并按时间排序 |
| 写邮件要翻多份文档引证据 | AI 起草 + 直接引用存档 |
| 自托管 + 私域文档 | 不外送上云，AI 在本地跑或通过安全通道调 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 自然语言问答 | 直接对存档问问题 |
| 截止日期提取 | 从票据 / 合同等文档中抽取 |
| 写信 / 报告 | 基于存档内容起草 |
| 研究助手 | 多文档交叉问答 |
| 隐私友好 | 接本地模型或自托管推理 |

## 相关概念

- [Tasogare](./tool-tasogare.md) — 网页阅读器 + MCP，给单本书配 AI；paperless-brain 是整个文档归档接 AI
- [CCSessions](./tool-ccsessions.md) — 浏览 / 预览 Claude Code 终端会话；paperless-brain 用类似思路做 AI 与文档对话
- [OpenBrowser](./tool-openbrowser.md) — 浏览器自动化框架，与 paperless-brain 配合可自动归档网络文档
- [Toolcraft](./tool-toolcraft.md) — 创意类应用 starter kit，paperless-brain 思路可借
