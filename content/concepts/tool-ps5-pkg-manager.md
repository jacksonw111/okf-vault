---
type: "Tool"
title: "ps5-pkg-manager（PS5 USB/SMB/光盘 pkg 流式安装）"
description: "在 PS5 上装 pkg 时，原方案要把包拷进内部存储（一份原始包 + 一份装完的文件，空间翻倍），SMB 共享与光盘还读不进去。ps5-pkg-manager 自己起一个 HTTP range 流服务，用虚拟 HTTP range 流把 USB / SMB / 光盘里的包直接喂给系统安装器。"
resource: "https://github.com/itsPLK/ps5-pkg-manager"
tags: "[ps5, pkg, http-range, streaming, install, homebrew]"
timestamp: "2026-09-21T22:00:00Z"
---

# ps5-pkg-manager

## 它是什么

[itsPLK/ps5-pkg-manager](https://github.com/itsPLK/ps5-pkg-manager) 解决 PS5 上 pkg 安装的**存储与介质限制**。

### 原方案的痛点

- 把 pkg 包先**拷进内部存储**——一份原始包 + 一份装完的文件，空间直接翻倍。
- **SMB 共享**与**光盘**里的 pkg，系统安装器读不进去。

### 它的做法

自己起一个 **HTTP range 流服务**，用**虚拟 HTTP range 流**把 USB / SMB / 光盘里的包直接喂给 PS5 的系统安装器。

## 为什么用它 / 适合什么场景

- pkg 包大到不想复制到内部存储时，**就地流式安装**。
- 包存放在外置 USB 盘 / SMB 共享 / 光盘上时，**绕过系统安装器的介质白名单**。
- 想**省一半内部存储**（不再需要原始包 + 解包后文件并存）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自起 HTTP range 服务 | 把任意介质的 pkg 包装成 HTTP range 流 |
| 多介质兼容 | USB、SMB 共享、光盘均可作为源 |
| 不复制到内部存储 | 包留在源介质上，安装器按需拉取 |
| 系统安装器对接 | 走 PS5 官方的 pkg 安装协议 |

## 项目链接

- 仓库：<https://github.com/itsPLK/ps5-pkg-manager>

## 媒体

![](https://pbs.twimg.com/media/HSodmojb0AAZp8q.jpg)

## 相关概念
