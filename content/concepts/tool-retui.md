---
type: "Tool"
title: "retui（subhasundardass/retui）"
description: "Go 写的终端 UI 框架,沿用 React 思路:函数式组件 + hooks 管状态,布局交给 flexbox,降低 TUI 开发心智。"
resource: "https://github.com/subhasundardass/retui"
tags: "[tui, terminal, go, react, hooks, flexbox]"
timestamp: "2026-07-15T01:27:00Z"
---

# retui

[retui](https://github.com/subhasundardass/retui) 是一套 Go 写的**终端界面框架**,借鉴 React 的心智模型:函数式组件 + hooks 管状态 + flexbox 布局。

## 它是什么

为 Go 程序员提供与 React 类似的 TUI 编程体验,把终端应用从「手动打印字符 + 处理光标」解脱到「声明式组件 + 布局描述」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 函数式组件 | 像写 React 一样写组件 |
| Hooks 管状态 | useState / useEffect 等状态原语 |
| Flexbox 布局 | 不用手动算坐标,声明式排版 |
| Go 单二进制 | 无 Node / 浏览器,产出单一可执行文件 |

## 适合什么场景

- 习惯了 React 的全栈 / 前端工程师,想用熟悉心智写 TUI。
- 内部运维工具 / CI 仪表盘不想上 Web,但又要交互体验。

## 媒体

![](https://pbs.twimg.com/media/HNHHIe0aMAAT1K1.jpg)

## 参考链接

- [项目仓库](https://github.com/subhasundardass/retui)

## 相关概念

- [HermitUI](./tool-hermitui.md) — 类似「把 React 风格带到另一介质」的 TUI/桌面框架,与本工具并列参考
- [NamethatUI / NavitUI / Plex-TUI](./tool-namethatui.md) — Go 生态里其他 TUI 工具样本
