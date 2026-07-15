---
type: "Tool"
title: "mimic（littledivy/mimic）"
description: "系统级进程拦截工具,拦截任意应用进程后像调用 Python 库一样调用它,让 CLI 工具和 GUI 应用都成为可编程 API。"
resource: "https://github.com/littledivy/mimic"
tags: "[process-interception, ffi, python-call, automation, system-tool]"
timestamp: "2026-07-15T11:16:23Z"
---

# mimic

[mimic](https://github.com/littledivy/mimic) 是一个**系统级进程拦截工具**——拦截任意应用进程,像调用 Python 库一样调用它,让 CLI 工具和 GUI 应用**变成可编程 API**。

## 它解决了什么

很多老牌 CLI / GUI 程序没有 SDK、没有 API,只能「起进程 + 截屏 + 模拟键鼠」。mimic 把它们的进程侧拉一层 Python 接口,**已运行的进程也能被挂钩**,反向把黑盒程序的能力暴露成 call-able 的函数。

## 关键能力

| 能力 | 说明 |
|------|------|
| 任意进程挂钩 | 不需要源码,挂上去就能用 |
| Python 调用模型 | 像 import 一个库那样调子 |
| CLI / GUI 通吃 | 不区分命令行还是图形界面 |
| 创意系统工具 | 把没法程序化的工具变成可程序化 |

## 参考链接

- [项目仓库](https://github.com/littledivy/mimic)

## 相关概念

(无清晰相关概念,单飞)
