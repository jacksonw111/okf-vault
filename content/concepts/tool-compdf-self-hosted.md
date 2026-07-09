---
type: Tool
title: "ComPDFKit Self-Hosted（企业可私有化 PDF 编辑与转换平台）"
description: "一套可私有化部署的开源 PDF 编辑与格式转换平台，企业在自家服务器上即可处理文档和图片。"
resource: "https://github.com/ComPDFKit/compdf-self-hosted"
tags: "[pdf, self-hosted, enterprise, document, format-conversion]"
timestamp: "2026-07-09T20:50:00Z"
---

# ComPDFKit Self-Hosted（企业可私有化 PDF 编辑与转换平台）

## 它是什么
`ComPDFKit/compdf-self-hosted` 是 **ComPDFKit** 团队开源的**私有化部署版 PDF / 文档处理平台**：

- **完全自托管**：跑在企业自家服务器 / 私有云
- **PDF 编辑**：注释 / 表单 / 签名 / 拆分 / 合并
- **格式转换**：PDF ↔ Word / Excel / PPT / 图片 / HTML 等互转
- **图片处理**：嵌入到 PDF 工作流

## 为什么用它 / 适合什么场景
- 公司不允许把**敏感文档**传到云端 PDF 服务。
- 想用一套**统一 SDK / 服务**支撑多个内部系统的 PDF 操作。
- 适合：金融 / 医疗 / 法律 / 政企——任何对文档机密性有强合规要求的场景。
- 对比 SaaS PDF 服务（Adobe / Smallpdf / iLovePDF）：自托管 + 数据不出局域网。

## 关键能力
| 能力 | 说明 |
|------|------|
| 私有化部署 | 一键 docker compose 起服务 |
| PDF 编辑 | 注释 / 表单 / 签名 / 拆分 / 合并 |
| 格式转换 | PDF ↔ Office / 图片 / HTML 等 |
| 图片处理 | 集成图片到 PDF 工作流 |
| SDK 完整 | 多个语言 + 后端 API |
| 自托管 | 数据不出自家机房 |

## 媒体参考

界面截图：
- ![](https://pbs.twimg.com/media/HMrN7aCa4AEkCEj.png)

## 相关概念
- [Obsidian Knowledge Agent](tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道把 PDF / 论文自动整理为 Obsidian 笔记（输入侧 PDF 处理的对端）
- [LawLink](tool-lawlink.md) — 中小律所开源自部署案件管理（同样强合规 PDF 场景）
- [Clarify](tool-clarify.md) — 面向 MDX + OpenAPI 的开源文档发布工具

## 参考链接
- 项目链接：<https://github.com/ComPDFKit/compdf-self-hosted>
