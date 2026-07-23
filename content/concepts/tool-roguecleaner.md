---
type: "Tool"
title: "RogueCleaner（Windows 流氓软件残留清理）"
description: "aakk007/RogueCleaner，扫描 Windows 上流氓软件乱塞的右键菜单 / 开机启动 / 后台服务 / 计划任务 / 浏览器插件 / 文件关联残留；清之前备份、清完复扫、可批次恢复。"
resource: "https://github.com/aakk007/RogueCleaner"
tags: "[windows, cleanup, anti-malware, rogue-software, system-recovery]"
timestamp: "2026-07-23T10:49:00Z"
---

# RogueCleaner（Windows 流氓软件残留清理）

## 它是什么

[`aakk007/RogueCleaner`](https://github.com/aakk007/RogueCleaner) 是 Windows 端的「**流氓软件残留清理工具**」——专门扫描 / 清理那些 Windows 上流氓软件、捆绑安装包、卸载不干净的应用在系统各处留下的「钉子」。

## 它清理什么

| 残留类型 | 典型表现 |
|------|------|
| 右键菜单 | 卸载后右键菜单还在的项 |
| 开机启动 | 卸载后开机自启的进程 |
| 后台服务 | 卸载后还在跑的服务 |
| 计划任务 | 卸载后定时触发的任务 |
| 浏览器插件 | 卸载后还在劫持首页的扩展 |
| 文件关联 | 卸载后还强行改写默认打开方式 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 扫描 | 自动识别流氓软件残留 |
| 备份 | 清理前先备份，避免误删 |
| 复扫 | 清完后再扫一遍确认干净 |
| 批次恢复 | 误删后可一次性恢复 |

## 为什么用它

- **Windows 通病**：装 / 卸软件频繁后，系统被各种「半卸载」状态污染
- **不像杀毒软件**：专精「清理残留」而非「查杀病毒」
- **可逆操作**：备份 + 批次恢复兜底，新手也不怕

## 适用场景

- 经常装 / 卸国产 / 免费软件的用户
- 二手电脑到手后「重置」环境
- 怀疑系统被流氓软件劫持

## 相关概念

- [Kudu](./tool-kudu-cleaner.md) — 同类跨平台系统清理，但偏通用清理而非流氓残留
- [WinTrash](./tool-wintrash.md) — Windows 单 .ps1 扫 18 类系统残留

## 原始链接

- [项目仓库](https://github.com/aakk007/RogueCleaner)