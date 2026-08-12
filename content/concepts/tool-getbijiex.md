---
type: "Tool"
title: "GetbijiEx"
description: "把 Get笔记知识库中订阅博主（多为抖音）的全部笔记一键导出为 Markdown，并附带 Agent skill：装好后对 Claude Code、Codex 说一句话就能触发导出，免去手动整理的麻烦。"
resource: "https://github.com/Likely7/GetbijiEx"
tags: ["getbiji", "douyin", "export", "markdown", "agent-skill", "knowledge-migration"]
timestamp: "2026-08-12T11:29:00Z"
---

# GetbijiEx

[GetbijiEx](https://github.com/Likely7/GetbijiEx) 把 **Get笔记**（抖音系笔记应用）里订阅博主的内容一键导出为 Markdown，并附带 Agent skill——装好后对 Claude Code、Codex 说一句话就能触发导出。

## 它是什么

Get笔记的内容导出工具：解决"在抖音系笔记 App 里订阅了大量博主，但笔记 / 知识库"被锁"在 App 内、想搬到本地知识库"的问题。

## 为什么用它 / 适合什么场景

- **摆脱平台锁定**：把内容从 Get笔记导出成标准 Markdown。
- **批量导出**：一键导出所有订阅博主笔记。
- **Agent 友好**：附带 Agent skill，直接由 Claude Code / Codex 触发。
- **本地知识库迁移**：方便搬到 Obsidian / Logseq / OKF 等本地工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键导出 | 全量导出订阅博主笔记 |
| Markdown 输出 | 标准格式，本地工具可直接读 |
| Agent skill 配套 | Claude Code / Codex 一句话触发 |
| 抖音系覆盖 | 适配 Get笔记生态（含抖音） |
| 替代手动整理 | 免去逐条复制粘贴 |

## 参考链接

- [项目仓库](https://github.com/Likely7/GetbijiEx)

## 相关概念

- [Sparkfetch](./tool-sparkfetch.md) — 把任意 URL 杂乱 HTML 转成干净 Markdown / JSON，同属"内容格式转换 / 导出"工具
- [HTML2PDF / Sanzar](./tool-html2pdf-sanzar.md) — HTML→PDF 的离线管线，与 GetbijiEx 同属"本地转换、不依赖服务"思路