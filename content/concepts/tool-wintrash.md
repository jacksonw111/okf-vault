---
type: "Tool"
title: "WinTrash（hasoftware/WinTrash）"
description: "单 .ps1 脚本,扫描 Windows 里 18 类残留——死 PATH、孤儿文件夹、幽灵服务、坏注册表、启动项、代理工具塞的自签根证书等,一键定位系统垃圾。"
resource: "https://github.com/hasoftware/WinTrash"
tags: "[windows, cleanup, powershell, maintenance, forensics]"
timestamp: "2026-07-15T11:19:00Z"
---

# WinTrash

[WinTrash](https://github.com/hasoftware/WinTrash) 就**一个 .ps1 文件**,扫 Windows 里 18 类残留:死 PATH、孤儿文件夹、幽灵服务、坏注册表、启动项、代理工具塞的自签根证书等。

## 它解决了什么

Windows 用久了系统里会塞一堆历史残留:卸了但路径还在 PATH 的旧工具、被替换但注册表还在的旧服务、各种代理工具(Z / clash / v2rayN)装完没清的自签根证书。手工一项项查太累;完整清理工具又会把有用的目录杀掉。WinTrash 只扫不删,先把可疑项报给你。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单 .ps1 | 没有外部依赖,管理员 powershell 直接跑 |
| 18 类扫描 | PATH / 孤儿目录 / 服务 / 注册表 / 启动项 / 根证书等 |
| 只读不删 | 默认报告不销毁,操作员决定 |
| 代理残留识别 | 特别针对代理工具留下的自签根证书清理 |

## 媒体

![](https://pbs.twimg.com/media/HNJ01aLbAAAm1dH.jpg)

## 参考链接

- [项目仓库](https://github.com/hasoftware/WinTrash)

## 相关概念

(无清晰相关概念,单飞)
