---
type: Tool
title: "xianyu-super-butler"
description: "闲鱼店铺管理平台：自动回复、AI 议价、自动发货、多账号管理、订单批量刷新，性能经浏览器实例池优化提速 5 倍。"
resource: "https://github.com/Mxucc/xianyu-super-butler"
tags: "[xianyu, ecommerce, automation, multi-account, browser-automation]"
timestamp: "2026-06-29T16:00:00Z"
---

# xianyu-super-butler

## 它是什么
xianyu-super-butler（闲鱼超级管家）是一款面向闲鱼卖家的开源店铺管理平台，提供现代化商务风 UI 和完整的自动化能力：关键词触发自动回复、AI 议价、多规格自动发货、订单列表批量刷新、多账号管理（扫码 / 密码 / Cookie 三种登录方式）、数据统计与 Excel 导入导出。

![](https://pbs.twimg.com/media/HL8kFOYb0AAbXYu.jpg)

## 为什么用它 / 适合什么场景
- **多账号卖家**：扫码 / 密码 / Cookie 三种登录方式并存，浏览器实例池避免账号间互相干扰。
- **想睡觉时还在成交**：关键词自动回复 + AI 议价 + 自动发货三件套，覆盖买家从问价到拍下到收货前咨询的常见节点。
- **订单太多刷不过来**：批量刷新 + 数据统计 + Excel 导出，方便盘库与对账。

## 关键能力
| 能力 | 说明 |
|------|------|
| 关键词自动回复 | 配置触发词自动回复 |
| AI 议价 | 大模型判断买家出价是否接受 |
| 多规格自动发货 | 不同 SKU 绑定不同发货内容 |
| 订单批量刷新 | 浏览器实例池提速 5 倍 |
| 多账号管理 | 扫码 / 密码 / Cookie 三种登录方式 |
| 数据统计 | 订单 / 销售 / 库存可视化 |
| Excel 导入导出 | 批量操作与对账 |

## 性能 / 风控
- 浏览器实例池 + 并发处理，让批量刷新提速约 5 倍
- 多账号同时在线仍要遵守闲鱼平台规则，避免风控

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071553263485513868)
- [项目链接](https://github.com/Mxucc/xianyu-super-butler)

## 相关概念
- [MediaCrawler](./tool-mediacrawler.md) — 同样是 Playwright 驱动的多平台自动化工具，定位在采集而非店铺管理
- [Obscura](./tool-obscura-headless-browser.md) — 反检测无头浏览器，自动化场景的底层依赖选项之一