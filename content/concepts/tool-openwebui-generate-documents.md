---
type: Tool
title: "Open WebUI Generate Documents"
description: "ianustec 开源的 Open WebUI 工具，用 python-docx 把模型产出的 Markdown（含 YAML 头）或 JSON 规范直接生成为原生、可编辑的 Word（.docx）文档。"
resource: "https://github.com/ianustec/openwebui-generate-documents"
tags: "[open-webui, docx, word, document, llm-output]"
timestamp: "2026-07-11T20:00:00Z"
---

# Open WebUI Generate Documents

## 它是什么

`ianustec/openwebui-generate-documents` 是一个 **Open WebUI 工具函数**，把模型输出的内容**直接转成原生、可二次编辑的 Word `.docx`**。

输入两种格式都行：

- **Markdown**（含 YAML 头）——把 YAML 当 frontmatter、把 Markdown body 转 docx。
- **JSON 规范**——按 JSON schema 结构化转 docx。

底层用 `python-docx` 写真正的 `.docx`（不是 HTML → Word），所以生成的文件**可以被 Word / WPS / Pages 正常二次编辑**。

## 为什么用它 / 适合什么场景

- 让 LLM 直接出 Word 文档，而不是 Markdown / HTML 还得手工复制。
- 写报告 / 合同 / 公文时需要可编辑的 `.docx`，不是 PDF / 图片。
- Open WebUI 用户想在对话里直接调「把上面这段生成 Word 给我」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生 .docx | 用 python-docx 写真正可编辑的 Word |
| Markdown 输入 | 支持 YAML frontmatter |
| JSON 输入 | 支持结构化 JSON schema |
| Open WebUI 工具函数 | 作为 Open WebUI 的工具注册 |

## 媒体参考

- 项目截图：

![Open WebUI Generate Documents](https://pbs.twimg.com/media/HM1_OeDawAACpgS.jpg)

## 相关概念

- [Markdown Desktop Browser](tool-markdown-desktop-browser.md) — 另一款把 Markdown 转其他格式的工具
- [Lengyi Markdown Editor](tool-lengyi-markdown-editor.md) — 纯前端单 HTML 文件 Markdown 编辑器

## 项目链接

- 项目仓库：<https://github.com/ianustec/openwebui-generate-documents>