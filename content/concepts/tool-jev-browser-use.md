---
type: "Tool"
title: "jev-browser-use（无障碍树驱动的浏览器操作）"
description: "把点击交给每百万输入 token $0.042 的便宜模型、Codex 只留打字和验收——这套分工能砍掉每步一轮主模型的账单。但它只吃无障碍树，canvas / iframe / 拖拽 / 上传全得自己接回去。"
resource: "https://github.com/wy-coliney/jev-browser-use"
tags: "[browser-use, accessibility-tree, jev, cost, codex, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# jev-browser-use（无障碍树驱动的浏览器操作）

## 它是什么

[jev-browser-use](https://github.com/wy-coliney/jev-browser-use) 是一个浏览器自动化工具：把「点击 / 选元素」交给每百万输入 token $0.042 的便宜模型（jev），Codex 等主模型只保留「打字 / 验收」。这套分工能砍掉每步一轮主模型的 token 账单。

## 关键设计

| 元素 | 说明 |
|------|------|
| 输入 | 仅吃无障碍树（accessibility tree） |
| 点击 / 选元素 | 便宜模型（jev）负责 |
| 打字 / 验收 | Codex 等主模型 |
| 计费优化 | 主模型只参与打字 + 验收，省 token |

## 适用与限制

- ✅ 元素能靠 name 点中的标准页面：大幅省钱
- ❌ canvas / iframe / 拖拽 / 上传：得自己接回去
- ⚠️ 「省下来的是操作时间还是调试时间」取决于页面里有多少元素能靠名字点中

## 适用场景

- 想用便宜模型做浏览器点击，主模型只做关键判断
- 已经在用 Codex + 想压低主模型账单
- 元素命名规范的页面（多数 SaaS / 工具类）

## 原始链接
- 项目主页：<https://github.com/wy-coliney/jev-browser-use>

## 相关概念
- [Astra-Ares](./tool-astra-ares.md) — 同思路：在 Codex 旁用便宜模型做档位路由
- [fast-browser-use](./tool-fast-browser-use.md) — 另一个本机 / 便宜的浏览器自动化方案