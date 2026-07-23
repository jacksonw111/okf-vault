---
type: "Tool"
title: "CmdBox（带别名 / 变量 / 标签的命令存储 + 快速执行工具）"
description: "PhantomLambSoft/CmdBox，给 shell 历史里翻不到、笔记里搜不到的命令组合一个「带别名 + 变量替换 + 标签分类」的本地存储与快速执行工具，让终端用户只记缩写就能跑复杂命令。"
resource: "https://github.com/PhantomLambSoft/CmdBox"
tags: "[cli, terminal, command-palette, alias, productivity]"
timestamp: "2026-07-23T06:36:00Z"
---

# CmdBox（带别名 / 变量 / 标签的命令存储 + 快速执行工具）

## 它是什么

[`PhantomLambSoft/CmdBox`](https://github.com/PhantomLambSoft/CmdBox) 解决「**终端用户记不住复杂命令 / 懒得翻 shell 历史**」的痛点——把命令当成「可复用的 snippet」存进本地仓库，配上别名、变量替换、标签分类，需要时秒级调出执行。

## 关键能力

| 能力 | 说明 |
|------|------|
| 别名 | 把一长串命令缩写成一个短词，如 `gpl` → `git pull origin $(current-branch)` |
| 变量替换 | 在执行时按提示填入变量，避免每次手改命令 |
| 标签分类 | 按用途打标签（git / docker / network），快速筛选 |
| 快速执行 | 不离开当前 shell，弹层式选择并执行 |
| 本地存储 | 命令库完全在用户本机 |

## 为什么用它

- **跨主机可移植**：把命令库带回家 / 公司 / 服务器
- **告别搜索效率低**：不再到处翻笔记 / 浏览器历史
- **降低命令编写错误**：变量替换避免拼写错误
- **可分享**：团队可共享一套 CmdBox 仓库作为内部命令规约

## 适用场景

- 运维 / SRE 日常巡检命令
- 开发人员常用的构建 / 测试 / 部署命令
- 数据分析师的 ETL / 数据库查询
- 需要在多台机器间保持命令习惯一致的人

## 媒体

视频：[CmdBox 演示](https://video.twimg.com/amplify_video/2079817757374492673/vid/avc1/854x462/bOPnew_QvMoljO2F.mp4?tag=29)

## 相关概念

- [Tork](./tool-tork.md) — 同类「终端里的工具箱」，但聚焦 BT / ISO 下载
- [Aether Android Agent](./tool-aether-android-agent.md) — 终端里跑 AI 代理，但走自然语言
- [LS / Nushell 类工具](./tool-nls.md) — 现代化的 `ls` 替代，提升终端体验

## 原始链接

- [项目仓库](https://github.com/PhantomLambSoft/CmdBox)