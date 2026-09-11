---
type: "Tool"
title: "budget-tracker-tui（终端预算追踪器）"
description: "终端党友好的个人预算工具：SQLite 落盘 + decimal 精确算账，CSV 去重导入支持，日常收支记账没问题，投资估值与盘前盯盘看个乐。"
resource: "https://github.com/Feromond/budget-tracker-tui"
tags: "[finance, tui, sqlite, personal-budget, python]"
timestamp: "2026-09-11T22:05:00Z"
---

# budget-tracker-tui

## 它是什么

[Feromond/budget-tracker-tui](https://github.com/Feromond/budget-tracker-tui) 是**终端（TUI）党的个人预算追踪器**：本地 SQLite 落盘、`decimal` 类型精确算账、CSV 去重导入，专为日常收支记账设计；投资估值、盘前盯盘这类功能「看看就好」，不是主力用途。

## 为什么用它 / 适合什么场景

- 想用终端管个人 / 家庭日常收支，不想装 GUI 软件。
- 需要 `decimal` 精确算账（财务数字绝不能浮点漂移）。
- 已有 CSV 流水（银行导出 / 支付宝导出）想清洗后导入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端 TUI | 键盘操作，SSH 友好 |
| SQLite 落盘 | 本地数据库，无云依赖 |
| decimal 精确 | 财务数字无浮点漂移 |
| CSV 导入 | 去重导入已有流水 |
| 收支记账 | 日常场景够用 |
| 投资模块 | 估值 / 预测为辅助 |

## 参考链接

- 项目仓库：<https://github.com/Feromond/budget-tracker-tui>

## 媒体

- ![](https://pbs.twimg.com/media/HR0fU3DaIAAO6Gl.jpg)

## 相关概念

- [tickflow-stock-panel](./tool-tickflow-stock-panel.md) — 自托管 A 股量化工作台
- [stock-strategy-dashboard](./tool-stock-strategy-dashboard.md) — A股 / 美股短线波段本地只读工作台
- [a-stock-data](./tool-a-stock-data.md) — A 股数据 API
</content>
</invoke>