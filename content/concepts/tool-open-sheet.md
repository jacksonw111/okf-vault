---
type: Tool
title: "Open-Sheet"
description: "让 Agent 写电子表格时不碰单元格坐标：模型写成 React，公式按名字引用，最后由框架解析为 A1 并导出带活公式的 .xlsx。"
resource: "https://github.com/lianghsun/open-sheet"
tags: [agent, spreadsheet, excel, react, xlsx, llm]
timestamp: "2026-08-24T15:19:00Z"
---

# Open-Sheet

## 它是什么

[lianghsun/open-sheet](https://github.com/lianghsun/open-sheet) 是给 LLM 写电子表格设计的中间层框架：模型不再直接生成 `B7`、`A1:C3` 这种单元格坐标，而是写成一份**带名字引用**的 React 组件，最后由框架统一解析成 A1 语法并导出带活公式的 `.xlsx`。

## 为什么用它 / 适合什么场景

- Agent 写分析文案很强，但写电子表格总是出错：数错表头行、插一行后整片 `B7` 引用悄悄失效。
- 想给 LLM 一个「按语义引用」写表格的方式：`Revenue / Cost / Profit` 这种名字而不是坐标。
- 想要输出仍是普通 .xlsx，能在 Excel / WPS / Numbers 里正常打开且公式联动。

## 关键能力

| 能力 | 说明 |
|------|------|
| 名字引用 | 模型按列名 / 字段名引用单元格，自动映射为 A1 |
| React 描述 | 模型产出 React JSX / TSX，工具人友好 |
| 自动坐标转换 | 框架把名字引用编译成合法 A1 语法 |
| 活公式输出 | 导出的 .xlsx 保留公式，可在 Excel / WPS 中联动修改 |
| 插入安全 | 行列插入后再编译不会让引用悄悄失效 |

## 相关概念

- [Spreadsheet AI 评测](./note-ai-agent-book-chemark.md) — 评测 Agent 写电子表格能力的基准
- [OfficeCLI](./tool-officecli.md) — 同类「AI 操作 Office」思路

## 参考链接

- [项目链接](https://github.com/lianghsun/open-sheet)
- ![](https://pbs.twimg.com/media/HQdA4XYbIAAGe5p.jpg)