---
type: "Tool"
title: "QuackWrangler"
description: "QuackWrangler 把 DuckDB 内置进 VS Code 扩展：CSV / Parquet / JSON 等本地数据文件无需 Python 环境即可在 VS Code 里完成筛选、变换、聚合、合并与导出。"
resource: "https://github.com/mohsinsurani/quackwrangler"
tags: [duckdb, vscode, data, csv, parquet, etl, query]
timestamp: "2026-08-10T13:44:00Z"
---

# QuackWrangler

## 它是什么

[QuackWrangler](https://github.com/mohsinsurani/quackwrangler) 把**DuckDB 内置**进 VS Code 扩展，目标是解决「VS Code 里打开 CSV / Parquet / JSON 只能预览、没法直接做可视化清洗整理」的痛点。装好后**不需要任何 Python 环境**——DuckDB 直接跑，就能对本地数据文件做筛选、变换、聚合、合并与导出。

## 为什么用它 / 适合什么场景

- 经常在 VS Code 里随手打开 CSV / Parquet 看数据，但又希望直接做 SQL 清洗和聚合（不想为这点小事再开 Jupyter / DBeaver）。
- 不想为简单 ETL 装 conda / pandas / pyarrow——DuckDB 一个二进制搞定。
- 想给团队里「只想看数据 / 不会 Python」的同事一个熟悉界面里直接处理数据的工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内置 DuckDB | 无需 Python，单二进制 |
| 多格式支持 | CSV / Parquet / JSON 等本地文件 |
| SQL 优先 | 直接用 DuckDB SQL 做筛选 / 变换 / 聚合 |
| 跨表合并 | JOIN 多份本地数据集 |
| 数据导出 | 处理结果直接导出 |
| VS Code 整合 | 命令面板 / 侧栏 / 编辑器内多入口 |

## 媒体

![](https://pbs.twimg.com/media/HPUygzcaIAAQ1RX.jpg)

## 参考链接

- [项目仓库](https://github.com/mohsinsurani/quackwrangler)
- [原始链接](https://x.com/QingQ77/status/2086810799063097783)

## 相关概念

- [tabiew](./tool-tabiew.md) — Rust 写的 TUI 表格数据查看器，CSV / Parquet / JSON / Excel + SQL 查询，同属「DuckDB 系本地数据工具」
