---
type: "Tool"
title: "DocJev"
description: "用模型判断把混在一起的 PDF / DOCX 拆成多份单文件——分类规则由用户写成 YAML，模型识别文档边界与混入页面，切出来的段可直接导成单份 PDF。"
resource: "https://github.com/jerryjliu/docjev"
tags: "[pdf, docx, document-splitting, llm, jev, open-source]"
timestamp: "2026-09-23T22:30:00Z"
---

# DocJev

## 它是什么

[DocJev](https://github.com/jerryjliu/docjev) 是一个**基于模型的文档拆分工具**：

> 一堆 PDF、DOCX 混着来的时候，得先弄清谁属于哪类，哪几页是从别处接上来的另一份文件。DocJev 把这份判断交给模型，规则你自己写成 YAML，切出来的段还能直接导成单份 PDF。

## 为什么用它 / 适合什么场景

- 客户 / 行政送来「**一堆 PDF 拼一起**」的合并文件，需要拆回原件。
- 想用**自定义 YAML 规则**控制分类逻辑（不必依赖写死的内置类型）。
- 需要在拆分同时判断**哪些页是从别处接进来的**（混合页面检测）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | PDF / DOCX 混排 |
| 规则 | 用户自写 YAML（分类逻辑可定制） |
| 拆分 | 自动切分单文件并导出为独立 PDF |
| 混合检测 | 识别「哪几页是从别处接上来的」 |

## 项目链接
- 项目主页：<https://github.com/jerryjliu/docjev>

## 媒体
![DocJev 截图 1](https://pbs.twimg.com/media/HSyi8_0b0AEBJvP.jpg)
![DocJev 截图 2](https://pbs.twimg.com/media/HSyi92qbkAAslXw.jpg)
