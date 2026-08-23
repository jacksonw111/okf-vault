---
type: Tool
title: "ssh-clipboard（SSH 点对点原生剪贴板同步工具）"
description: "Rust 写的跨设备剪贴板工具：文本、图片、文件、富文本通过持久化点对点 SSH 连接同步，走系统剪贴板 API，不开端口、不注册账号"
resource: "https://github.com/standardagents/ssh-clipboard"
tags: [ssh, clipboard, rust, p2p, cross-device]
timestamp: "2026-08-23T06:27:00Z"
---

# ssh-clipboard（SSH 点对点原生剪贴板同步工具）

## 它是什么

[standardagents/ssh-clipboard](https://github.com/standardagents/ssh-clipboard) 是一个 **Rust 写的跨设备剪贴板同步工具**：这台复制，那台粘贴，**文本、图片、文件、富文本都保持原生格式**。数据走**持久化的点对点 SSH 连接**，**不要中继服务器、不注册账号、不开新端口**。

它调的是 macOS `pasteboard` 和 Linux Wayland/X11 的**系统剪贴板**，不是终端里那种 escape sequence 模拟——所以 Finder 能直接粘贴文件，Raycast 这类剪贴板管理器也不受影响。

## 为什么用它 / 适合什么场景

- 多台电脑之间同步剪贴板，不想经过第三方服务器（中继 / 隐私风险）。
- 想要"系统级"剪贴板同步：图片、文件、富文本都能跨设备传递，不只是纯文本。
- 自带 SSH 环境即可使用，不引入额外账号、端口、中继。

## 关键能力

| 能力 | 说明 |
|------|------|
| 系统剪贴板 API | macOS pasteboard / Linux Wayland & X11，不是 escape 模拟 |
| 持久 SSH 连接 | 点对点直连，不经过中继 |
| 多格式同步 | 文本 / 图片 / 文件 / 富文本保持原生格式 |
| 零额外端口 | 直接复用 SSH，不在防火墙开新洞 |
| 零账号 | 用 SSH 密钥做身份认证 |

## 相关概念

- [Fallegji](./tool-fallegji.md) — 同样基于 P2P / E2EE 的去中心化通信工具
- [SimpleX Chat](./tool-simplex-chat.md) — 同样主张"无中心服务器"的隐私通讯

## 参考链接

- [项目链接](https://github.com/standardagents/ssh-clipboard)
