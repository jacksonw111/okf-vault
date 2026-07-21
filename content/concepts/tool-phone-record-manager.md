---
type: Tool
title: "phone-record-manager（手机号绑定关系管理器）"
description: "Windows 桌面工具（Python + PySide6 + SQLite）：登记每个手机号绑定过哪些网站 / App / 账号，手动跟踪换号进度，数据全在本机、不上云。"
resource: "https://github.com/NextWeb4/phone-record-manager"
tags: [windows, python, pyside6, sqlite, privacy, phone-number]
timestamp: "2026-07-21T15:37:00Z"
---

# phone-record-manager（手机号绑定关系管理器）

## 它是什么
[phone-record-manager](https://github.com/NextWeb4/phone-record-manager) 是一款 Windows 本地桌面工具：用 Python + PySide6 + SQLite 写成，专门用来登记 **每个手机号绑定了哪些网站 / App / 账号**，以及「换号」进行到了哪一步。数据完全存本地 SQLite，不上云，适合有隐私顾虑又想把账号 / 手机号关系摸清楚的人。

## 为什么用它 / 适合什么场景
- 准备换号 / 注销旧号，想知道哪些账号还绑着老号、哪些没换完。
- 同时持有多张卡 / 多个号，想统一记录各自的绑定清单。
- 不愿把「手机号 ↔ 账号」这种高度隐私信息交给任何云端服务。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地优先 | PySide6 + SQLite，所有数据在本机 |
| 绑定清单登记 | 每条记录：手机号 / 网站或 App / 账号 / 备注 |
| 换号进度跟踪 | 标记每条记录是否已迁移到新号 |
| 离线可用 | 无需联网，无云端依赖 |
| Windows 原生体验 | PySide6 桌面程序 |

## 相关概念
- [HermitUI](tool-hermitui.md) — 同样把隐私放在第一位的本地 AI 聊天界面（同类「本地优先」范式）

## 参考链接
- 项目链接: <https://github.com/NextWeb4/phone-record-manager>
