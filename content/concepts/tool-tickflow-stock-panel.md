---
type: "Tool"
title: "tickflow-stock-panel（A 股量化自托管工作台）"
description: "把选股、回测、监控、复盘、个股分析这些原本零散的 A 股量化工具整合成一个自托管工作台：行情看板 + 自选股 + 18 个内置策略 + 自定义信号 + AI 生成策略 + 指标流水线 + 回测 + 盘中监控 + 个股/财务/概念/行业分析 + 连板梯队 + AI 盘后复盘 + 第三方数据扩展。"
resource: "https://github.com/shy3130/tickflow-stock-panel"
tags: "[a-stock, quant, self-hosted, trading, strategy, backtest, dashboard]"
timestamp: "2026-07-08T15:30:00Z"
---

# tickflow-stock-panel

## 它是什么

[tickflow-stock-panel](https://github.com/shy3130/tickflow-stock-panel) 是一个**自托管的 A 股量化工作台**，把散户做量化时常需要拼凑的多套工具（行情、回测、监控、复盘、个股分析）整合到同一个 Web 应用里。

定位：**帮散户和量化爱好者把研究流程系统化**——不是 AI 荐股，而是把零散的选股 / 回测 / 监控 / 复盘环节串成一条流水线。

## 关键能力

| 模块 | 说明 |
|------|------|
| 行情看板 | A 股实时行情展示与盯盘 |
| 自选股 | 多组合管理 + 自选标的跟踪 |
| 内置策略 | 18 个开箱即用的策略模板 |
| 自定义信号 | 按需编写与触发自定义信号 |
| AI 生成策略 | 用 LLM 辅助生成新策略 |
| 指标流水线 | 自由组合技术指标 |
| 回测 | 在历史数据上验证策略 |
| 盘中监控 | 实时监控信号触发 / 异动 |
| 个股 / 财务 / 概念 / 行业分析 | 多维度基本面 + 概念板块分析 |
| 连板梯队 | 涨停板 / 连板股梯队展示 |
| AI 盘后复盘 | 由 AI 总结当日盘面 |
| 第三方数据扩展 | 接入外部数据源 |

## 适合谁

- 散户但想**系统化**做研究的量化爱好者。
- 已有零散脚本 / Excel 表，希望迁移到统一工作台的玩家。
- 想学习「策略 → 回测 → 监控 → 复盘」闭环的研究者。

## 媒体

![tickflow-stock-panel 工作台预览](https://pbs.twimg.com/media/HMeDC4cb0AErZwR.jpg)

## 参考链接

- [项目仓库](https://github.com/shy3130/tickflow-stock-panel)

## 相关概念

- [A 股数据 API](./tool-a-stock-data.md) — 同为 A 股行情 / 数据工具，但走「API / 数据源」路线
- [全球股票数据](./tool-global-stock-data.md) — 同为股票数据聚合，范围覆盖更广（含美股 / 港股）