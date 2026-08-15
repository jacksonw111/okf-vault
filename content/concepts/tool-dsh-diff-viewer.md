---
type: "Tool"
title: "dsh-diff-viewer（DSH PiUI 风格 diff 查看器）"
description: "把 DSH Web GUI 里 write/edit 调用的 diff 显示，换成更顺眼的 PiUI 风格查看器。纯插件，靠 ui-tool 的 keyed 接管把 edit/write 的 diff 渲染换成自定义组件，不碰核心代码，卸载就恢复原样。"
tags: "[dsh, diff-viewer, plugin, ui-tool, piui]"
timestamp: "2026-08-15T10:42:00Z"
resource: "https://github.com/lehhair/dsh-diff-viewer"
---

# dsh-diff-viewer（DSH PiUI 风格 diff 查看器）

## 它是什么

`lehhair/dsh-diff-viewer` 是 DSH（一个 AI 编码代理 Web GUI）的**纯插件**，把 DSH 内 `write` / `edit` 工具调用产生的 diff 视图，从默认的渲染换成更顺眼的 PiUI 风格查看器。

实现方式是利用 DSH 的 `ui-tool` 扩展点的 `keyed` 接管机制——把这两个工具的 diff 渲染换成自定义组件，**不修改 DSH 核心代码**，卸载即恢复原状。

> ![](https://pbs.twimg.com/media/HPvLHzNbcAANMQu.jpg)

## 为什么用它 / 适合什么场景

- **改 diff 体验**：DSH 默认 diff 视图偏简陋，PiUI 风格更好读。
- **零侵入**：是插件不是 fork，DSH 升级不影响本插件。
- **可逆**：不想用就卸载，UI 立刻回到默认。

## 关键能力

| 能力 | 说明 |
|------|------|
| 接管 `write` diff | 把整文件写入的 diff 渲染换成 PiUI 风格 |
| 接管 `edit` diff | 把 search/replace 调用的 diff 渲染换掉 |
| `ui-tool keyed` 机制 | 通过 DSH 的扩展点「接管」，不改核心 |
| 零侵入 | DSH 升级 / 切换主题都不影响 |
| 可卸载 | 卸载即恢复 DSH 默认 diff 视图 |

## 工作机制

```
DSH 内部 write / edit 工具被调用
         ↓
   ui-tool keyed 扩展点
         ↓
dsh-diff-viewer 接管渲染
         ↓
   PiUI 风格 diff 组件
```

## 适用人群

- DSH 重度用户，每天看大量 write / edit diff。
- 觉得 DSH 默认 diff 不够顺眼、又不愿 fork 改的人。
- 想给 DSH 加 UI 改造插件的开发者（参考本插件的接入方式）。

## 参考链接

- [项目链接](https://github.com/lehhair/dsh-diff-viewer)

## 相关概念

- [Aura-IDE](tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，写文件前先显示 diff 让用户逐条审批