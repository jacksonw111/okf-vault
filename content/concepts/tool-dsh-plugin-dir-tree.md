---
type: Tool
title: "dsh-plugin-dir-tree（DSH 对话框工作区目录树浮窗）"
description: "bentong-chain 开源：在 DeepSeek Harness 对话界面以浮窗展示当前工作区的目录树，拖拽文件 / 文件夹即可把完整路径填入对话框，省去手动敲路径。"
resource: "https://github.com/bentong-chain/dsh-plugin-dir-tree"
tags: [dsh, deepseek-harness, plugin, file-tree, ux]
timestamp: 2026-08-21T07:22:00Z
---

# dsh-plugin-dir-tree（DSH 对话框工作区目录树浮窗）

## 它是什么
dsh-plugin-dir-tree 是一个 DeepSeek Harness 插件：在 dsh 的对话界面里以**浮窗**形式展示当前工作区的目录树，用户可以把文件 / 文件夹直接拖到对话框，路径自动填入——不用手动敲完整路径，也不用回到 OS 文件管理器里复制粘贴。

## 为什么用它 / 适合什么场景
- 长会话里反复让 agent 读 / 改多个文件，路径输入是高频操作。
- 项目目录深、文件名长容易打错，拖拽更稳。
- 想给 dsh 加一个「文件浏览器」交互但不想替换整个 dsh 桌面端。

## 关键能力
| 能力 | 说明 |
|------|------|
| 浮窗目录树 | 在 dsh 对话界面内弹出当前工作区结构 |
| 拖拽填路径 | 文件 / 文件夹拖到对话框即填入路径 |
| 插件化 | 作为 dsh 插件挂载，不改 dsh 主进程 |
| 即装即用 | 一行命令启动，无重配置 |

## 一句话总结
**给 DSH 对话框加一个「目录树浮窗」——文件直接拖进对话，不用再敲路径。**

## 原始链接
- [bentong-chain/dsh-plugin-dir-tree](https://github.com/bentong-chain/dsh-plugin-dir-tree) — 原始仓库

## 媒体
- ![目录树浮窗](https://pbs.twimg.com/media/HQNkzIYbkAALWbK.jpg)

## 相关概念
- [DSH Market](./concepts/tool-dsh-market.md) — DSH 内置插件市场
- [dsh-visualize](./concepts/tool-dsh-visualize.md) — DSH 可视化卡片插件