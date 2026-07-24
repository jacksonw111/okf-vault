---
type: Tool
title: "pdfdown（浏览器内本地 PDF→Markdown）"
description: "把 PDF 扔进浏览器页面,直接拿到 Markdown。全程本地跑,不上传,不经过服务器。"
resource: "https://github.com/stephenturner/pdfdown"
tags: [pdf, markdown, converter, browser, local-first, privacy]
timestamp: "2026-07-24T00:00:00Z"
---

# pdfdown

[pdfdown](https://github.com/stephenturner/pdfdown) 是一个**浏览器内运行**的 PDF→Markdown 转换器——把 PDF 扔进页面，**直接在本地**拿到 Markdown 文本，**全程不经过服务器**。

## 它解决的问题

把 PDF 转成 Markdown，传统路径：
- 上传到云端 OCR 服务 → 数据出境 + 隐私风险 + 配额限制
- 装本地 OCR 工具 → 配置复杂、占用大

pdfdown 把这件事压到一个**打开即用**的浏览器页面里：
- 文件不出本机
- 不依赖云服务
- 转换结果就是干净的 Markdown，可直接喂给 Obsidian / AI / 编辑器

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器内运行 | 打开网页就可用 |
| 完全本地 | PDF 文件不离开本机 |
| 输出 Markdown | 直接得到干净 Markdown |
| 无需服务器 | 没有后端依赖 |
| 隐私友好 | 敏感合同 / 论文 / 内部资料都敢扔 |

## 适用场景

- 把内部合同 / 协议转 Markdown 进知识库
- 把论文 PDF 转 Markdown 喂给 AI 总结
- 临时拿到一份 PDF 又不想装客户端

## 参考链接

- 项目仓库: <https://github.com/stephenturner/pdfdown>

## 媒体

![](https://pbs.twimg.com/media/HN9RBSvakAE-uJO.jpg)

## 相关概念

- [MarkdownReader](tool-markdown-reader-windows.md) — Windows 上的轻量 Markdown 编辑器，本工具是其「输入侧」伙伴
- [obsidian-knowledge-agent](tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道把 PDF / 论文自动整理为 Obsidian 笔记，pdfdown 可作为其转换环节