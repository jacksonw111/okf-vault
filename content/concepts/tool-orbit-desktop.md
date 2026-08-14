---
type: "Tool"
title: "orbit-desktop"
description: "23aneessss 开源的本地优先 macOS 工作区：把习惯 / 想法 / 任务 / 可视工作流 / 人脉跟进收进同一应用，数据只存本机；画布模块用 SwiftUI 原生复刻 React Flow。"
resource: "https://github.com/23aneessss/orbit-desktop"
tags: ["macos", "swiftui", "local-first", "habits", "tasks", "canvas", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# orbit-desktop

## 它是什么
orbit-desktop 是一款本地优先的 macOS 工作区，把「散在多个 App」的能力收进同一处：习惯打卡（52 周热力图 + 每日勾选）、想法笔记、任务（列表 + 空间看板双视图）、可视化工作流（拖拽节点 + 贝塞尔连线 + 重叠合并）、人脉跟进。数据全部存本机，不依赖云服务。画布模块用 SwiftUI 原生复刻 React Flow：节点按世界坐标存、用真 SwiftUI View 渲染，网格、连线、连接预览和笔迹全部走 SwiftUI Canvas，不嵌 WebView、不引 React。

## 为什么用它 / 适合什么场景
- 已经受够了 Notion / Tana / Obsidian + Things + Habitica + 各种画布 App 反复切。
- 想要「一个原生 App 管这些事」且数据完全在自己 Mac 上的本地优先用户。
- macOS 偏好 SwiftUI 原生体验，不想再开一个 Electron 巨物。

## 关键能力
| 能力 | 说明 |
|------|------|
| 习惯 | 52 周热力图 + 每日勾选 |
| 任务 | 列表 + 空间看板双视图 |
| 画布 | SwiftUI 原生（世界坐标 / Canvas 绘制） |
| 人脉跟进 | 内置模块 |
| 数据 | 本地优先 |

## 媒体

界面截图：![界面截图](https://pbs.twimg.com/media/HPkYOLZbUAA2FkJ.jpg)

## 相关概念
- [LifeOS](./tool-lifeos.md) — 给 Claude Code / Cursor 等编码代理加外挂的 TELOS + 七段算法循环框架，与 orbit-desktop 在「个人工作区」概念上互补（orbit-desktop 偏个人 GUI，LifeOS 偏 Agent 工作流）
- [Niamos](./tool-niamos.md) — Obsidian 第二大脑模板，orbit-desktop 是 macOS 原生路线
- [Pinvou Agent](./tool-pinvou-agent.md) — 聊天 / 设计 / 写代码收进同一个桌面工作台，与 orbit-desktop 同属「桌面多功能聚合」
