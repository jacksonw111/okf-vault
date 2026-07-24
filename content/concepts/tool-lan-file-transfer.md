---
type: Tool
title: "lan-file-transfer（局域网文件共享桌面工具）"
description: "Windows 桌面文件共享工具,Tkinter 启动 FastAPI 后端,同局域网设备通过浏览器访问。支持游客 / 普通用户 / 管理员三层权限,文件按用户组分可见范围,所有操作都有审计日志。"
resource: "https://github.com/NextWeb4/lan-file-transfer"
tags: [lan, file-sharing, desktop, fastapi, tkinter, windows]
timestamp: "2026-07-24T00:00:00Z"
---

# lan-file-transfer

[lan-file-transfer](https://github.com/NextWeb4/lan-file-transfer) 是一款**Windows 桌面文件共享工具**——TUI/Tkinter 启个 FastAPI 后端，**同局域网**设备通过浏览器就能访问，**不需要自建服务器**也不需要走第三方云。

## 它解决的问题

局域网互传文件，传统痛点：

| 路径 | 痛点 |
|------|------|
| 自建文件服务器 | 部署 / 维护成本高 |
| 微信 / 网盘 / AirDrop | 数据过第三方之手，隐私风险 + 大文件限速 |
| 共享文件夹 | 没权限控制、没审计、跨平台差 |

lan-file-transfer 的设计取舍：
- **不走云**：纯局域网内，数据不出公司 / 家庭网
- **三层权限**：游客 / 普通用户 / 管理员
- **审计日志**：每个文件操作都留痕
- **Web 入口**：被访问方用浏览器就行，不必每台机器都装客户端

## 关键能力

| 能力 | 说明 |
|------|------|
| Tkinter 桌面端 | Windows 上 GUI 启停 |
| FastAPI 后端 | 提供 HTTP 文件服务 |
| 浏览器访问 | 同局域网设备用浏览器即可 |
| 三层权限 | 游客 / 普通用户 / 管理员 |
| 用户组可见性 | 文件按用户组分可见范围 |
| 审计日志 | 所有操作可追溯 |
| 无需云 | 数据全在局域网 |

## 适用场景

- 小团队 / 工作室内部传大文件
- 家庭内多设备共享资料
- 想给「共享文件夹」加权限与审计

## 参考链接

- 项目仓库: <https://github.com/NextWeb4/lan-file-transfer>

## 相关概念

- [SafeBucket](tool-safebucket.md) — Go + React 写的预签名 URL 直传直下，文件不经服务器中转，本工具是「局域网直传」互补方案
- [kodbox](tool-kodbox.md) — 浏览器即云端 OS 的开源 Web 文件管理器，万物皆可挂载，Web 入口思路一致